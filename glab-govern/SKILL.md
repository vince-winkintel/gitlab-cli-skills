---
name: glab-govern
description: Configure and diagnose GitLab AI agent governance hooks, fallback periodic sync, and explicitly approved Claude Code, OpenCode, Codex, or Cursor session audit uploads. Use for glab govern setup, govern doctor, and govern audit sync, including agent selection and uninstall.
---

# glab govern

Configure and operate GitLab's experimental AI agent governance support for external agents.

## Safety and scope

- Governance sync is an external data upload, not just local diagnostic logging. Uploaded events can include user prompts, tool-call arguments (commands, file paths, edits; replaced with a marker over 8 KB), outcomes/errors/durations, model, and token usage. Tool output and response text are not uploaded. Do not assume this excludes secrets in prompts or arguments.
- `glab govern setup` installs Claude Code `Stop` and `SessionEnd` hooks in `~/.claude/settings.json` and, by default, a durable fallback periodic sync job on macOS/Linux. Obtain approval for both the settings change and transcript upload scope before running setup.
- Use `--no-fallback-sync` for hooks only; the hooks still upload audit events. This is not a no-upload mode.
- `--agents codex,cursor` enables transcript discovery without agent hooks, including sessions from before enablement, for repositories on GitLab hosts you are logged in to. Enabling these agents needs explicit approval for historical uploads and all eligible repositories, not just the current checkout.
- This integration does not automatically govern Hermes. OpenCode hook-recorded sessions are supported and read through `opencode export`; setup's installed hooks are for Claude Code.
- Prefer `glab govern doctor` for read-only diagnosis. This refresh's help verification does not authorize running setup, sync, uninstall, or changing host services.

## Setup and verification

```bash
# Inspect the experimental surface without changing settings or uploading transcripts
glab govern --help
glab govern setup --help
glab govern audit sync --help
glab govern doctor
```

After reviewing the target host, visible GitLab actor, eligible repositories, and upload contents, choose exactly the approved setup scope:

```bash
# Hooks plus the default macOS/Linux fallback job
glab govern setup

# Hooks only, without a periodic sync job
glab govern setup --no-fallback-sync

# Explicitly include Codex and Cursor historical/local sessions
glab govern setup --agents codex,cursor
```

Use `--yes` only after the underlying change/upload scope is approved. Setup is rerunnable: existing hooks are not duplicated and the fallback job is replaced. The agent list replaces the previously enabled list; `--agents ""` stops Codex/Cursor discovery. Inspect the settings/job files and rerun `glab govern doctor` after changes.

## Fallback periodic sync

On macOS, setup installs `~/Library/LaunchAgents/com.gitlab.glab-govern-audit-sync.plist`. On Linux it installs the user timer `~/.config/systemd/user/glab-govern-audit-sync.timer`. The fallback job runs `glab govern audit sync --all` every 30 minutes (also 5 minutes after boot on Linux) until removed. It uses stored credentials and the glab configuration directory selected at setup. Windows has no fallback periodic sync.

`--all` sends each recorded/discovered session to its own project and host, not simply the current checkout or one `--repo` target. It marks sessions complete after 24 hours of inactivity. Claude Code sessions are paused while the glab Stop hook is missing. `doctor` reports fallback configuration and the last-run result.

A never-synced session inactive for 89 days is not uploaded. If an instance does not yet accept an agent's sessions, those sessions are skipped permanently; upgrading the instance does not backfill them, while sessions created after the upgrade are eligible.

## Manual audit sync

For current-session sync, first verify the intended actor, host, and project:

```bash
: "${GITLAB_HOST:?set GITLAB_HOST to the intended GitLab hostname}"
glab auth status --hostname "$GITLAB_HOST"
glab api --hostname "$GITLAB_HOST" user
# Upload only after the target and transcript scope have been approved
glab govern audit sync --repo my-group/my-project
```

The normal target comes from `-R/--repo` when supplied (namespace path, full URL, or Git URL), otherwise the current checkout's Git remote. Do not run from an arbitrary checkout. Use `--complete` only when the session should be completed. `--silent` hides output for hooks; avoid it during initial verification. Do not use `--all` as a harmless connectivity test.

Agent limitations:
- OpenCode does not send prompts/responses; an outcome is included only if the tool call was complete when first synced.
- Codex tool outcomes are reported as `completed`, not proven successful.
- Cursor sends only prompts and tool calls, timed by transcript modification; it has no outcome/token/timestamp records. Ambiguous workspace mappings or file calls outside the inferred workspace cause that session to be skipped rather than uploaded to the wrong project.

## Uninstall and pause

```bash
# After approving removal of the local job and agent discovery
glab govern setup --uninstall
```

Uninstall removes the fallback periodic job and stops Codex/Cursor sync, but leaves the Claude Code hooks in place. To stop hook-triggered uploads too, inspect and remove the exact `glab govern audit sync` hook entries from `~/.claude/settings.json`; preserve unrelated hooks/settings. Verify the resulting settings, absence of the exact job, and `doctor` output. `--no-fallback-sync` is a hooks-only setup option, not a replacement for uninstalling an already-installed fallback job.

## Troubleshooting

- Missing hooks: inspect the settings file and the glab executable's non-interactive `PATH`; rerun setup only within approved scope.
- Failed auth/connectivity: verify the intended actor using `glab auth status` and `glab api user`; never print tokens or upload a transcript just to test access.
- Unexpected uploads: inspect the fallback job, stored host credentials, agent list, and per-session repository mappings. Stop the approved job/hooks before changing credentials or project state.
- Wrong project or potentially sensitive prompts/arguments: stop before sync; do not treat outcome labels, omitted responses, or argument truncation as content redaction.

## Command reference

See [references/commands.md](references/commands.md) for complete checksum-verified parent, setup, doctor, audit, and audit-sync help.
