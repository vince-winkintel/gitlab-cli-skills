#!/usr/bin/env bash
# build-claude-skill.sh
#
# Generates claude-skill.zip — a single-SKILL.md zip suitable for upload to
# Claude.ai organization settings (which requires exactly one SKILL.md).
#
# Usage:
#   bash scripts/build-claude-skill.sh [--output <path>] [--root <repo-root>]
#
# Options:
#   --output  Path for the output zip file (default: ./claude-skill.zip)
#   --root    Repo root directory (default: directory of this script's parent)
#
# Output:
#   claude-skill.zip  containing a single merged SKILL.md
#
# The merged file includes:
#   1. The top-level SKILL.md (OpenClaw frontmatter stripped)
#   2. Each sub-skill SKILL.md in alphabetical order (frontmatter stripped)

set -euo pipefail

# ── Resolve paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_ZIP="$REPO_ROOT/claude-skill.zip"

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --output) OUTPUT_ZIP="$2"; shift 2 ;;
    --root)   REPO_ROOT="$2";  shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

# ── Temp workspace ────────────────────────────────────────────────────────────
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

MERGED="$WORK_DIR/SKILL.md"

# ── Helper: strip YAML frontmatter and emit content ───────────────────────────
# Frontmatter is the block between the first pair of `---` lines.
strip_frontmatter() {
  local file="$1"
  awk '
    BEGIN { in_front=0; done=0 }
    /^---$/ && !done {
      if (!in_front) { in_front=1; next }
      else           { in_front=0; done=1; next }
    }
    !in_front { print }
  ' "$file"
}

# ── Build merged SKILL.md ─────────────────────────────────────────────────────
echo "Building merged SKILL.md from $REPO_ROOT..."

# Required YAML frontmatter (Claude.ai requires name + description)
cat >> "$MERGED" <<'FRONTMATTER'
---
name: gitlab-cli-skills
description: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 37+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.
dependencies:
  - glab
---

FRONTMATTER

# Intro body
cat >> "$MERGED" <<'INTRO'
# GitLab CLI Skills — Comprehensive glab Reference

This skill provides complete reference and workflows for the GitLab CLI (`glab`).
It covers authentication, merge requests, CI/CD pipelines, issues, releases,
repositories, and 30+ other glab commands.

---

INTRO

# 1. Top-level skill (overview + routing) — strip its frontmatter since we wrote our own
TOP_LEVEL="$REPO_ROOT/SKILL.md"
if [[ -f "$TOP_LEVEL" ]]; then
  echo "## Overview" >> "$MERGED"
  echo "" >> "$MERGED"
  strip_frontmatter "$TOP_LEVEL" >> "$MERGED"
  echo "" >> "$MERGED"
  echo "---" >> "$MERGED"
  echo "" >> "$MERGED"
fi

# 2. Sub-skills in alphabetical order (any directory containing a SKILL.md,
#    excluding the root itself and the scripts/ directory)
SUB_SKILLS=()
while IFS= read -r skill_file; do
  SUB_SKILLS+=("$skill_file")
done < <(
  find "$REPO_ROOT" -mindepth 2 -maxdepth 2 -name "SKILL.md" \
    ! -path "$REPO_ROOT/scripts/*" \
    | sort
)

TOTAL=${#SUB_SKILLS[@]}
COUNT=0

for skill_file in "${SUB_SKILLS[@]}"; do
  sub_dir="$(basename "$(dirname "$skill_file")")"
  COUNT=$((COUNT + 1))
  echo "  [$COUNT/$TOTAL] $sub_dir"

  # Section heading derived from directory name (e.g. glab-mr → glab mr)
  heading="${sub_dir//-/ }"

  {
    echo "## $heading"
    echo ""
    strip_frontmatter "$skill_file"
    echo ""
    echo "---"
    echo ""
  } >> "$MERGED"
done

# ── Package into zip ──────────────────────────────────────────────────────────
# Claude.ai requires files inside a subdirectory, not at the zip root:
#   claude-skill.zip
#    └── gitlab-cli-skills/
#        └── SKILL.md
rm -f "$OUTPUT_ZIP"

# Use zip if available, otherwise fall back to python3 (always present)
if command -v zip &>/dev/null; then
  mkdir -p "$WORK_DIR/gitlab-cli-skills"
  cp "$MERGED" "$WORK_DIR/gitlab-cli-skills/SKILL.md"
  (cd "$WORK_DIR" && zip -qr "$OUTPUT_ZIP" gitlab-cli-skills/)
else
  python3 -c "
import zipfile, sys
output, source = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(source, 'gitlab-cli-skills/SKILL.md')
" "$OUTPUT_ZIP" "$MERGED"
fi

LINES=$(wc -l < "$MERGED")
SIZE=$(wc -c < "$MERGED")
echo ""
echo "✅ Done."
echo "   Merged:  $TOTAL sub-skills + top-level"
echo "   Lines:   $LINES"
echo "   Size:    $SIZE bytes"
echo "   Output:  $OUTPUT_ZIP"
