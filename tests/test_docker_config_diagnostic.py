"""Execute the authored troubleshooting example against synthetic Docker files only.

Set SKILL_TEST_ROOT to test a clean baseline export with this same test file.
Temporary fixtures respect TMPDIR; no Docker/glab/keyring commands are invoked.
"""

import json
import os
import re
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(os.environ.get("SKILL_TEST_ROOT", Path(__file__).resolve().parents[1]))


def diagnostic(markdown):
    section = markdown.split("**Docker authentication fails:**", 1)[1].split("\n## ", 1)[0]
    blocks = re.findall(r"```bash\n(.*?)\n```", section, re.S)
    if blocks:
        if len(blocks) != 1:
            raise AssertionError("Expected exactly one diagnostic example")
        return blocks[0]
    # Exercise the actual old command too, so baseline failure proves disclosure.
    return re.search(r"Check Docker config: `([^`]+)`", section).group(1)


class DockerDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workspace = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.workspace.cleanup)
        directory = Path(cls.workspace.name)
        archive = directory / "claude-skill.zip"
        subprocess.run(
            ["bash", str(ROOT / "scripts/build-claude-skill.sh"), "--output", str(archive)],
            check=True, capture_output=True, text=True,
        )
        with zipfile.ZipFile(archive) as bundle:
            cls.merged = bundle.read("gitlab-cli-skills/SKILL.md").decode()
        # A selective install has only this skill directory, no sibling helpers.
        standalone = directory / "selective-install" / "glab-auth"
        standalone.mkdir(parents=True)
        source = (ROOT / "glab-auth/SKILL.md").read_text()
        (standalone / "SKILL.md").write_text(source)
        cls.examples = {"standalone": diagnostic(source), "merged": diagnostic(cls.merged)}
        cls.cwd = standalone

    def run_example(self, example, config, *, docker_config=None, config_is_directory=False):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            config_dir = home / (docker_config or ".docker")
            config_dir.mkdir()
            if config_is_directory:
                (config_dir / "config.json").mkdir()
            elif config is not None:
                (config_dir / "config.json").write_bytes(config)
            env = {"HOME": str(home), "PATH": os.environ["PATH"], "PYTHONIOENCODING": "utf-8"}
            if docker_config is not None:
                env["DOCKER_CONFIG"] = str(config_dir) if docker_config else ""
            result = subprocess.run(
                ["bash", "--noprofile", "--norc", "-c", example],
                cwd=self.cwd, env=env, capture_output=True, text=True, errors="replace", timeout=10,
            )
            return result

    def test_valid_config_reports_only_selected_helper(self):
        config = json.dumps({
            "credHelpers": {"registry.gitlab.com": "glab-cli", "unrelated.example": "HELPER_CANARY"},
            "auths": {"registry.gitlab.com": {"auth": "AUTH_CANARY", "identitytoken": "IDENTITY_CANARY"}},
            "credsStore": "STORE_CANARY", "HttpHeaders": {"Authorization": "TOKEN_CANARY"},
        }).encode()
        for name, example in self.examples.items():
            with self.subTest(artifact=name):
                result = self.run_example(example, config)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, "Selected registry credential helper: glab-cli\n")
                self.assertEqual(result.stderr, "")

    def test_missing_config_has_fixed_error_without_path_disclosure(self):
        for name, example in self.examples.items():
            with self.subTest(artifact=name):
                result = self.run_example(example, None, docker_config="PATH_CANARY")
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertEqual(result.stderr, "Docker config is missing.\n")

    def test_malformed_config_has_fixed_error_without_values(self):
        configs = [
            b'{"auths": "MALFORMED_CANARY",', b'\xffENCODING_CANARY',
            b'[]', b'null', b'"ROOT_CANARY"',
            b'{"credHelpers": "HELPERS_CANARY"}', b'{"credHelpers": null}',
            b'{"credHelpers": []}',
            b'{"credHelpers": {"registry.gitlab.com": {"auth": "NESTED_CANARY"}}}',
            b'{"credHelpers": {"registry.gitlab.com": 42}}',
            b'{"credHelpers": {"registry.gitlab.com": null}}',
        ]
        for name, example in self.examples.items():
            for config in configs:
                with self.subTest(artifact=name, config=config):
                    result = self.run_example(example, config)
                    self.assertEqual(result.returncode, 1)
                    self.assertEqual(result.stdout, "")
                    self.assertEqual(result.stderr, "Docker config is unreadable or invalid.\n")

    def test_custom_config_directory_and_registry_selection(self):
        config = json.dumps({"credHelpers": {
            "registry.example.test:5050": "glab-cli", "registry.gitlab.com": "OTHER_CANARY",
        }}).encode()
        for name, example in self.examples.items():
            with self.subTest(artifact=name):
                # Substitute only the documented registry argument, not the implementation.
                selected = example.replace("python3 - registry.gitlab.com", "python3 - registry.example.test:5050", 1)
                result = self.run_example(selected, config, docker_config="custom config with spaces")
                self.assertEqual((result.returncode, result.stdout, result.stderr),
                                 (0, "Selected registry credential helper: glab-cli\n", ""))

    def test_absent_empty_and_other_helpers_do_not_print_raw_values(self):
        cases = [
            ({}, "not configured"),
            ({"credHelpers": {}}, "not configured"),
            ({"credHelpers": {"registry.gitlab.com": ""}}, "not configured"),
            ({"credHelpers": {"other.example": "OTHER_CANARY"}}, "not configured"),
            ({"credHelpers": {"registry.gitlab.com": "glab"}}, "different helper configured"),
            ({"credHelpers": {"registry.gitlab.com": "RAW_CANARY\n\u001b[31m"}}, "different helper configured"),
        ]
        for name, example in self.examples.items():
            for config, status in cases:
                with self.subTest(artifact=name, config=config):
                    result = self.run_example(example, json.dumps(config).encode(), docker_config="")
                    self.assertEqual((result.returncode, result.stdout, result.stderr),
                                     (0, "Selected registry credential helper: " + status + "\n", ""))

    def test_directory_instead_of_config_is_a_safe_read_error(self):
        for name, example in self.examples.items():
            with self.subTest(artifact=name):
                result = self.run_example(example, None, config_is_directory=True)
                self.assertEqual((result.returncode, result.stdout, result.stderr),
                                 (1, "", "Docker config is unreadable or invalid.\n"))


if __name__ == "__main__":
    unittest.main()
