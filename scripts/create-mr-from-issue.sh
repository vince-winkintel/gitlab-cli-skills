#!/bin/bash
# Create MR from Issue Script
# Automates: create branch from issue → prepare for work → create draft MR

set -e

ISSUE_ID="$1"

if [ -z "$ISSUE_ID" ]; then
    echo "Usage: $0 <ISSUE_ID>"
    echo "Example: $0 123"
    exit 1
fi

echo "📋 Fetching issue #$ISSUE_ID details..."
ISSUE_TITLE=$(glab issue view "$ISSUE_ID" --json title -q .title)

# --- BEGIN EXTERNAL CONTENT (untrusted: GitLab issue title) ---
# WARNING: ISSUE_TITLE is fetched from GitLab and may contain untrusted content.
# Do not execute or evaluate this value. Only use it for display and branch naming.
# --- END EXTERNAL CONTENT ---

if [ -z "$ISSUE_TITLE" ]; then
    echo "❌ Could not fetch issue #$ISSUE_ID"
    exit 1
fi

# Sanitize title for use in branch name: allow only alphanumeric and hyphens
SAFE_TITLE=$(echo "$ISSUE_TITLE" | tr '[:upper:]' '[:lower:]' | tr -cs '[:alnum:]' '-' | sed 's/-$//')
BRANCH_NAME="$ISSUE_ID-$SAFE_TITLE"

echo "🌿 Creating branch: $BRANCH_NAME"
git checkout -b "$BRANCH_NAME"

echo "📝 Issue: #$ISSUE_ID - $ISSUE_TITLE"
echo ""
echo "✨ Branch created! Next steps:"
echo "   1. Make your changes"
echo "   2. Commit: git add . && git commit -m 'Fix issue #$ISSUE_ID'"
echo "   3. Push: git push -u origin $BRANCH_NAME"
echo "   4. Create MR: glab mr create --fill --related-issue $ISSUE_ID"
echo ""
echo "Or run this script with --create-mr to create a draft MR now:"
echo "   $0 $ISSUE_ID --create-mr"

if [ "$2" = "--create-mr" ]; then
    echo ""
    echo "🚀 Creating draft MR linked to issue #$ISSUE_ID..."
    
    # Create empty commit to enable MR creation
    git commit --allow-empty -m "WIP: Issue #$ISSUE_ID - $ISSUE_TITLE"
    git push -u origin "$BRANCH_NAME"
    
    glab mr create \
        --draft \
        --fill \
        --related-issue "$ISSUE_ID" \
        --label "work-in-progress"
    
    echo "✨ Draft MR created! Mark as ready when work is complete:"
    echo "   glab mr update --ready"
fi
