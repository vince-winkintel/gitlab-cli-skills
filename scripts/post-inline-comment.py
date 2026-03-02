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
  GITLAB_TOKEN   — Personal access token (or set via glab auth)
  GITLAB_HOST    — GitLab host URL (default: https://gitlab.com)

REQUIREMENTS:
  - Python 3.6+ (stdlib only, no pip installs needed)
  - glab authenticated (token auto-read from glab config if GITLAB_TOKEN not set)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import urllib.error


def get_token():
    """Get GitLab token from env or glab config."""
    token = os.environ.get("GITLAB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["glab", "config", "get", "token", "--host", "gitlab.com"],
            capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    print("ERROR: No GitLab token found. Set GITLAB_TOKEN env var or run 'glab auth login'.", file=sys.stderr)
    sys.exit(1)


def get_mr_versions(token, host, project_id, mr_iid):
    """Fetch current HEAD/START/BASE SHAs for an MR."""
    url = f"{host}/api/v4/projects/{project_id}/merge_requests/{mr_iid}/versions"
    req = urllib.request.Request(url, headers={"PRIVATE-TOKEN": token})
    with urllib.request.urlopen(req) as resp:
        versions = json.loads(resp.read())
    if not versions:
        raise ValueError(f"No versions found for MR !{mr_iid}")
    latest = versions[0]
    return {
        "head_sha": latest["head_commit_sha"],
        "start_sha": latest["start_commit_sha"],
        "base_sha": latest["base_commit_sha"],
    }


def get_diff_line_number(token, host, project_id, mr_iid, file_path, search_line):
    """
    Find the correct new_line number for a given file path.
    search_line: either an integer (direct line number) or a string to search for in added lines.
    Returns the line number in the new file.
    """
    if isinstance(search_line, int):
        return search_line

    url = f"{host}/api/v4/projects/{project_id}/merge_requests/{mr_iid}/diffs"
    req = urllib.request.Request(url, headers={"PRIVATE-TOKEN": token})
    with urllib.request.urlopen(req) as resp:
        diffs = json.loads(resp.read())

    for d in diffs:
        if d.get("new_path") != file_path:
            continue
        diff_text = d.get("diff", "")
        new_line = 0
        for line in diff_text.split("\n"):
            hunk = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            if hunk:
                new_line = int(hunk.group(1)) - 1
                continue
            if line.startswith("-") or line.startswith("\\"):
                continue
            new_line += 1
            if line.startswith("+") and search_line in line:
                return new_line

    raise ValueError(f"Could not find '{search_line}' in added lines of {file_path}")


def post_inline_comment(token, host, project_id, mr_iid, shas, file_path, line_number, body):
    """
    Post a single inline comment on a MR diff using JSON body.
    Returns (disc_id, is_inline) tuple.
    """
    url = f"{host}/api/v4/projects/{project_id}/merge_requests/{mr_iid}/discussions"

    payload = {
        "body": body,
        "position": {
            "base_sha": shas["base_sha"],
            "start_sha": shas["start_sha"],
            "head_sha": shas["head_sha"],
            "position_type": "text",
            "new_path": file_path,
            "new_line": line_number,
            "old_path": file_path,  # same as new_path; old_line omitted = None
            "old_line": None,
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"PRIVATE-TOKEN": token, "Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            r = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        raise RuntimeError(f"HTTP {e.code}: {error_body}")

    note = r.get("notes", [{}])[0]
    disc_id = r.get("id")
    is_inline = note.get("position") is not None

    return disc_id, is_inline


def main():
    parser = argparse.ArgumentParser(
        description="Post inline diff comments on GitLab MRs via JSON body."
    )
    parser.add_argument("--project", required=True, help="GitLab project path (e.g. mygroup/myproject)")
    parser.add_argument("--mr", required=True, type=int, help="MR IID (e.g. 42)")
    parser.add_argument("--host", default="https://gitlab.com", help="GitLab host URL")
    parser.add_argument("--file", help="File path in repo (for single comment)")
    parser.add_argument("--line", type=int, help="Line number in new file (for single comment)")
    parser.add_argument("--body", help="Comment text (for single comment)")
    parser.add_argument("--batch", help="Path to JSON file with list of {file, line, body} objects")
    args = parser.parse_args()

    if not args.batch and not (args.file and args.line and args.body):
        parser.error("Provide either --batch or all of --file, --line, --body")

    token = get_token()
    project_id = urllib.parse.quote(args.project, safe="")
    host = args.host.rstrip("/")

    print(f"Fetching current HEAD SHAs for MR !{args.mr}...")
    shas = get_mr_versions(token, host, project_id, args.mr)
    print(f"  head_sha: {shas['head_sha'][:12]}...")

    if args.batch:
        with open(args.batch) as f:
            comments = json.load(f)
    else:
        comments = [{"file": args.file, "line": args.line, "body": args.body}]

    results = []
    for c in comments:
        file_path = c["file"]
        line_number = c["line"]
        body = c["body"]

        print(f"\nPosting: {file_path}:{line_number}")
        print(f"  Body: {body[:80]}{'...' if len(body) > 80 else ''}")

        try:
            disc_id, is_inline = post_inline_comment(
                token, host, project_id, args.mr, shas, file_path, line_number, body
            )
            status = "✅ INLINE" if is_inline else "⚠️  GENERAL (position rejected — check line number)"
            print(f"  {status} | disc_id: {disc_id}")
            results.append({
                "disc_id": disc_id,
                "is_inline": is_inline,
                "file": file_path,
                "line": line_number
            })
        except Exception as e:
            print(f"  ❌ FAILED: {e}")
            results.append({"error": str(e), "file": file_path, "line": line_number})

    print(f"\n{'='*50}")
    inline_count = sum(1 for r in results if r.get("is_inline"))
    general_count = sum(1 for r in results if r.get("is_inline") is False)
    error_count = sum(1 for r in results if "error" in r)
    print(f"Summary: {inline_count} inline ✅  {general_count} general ⚠️  {error_count} failed ❌")

    if any(r.get("is_inline") is False for r in results):
        print("\n⚠️  Some comments posted as general (non-inline).")
        print("   This means the line number doesn't correspond to an added line in the diff.")
        print("   Check that --line points to a '+' line in the diff, not a context line.")

    # Output disc IDs for automation
    disc_ids = [r["disc_id"] for r in results if r.get("disc_id")]
    if disc_ids:
        print(f"\nDiscussion IDs: {json.dumps(disc_ids)}")

    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
