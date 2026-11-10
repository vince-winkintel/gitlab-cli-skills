---
name: glab-govern
description: Manage glab minder and legacy glab govern. Configure and diagnose GitLab AI agent governance hooks, fallback periodic sync, and explicitly approved Claude Code, OpenCode, Codex, or Cursor session audit uploads. Use for glab minder setup, govern doctor, and govern audit sync, including agent selection and uninstall. Triggers on AI agent governance, agent audit, session audit, Claude hooks, OpenCode audit, Codex audit, Cursor audit, fallback sync, govern setup, govern doctor, govern audit sync, govern uninstall.
---

# glab minder (glab-govern skill)

Configure and operate GitLab's experimental AI agent governance support for external agents.

## Credential redaction and audit schema

Credential-like JSON keys include names such as `OPENAI_API_KEY` and `PGPASSWORD`; pagination tokens and `PWD` holding a path are excluded. Text assignments to credential-like names are also redacted when their values match the length/content heuristic (at least eight characters and a digit); scanning a long value is bounded to 256 characters. Unknown formats, short values, and remaining suffixes can still leak. This does not make transcript upload safe by default or sanitize local files.

Audit events use Duo Agent Platform names such as `ai_tool_invoked`, `ai_tool_response_received`, `ai_tool_execution_failed`, `ai_user_input_received`, and `ai_llm_response_received`. Details use `agent_name`, `tool_args`, `content`, `content_length`, `model_name`, `prompt_token_count`, and `completion_token_count`; tool outcomes, namespace, call IDs, and duration remain. Consumers must use the current schema rather than assuming old key names. Approval still covers the actual prompts, arguments, and metadata uploaded.

## Command compatibility

Use `glab minder` for current operations. `glab govern` is a hidden compatibility command retained for existing hooks, OpenCode plugins, and periodic sync; do not rename installed `glab-govern` filenames or recreate services just to match the new command name. This standalone skill keeps its `glab-govern` installation name and covers both spellings. All existing setup, uninstall, historical-discovery, and transcript-upload approval gates still apply.

## OpenCode integration and diagnosis

After explicit approval, `glab minder setup --agents opencode` installs `~/.config/opencode/plugins/glab-govern.js` (or `$XDG_CONFIG_HOME/opencode/plugins/glab-govern.js`) for OpenCode 1.4 or later on macOS/Linux. OpenCode loads it for all sessions in every project and syncs each session when it goes idle. Sessions use their own GitLab host/project mappings. OpenCode 2 uses `opencode session export`; earlier supported releases use `opencode export`.

Later setup runs keep a previously selected glab-owned plugin current even if `opencode` is omitted. Only `setup --uninstall` removes it. A foreign file at the destination is not overwritten or removed; resolve it deliberately before an approved installation. `--no-fallback-sync` still installs/runs the plugin and does not remove an existing periodic job. Plugin installation and transcript uploads require approval independently of reading help or doctor output. Installation can partly succeed; inspect hooks, plugin, and job after any failure.

Doctor reports agent-neutral hook/session status, OpenCode detection and plugin state, and background sync outcomes. Project lookup 404s are reported separately as projects not found, not generic sync errors; sessions are retained for a later run. Deleted/inaccessible projects and missing job credentials can all cause this. Failed hosts without credentials are called out; an unreadable/locked keyring remains an error. When AI Governance is off, ask a group Owner or administrator to enable it; it is unavailable for personal projects on GitLab.com. Do not change project settings or upload a transcript merely to clear a diagnostic.

## Session and tool metadata

New governance sessions include `glab_version` and the transcript's `agent_version` when available. Claude Code records supply their version, Codex uses `session_meta.cli_version`, and OpenCode uses the export's `info.version`; Cursor supplies no version. Empty values and values longer than 255 characters after trimming are omitted. These are informational metadata, not proof of task success; this creation path does not send a separate version-metadata update for an existing session.

Codex tool-call events and their matched results include `tool_namespace` when present, and qualify the tool name as `<namespace>__<name>`. A trailing `__` separator is removed from the recorded namespace; an all-underscore namespace becomes empty. Built-in tools without a namespace retain their bare names. Treat this metadata as part of the approved transcript-upload scope, alongside prompts and tool arguments.

