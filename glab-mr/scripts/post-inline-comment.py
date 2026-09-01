#!/usr/bin/env python3
"""
post-inline-comment.py — Post inline diff comments on GitLab MRs via JSON body.

WHY THIS SCRIPT EXISTS:
  `glab api --field position[new_line]=N` silently falls back to a general (non-inline)
  comment when GitLab rejects the position. This happens reliably for:
    - Entirely new files (new_file=True in the diff)
    - Deeply nested URL-encoded paths
    - Any case where form-encoded position fields are not parsed correctly server-side

  The fix is to send position data as a proper JSON body. This script does that.

USAGE:
  # Post a single inline comment
  python3 post-inline-comment.py \
    --project "mygroup/myproject" \
    --mr 42 \
    --file "src/utils/helpers.ts" \
    --line 16 \
    --body "This returns the wrapper object, not the value. Use .data instead."

  # Post from a JSON file (batch mode)
  python3 post-inline-comment.py --project "mygroup/myproject" --mr 42 --batch comments.json

BATCH FILE FORMAT (comments.json):
  [
    {
      "file": "src/utils/helpers.ts",
      "line": 16,
      "body": "Comment text here"
    },
    {
      "file": "src/routes/+page.svelte",
      "line": 58,
      "body": "Another comment"
    }
  ]

ENVIRONMENT:
  GITLAB_HOST    — GitLab host URL (default: https://gitlab.com)

SECURITY:
  - Authentication stays inside glab; this script never reads or prints token values
  - Only HTTPS hosts are accepted (enforced at startup)
  - Comment body is capped at 10,000 characters
  - --project and --file inputs are validated before use
  - Batch files are size-limited (max 100 comments per run)

REQUIREMENTS:
  - Python 3.6+ (stdlib only, no pip installs needed)
  - glab authenticated (run: glab auth login)
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
from typing import Optional

# ── Security constants ────────────────────────────────────────────────────────
MAX_BODY_LENGTH = 10_000      # GitLab's own limit is ~1MB but we cap for safety
MAX_BATCH_SIZE  = 100         # prevent runaway API usage
MAX_BATCH_FILE_BYTES = 1_048_576  # 1 MB batch file limit
VALID_PROJECT_RE = re.compile(r'[\w.\-]+(/[\w.\-]+)+')  # group/project or group/sub/project
VALID_FILE_RE    = re.compile(
    r'[^\x00-\x1f\x7f-\x9f\u061c\u200e\u200f\u202a-\u202e\u2066-\u2069]+'
)  # no terminal or bidirectional control characters
BIDI_CONTROL_CHARS = frozenset(
    "\u061c\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069"
)

# ── Input validation ──────────────────────────────────────────────────────────

def validate_host(host):
    """Enforce an unambiguous HTTPS host URL before invoking glab."""
    try:
        parsed = urllib.parse.urlparse(host)
    except ValueError:
        print("ERROR: --host is not a valid URL.", file=sys.stderr)
        sys.exit(1)
    if parsed.scheme != "https":
        print(
            f"ERROR: --host must use HTTPS (got '{parsed.scheme}://').\n"
            "  Credential transmission over HTTP is not allowed.",
            file=sys.stderr
        )
        sys.exit(1)
    if not parsed.netloc:
        print("ERROR: --host must include a hostname.", file=sys.stderr)
        sys.exit(1)
    if parsed.username or parsed.password:
        print("ERROR: --host must not include username or password information.", file=sys.stderr)
        sys.exit(1)
    try:
        port = parsed.port
    except ValueError:
        print("ERROR: --host contains an invalid port.", file=sys.stderr)
        sys.exit(1)
    if port not in (None, 443):
        print("ERROR: --host must use the standard HTTPS port because glab --hostname does not accept ports.", file=sys.stderr)
        sys.exit(1)
    if parsed.path not in ("", "/") or parsed.params or parsed.query or parsed.fragment:
        print("ERROR: --host must be only an HTTPS scheme and host, with no path, query, or fragment.", file=sys.stderr)
        sys.exit(1)
    return host.rstrip("/")


def validate_project(project):
    """Validate project path format: group/project or group/subgroup/project."""
    if not VALID_PROJECT_RE.fullmatch(project):
        print(
            f"ERROR: --project {project!r} is not a valid GitLab project path.\n"
            "  Expected format: 'group/project' or 'group/subgroup/project'",
            file=sys.stderr
        )
        sys.exit(1)
    return project


def validate_file_path(file_path):
    """Validate that a file path doesn't contain dangerous characters."""
    if not file_path or not VALID_FILE_RE.fullmatch(file_path):
        print(f"ERROR: Invalid file path: {repr(file_path)}", file=sys.stderr)
        sys.exit(1)
    return file_path


