#!/usr/bin/env bash
# Refresh deterministic generated repository metadata for gitlab-cli-skills.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/refresh_skill.py" "$@"
