# GitLab Inline Comment Automation

## Overview

The `post-inline-comment.py` helper posts inline code review comments to GitLab merge requests at specific file lines. It is the preferred helper because it can recover from GitLab `line_code` validation failures by computing the diff `line_code` and retrying with `position[line_range][start/end][line_code]`.

## Why Use Inline Comments?

**Problem:** GitLab's native `glab mr note` command only creates general MR comments. When reviewing code, you often want to comment on specific lines, but there's no built-in glab command for this.

**Solution:** This script uses the GitLab Discussions API to post inline comments with proper position data (file path, line number, and commit SHAs).

**Benefits:**
- 📍 **Contextualized feedback** - Comments appear at exact line locations
- ⏱️ **Saves time** - No manual clicking in GitLab UI
- 🤖 **Enables automation** - Can be integrated into review workflows
- ✅ **Better UX** - Developers see feedback in context

## Installation

```bash
# The helper is already in the gitlab-cli-skills repo
cd /path/to/gitlab-cli-skills/scripts
chmod +x post-inline-comment.py

# Optional: Add to PATH for global access
ln -s "$(pwd)/post-inline-comment.py" ~/.local/bin/post-inline-comment
```

## Requirements

- **glab CLI** - Configured and authenticated (`glab auth login`)
- **Python 3** - Stdlib only, no pip install needed

## Usage

```bash
post-inline-comment.py --project <group/project> --mr <mr_iid> --file <file_path> --line <line_number> --body <comment_text>
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `project` | Repository path | `owner/repo` |
| `mr` | Merge request IID (numeric) | `42` |
| `file` | File path relative to repo root | `src/main.js` |
| `line` | Line number in NEW version | `100` |
| `body` | Comment (supports markdown) | `Bug: Add null check` |

### Examples

**Simple comment:**
```bash
post-inline-comment.py \
  --project "owner/repo" \
  --mr 42 \
  --file "src/components/Button.tsx" \
  --line 25 \
  --body "Consider using a more descriptive variable name here"
```

**Bug report with markdown:**
```bash
post-inline-comment.py \
  --project "owner/repo" \
  --mr 42 \
  --file "src/utils/validator.js" \
  --line 10 \
  --body "**Bug**: This regex doesn't handle edge case when input is \`null\`. Add: \`if (!input) return false;\`"
```

**Multiple comments (batch review):**
```bash
python3 post-inline-comment.py --project "owner/repo" --mr 42 --batch comments.json
```

Example `comments.json`:

```json
[
  { "file": "src/api.js", "line": 15, "body": "Add error handling" },
  { "file": "src/api.js", "line": 22, "body": "Use async/await instead of .then()" },
  { "file": "src/types.ts", "line": 8, "body": "Missing JSDoc comment" }
]
```

## How It Works

1. **Reads the GitLab token** from `GITLAB_TOKEN` or glab config
2. **Fetches MR metadata and all diff pages** to get:
   - Project ID
   - Base SHA (target branch commit)
   - Head SHA (source branch commit)
   - Start SHA (merge base commit)
   - Raw file diff text for anchor recovery
   - Actual `old_path` / `new_path` values for renamed-file anchors
3. **Builds JSON payload** with position data:
   ```json
   {
     "body": "Comment text",
     "position": {
       "base_sha": "abc123...",
       "head_sha": "def456...",
       "start_sha": "abc123...",
       "position_type": "text",
       "new_path": "src/file.js",
       "new_line": 42
     }
   }
   ```
4. **Posts to GitLab API** with a JSON body
5. **If GitLab rejects the simple payload with a `line_code` validation error**:
   - Parse the file diff
   - Derive the correct old/new diff line pair for the target line
   - Compute `sha1(diff_path) + '_' + oldLine + '_' + newLine`
   - Retry using `position[line_range][start/end][line_code]`
   - Reuse the diff's actual `old_path` / `new_path` when the file was renamed
6. **Validates response** - Checks that note type is `DiffNote` (inline) not `DiscussionNote` (general)

## Output

### Success Output

```
✅ Success!
Discussion ID: abc123...
Note ID: 3106970438
Note Type: DiffNote
Inline: true