def validate_body(body):
    """Trim and cap comment body length."""
    body = body.strip()
    if not body:
        print("ERROR: Comment body cannot be empty.", file=sys.stderr)
        sys.exit(1)
    if len(body) > MAX_BODY_LENGTH:
        print(
            f"WARNING: Comment body truncated from {len(body)} to {MAX_BODY_LENGTH} characters.",
            file=sys.stderr
        )
        body = body[:MAX_BODY_LENGTH]
    return body


def validate_line(line):
    """Line number must be a positive integer."""
    if not isinstance(line, int) or line < 1:
        print(f"ERROR: Line number must be a positive integer (got {line!r}).", file=sys.stderr)
        sys.exit(1)
    return line


def load_batch_file(path):
    """Load and validate a batch comments JSON file."""
    try:
        size = os.path.getsize(path)
        if size > MAX_BATCH_FILE_BYTES:
            print(
                f"ERROR: Batch file is too large ({size} bytes, max {MAX_BATCH_FILE_BYTES}).",
                file=sys.stderr
            )
            sys.exit(1)
        with open(path) as f:
            comments = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(
            f"ERROR: Could not load batch file {path!r}: {sanitize_glab_error(str(e))}",
            file=sys.stderr,
        )
        sys.exit(1)

    if not isinstance(comments, list):
        print("ERROR: Batch file must contain a JSON array.", file=sys.stderr)
        sys.exit(1)
    if len(comments) > MAX_BATCH_SIZE:
        print(
            f"ERROR: Batch file contains {len(comments)} comments (max {MAX_BATCH_SIZE}).",
            file=sys.stderr
        )
        sys.exit(1)

    # Validate each entry
    validated = []
    for i, c in enumerate(comments):
        if not isinstance(c, dict) or not all(k in c for k in ("file", "line", "body")):
            print(f"ERROR: Batch entry {i} missing required keys (file, line, body).", file=sys.stderr)
            sys.exit(1)
        validated.append({
            "file": validate_file_path(c["file"]),
            "line": validate_line(int(c["line"])),
            "body": validate_body(c["body"]),
        })
    return validated


# ── glab API helpers ──────────────────────────────────────────────────────────

class GlabApiError(RuntimeError):
    """Raised when a glab api call fails."""


def get_hostname(host):
    """Return the hostname that glab should use for an already-validated host URL."""
    parsed = urllib.parse.urlparse(host)
    return parsed.hostname or "gitlab.com"


