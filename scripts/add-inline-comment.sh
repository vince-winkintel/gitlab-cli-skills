#!/usr/bin/env bash
# Compatibility wrapper for the JSON-body inline comment helper.
#
# Usage: add-inline-comment.sh <repo> <mr_iid> <file_path> <line_number> <comment_text>
# Pass comment_text as one quoted fifth argument.

set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <repo> <mr_iid> <file_path> <line_number> <comment_text>" >&2
  echo "Example: $0 owner/repo 42 \"src/main.js\" 100 \"Bug: Add null check here\"" >&2
  exit 1
fi

REPO="$1"
MR_IID="$2"
FILE_PATH="$3"
LINE_NUMBER="$4"
COMMENT_TEXT="$5"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOST="${GITLAB_HOST:-https://gitlab.com}"
case "$HOST" in
  https://*) ;;
  http://*) ;;
  *) HOST="https://$HOST" ;;
esac

exec python3 "$SCRIPT_DIR/post-inline-comment.py" \
  --host "$HOST" \
  --project "$REPO" \
  --mr "$MR_IID" \
  --file "$FILE_PATH" \
  --line "$LINE_NUMBER" \
  --body "$COMMENT_TEXT"
