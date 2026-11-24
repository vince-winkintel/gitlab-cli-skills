---
name: glab-check-update
description: Check for updates to glab and installed glab-managed GitLab Duo CLI and Orbit binaries. Use when checking whether glab, Duo CLI, or Orbit is up to date or finding available updates. Triggers on update glab, check version, glab version, CLI update, Duo CLI update, orbit update.
---

# glab check-update

## Managed updates and public-client routing

Requires glab v1.132.0 or later for the behavior in this section. This is a source-backed summary; retained help captures keep their original immutable version and are not v1.132.0 binary verification.

`check-update` also reports the GitLab Endpoint Agent Platform when installed on Linux, alongside Duo and Orbit. Managed registry metadata lookups have a 15-second bound; failed attempted checks are timestamped, and fresh downloads stamp their check time. This avoids repeating an unreachable registry lookup on every normal run; explicit update operations remain separate changes.

Public glab release checks and `whatsnew` use the Factory's unauthenticated `gitlab.com` client. This client does not load a self-managed token or config-derived organization header. It does not expand permissions or authorize downloading/running a managed client.

Source: [check_update.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/update/check_update.go), [whatsnew.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/whatsnew/whatsnew.go), [factory.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/cmdutils/factory.go), [manager.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/binarymgr/manager.go), [runner.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/binarymgr/runner.go).

Historical captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

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
