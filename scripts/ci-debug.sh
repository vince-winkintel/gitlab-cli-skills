#!/bin/bash
# CI Debug Helper Script
# Automates: find failed jobs → show logs for each

set -e

PIPELINE_ID="$1"

if [ -z "$PIPELINE_ID" ]; then
    echo "Usage: $0 <PIPELINE_ID>"
    echo "Example: $0 12345"
    echo ""
    echo "To get pipeline ID for current branch:"
    echo "  glab ci status"
    exit 1
fi

echo "🔍 Fetching pipeline #$PIPELINE_ID..."

# Get pipeline status
PIPELINE_STATUS=$(glab ci view "$PIPELINE_ID" --json status -q .status 2>/dev/null || echo "unknown")

echo "Pipeline Status: $PIPELINE_STATUS"
echo ""

# Get failed jobs
echo "🔍 Finding failed jobs..."
FAILED_JOBS=$(glab ci view "$PIPELINE_ID" --json jobs -q '.jobs[] | select(.status=="failed") | .id' 2>/dev/null)

if [ -z "$FAILED_JOBS" ]; then
    echo "✅ No failed jobs found in pipeline #$PIPELINE_ID"
    exit 0
fi

echo "❌ Failed jobs found:"
echo "$FAILED_JOBS" | while read -r job_id; do
    JOB_NAME=$(glab ci view "$PIPELINE_ID" --json jobs -q ".jobs[] | select(.id==$job_id) | .name")
    echo "  - Job #$job_id: $JOB_NAME"
done
echo ""

# Show logs for each failed job
echo "📋 Fetching logs for failed jobs..."
echo "=================================="
echo ""

echo "$FAILED_JOBS" | while read -r job_id; do
    JOB_NAME=$(glab ci view "$PIPELINE_ID" --json jobs -q ".jobs[] | select(.id==$job_id) | .name")
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Job #$job_id: $JOB_NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Get last 50 lines of log (usually contains the error)
    glab ci trace "$job_id" 2>/dev/null | tail -n 50
    
    echo ""
    echo "Full logs: glab ci trace $job_id"
    echo ""
done

echo "=================================="
echo "Summary:"
echo "  Pipeline: #$PIPELINE_ID ($PIPELINE_STATUS)"
echo "  Failed jobs: $(echo "$FAILED_JOBS" | wc -l)"
echo ""
echo "Next steps:"
echo "  - Review error messages above"
echo "  - View full logs: glab ci trace <job-id>"
echo "  - Retry failed jobs: glab ci retry <job-id>"
echo "  - Retry entire pipeline: glab ci run"
