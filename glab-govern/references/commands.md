# glab govern command reference

> Capture key `d43ccacec`: checksum-verified macOS arm64 release binary, source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`, binary archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`. Marked help preserves all renderer output except trailing spaces/tabs; unmarked blocks retain their stated older provenance.

> Only the unmarked historical help blocks were captured from the checksum-verified glab v1.122.0 macOS arm64 release binary. In those blocks, only terminal padding/trailing whitespace is removed; renderer wrapping and example truncation are preserved. Archive SHA-256: `cbdd6e28d35f9eb09aef79ad23d2712d67c9254677a60ed6d701b5362f659fef`. No product-spelling substitutions were needed in those captures. The marked `govern setup` block follows capture key `d43ccacec` above.

## govern

```text

  Manage AI agent governance for external agents running against GitLab projects. Configure hooks and diagnose setup
  issues.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern <command> [command] [--flags]

  COMMANDS

    audit <command> [command]  Manage AI agent audit events and sessions. (EXPERIMENTAL)
    doctor                     Diagnose AI agent governance configuration, authentication, and hook setup. (EXPERIMENTAL)
    setup [--flags]            Configure this machine to record AI agent sessions. (EXPERIMENTAL)

  FLAGS

    -h --help                  Show help for this command.

```

## govern setup

> Capture `d43ccacec` (key above).

```text

  Configure the current machine for AI agent governance session capture.

  Installs the following:

  - Stop hook in `~/.claude/settings.json`, which syncs the session after every agent turn.
  - SessionEnd hook in `~/.claude/settings.json`, which syncs the session and marks it completed.
  - Fallback periodic sync: a launchd agent (`~/Library/LaunchAgents/com.gitlab.glab-govern-audit-sync.plist`) on macOS,
  or a systemd user timer (`~/.config/systemd/user/glab-govern-audit-sync.timer`) on Linux.

  The fallback periodic sync runs `glab govern audit sync --all` every 30 minutes, and on Linux also 5 minutes after
  boot, until you remove it. It uploads anything the hooks missed for sessions they have already recorded (see `glab
  govern audit sync --help` for what is uploaded), using your stored glab credentials and the glab configuration
  directory in use when you run setup. Each session goes to the project and host of the Git repository the agent ran in.
  It also marks sessions completed once they have been idle for 24 hours. It pauses Claude Code sessions while the hooks
  are not installed. Pass `--no-fallback-sync` to install only the hooks. The fallback periodic sync is not available on
  Windows.

  Pass `--agents codex,cursor` to also sync Codex and Cursor sessions. glab installs no hooks for those agents: the
  fallback periodic sync finds their sessions by scanning their transcripts in `~/.codex/sessions` and
  `~/.cursor/projects`, including sessions from before you enabled them, and uploads those from repositories on GitLab
  hosts you are logged in to with glab. Their sessions are marked completed once they have been idle for 24 hours. Run
  setup again with a different `--agents` list to change which agents are synced, or with `--agents ""` to stop. Every
  setup prompt names the agents that are synced, and `--uninstall` also stops syncing them.

  Safe to run multiple times: existing hooks are not duplicated, and an existing fallback periodic sync job is replaced.
  Run `glab govern doctor` afterwards to verify the setup.

  Run `glab govern setup --uninstall` to remove everything setup installed: the hooks, the fallback periodic sync job,
  and Codex and Cursor session syncing. Other hooks and settings in `~/.claude/settings.json` are left unchanged.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern setup [--flags]

  EXAMPLES

    # Configure hooks and the fallback periodic sync
    $ glab govern setup

    # Configure only the hooks
    $ glab govern setup --no-fallback-sync

    # Also sync Codex and Cursor sessions through the fallback periodic sync
    $ glab govern setup --agents codex,cursor

    # Remove the hooks and the fallback periodic sync
    $ glab govern setup --uninstall

  FLAGS

    --agents            Also sync sessions from these agents, found by the fallback periodic sync without hooks: codex, cursor. Replaces the agents enabled by an earlier run. Multiple agents can be comma-separated or specified by repeating the flag.
    -h --help           Show help for this command.
    --no-fallback-sync  Install only the hooks, without the fallback periodic sync job.
    --uninstall         Remove the hooks and the fallback periodic sync job, and stop syncing Codex and Cursor sessions.
    -y --yes            Skip confirmation prompt.

```

