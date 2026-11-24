---
name: glab-govern
description: Manage glab minder and legacy glab govern. Configure and diagnose GitLab AI agent governance hooks, fallback periodic sync, and explicitly approved Claude Code, OpenCode, Codex, or Cursor session audit uploads. Use for glab minder setup, govern doctor, and govern audit sync, including agent selection and uninstall. Triggers on AI agent governance, agent audit, session audit, Claude hooks, OpenCode audit, Codex audit, Cursor audit, fallback sync, govern setup, govern doctor, govern audit sync, govern uninstall.
---

# glab minder (glab-govern skill)

Configure and operate GitLab's experimental AI agent governance support for external agents.

Historical captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

## Managed agent routing and session consent

Requires glab v1.132.0 or later for the behavior in this section. This is a source-backed summary; retained help captures keep their original immutable version and are not v1.132.0 binary verification.

`minder setup`, `doctor`, and `audit` remain built-in governance commands on supported platforms. Other arguments route to the managed `agent-client agent …`; execution of that client is supported only on Linux amd64/arm64. `minder update` and leading `--install`/`--update` manage the binary; `minder install` is instead a forwarded agent command. Installation, execution and governance setup/upload are separate approvals. Do not automatically install it, set auto-run/download preferences, or create agent trust/approval state.

Use `glab help minder` to inspect glab's own wrapper. `minder --help` can execute an already installed client, so it is not a glab-only inspection. Managed Minder downloads require a registry checksum; automatic compatibility is capped at major 1. A custom path skips managed checks. Registry metadata lookups are bounded to 15 seconds; failed update attempts are timestamped so ordinary repeated runs do not retry on every invocation. This does not authorize an update.

Fresh setup defaults to activity after each agent's first recorded setup, including only new turns of resumed sessions. `--include-history` explicitly includes the last 89 days for newly set-up agents; already recorded agents retain their prior scope. Earlier installations with no recorded setup time retain historical upload behavior until an approved setup runs again. Setup prompts describe local records (session IDs, transcript paths and sync positions), agents, changes and uploads; `--yes` consents to that full scope. Never infer consent from running another command or upgrading glab.

Cursor has no event timestamps: setup records existing transcript ends, and later appended activity is eligible. A copied chat with a new ID counts as new and can upload in full. Manual `audit sync --hook cursor` accepts Cursor stop/sessionEnd JSON and launches silent background sync; setup still does not install Cursor or Codex hooks. Cursor workspace mapping must be unambiguous; sessionEnd does not immediately complete a session (24-hour idle completion applies). Approve any separately installed hook and its upload scope.

Removing owned Claude hooks or the OpenCode plugin pauses even already-open sessions' single-session sync, as well as fallback sync. Uninstall removes local session records last, after removing the writers, and forgets setup times/selection; unreadable hook/plugin state can retain records for a later approved retry. This does not delete audit data already uploaded to GitLab. Active discovered sessions without a GitLab remote are reported as skipped. Project-splitting types and tests are groundwork, not an enabled per-entry routing feature: sync still posts each session to its recorded project. Audit event IDs use SHA-256-derived UUIDv8 instead of SHA-1 UUIDv5; consumers must not assume the older derivation or replay transcripts to migrate IDs. Shared redaction retains its best-effort limits; moving it to a shared module does not broaden secret coverage.

Source: [minder.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/minder/minder.go), [minder.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/binarymgr/binaries/minder.go), [setup.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/govern/setup/setup.go), [since_setup.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/govern/audit/sync/since_setup.go), [hook.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/govern/audit/sync/hook.go), [sync.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/govern/audit/sync/sync.go), [parts.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/govern/audit/sync/parts.go).

## Codex Stop-hook ingestion and sync limits

`minder audit sync --hook codex` accepts the JSON supplied on stdin by a Codex Stop hook, including the session ID, transcript path, and working directory. It starts a detached sync in the session's directory, prints nothing, and returns success even when hook input or background startup fails; success is not evidence of upload. It cannot be combined with `--all`, `--complete`, or `--repo`. Codex must already be enabled. Setup still configures Codex/Cursor as discovery-only agents and does not install a Codex hook; the existing fallback-sync requirements remain. A separately configured Stop hook needs explicit authorization for both the settings change and transcript upload scope.

