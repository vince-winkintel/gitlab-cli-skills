#!/bin/bash
# MR Review Workflow Script
# Automates: checkout MR → run tests → post result as comment → approve if passed

set -e

MR_ID="$1"
TEST_COMMAND="${2:-npm test}"

if [ -z "$MR_ID" ]; then
    echo "Usage: $0 <MR_ID> [test_command]"
    echo "Example: $0 123"
    echo "Example: $0 123 'pnpm test'"
    exit 1
fi

# Validate MR_ID is numeric to prevent injection
if ! [[ "$MR_ID" =~ ^[0-9]+$ ]]; then
    echo "❌ Error: MR_ID must be a numeric value (got: $MR_ID)" >&2
    exit 1
fi

# Validate TEST_COMMAND against allowlist to prevent arbitrary code execution.
# eval is intentionally NOT used here — see SECURITY.md for rationale.
ALLOWED_COMMANDS=("npm test" "pnpm test" "yarn test" "make test" "cargo test" "go test ./..." "bundle exec rspec" "pytest" "mvn test" "gradle test")
COMMAND_ALLOWED=false
for allowed in "${ALLOWED_COMMANDS[@]}"; do
    if [[ "$TEST_COMMAND" == "$allowed" ]]; then
        COMMAND_ALLOWED=true
        break
    fi
done

if [ "$COMMAND_ALLOWED" = false ]; then
    echo "❌ Error: Test command not in allowlist: '$TEST_COMMAND'" >&2
    echo "" >&2
    echo "Allowed commands:" >&2
    for cmd in "${ALLOWED_COMMANDS[@]}"; do
        echo "  - $cmd" >&2
    done
    echo "" >&2
    echo "To add a new command, update the ALLOWED_COMMANDS array in this script." >&2
    exit 1
fi

echo "🔄 Checking out MR !$MR_ID..."
glab mr checkout "$MR_ID"

echo "🧪 Running tests: $TEST_COMMAND"
if $TEST_COMMAND; then
    echo "✅ Tests passed!"

    echo "📝 Adding approval comment..."
    glab mr note "$MR_ID" -m "✅ Tests passed locally - approving"

    echo "👍 Approving MR..."
    glab mr approve "$MR_ID"

    echo "✨ Review complete - MR approved"
else
    echo "❌ Tests failed!"

    echo "📝 Adding failure comment..."
    glab mr note "$MR_ID" -m "❌ Tests failed locally - please review

Test command: \`$TEST_COMMAND\`

See output above for details."

    echo "⚠️  Review complete - MR not approved due to test failures"
    exit 1
fi