## govern doctor

```text

  Check that AI agent governance is correctly configured on this machine.

  Verifies:

  - Authentication: glab is authenticated with a valid token
  - glab in PATH: the binary is findable so hooks will work
  - Claude Code hooks: Stop and SessionEnd hooks are installed
  - API connectivity: can reach the GitLab API
  - Fallback periodic sync: whether the scheduled job is installed and loaded, whether the glab binary it runs still
  exists, and the result of its last run

  Outputs a clear remediation command for any check that fails.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern doctor [--flags]

  EXAMPLES

    # Check AI agent governance configuration on this machine
    $ glab govern doctor

  FLAGS

    -h --help  Show help for this command.

```

## govern audit

```text

  Manage audit events and sessions for external AI agents.
  Sync session data from local agent transcripts to GitLab.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern audit <command> [command] [--flags]

  COMMANDS

    sync [--flags]  Sync agent session data to GitLab. (EXPERIMENTAL)

  FLAGS

    -h --help       Show help for this command.

```

## govern audit sync

```text

  Read new entries from the local agent transcript since the last sync and POST them to GitLab as audit events.

  The audit events contain the prompts you type, each tool call with its arguments (such as commands, file paths, and
  edits, replaced with a marker when over 8 KB), each tool call's outcome, duration, and error message, and the model
  and token usage of each response. Tool output and the text of responses are not sent. A session that has never synced
  and has had no activity in the last 89 days is not uploaded, because GitLab does not accept events that old.

  Some agents record less:

  - OpenCode: prompts and responses are not sent, and a tool call's outcome is sent only if the call had finished when
  it was first synced.
  - Codex: a tool call's outcome is "completed", because Codex does not record whether it succeeded.
  - Cursor: only prompts and tool calls are sent, timed by the transcript's last modification, because Cursor records no
  results, token usage, or timestamps. A Cursor session is not synced if the files its tool calls read or write are
  outside the workspace glab finds, or if several directories match the workspace's name and those files don't show
  which, so that it is not uploaded to the wrong project.

  If a GitLab instance does not accept an agent's sessions yet, they are not uploaded, then or after the instance is
  upgraded. Sessions from after the upgrade are.

  Called by the Stop hook after every agent turn. Also used by the SessionEnd hook (with `--complete`) to mark the
  session as complete. The hooks also record the session's project, host, and transcript location so that `--all` can
  sync it later.

  Project is resolved from the Git remote of the current directory, or overridden with `-R/--repo`.

  With `--all`, syncs every session the hooks have recorded, each to the project and host it was recorded with. Sessions
  inactive for 24 hours are marked completed. Claude Code sessions are skipped while the glab Stop hook is missing from
  `~/.claude/settings.json`, so removing the hooks pauses them. The fallback periodic sync installed by `glab govern
  setup` runs this, and `glab govern doctor` shows the result of its last run.

  Supports Claude Code and OpenCode sessions recorded by hooks. OpenCode sessions are read with `opencode export`. With
  `--all`, it also finds and syncs the sessions of agents enabled with `glab govern setup --agents` (Codex and Cursor)
  by scanning their transcripts, for repositories on GitLab hosts glab is logged in to.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern audit sync [--flags]

  EXAMPLES

    # Sync the current agent session to GitLab
    $ glab govern audit sync

    # Sync and mark the session as completed
    $ glab govern audit sync --complete

    # Sync against a specific project
    $ glab govern audit sync -R my-group/my-project

    # Sync every recorded session that has unsynced activity
    $ glab govern audit sync --all

  FLAGS

    --all       Sync all sessions recorded by the hooks. Used by the fallback periodic sync.
    --complete  Mark the session as completed. Used by the SessionEnd hook.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --silent    Suppress all output. Used when invoked from hooks.

```