Transcript readers retain each entry's working directory where the source provides it (including Codex turn context and tool-specific working directories). This is internal transcript metadata, not a promise of a new audit-event `cwd` field or automatic per-entry project routing. A session started without a GitLab remote is retained for diagnostics as unsynced. When it later gains a GitLab project, prior activity is skipped before recording that target; do not expect backfill of activity from the earlier folder.

Audit batching accounts for JSON-encoded size: up to 500 events, 4,500 JSON elements, and a 4 MiB request target below GitLab's 5 MB body limit. Large prompt content is truncated, oversized tool arguments are replaced, and event details have their own encoded-size limit. On supported JSON-limit errors, batches split; an individually unpostable event can be skipped and counted. With fallback sync installed, a hook leaves this work for fallback. Earlier successful batches remain posted and are deduplicated on replay. Use doctor/status to assess partial uploads; do not relax upload approval or manually resend entire transcripts.

## Credential redaction and audit schema

Credential-like JSON keys include names such as `OPENAI_API_KEY`, `PGPASSWORD`, `openaiApiKey`, and `accessToken` (camelCase/acronym word boundaries are recognized); pagination tokens and `PWD` holding a path are excluded. Text assignments to credential-like names are also redacted when their values match the length/content heuristic (at least eight characters and a digit); scanning a long value is bounded to 256 characters. Unknown formats, short values, and remaining suffixes can still leak. This does not make transcript upload safe by default or sanitize local files.

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
- `--agents codex,cursor` enables transcript discovery without agent hooks for repositories on GitLab hosts you are logged in to. Before glab v1.132.0, enabling these agents also uploads pre-existing sessions from the last 89 days and requires explicit approval for historical uploads. With glab v1.132.0 or later, the setup-time/history rules above apply; an older fallback-job binary can still use historical discovery, so inspect doctor version-drift diagnostics before approving the scope. Enabling these agents needs explicit approval for the selected upload times and all eligible repositories, not just the current checkout.
- This integration does not automatically govern Hermes. `--agents opencode` installs a global OpenCode plugin with upload scope across every OpenCode project; obtain explicit approval for that scope.
- Prefer `glab minder doctor` for read-only diagnosis. Help inspection does not authorize running setup, sync, uninstall, or changing host services.

## Setup and verification

```bash
# Inspect the experimental surface without changing settings or uploading transcripts
glab help minder
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

# Enable Codex and Cursor only within the approved upload scope (including history on older glab)
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

Uninstall removes the installed Claude Code hooks, glab-owned OpenCode plugin, and fallback periodic job, and stops Codex/Cursor syncing; unrelated hooks and settings are preserved. With glab v1.132.0 or later it also removes local session records; older versions do not provide that cleanup. If settings cannot be read, removal of other components can still occur while hook removal fails. Review warnings, repair the settings, and rerun the approved uninstall before considering capture stopped. Verify the resulting settings, absence of the exact job, and `doctor` output. `--no-fallback-sync` is a hooks/plugin setup option, not a replacement for uninstalling an already-installed fallback job.

## Troubleshooting

- Missing hooks: inspect the settings file and the glab executable's non-interactive `PATH`; rerun setup only within approved scope.
- Failed auth/connectivity: verify the intended actor using `glab auth status` and `glab api user`; never print tokens or upload a transcript just to test access.
- Unexpected uploads: inspect the fallback job, stored host credentials, agent list, and per-session repository mappings. Stop the approved job/hooks before changing credentials or project state.
- Wrong project or potentially sensitive prompts/arguments: stop before sync; do not treat outcome labels, omitted responses, or argument truncation as content redaction.

## Command reference

See [historical captured help](references/help-206ebab4f.md) for complete checksum-verified parent, setup, doctor, audit, and audit-sync help.