✅ Inline comment posted successfully at src/main.js:42
URL: https://gitlab.com/owner/repo/-/merge_requests/42#note_3106970438
```

The script also outputs the full JSON response for programmatic use.

### Error Output

```
❌ Error: HTTP 400
{
  "message": "400 Bad request - Position is invalid"
}
```

Common errors:
- **400 Bad Request** - Line number doesn't exist in diff
- **401 Unauthorized** - Token invalid or expired
- **404 Not Found** - MR or repo doesn't exist

## Troubleshooting

### "Could not extract GitLab token"

**Cause:** glab CLI not authenticated or config file missing.

**Fix:**
```bash
glab auth login
glab auth status  # Verify authentication
```

### `line_code` validation error

**Cause:** For some MR/file/diff combinations, GitLab rejects the simpler `new_line`/`old_line` payload unless the request also includes computed `position[line_range][start/end][line_code]` values.

**Fix:**
- Use `post-inline-comment.py`, which retries automatically with computed `line_code`
- Verify the target line exists in the MR diff
- Verify the file path matches the diff path exactly

### Comment appears as general, not inline

**Cause:** Inline anchoring still failed after the retry path.
- File path might be incorrect (must be relative to repo root)
- Line number might be outside the diff range
- The target line may not map cleanly to the MR diff

**Debug:**
```bash
# Check the diff to see available lines
glab mr diff 42 --repo owner/repo | grep -A5 -B5 "src/file.js"
```

## Integration with Code Review Workflows

### Example: Automated Review Script

```bash
#!/bin/bash
# review-mr.sh - Automated code review helper

REPO="$1"
MR_IID="$2"

# Fetch MR diff
DIFF=$(glab mr diff "$MR_IID" --repo "$REPO")

# Check for common issues
if echo "$DIFF" | grep -q "console.log"; then
    # Find line number of console.log
    LINE=$(echo "$DIFF" | grep -n "console.log" | head -1 | cut -d: -f1)
    FILE=$(echo "$DIFF" | grep -B20 "console.log" | grep "^+++" | head -1 | cut -d/ -f2-)
    
    python3 post-inline-comment.py --project "$REPO" --mr "$MR_IID" --file "$FILE" --line "$LINE" \
        --body "⚠️ Remove console.log before merging"
fi

# Check for TODO comments
if echo "$DIFF" | grep -q "TODO"; then
    # ... similar logic
fi
```

### Example: Review from Analysis Tool

```bash
#!/bin/bash
# Run ESLint and post inline comments for each issue

REPO="owner/repo"
MR_IID="42"

# Run linter and parse output
eslint src/ --format json | jq -r '.[] | "\(.filePath):\(.messages[].line) \(.messages[].message)"' | \
while IFS=: read -r file line message; do
    # Remove absolute path prefix
    rel_path="${file#/absolute/path/to/repo/}"
    
    python3 post-inline-comment.py --project "$REPO" --mr "$MR_IID" --file "$rel_path" --line "$line" --body "ESLint: $message"
done
```

## Limitations

1. **Line must exist in diff** - Can only comment on lines that were added or changed in the MR
2. **File path must be exact** - Must match the path relative to repo root exactly
3. **New file lines only** - Line number refers to the NEW version (after changes)
4. **GitLab.com only** - Script uses `https://gitlab.com/api/v4/` (modify for self-hosted)

## API Reference

This script uses the [GitLab Discussions API](https://docs.gitlab.com/ee/api/discussions.html#create-a-new-thread-in-the-merge-request-diff).

**Endpoint:**
```
POST /projects/:id/merge_requests/:merge_request_iid/discussions
```

**Key fields:**
- `body` - Comment text (markdown supported)
- `position.base_sha` - Target branch commit
- `position.head_sha` - Source branch commit
- `position.new_path` - File path
- `position.new_line` - Line number

## Development

### Testing

Test on a personal repo before using on production MRs:

```bash
# Create test MR
glab mr create --title "Test MR" --repo owner/test-repo

# Post test comment
./post-inline-comment.py \
  --project "owner/test-repo" \
  --mr 1 \
  --file "README.md" \
  --line 1 \
  --body "TEST: This is a test inline comment"

# Verify in GitLab UI
# Delete test comment and MR when done
```

### Contributing

Improvements welcome! This script is part of [gitlab-cli-skills](https://github.com/vince-winkintel/gitlab-cli-skills).

**Ideas for enhancement:**
- Support for self-hosted GitLab instances (configurable API URL)
- Batch mode (read comments from file or stdin)
- Support for line ranges (multi-line comments)
- Integration with existing `glab-mr` review workflow

## Related Skills

- **glab-mr** - Main MR management skill
- **Code review workflows** - Documented in `glab-mr/SKILL.md`
- **CI automation** - Can be triggered from CI pipelines

## License

Same as gitlab-cli-skills: MIT License

---

**Version:** 1.0.0 (2026-02-23)  
**Tested on:** GitLab.com with glab CLI v1.48.0
