import importlib.util
import json
import os
import re
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "post-inline-comment.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("post_inline_comment", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeRun:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, args, **kwargs):
        self.calls.append((args, kwargs))
        if not self.responses:
            raise AssertionError("unexpected subprocess.run call: %r" % (args,))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return subprocess.CompletedProcess(args, response[0], response[1], response[2])


def included_response(body, headers=None, status="HTTP/2 200 OK"):
    header_lines = [status]
    for name, value in (headers or {}).items():
        header_lines.append("%s: %s" % (name, value))
    return "\r\n".join(header_lines) + "\r\n\r\n" + json.dumps(body)


class GlabApiTests(unittest.TestCase):
    def setUp(self):
        self.helper = load_helper()

    def test_get_paginates_with_include_headers_and_hostname(self):
        """Catches dropping X-Next-Page handling or omitting --hostname."""
        fake_run = FakeRun([
            (0, included_response([{"new_path": "a.py"}], {"x-next-page": "2"}), ""),
            (0, included_response([{"new_path": "b.py"}], {"X-Next-Page": ""}), ""),
        ])

        with mock.patch.object(self.helper.subprocess, "run", fake_run):
            diffs = self.helper.get_mr_diffs("https://gitlab.example.com", "group%2Fproject", 7)

        self.assertEqual([d["new_path"] for d in diffs], ["a.py", "b.py"])
        self.assertEqual(len(fake_run.calls), 2)
        first_args, first_kwargs = fake_run.calls[0]
        second_args, _ = fake_run.calls[1]
        self.assertEqual(first_args[:4], ["glab", "api", "--hostname", "gitlab.example.com"])
        self.assertIn("--include", first_args)
        self.assertIn("/projects/group%2Fproject/merge_requests/7/diffs?per_page=100&page=1", first_args)
        self.assertIn("/projects/group%2Fproject/merge_requests/7/diffs?per_page=100&page=2", second_args)
        self.assertFalse(first_kwargs.get("shell", False))

    def test_verify_glab_identity_prints_selected_host_and_username(self):
        """Catches writes happening without a visible account preflight."""
        fake_run = FakeRun([(0, json.dumps({"username": "alice", "name": "Alice"}), "")])

        with mock.patch.object(self.helper.subprocess, "run", fake_run), \
                mock.patch("sys.stdout") as stdout:
            username = self.helper.verify_glab_identity("https://gitlab.example.com:443")

        self.assertEqual(username, "alice")
        args, _ = fake_run.calls[0]
        self.assertEqual(args, ["glab", "api", "--hostname", "gitlab.example.com", "/user"])
        self.assertIn("GitLab host: gitlab.example.com", "".join(c.args[0] for c in stdout.write.call_args_list))
        self.assertIn("GitLab user: alice", "".join(c.args[0] for c in stdout.write.call_args_list))

    def test_verify_glab_identity_rejects_empty_username(self):
        """Catches accepting an ambiguous authenticated account before writes."""
        fake_run = FakeRun([(0, json.dumps({"username": ""}), "")])

        with mock.patch.object(self.helper.subprocess, "run", fake_run):
            with self.assertRaisesRegex(self.helper.GlabApiError, "username"):
                self.helper.verify_glab_identity("https://gitlab.example.com")

    def test_host_validation_rejects_ambiguous_urls_and_unsupported_ports(self):
        """Catches passing ports that real glab --hostname rejects or accepting ambiguous URLs."""
        host = self.helper.validate_host("https://gitlab.example.com:443")
        self.assertEqual(self.helper.get_hostname(host), "gitlab.example.com")

        bad_hosts = [
            "https://user@gitlab.example.com",
            "https://gitlab.example.com/path",
            "https://gitlab.example.com/?q=1",
            "https://gitlab.example.com/#frag",
            "https://gitlab.example.com:8443",
        ]
        for bad_host in bad_hosts:
            with self.subTest(bad_host=bad_host):
                with mock.patch("sys.stderr"):
                    with self.assertRaises(SystemExit):
                        self.helper.validate_host(bad_host)

    def test_post_sends_literal_json_on_stdin_with_input_dash_and_hostname(self):
        """Catches rebuilding POSTs as form fields or direct token-auth HTTP."""
        payload = {
            "body": "please fix",
            "position": {"position_type": "text", "new_path": "a.py", "new_line": 3},
        }
        response = {"id": "disc1", "notes": [{"position": {"new_line": 3}}]}
        fake_run = FakeRun([(0, json.dumps(response), "")])

        with mock.patch.object(self.helper.subprocess, "run", fake_run):
            result = self.helper.post_discussion(
                "https://gitlab.example.com", "group%2Fproject", 7, payload
            )

        self.assertEqual(result, response)
        args, kwargs = fake_run.calls[0]
        self.assertEqual(args[:4], ["glab", "api", "--hostname", "gitlab.example.com"])
        self.assertIn("--input", args)
        self.assertEqual(args[args.index("--input") + 1], "-")
        self.assertIn("--method", args)
        self.assertEqual(args[args.index("--method") + 1], "POST")
        self.assertIn("/projects/group%2Fproject/merge_requests/7/discussions", args)
        self.assertEqual(json.loads(kwargs["input"]), payload)
        self.assertNotIn("PRIVATE-TOKEN", " ".join(args))
        self.assertNotIn("config get token", " ".join(args))

    def test_glab_errors_redact_sensitive_header_lines(self):
        """Catches leaking authorization material from glab stderr."""
        raw = "\n".join([
            "\x1b[31m> Authorization: Bearer bearer-secret\x1b[0m",
            "PRIVATE-TOKEN: glpat-secret",
            "JOB-TOKEN: ci-secret",
            "OAUTH-TOKEN: oauth-secret",
            "message: line_code must be valid",
        ])

        redacted = self.helper.sanitize_glab_error(raw)

        self.assertNotIn("bearer-secret", redacted)
        self.assertNotIn("\x1b", redacted)
        self.assertNotIn("glpat-secret", redacted)
        self.assertNotIn("ci-secret", redacted)
        self.assertNotIn("oauth-secret", redacted)
        self.assertIn("message: line_code must be valid", redacted)

    def test_file_path_validation_rejects_terminal_control_characters(self):
        """Catches file paths that could inject terminal output when progress is printed."""
        for path in ["src/unsafe\x1b[31m.py", "src/unsafe\tname.py", "src/unsafe\x7fname.py"]:
            with self.subTest(path=path), mock.patch("sys.stderr"):
                with self.assertRaises(SystemExit):
                    self.helper.validate_file_path(path)

    def test_non_inline_response_is_reported(self):
        """Catches treating a general discussion response as a valid inline note."""
        shas = {"base_sha": "base", "start_sha": "start", "head_sha": "head"}
        diffs = [{"old_path": "a.py", "new_path": "a.py", "diff": "@@ -1 +1 @@\n+new"}]
        response = {"id": "disc-general", "notes": [{"position": None}]}

        with mock.patch.object(self.helper, "post_discussion", return_value=response):
            disc_id, is_inline, used_retry = self.helper.post_inline_comment(
                "https://gitlab.example.com", "group%2Fproject", 7, shas, diffs, "a.py", 1, "body"
            )

        self.assertEqual(disc_id, "disc-general")
        self.assertFalse(is_inline)
        self.assertFalse(used_retry)

    def test_line_code_retry_uses_same_glab_post_path(self):
        """Catches losing the fallback that retries with position.line_range."""
        shas = {"base_sha": "base", "start_sha": "start", "head_sha": "head"}
        diffs = [{"old_path": "a.py", "new_path": "a.py", "diff": "@@ -1 +10 @@\n+target"}]
        calls = []

        def fake_post(host, project_id, mr_iid, payload):
            calls.append((host, project_id, mr_iid, payload))
            if len(calls) == 1:
                raise self.helper.GlabApiError("glab api failed: line_code must be a valid line code")
            return {"id": "disc-inline", "notes": [{"position": {"line_range": {}}}]}

        with mock.patch.object(self.helper, "post_discussion", side_effect=fake_post):
            disc_id, is_inline, used_retry = self.helper.post_inline_comment(
                "https://gitlab.example.com", "group%2Fproject", 7, shas, diffs, "a.py", 10, "body"
            )

        self.assertEqual(disc_id, "disc-inline")
        self.assertTrue(is_inline)
        self.assertTrue(used_retry)
        retry_payload = calls[1][3]
        self.assertIn("line_range", retry_payload["position"])
        self.assertEqual(calls[1][:3], ("https://gitlab.example.com", "group%2Fproject", 7))