## Redaction and incomplete transcripts

Before upload, glab applies pattern-based redaction to session goals, user prompts, tool-result errors, and tool-call arguments. Valid JSON arguments are walked for recognized secrets in string values and keys; redacted arguments are re-encoded. Goal redaction happens before goal truncation. Recognized common secret formats are replaced with typed markers such as `[REDACTED:credential]`; unknown formats and sensitive content outside those patterns can remain. This is not a blanket secret-safety guarantee and does not scrub local transcript files. Review the upload scope and obtain approval even when redaction is enabled; never upload a transcript just to test the filter.

Claude Code JSONL parsing defers a final line without a newline, even if its JSON is already complete, so a later sync can read the finished entry. Earlier complete entries can still sync. Malformed newline-terminated JSON is still skipped; this is not recovery for arbitrary corrupt transcripts. A successful sync does not prove an unfinished final entry was uploaded. Do not modify an active transcript to force it through sync.

## Safety and scope

- Governance sync is an external data upload, not just local diagnostic logging. Uploaded data can include user prompts, tool-call arguments (commands, file paths, edits; replaced with a marker over 8 KB), outcomes/errors/durations, model, token usage, version metadata, and Codex tool namespaces. Tool output and response text are not uploaded. Pattern-based redaction reduces some exposure but does not guarantee these fields are free of secrets.
- On a fresh setup without an agent selection, `glab minder setup` selects Claude Code, installs its `Stop` and `SessionEnd` hooks in `~/.claude/settings.json`, and installs a durable fallback periodic sync job on macOS/Linux. Later runs reuse the previously selected agents. Obtain approval for both the settings change and transcript upload scope before running setup.
- Use `--no-fallback-sync` to install selected hooks/plugins without installing or replacing the fallback job. By itself it does not remove an existing job or clear stored agents; verify those separately before treating the machine as hooks-only. The hooks still upload audit events. This is not a no-upload mode.
- `--agents codex,cursor` enables transcript discovery without agent hooks, including sessions from before enablement, for repositories on GitLab hosts you are logged in to. Enabling these agents needs explicit approval for historical uploads and all eligible repositories, not just the current checkout.
- This integration does not automatically govern Hermes. `--agents opencode` installs a global OpenCode plugin with upload scope across every OpenCode project; obtain explicit approval for that scope.
- Prefer `glab minder doctor` for read-only diagnosis. Help inspection does not authorize running setup, sync, uninstall, or changing host services.

## Setup and verification

```bash
# Inspect the experimental surface without changing settings or uploading transcripts
glab minder --help
glab minder setup --help
glab minder audit sync --help
glab minder doctor
```

After reviewing the target host, visible GitLab actor, eligible repositories, and upload contents, choose exactly the approved setup scope:

```bash
# Previously selected agents (Claude Code on a fresh setup) plus fallback sync
glab minder setup

# Select Claude Code hooks without installing/replacing the job (existing agents/jobs remain)
glab minder setup --agents claude-code --no-fallback-sync

# Explicitly include Codex and Cursor historical/local sessions
glab minder setup --agents codex,cursor
```

`--agents` accepts `claude-code`, `opencode`, `codex`, and `cursor`, comma-separated or repeated. Explicit selection adds to the existing hook/plugin and discovery lists; it never narrows the selection. On a fresh machine `--agents opencode` selects OpenCode without implicitly adding Claude Code. Omitting `--agents` reuses the recorded selection, defaulting to Claude Code only when no agents were set up. Setup also recognizes earlier installed hooks/plugins when no recorded selection exists.

`--agents opencode --no-fallback-sync` installs the selected plugin without installing/replacing the job. Explicit Codex/Cursor selection cannot be combined with `--no-fallback-sync`; they rely on the fallback job. A retained discovery-only selection without hooks/plugins is also rejected with that flag. If hooks/plugins and stored discovery already coexist, `--no-fallback-sync` can leave discovery and an existing job intact. It is never a way to narrow upload scope.

