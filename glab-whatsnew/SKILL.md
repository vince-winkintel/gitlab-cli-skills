---
name: glab-whatsnew
description: View GitLab CLI release notes with glab whatsnew. Use when checking what changed after upgrading glab, reviewing release notes since a baseline version, or asking what's new in the GitLab CLI. Triggers on whatsnew, what's new, release notes, glab upgrade notes, glab changelog since.
---

# glab whatsnew

View GitLab CLI release notes from the terminal.

## Quick start

```bash
# Show release notes since the last viewed/post-upgrade baseline, capped at 10 releases
glab whatsnew

# Show notes for the latest published release
glab whatsnew --latest

# Show notes for a specific release
glab whatsnew v1.102.0

# Show notes for every release after a baseline
glab whatsnew --since v1.100.0
```

## When to use

Use `glab whatsnew` after upgrading `glab` or before updating automation that depends on command behavior. It is the quickest CLI-native path for inspecting upstream release notes without opening a browser.

## Behavior notes

- With no arguments, `glab whatsnew` shows releases published since the last time you ran `whatsnew` or saw the post-upgrade banner.
- The implicit history is capped at the most recent 10 releases.
- Use `--since <version>` for deterministic automation or review work where you need an explicit baseline.
- Use `--latest` when you only care about the latest published release.

## Agent workflow

```bash
# Review all releases newer than the skill repo's last processed glab baseline
glab whatsnew --since v1.100.0

# Then inspect command help for any relevant new/changed command surfaces
glab repo prune --help
glab mr note create --help
glab stack sync --help
```

Do not treat release-note prose alone as a contract. For skill updates, verify changed command surfaces with `glab <command> --help` or upstream docs/source before editing guidance.

## Command reference

```text
glab whatsnew [version] [--flags]

Flags:
  --latest   Show release notes for the latest published release only
  --since    Show release notes for every release newer than this version
  -h --help  Show help for this command
```