class ArtifactRegressionTests(unittest.TestCase):
    def test_source_and_merged_artifact_do_not_extract_plaintext_glab_tokens(self):
        """Catches reintroducing the reported glab config token extraction snippet."""
        forbidden_patterns = [
            re.compile(r'glab\s+config\s+get\s+token'),
            re.compile(r'["\']glab["\']\s*,\s*["\']config["\']\s*,\s*["\']get["\']\s*,\s*["\']token["\']'),
            re.compile(r'PRIVATE-TOKEN["\']?\s*:\s*token'),
            re.compile(r'glab\s+auth\s+token'),
        ]
        source_paths = [
            ROOT / "scripts" / "post-inline-comment.py",
            ROOT / "scripts" / "add-inline-comment.sh",
            ROOT / "glab-mr" / "SKILL.md",
            ROOT / "glab-mr" / "scripts" / "post-inline-comment.py",
            ROOT / "gitlab-cli-skills" / "scripts" / "post-inline-comment.py",
            ROOT / "SECURITY.md",
        ]
        for path in source_paths:
            text = path.read_text()
            for pattern in forbidden_patterns:
                self.assertIsNone(pattern.search(text), "%s matched %s" % (pattern.pattern, path))

        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / "claude-skill.zip"
            result = subprocess.run(
                ["bash", str(ROOT / "scripts" / "build-claude-skill.sh"), "--output", str(output), "--root", str(ROOT)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            with zipfile.ZipFile(output) as zf:
                skill_entries = [name for name in zf.namelist() if name == "gitlab-cli-skills/SKILL.md"]
                self.assertEqual(skill_entries, ["gitlab-cli-skills/SKILL.md"])
                merged = zf.read("gitlab-cli-skills/SKILL.md").decode("utf-8")
        for pattern in forbidden_patterns:
            self.assertIsNone(pattern.search(merged), "%s matched merged artifact" % pattern.pattern)


class ShellWrapperTests(unittest.TestCase):
    def test_wrapper_normalizes_a_bare_glab_host_without_exposing_credentials(self):
        """Keeps the standard bare GITLAB_HOST form compatible with strict URL validation."""
        with tempfile.TemporaryDirectory() as td:
            fake_python = Path(td) / "python3"
            fake_python.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
            fake_python.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = td + os.pathsep + env.get("PATH", "")
            env["GITLAB_HOST"] = "gitlab.example.com"

            result = subprocess.run(
                [
                    "bash",
                    str(ROOT / "scripts" / "add-inline-comment.sh"),
                    "group/project",
                    "42",
                    "src/main.py",
                    "7",
                    "Review comment",
                ],
                capture_output=True,
                text=True,
                env=env,
                timeout=10,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        args = result.stdout.splitlines()
        self.assertEqual(args[args.index("--host") + 1], "https://gitlab.example.com")
        self.assertNotIn("token", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
