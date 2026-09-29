---
name: glab-govern
description: Configure and diagnose GitLab AI agent governance hooks and sync Claude Code session audit events with glab. Use when setting up glab govern, checking governance readiness, or explicitly syncing an agent session to GitLab. Triggers on glab govern, AI agent governance, agent audit, session audit, Claude hooks, govern doctor, govern audit sync.
---

# glab govern

Configure and operate GitLab's experimental AI agent governance support for external agents.

## Safety and scope

- `glab govern` is experimental; confirm the installed command surface before durable automation.
- `glab govern setup` changes `~/.claude/settings.json` by installing Claude Code `Stop` and `SessionEnd` hooks. Review that file before and after setup. The command is safe to rerun because it does not duplicate existing hooks.
- The generated hooks invoke `glab govern audit sync`; they apply to Claude Code, not automatically to Hermes, Codex, or other agents.
- `glab govern audit sync` reads local agent transcript entries and sends them to GitLab as audit events. Treat transcript content as potentially sensitive and do not sync until the target project, hostname, and visible GitLab actor are verified.
- Prefer `glab govern doctor` for read-only diagnosis before changing hook configuration or sending audit events.

## Setup and verification

```bash
# Inspect the current experimental command surface
glab govern --help
glab govern setup --help

# Configure Claude Code Stop and SessionEnd hooks interactively
glab govern setup

# Verify authentication, PATH, hooks, and API connectivity
glab govern doctor
```

Use `glab govern setup --yes` only after the hook change is approved and the target settings file has been reviewed. After setup, inspect `~/.claude/settings.json` and rerun `glab govern doctor`; do not treat a zero-exit setup alone as proof that hooks are usable.

## Manual audit sync

From a checkout whose Git remote resolves to the intended GitLab project:

```bash
glab auth status --hostname "$GITLAB_HOST"
glab api --hostname "$GITLAB_HOST" user
glab govern audit sync
```

For an explicit target, use the standard repository selector:

```bash
glab govern audit sync --repo my-group/my-project
```

Use `--complete` only when the session should be marked complete. `--silent` suppresses output for hook use; avoid it during initial setup and troubleshooting because it hides useful evidence.

## Target resolution

`glab govern audit sync` resolves the target in this order:

1. `-R/--repo` when provided. It accepts `OWNER/REPO`, `GROUP/NAMESPACE/REPO`, a full URL, or a Git URL.
2. The Git remote of the current directory.

Do not run it from an arbitrary checkout or rely on ambient shell identity. Verify the exact host, project, and actor immediately before the write.

## Troubleshooting

**`doctor` reports missing hooks:**
- Inspect `~/.claude/settings.json` for conflicting or malformed hook configuration.
- Rerun `glab govern setup` only after reviewing the proposed scope.
- Confirm the `glab` binary used by hooks is on the non-interactive `PATH`.

**Authentication or API connectivity fails:**
- Run `glab auth status --hostname <host>` and `glab api --hostname <host> user`.
- Re-authenticate the intended actor without printing token values.
- For self-managed GitLab, pass a full project URL or Git URL with `--repo` when ambient remote resolution is not sufficient.

**The wrong project would receive transcript data:**
- Stop before syncing.
- Use explicit `--repo`, or change to the intended checkout and verify its Git remote.
- Do not send a test transcript to an unrelated project just to validate connectivity.

## Command reference

See [references/commands.md](references/commands.md) for checksum-verified `govern`, `setup`, `doctor`, `audit`, and `audit sync` help.
