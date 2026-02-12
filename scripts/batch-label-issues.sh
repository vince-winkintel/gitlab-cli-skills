#!/bin/bash
# Batch Label Issues Script
# Automates: apply labels to multiple issues at once

set -e

LABEL="$1"
shift
ISSUE_IDS=("$@")

if [ -z "$LABEL" ] || [ ${#ISSUE_IDS[@]} -eq 0 ]; then
    echo "Usage: $0 <label> <issue_id1> [issue_id2] [issue_id3] ..."
    echo "Example: $0 bug 123 456 789"
    echo "Example: $0 'priority::high' 100 101 102"
    exit 1
fi

echo "🏷️  Applying label '$LABEL' to ${#ISSUE_IDS[@]} issue(s)..."
echo ""

SUCCESS_COUNT=0
FAIL_COUNT=0

for issue_id in "${ISSUE_IDS[@]}"; do
    echo -n "Issue #$issue_id... "
    
    if glab issue update "$issue_id" --label "$LABEL" >/dev/null 2>&1; then
        echo "✅"
        ((SUCCESS_COUNT++))
    else
        echo "❌ (failed)"
        ((FAIL_COUNT++))
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Summary:"
echo "  Label applied: '$LABEL'"
echo "  Successful: $SUCCESS_COUNT"
echo "  Failed: $FAIL_COUNT"
echo "  Total: ${#ISSUE_IDS[@]}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $FAIL_COUNT -gt 0 ]; then
    echo ""
    echo "⚠️  Some issues failed. Possible reasons:"
    echo "  - Issue doesn't exist"
    echo "  - Insufficient permissions"
    echo "  - Invalid label name"
    exit 1
fi
