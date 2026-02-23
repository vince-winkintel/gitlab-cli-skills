# GitLab Inline Comment Automation

## Overview

The `add-inline-comment.sh` script enables posting inline code review comments to GitLab merge requests at specific file lines. This is more effective than general MR comments because developers can see feedback directly in context without hunting through code.

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
# The script is already in the gitlab-cli-skills repo
cd /path/to/gitlab-cli-skills/scripts
chmod +x add-inline-comment.sh

# Optional: Add to PATH for global access
ln -s $(pwd)/add-inline-comment.sh ~/.local/bin/add-inline-comment
```

## Requirements

- **glab CLI** - Configured and authenticated (`glab auth login`)
- **jq** - For JSON parsing (`apt install jq` or `brew install jq`)
- **curl** - For API calls (usually pre-installed)

## Usage

```bash
add-inline-comment.sh <repo> <mr_iid> <file_path> <line_number> <comment_text>
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `repo` | Repository path | `owner/repo` |
| `mr_iid` | Merge request IID (numeric) | `42` |
| `file_path` | File path relative to repo root | `src/main.js` |
| `line_number` | Line number in NEW version | `100` |
| `comment_text` | Comment (supports markdown) | `Bug: Add null check` |

### Examples

**Simple comment:**
```bash
add-inline-comment.sh \
  "owner/repo" \
  "42" \
  "src/components/Button.tsx" \
  "25" \
  "Consider using a more descriptive variable name here"
```

**Bug report with markdown:**
```bash
add-inline-comment.sh \
  "owner/repo" \
  "42" \
  "src/utils/validator.js" \
  "10" \
  "**Bug**: This regex doesn't handle edge case when input is \`null\`. Add: \`if (!input) return false;\`"
```

**Multiple comments (batch review):**
```bash
#!/bin/bash
REPO="owner/repo"
MR_IID="42"

add-inline-comment.sh "$REPO" "$MR_IID" "src/api.js" 15 "Add error handling"
add-inline-comment.sh "$REPO" "$MR_IID" "src/api.js" 22 "Use async/await instead of .then()"
add-inline-comment.sh "$REPO" "$MR_IID" "src/types.ts" 8 "Missing JSDoc comment"
```

## How It Works

1. **Extracts GitLab token** from `~/.config/glab-cli/config.yml`
2. **Fetches MR metadata** via `glab api` to get:
   - Project ID
   - Base SHA (target branch commit)
   - Head SHA (source branch commit)
   - Start SHA (merge base commit)
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
4. **Posts to GitLab API** via `curl` (using `glab api` doesn't work for nested JSON)
5. **Validates response** - Checks that note type is `DiffNote` (inline) not `DiscussionNote` (general)

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

### "Position is invalid"

**Cause:** Line number doesn't exist in the file diff.

**Fix:**
- Verify the line number exists in the **NEW** version of the file
- Check that the file was actually changed in this MR
- Use `glab mr diff <iid>` to see what lines are in the diff

### Comment appears as general, not inline

**Cause:** This shouldn't happen if the script succeeded, but if it does:
- File path might be incorrect (must be relative to repo root)
- Line number might be outside the diff range

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
    
    add-inline-comment.sh "$REPO" "$MR_IID" "$FILE" "$LINE" \
        "⚠️ Remove console.log before merging"
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
    
    add-inline-comment.sh "$REPO" "$MR_IID" "$rel_path" "$line" "ESLint: $message"
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
./add-inline-comment.sh \
  "owner/test-repo" \
  "1" \
  "README.md" \
  "1" \
  "TEST: This is a test inline comment"

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
