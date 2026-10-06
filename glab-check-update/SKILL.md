---
name: glab-check-update
description: Check for glab CLI updates and view latest version information. Use when checking if glab is up to date or finding available updates. Triggers on update glab, check version, glab version, CLI update.
---

# glab check-update

## Overview

Check for glab updates and report available updates for installed glab-managed GitLab Duo CLI and Orbit binaries.

## Quick start

```bash
glab check-update --help
```

## Update nudge behavior

`glab check-update` and its `glab update` alias always check when invoked explicitly. They now also report available updates for installed, glab-managed GitLab Duo CLI and Orbit binaries. Custom binary paths and managed binaries that are not installed are skipped. Automatic checks after other commands remain throttled to at most once every 24 hours and can be disabled with `glab config set check_update false`.

The update nudge is install-aware and agent-aware: when glab can detect the install method, it includes the matching upgrade command, and when a coding-agent environment is detected, it emits a compact bracketed line suitable for agents to relay instead of a multi-line human prompt. If the install method is unknown, expect only the release-notes URL rather than a guessed upgrade command.

## Subcommands

This command has no subcommands.

## Command reference

See [references/commands.md](references/commands.md) for checksum-verified `--help` output.
