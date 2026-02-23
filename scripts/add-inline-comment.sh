#!/bin/bash
# add-inline-comment.sh
# Post inline code review comments to GitLab MRs at specific line numbers
# Part of: gitlab-cli-skills
# 
# Usage: add-inline-comment.sh <repo> <mr_iid> <file_path> <line_number> <comment_text>
# Example: add-inline-comment.sh owner/repo 42 "src/File.js" 100 "Bug: This needs fixing"

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ $# -lt 5 ]; then
    echo -e "${RED}Usage: $0 <repo> <mr_iid> <file_path> <line_number> <comment_text>${NC}" >&2
    echo "" >&2
    echo "Arguments:" >&2
    echo "  repo           Repository path (e.g., 'owner/repo')" >&2
    echo "  mr_iid         Merge request IID (numeric ID)" >&2
    echo "  file_path      Path to file relative to repo root" >&2
    echo "  line_number    Line number in the NEW version of the file" >&2
    echo "  comment_text   Comment text (supports markdown)" >&2
    echo "" >&2
    echo "Example:" >&2
    echo "  $0 owner/repo 42 \"src/main.js\" 100 \"Bug: Add null check here\"" >&2
    exit 1
fi

REPO="$1"
MR_IID="$2"
FILE_PATH="$3"
LINE_NUMBER="$4"
COMMENT_TEXT="$5"

# URL-encode the repo path
REPO_ENCODED=$(echo "$REPO" | sed 's/\//%2F/g')

# Extract GitLab token from glab config
GITLAB_TOKEN=$(grep "token:" ~/.config/glab-cli/config.yml | head -1 | awk '{print $NF}')

if [ -z "$GITLAB_TOKEN" ]; then
    echo -e "${RED}Error: Could not extract GitLab token from glab config${NC}" >&2
    echo "Make sure you're authenticated with: glab auth login" >&2
    exit 1
fi

# Get MR metadata to extract project ID and SHAs
echo -e "${YELLOW}Fetching MR metadata...${NC}" >&2
MR_DATA=$(glab api "/projects/$REPO_ENCODED/merge_requests/$MR_IID" 2>&1)

if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Could not fetch MR metadata${NC}" >&2
    echo "$MR_DATA" >&2
    exit 1
fi

PROJECT_ID=$(echo "$MR_DATA" | jq -r '.project_id')
BASE_SHA=$(echo "$MR_DATA" | jq -r '.diff_refs.base_sha')
HEAD_SHA=$(echo "$MR_DATA" | jq -r '.diff_refs.head_sha')
START_SHA=$(echo "$MR_DATA" | jq -r '.diff_refs.start_sha')

if [ -z "$PROJECT_ID" ] || [ "$PROJECT_ID" = "null" ]; then
    echo -e "${RED}Error: Could not get project ID from MR${NC}" >&2
    exit 1
fi

if [ -z "$BASE_SHA" ] || [ "$BASE_SHA" = "null" ]; then
    echo -e "${RED}Error: Could not get SHAs from MR diff_refs${NC}" >&2
    exit 1
fi

echo -e "${YELLOW}Project ID: $PROJECT_ID${NC}" >&2
echo -e "${YELLOW}Base SHA: ${BASE_SHA:0:8}...${NC}" >&2
echo -e "${YELLOW}Head SHA: ${HEAD_SHA:0:8}...${NC}" >&2
echo -e "${YELLOW}Target: $FILE_PATH:$LINE_NUMBER${NC}" >&2

# Escape JSON special characters in comment text
COMMENT_ESCAPED=$(echo "$COMMENT_TEXT" | jq -Rs .)

# Build JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "body": $COMMENT_ESCAPED,
  "position": {
    "base_sha": "$BASE_SHA",
    "start_sha": "$START_SHA",
    "head_sha": "$HEAD_SHA",
    "position_type": "text",
    "new_path": "$FILE_PATH",
    "new_line": $LINE_NUMBER
  }
}
EOF
)

# Post inline comment
echo -e "${YELLOW}Posting inline comment...${NC}" >&2
RESPONSE=$(curl -s -w "\n%{http_code}" -X POST \
    "https://gitlab.com/api/v4/projects/$PROJECT_ID/merge_requests/$MR_IID/discussions" \
    -H "PRIVATE-TOKEN: $GITLAB_TOKEN" \
    -H "Content-Type: application/json" \
    -d "$JSON_PAYLOAD")

HTTP_CODE=$(echo "$RESPONSE" | tail -n 1)
BODY=$(echo "$RESPONSE" | sed '$d')

if [ "$HTTP_CODE" -ge 200 ] && [ "$HTTP_CODE" -lt 300 ]; then
    DISCUSSION_ID=$(echo "$BODY" | jq -r '.id')
    NOTE_ID=$(echo "$BODY" | jq -r '.notes[0].id')
    HAS_POSITION=$(echo "$BODY" | jq -r '.notes[0].position != null')
    NOTE_TYPE=$(echo "$BODY" | jq -r '.notes[0].type')
    
    echo "" >&2
    echo -e "${GREEN}✅ Success!${NC}" >&2
    echo -e "${GREEN}Discussion ID: $DISCUSSION_ID${NC}" >&2
    echo -e "${GREEN}Note ID: $NOTE_ID${NC}" >&2
    echo -e "${GREEN}Note Type: $NOTE_TYPE${NC}" >&2
    echo -e "${GREEN}Inline: $HAS_POSITION${NC}" >&2
    
    if [ "$NOTE_TYPE" = "DiffNote" ] && [ "$HAS_POSITION" = "true" ]; then
        echo "" >&2
        echo -e "${GREEN}✅ Inline comment posted successfully at $FILE_PATH:$LINE_NUMBER${NC}" >&2
        echo -e "${GREEN}URL: https://gitlab.com/$REPO/-/merge_requests/$MR_IID#note_$NOTE_ID${NC}" >&2
    else
        echo "" >&2
        echo -e "${YELLOW}⚠️  Warning: Comment was posted but may not be inline${NC}" >&2
        echo -e "${YELLOW}   Type: $NOTE_TYPE (expected: DiffNote)${NC}" >&2
        echo -e "${YELLOW}   Has position: $HAS_POSITION (expected: true)${NC}" >&2
    fi
    
    # Output JSON for programmatic use
    echo "$BODY"
else
    echo "" >&2
    echo -e "${RED}❌ Error: HTTP $HTTP_CODE${NC}" >&2
    echo "$BODY" | jq . >&2
    exit 1
fi