Use `--yes` only after approving the complete retained and added upload scope. Existing hooks are not duplicated and ordinary setup replaces the fallback job. An empty `--agents ""` is invalid. To remove an agent, explicitly approve `setup --uninstall`, verify removal, then separately approve setup with exactly the desired agents. Uninstall forgets the selection, so the next setup without `--agents` defaults to Claude Code again. `--agents` and `--uninstall` are mutually exclusive. Inspect settings/plugin/job files and rerun `glab minder doctor` after changes. A failed fallback installation can leave the previous job removed while other installation steps remain; do not assume the “Setup complete” line means every component succeeded.

## Fallback periodic sync

On macOS, setup installs `~/Library/LaunchAgents/com.gitlab.glab-govern-audit-sync.plist`. On Linux it installs the user timer `~/.config/systemd/user/glab-govern-audit-sync.timer`. The fallback job runs `glab minder audit sync --all` every 30 minutes (also 5 minutes after boot on Linux) until removed. It uses stored credentials and the glab configuration directory selected at setup. Windows has no fallback periodic sync.

`--all` sends each recorded/discovered session to its own project and host, not simply the current checkout or one `--repo` target. It marks sessions complete after 24 hours of inactivity. Claude Code sessions are paused while the glab Stop hook is missing; OpenCode sessions are paused while the glab plugin is missing. `doctor` reports fallback configuration, the last-run result, and whether the job's configured glab binary reports a different version from the running CLI. A drift warning recommends rerunning setup; that is a settings/job change requiring the same upload-scope approval, not an automatic repair.

A never-synced session inactive for 89 days is not uploaded. If an instance does not yet accept an agent's sessions, those sessions are skipped permanently; upgrading the instance does not backfill them, while sessions created after the upgrade are eligible.

## Manual audit sync

For current-session sync, first verify the intended actor, host, and project:

```bash
: "${GITLAB_HOST:?set GITLAB_HOST to the intended GitLab hostname}"
glab auth status --hostname "$GITLAB_HOST"
glab api --hostname "$GITLAB_HOST" user
# Upload only after the target and transcript scope have been approved
glab minder audit sync --repo "https://$GITLAB_HOST/my-group/my-project"
```

The normal target comes from `-R/--repo` when supplied (namespace path, full URL, or Git URL), otherwise the current checkout's Git remote. Do not run from an arbitrary checkout. Use `--complete` only when the session should be completed. `--silent` hides output for hooks; avoid it during initial verification. Do not use `--all` as a harmless connectivity test.

Agent limitations:
- OpenCode does not send prompts/responses; an outcome is included only if the tool call was complete when first synced.
- Codex tool outcomes are reported as `completed`, not proven successful.
- Cursor sends only prompts and tool calls, timed by transcript modification; it has no outcome/token/timestamp records. Ambiguous workspace mappings or file calls outside the inferred workspace cause that session to be skipped rather than uploaded to the wrong project.

## Uninstall and pause

```bash
# After approving removal of the local job and agent discovery
glab minder setup --uninstall
```

Uninstall removes the installed Claude Code hooks, glab-owned OpenCode plugin, and fallback periodic job, and stops Codex/Cursor syncing; unrelated hooks and settings are preserved. If settings cannot be read, removal of other components can still occur while hook removal fails. Review warnings, repair the settings, and rerun the approved uninstall before considering capture stopped. Verify the resulting settings, absence of the exact job, and `doctor` output. `--no-fallback-sync` is a hooks/plugin setup option, not a replacement for uninstalling an already-installed fallback job.

## Troubleshooting

- Missing hooks: inspect the settings file and the glab executable's non-interactive `PATH`; rerun setup only within approved scope.
- Failed auth/connectivity: verify the intended actor using `glab auth status` and `glab api user`; never print tokens or upload a transcript just to test access.
- Unexpected uploads: inspect the fallback job, stored host credentials, agent list, and per-session repository mappings. Stop the approved job/hooks before changing credentials or project state.
- Wrong project or potentially sensitive prompts/arguments: stop before sync; do not treat outcome labels, omitted responses, or argument truncation as content redaction.

## Command reference

See [references/commands.md](references/commands.md) for complete checksum-verified parent, setup, doctor, audit, and audit-sync help.