def sanitize_terminal(text, limit: Optional[int] = 500, multiline=False):
    """Remove terminal controls from untrusted text before displaying it."""
    text = str(text or "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r'\x1b\][^\x07]*(?:\x07|\x1b\\)', '', text)
    text = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', text)
    text = ''.join(
        char for char in text
        if char not in BIDI_CONTROL_CHARS and (
            (multiline and char in "\n\t")
            or 0x20 <= ord(char) < 0x7f
            or ord(char) >= 0xa0
        )
    )
    text = text.strip()
    if limit is not None and len(text) > limit:
        text = text[:limit] + "...(truncated)"
    return text


def sanitize_glab_error(text, limit=500):
    """Bound and redact glab stderr/stdout before showing it to a user."""
    text = sanitize_terminal(text, limit=None, multiline=True)
    text = re.sub(
        r'(?im)^(\s*>?\s*)(Authorization|PRIVATE-TOKEN|JOB-TOKEN|OAUTH-TOKEN)\s*:.*$',
        lambda match: "%s%s: [REDACTED]" % (match.group(1), match.group(2)),
        text,
    )
    text = re.sub(r'glpat-[A-Za-z0-9_\-]+', 'glpat-[REDACTED]', text)
    text = re.sub(r'(?i)(PRIVATE-TOKEN|Authorization|Bearer|token)([=: ]+)(\S+)', r'\1\2[REDACTED]', text)
    if len(text) > limit:
        text = text[:limit] + "...(truncated)"
    return text


def parse_included_response(output):
    """Parse `glab api --include` output into (JSON body, response headers)."""
    normalized = output.replace("\r\n", "\n")
    status_lines = list(re.finditer(r'(?m)^HTTP/\S+\s+\d{3}(?:\s+[^\n]*)?$', normalized))
    if not status_lines:
        raise GlabApiError("glab api response did not include an HTTP status line")
    # Start at the final response's status line, then split at that header block's
    # first blank line. This keeps blank lines in pretty-printed JSON bodies intact.
    final_response = normalized[status_lines[-1].start():]
    header_text, sep, body_text = final_response.partition("\n\n")
    if not sep:
        raise GlabApiError("glab api response did not include HTTP headers")

    active_headers = header_text.splitlines()
    headers = {}
    for line in active_headers:
        if ":" not in line:
            continue
        name, value = line.split(":", 1)
        headers[name.strip().lower()] = value.strip()
    return json.loads(body_text), headers


def run_glab_api(host, endpoint, method=None, payload=None, include_headers=False):
    """Run an authenticated GitLab API call through glab without reading credentials."""
    args = ["glab", "api", "--hostname", get_hostname(host)]
    if include_headers:
        args.append("--include")
    if method:
        args.extend(["--method", method])
    input_text = None
    if payload is not None:
        args.extend(["--header", "Content-Type: application/json", "--input", "-"])
        input_text = json.dumps(payload)
    args.append(endpoint)

    try:
        result = subprocess.run(
            args,
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=30,
        )
    except FileNotFoundError:
        raise GlabApiError("glab executable not found. Install glab and run: glab auth login")
    except subprocess.TimeoutExpired:
        raise GlabApiError("glab api timed out")

    if result.returncode != 0:
        # glab writes structured API errors to stdout but may also write a generic
        # `glab: HTTP 400` status to stderr. Keep stdout first so callers can
        # inspect validation details such as `line_code` and apply safe retries.
        detail = sanitize_glab_error("\n".join(
            part for part in (result.stdout, result.stderr) if part
        ))
        if detail:
            raise GlabApiError("glab api failed: %s" % detail)
        raise GlabApiError("glab api failed with exit code %s" % result.returncode)

    if include_headers:
        try:
            return parse_included_response(result.stdout)
        except (json.JSONDecodeError, GlabApiError) as e:
            raise GlabApiError("Could not parse glab api response: %s" % e)

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise GlabApiError("Could not parse glab api JSON response: %s" % e)


def _api_get(host, endpoint):
    """Authenticated GET request, returns parsed JSON."""
    return run_glab_api(host, endpoint)


def _api_get_with_headers(host, endpoint):
    """Authenticated GET request, returns (parsed_json, headers)."""
    return run_glab_api(host, endpoint, include_headers=True)


def verify_glab_identity(host):
    """Verify and display the selected GitLab host/account before write workflow calls."""
    user = _api_get(host, "/user")
    username = sanitize_terminal(user.get("username")) if isinstance(user, dict) else ""
    if not username:
        raise GlabApiError("glab /user response did not include a non-empty username")
    print(f"GitLab host: {sanitize_terminal(get_hostname(host))}")
    print(f"GitLab user: {username}")
    return username


def get_mr_versions(host, project_id, mr_iid):
    """Fetch current HEAD/START/BASE SHAs for an MR."""
    endpoint = f"/projects/{project_id}/merge_requests/{mr_iid}/versions"
    versions = _api_get(host, endpoint)
    if not versions:
        raise ValueError(f"No versions found for MR !{mr_iid}")
    latest = versions[0]
    return {
        "head_sha":  latest["head_commit_sha"],
        "start_sha": latest["start_commit_sha"],
        "base_sha":  latest["base_commit_sha"],
    }


def get_mr_diffs(host, project_id, mr_iid):
    """Fetch all MR diffs so we can compute line_code anchors when GitLab requires them."""
    diffs = []
    page = 1

    while True:
        endpoint = (
            f"/projects/{project_id}/merge_requests/{mr_iid}/diffs"
            f"?per_page=100&page={page}"
        )
        page_diffs, headers = _api_get_with_headers(host, endpoint)
        diffs.extend(page_diffs)

        next_page = (headers.get("x-next-page") or "").strip()
        if not next_page:
            break
        page = int(next_page)

    return diffs


def find_file_diff(diffs, file_path):
    """Return the diff entry matching file_path on either old or new side."""
    for diff in diffs:
        if diff.get("new_path") == file_path or diff.get("old_path") == file_path:
            return diff
    raise ValueError(f"Could not find diff for file '{file_path}' in this MR.")


def compute_diff_anchor(diff_text, target_new_line):
    """Map a target new-side line number to the diff's old/new anchor pair."""
    old_line = None
    new_line = None

    for raw_line in diff_text.splitlines():
        hunk = re.match(r'^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@', raw_line)
        if hunk:
            old_line = int(hunk.group(1))
            new_line = int(hunk.group(2))
            continue

        if old_line is None or new_line is None:
            continue

        if raw_line.startswith('\\'):
            continue

        if raw_line.startswith('+'):
            if new_line == target_new_line:
                return {
                    "type": "new",
                    "old_line": 0,
                    "new_line": new_line,
                }
            new_line += 1
            continue

        if raw_line.startswith('-'):
            old_line += 1
            continue

        if new_line == target_new_line:
            return {
                "type": "new",
                "old_line": old_line,
                "new_line": new_line,
            }
        old_line += 1
        new_line += 1

    raise ValueError(
        f"Could not map new-side line {target_new_line} to a diff anchor. "
        "Make sure the line exists in the MR diff."
    )


def compute_line_code(file_path, old_line, new_line):
    """GitLab diff line code format: sha1(path)_{old}_{new}."""
    file_hash = hashlib.sha1(file_path.encode("utf-8")).hexdigest()
    return f"{file_hash}_{old_line}_{new_line}"


def get_position_paths(diff_entry, requested_file_path):
    """Return the old/new paths GitLab expects for this diff position."""
    return {
        "old_path": diff_entry.get("old_path") or requested_file_path,
        "new_path": diff_entry.get("new_path") or requested_file_path,
    }


def build_inline_payload(shas, diff_entry, file_path, line_number, body):
    paths = get_position_paths(diff_entry, file_path)
    return {
        "body": body,
        "position": {
            "base_sha":      shas["base_sha"],
            "start_sha":     shas["start_sha"],
            "head_sha":      shas["head_sha"],
            "position_type": "text",
            "new_path":      paths["new_path"],
            "new_line":      line_number,
            "old_path":      paths["old_path"],
            "old_line":      None,
        }
    }


def build_line_range_payload(shas, diff_entry, file_path, body, anchor):
    paths = get_position_paths(diff_entry, file_path)
    line_code_path = paths["new_path"] if anchor["type"] == "new" else paths["old_path"]
    point = {
        "type": anchor["type"],
        "line_code": compute_line_code(line_code_path, anchor["old_line"], anchor["new_line"]),
    }
    if anchor["old_line"] is not None:
        point["old_line"] = anchor["old_line"]
    if anchor["new_line"] is not None:
        point["new_line"] = anchor["new_line"]

    return {
        "body": body,
        "position": {
            "base_sha":      shas["base_sha"],
            "start_sha":     shas["start_sha"],
            "head_sha":      shas["head_sha"],
            "position_type": "text",
            "old_path":      paths["old_path"],
            "new_path":      paths["new_path"],
            "line_range": {
                "start": dict(point),
                "end":   dict(point),
            },
        }
    }


def post_discussion(host, project_id, mr_iid, payload):
    endpoint = f"/projects/{project_id}/merge_requests/{mr_iid}/discussions"
    return run_glab_api(host, endpoint, method="POST", payload=payload)


def is_line_code_validation_error(error_text):
    return "line_code" in error_text and "valid" in error_text.lower()


def post_inline_comment(host, project_id, mr_iid, shas, diffs, file_path, line_number, body):
    """
    Post a single inline comment on a MR diff using a JSON body.
    First try the simple new_line payload; if GitLab rejects it with a line_code
    validation error, compute the diff anchor and retry with position.line_range.
    Returns (disc_id, is_inline, used_line_code_retry) tuple.
    """
    diff_entry = find_file_diff(diffs, file_path)

    try:
        r = post_discussion(host, project_id, mr_iid, build_inline_payload(shas, diff_entry, file_path, line_number, body))
        used_line_code_retry = False
    except Exception as e:
        error_text = str(e)
        if not is_line_code_validation_error(error_text):
            raise

        anchor = compute_diff_anchor(diff_entry.get("diff", ""), line_number)
        retry_payload = build_line_range_payload(shas, diff_entry, file_path, body, anchor)
        r = post_discussion(host, project_id, mr_iid, retry_payload)
        used_line_code_retry = True

    note = r.get("notes", [{}])[0]
    disc_id = r.get("id")
    is_inline = note.get("position") is not None

    return disc_id, is_inline, used_line_code_retry


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Post inline diff comments on GitLab MRs via JSON body.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--project", required=True,
                        help="GitLab project path, e.g. mygroup/myproject")
    parser.add_argument("--mr", required=True, type=int,
                        help="MR IID (integer), e.g. 42")
    parser.add_argument("--host", default="https://gitlab.com",
                        help="GitLab host URL (must be HTTPS)")
    parser.add_argument("--file",  help="File path in repo (single comment mode)")
    parser.add_argument("--line",  type=int, help="Line number in new file (single comment mode)")
    parser.add_argument("--body",  help="Comment text (single comment mode)")
    parser.add_argument("--batch", help="Path to JSON file with [{file, line, body}] array")
    args = parser.parse_args()

    if not args.batch and not (args.file and args.line and args.body):
        parser.error("Provide either --batch or all of --file, --line, --body")

    # Validate all inputs before touching the network
    host       = validate_host(args.host)
    project    = validate_project(args.project)
    project_id = urllib.parse.quote(project, safe="")

    if args.batch:
        comments = load_batch_file(args.batch)
    else:
        comments = [{
            "file": validate_file_path(args.file),
            "line": validate_line(args.line),
            "body": validate_body(args.body),
        }]

    try:
        verify_glab_identity(host)
    except Exception as e:
        print(
            f"ERROR: Could not verify glab identity: {sanitize_glab_error(str(e))}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Fetching current HEAD SHAs for MR !{args.mr}...")
    try:
        shas = get_mr_versions(host, project_id, args.mr)
        diffs = get_mr_diffs(host, project_id, args.mr)
    except Exception as e:
        print(
            f"ERROR: Could not fetch MR metadata/diffs: {sanitize_glab_error(str(e))}",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"  head_sha: {sanitize_terminal(shas.get('head_sha'))[:12]}...")

    results = []
    for c in comments:
        file_path   = c["file"]
        line_number = c["line"]
        body        = c["body"]

        print(f"\nPosting: {file_path}:{line_number}")
        print(f"  Body length: {len(body)} characters")

        try:
            disc_id, is_inline, used_line_code_retry = post_inline_comment(
                host, project_id, args.mr, shas, diffs, file_path, line_number, body
            )
            if is_inline and used_line_code_retry:
                status = "✅ INLINE (line_code retry)"
            elif is_inline:
                status = "✅ INLINE"
            else:
                status = "⚠️  GENERAL (position rejected — check line number)"
            print(f"  {status} | disc_id: {sanitize_terminal(disc_id)}")
            results.append({
                "disc_id":              disc_id,
                "is_inline":            is_inline,
                "used_line_code_retry": used_line_code_retry,
                "file":                 file_path,
                "line":                 line_number,
            })
        except Exception as e:
            print(f"  ❌ FAILED: {sanitize_glab_error(str(e))}", file=sys.stderr)
            results.append({"error": str(e), "file": file_path, "line": line_number})

    # Summary
    print(f"\n{'=' * 50}")
    inline_count  = sum(1 for r in results if r.get("is_inline") is True)
    retried_count = sum(1 for r in results if r.get("used_line_code_retry") is True)
    general_count = sum(1 for r in results if r.get("is_inline") is False)
    error_count   = sum(1 for r in results if "error" in r)
    print(f"Summary: {inline_count} inline ✅  {retried_count} retried-with-line_code 🔁  {general_count} general ⚠️  {error_count} failed ❌")

    if general_count:
        print(
            "\n⚠️  Some comments posted as general (non-inline).\n"
            "   The line number doesn't correspond to an added (+) line in the diff.\n"
            "   Use the get_new_line_number() helper in glab-mr/SKILL.md to find valid lines."
        )

    disc_ids = [r["disc_id"] for r in results if r.get("disc_id")]
    if disc_ids:
        print(f"\nDiscussion IDs: {json.dumps(disc_ids)}")

    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
