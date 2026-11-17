# Captured glab-govern help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab govern

<!-- help-capture: 206ebab4f:66671cef03bb -->

```text

  Manage AI governance. (EXPERIMENTAL)

  USAGE

    glab govern <command> [command] [--flags]

  COMMANDS

    audit <command> [command]  Manage AI agent audit events and sessions. (EXPERIMENTAL)
    doctor                     Diagnose AI governance configuration, authentication, and hook setup. (EXPERIMENTAL)
    setup [--flags]            Configure this machine to record AI agent sessions. (EXPERIMENTAL)

  FLAGS

    -h --help                  Show help for this command.

```

## glab govern audit

<!-- help-capture: 206ebab4f:d56440b7eb54 -->

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

## glab govern audit sync

<!-- help-capture: 206ebab4f:304e0816f25c -->

```text

  Read new entries from the local agent transcript since the last sync and POST them to GitLab as audit events.

  The audit events contain the prompts you type, each tool call with its arguments (such as commands, file paths, and
  edits, replaced with a marker when over 8 KB), each tool call's outcome, duration, and error message, and the model
  and token usage of each response. Tool output and the text of responses are not sent.

  Before anything is sent, glab replaces common secret formats with a marker such as `[REDACTED:gitlab_token]`: GitLab,
  GitHub, Slack, npm and PyPI tokens, AWS, Google, Stripe, OpenAI and Anthropic API keys, JWTs, private keys,
  credentials in Authorization and token headers or under credential-like keys, and passwords in URLs. This is best
  effort: other secrets in prompts, commands, or file contents are sent as they are.

  When glab creates a session on GitLab, it also sends the glab version and the agent's version. A session that has
  never synced and has had no activity in the last 89 days is not uploaded, because GitLab does not accept events that
  old.

  Some agents record less:

  - OpenCode: prompts and responses are not sent, and a tool call's outcome is sent only if the call had finished when
  it was first synced.
  - Codex: a tool call's outcome is "completed", because Codex does not record whether it succeeded.
  - Cursor: only prompts and tool calls are sent, timed by the transcript's last modification, because Cursor records no
  results, token usage, timestamps, or version. A Cursor session is not synced if the files its tool calls read or write
  are outside the workspace glab finds, or if several directories match the workspace's name and those files don't show
  which, so that it is not uploaded to the wrong project.

  If a GitLab instance does not accept an agent's sessions yet, they are not uploaded, then or after the instance is
  upgraded. Sessions from after the upgrade are.

  Called by the Stop hook after every agent turn. Also used by the SessionEnd hook (with `--complete`) to mark the
  session as complete. The hooks also record the session's project, host, and transcript location so that `--all` can
  sync it later.

  With `--hook codex`, reads the session from the JSON that a Codex Stop hook gets on stdin, and syncs it with a glab
  started in the background, so Codex does not wait for the upload. It prints nothing, because Codex reads a Stop hook's
  output as a reason to continue. The project is resolved from the session's directory.

  Project is resolved from the Git remote of the current directory, or overridden with `-R/--repo`.

  With `--all`, syncs every session the hooks have recorded, each to the project and host it was recorded with. Sessions
  inactive for 24 hours are marked completed. Sessions from agents that use hooks are skipped while the glab hooks are
  missing, so removing the hooks pauses them. The fallback periodic sync installed by `glab minder setup` runs this, and
  `glab minder doctor` shows the result of its last run.

  Supports Claude Code, OpenCode, Codex, and Cursor sessions. OpenCode sessions are read with `opencode session export`,
  or `opencode export` before OpenCode 2. With `--all`, it also finds and syncs the sessions of Codex and Cursor, when
  they are enabled with `glab minder setup --agents`, by scanning their transcripts, for repositories on GitLab hosts
  glab is logged in to.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern audit sync [--flags]

  EXAMPLES

    # Sync the current agent session to GitLab
    $ glab minder audit sync

    # Sync and mark the session as completed
    $ glab minder audit sync --complete

    # Sync against a specific project
    $ glab minder audit sync -R my-group/my-project

    # Sync every recorded session that has unsynced activity
    $ glab minder audit sync --all

  FLAGS

    --all       Sync all sessions recorded by the hooks. Used by the fallback periodic sync.
    --complete  Mark the session as completed. Used by the SessionEnd hook.
    -h --help   Show help for this command.
    --hook      Read the session from the stdin of this agent's hook, and sync it in the background: codex. Used by the Codex Stop hook.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --silent    Suppress all output. Used when invoked from hooks.

```

## glab govern doctor

<!-- help-capture: 206ebab4f:5a77a4d42ad5 -->

```text

  Check that AI governance is correctly configured on this machine.

  Verifies:

  - Authentication: glab is authenticated with a valid token
  - glab in PATH: the binary is findable so hooks will work
  - Agent session hooks: if Claude Code sessions are synced, the Stop and SessionEnd hooks are installed
  - OpenCode plugin: if OpenCode sessions are synced, the glab plugin is installed and up to date
  - API connectivity: can reach the GitLab API
  - Fallback periodic sync: whether the scheduled job is installed and loaded, whether the glab binary it runs still
  exists and is the same build as this glab, and the result of its last run

  Outputs a clear remediation command for any check that fails.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern doctor [--flags]

  EXAMPLES

    # Check AI agent governance configuration on this machine
    $ glab minder doctor

  FLAGS

    -h --help  Show help for this command.

```

## glab govern setup

<!-- help-capture: 206ebab4f:fd61215028ae -->

```text

  Configure the current machine for AI governance session capture.

  Choose the agents to sync with `--agents`. Without it, setup syncs the agents set up by an earlier run, or Claude Code
  if there are none. For each agent, setup installs:

  - Claude Code (`claude-code`): a Stop hook in `~/.claude/settings.json`, which syncs the session after every agent
  turn, and a SessionEnd hook, which syncs the session and marks it completed.
  - OpenCode (`opencode`), version 1.4 or later: a plugin in `~/.config/opencode/plugins/glab-govern.js` (under
  `$XDG_CONFIG_HOME` when it is set), which syncs the session every time it goes idle. OpenCode loads it for all your
  sessions, in every project. Later setups keep it up to date.
  - Codex (`codex`) and Cursor (`cursor`): nothing. The fallback periodic sync finds their sessions by scanning their
  transcripts in `~/.codex/sessions` and `~/.cursor/projects`, including sessions from before you enabled them, and
  uploads those from repositories on GitLab hosts you are logged in to with glab. Their sessions are marked completed
  once they have been idle for 24 hours.

  Setup also installs the fallback periodic sync: a launchd agent (`~/Library/LaunchAgents/com.gitlab.glab-govern-audit-
  sync.plist`) on macOS, or a systemd user timer (`~/.config/systemd/user/glab-govern-audit-sync.timer`) on Linux.

  The fallback periodic sync runs `glab minder audit sync --all` every 30 minutes, and on Linux also 5 minutes after
  boot, until you remove it. It uploads anything the hooks missed for sessions they have already recorded (see `glab
  minder audit sync --help` for what is uploaded), using your stored glab credentials and the glab configuration
  directory in use when you run setup. Each session goes to the project and host of the Git repository the agent ran in.
  It also marks sessions completed once they have been idle for 24 hours. It pauses sessions from agents that use hooks
  while those hooks are not installed. Pass `--no-fallback-sync` to install only the hooks and plugin, which Codex and
  Cursor cannot be synced without. The fallback periodic sync is not available on Windows.

  Run setup again with `--agents` to add agents. Agents set up by an earlier run stay set up, so to stop syncing an
  agent, run `--uninstall` and then set up the agents you want. Every setup prompt names the agents that are synced.

  Safe to run multiple times: existing hooks are not duplicated, and an existing fallback periodic sync job is replaced.
  Run `glab minder doctor` afterwards to verify the setup.

  Run `glab minder setup --uninstall` to remove everything setup installed: the hooks, the OpenCode plugin, the fallback
  periodic sync job, and Codex and Cursor session syncing. It also forgets the agents you set up, so the next setup
  starts with Claude Code again. Other hooks and settings in `~/.claude/settings.json`, and other OpenCode plugins, are
  left unchanged.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern setup [--flags]

  EXAMPLES

    # Sync Claude Code sessions, or the agents set up earlier
    $ glab minder setup

    # Sync OpenCode sessions
    $ glab minder setup --agents opencode

    # Sync Claude Code, OpenCode, and Codex sessions
    $ glab minder setup --agents claude-code,opencode,codex

    # Install only the hooks and plugin, without the fallback periodic sync
    $ glab minder setup --no-fallback-sync

    # Remove everything setup installed
    $ glab minder setup --uninstall

  FLAGS

    --agents            Agents to sync sessions from: claude-code, opencode, codex, cursor. Added to the agents set up by an earlier run. The OpenCode plugin runs for all your OpenCode sessions. Multiple agents can be comma-separated or specified by repeating the flag.
    -h --help           Show help for this command.
    --no-fallback-sync  Install only the hooks and plugin, without the fallback periodic sync job.
    --uninstall         Remove the hooks, the OpenCode plugin, and the fallback periodic sync job, and stop syncing Codex and Cursor sessions.
    -y --yes            Skip confirmation prompt.

```

## glab minder

<!-- help-capture: 206ebab4f:41088a3eca8f -->

```text

  Manage AI governance for external agents running against GitLab projects. Configure hooks and diagnose setup issues.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab minder <command> [command] [--flags]

  COMMANDS

    audit <command> [command]  Manage AI agent audit events and sessions. (EXPERIMENTAL)
    doctor                     Diagnose AI governance configuration, authentication, and hook setup. (EXPERIMENTAL)
    setup [--flags]            Configure this machine to record AI agent sessions. (EXPERIMENTAL)

  FLAGS

    -h --help                  Show help for this command.

```

## glab minder audit

<!-- help-capture: 206ebab4f:c906096df7ae -->

```text

  Manage audit events and sessions for external AI agents.
  Sync session data from local agent transcripts to GitLab.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab minder audit <command> [command] [--flags]

  COMMANDS

    sync [--flags]  Sync agent session data to GitLab. (EXPERIMENTAL)

  FLAGS

    -h --help       Show help for this command.

```

## glab minder audit sync

<!-- help-capture: 206ebab4f:d9834888e066 -->

```text

  Read new entries from the local agent transcript since the last sync and POST them to GitLab as audit events.

  The audit events contain the prompts you type, each tool call with its arguments (such as commands, file paths, and
  edits, replaced with a marker when over 8 KB), each tool call's outcome, duration, and error message, and the model
  and token usage of each response. Tool output and the text of responses are not sent.

  Before anything is sent, glab replaces common secret formats with a marker such as `[REDACTED:gitlab_token]`: GitLab,
  GitHub, Slack, npm and PyPI tokens, AWS, Google, Stripe, OpenAI and Anthropic API keys, JWTs, private keys,
  credentials in Authorization and token headers or under credential-like keys, and passwords in URLs. This is best
  effort: other secrets in prompts, commands, or file contents are sent as they are.

  When glab creates a session on GitLab, it also sends the glab version and the agent's version. A session that has
  never synced and has had no activity in the last 89 days is not uploaded, because GitLab does not accept events that
  old.

  Some agents record less:

  - OpenCode: prompts and responses are not sent, and a tool call's outcome is sent only if the call had finished when
  it was first synced.
  - Codex: a tool call's outcome is "completed", because Codex does not record whether it succeeded.
  - Cursor: only prompts and tool calls are sent, timed by the transcript's last modification, because Cursor records no
  results, token usage, timestamps, or version. A Cursor session is not synced if the files its tool calls read or write
  are outside the workspace glab finds, or if several directories match the workspace's name and those files don't show
  which, so that it is not uploaded to the wrong project.

  If a GitLab instance does not accept an agent's sessions yet, they are not uploaded, then or after the instance is
  upgraded. Sessions from after the upgrade are.

  Called by the Stop hook after every agent turn. Also used by the SessionEnd hook (with `--complete`) to mark the
  session as complete. The hooks also record the session's project, host, and transcript location so that `--all` can
  sync it later.

  With `--hook codex`, reads the session from the JSON that a Codex Stop hook gets on stdin, and syncs it with a glab
  started in the background, so Codex does not wait for the upload. It prints nothing, because Codex reads a Stop hook's
  output as a reason to continue. The project is resolved from the session's directory.

  Project is resolved from the Git remote of the current directory, or overridden with `-R/--repo`.

  With `--all`, syncs every session the hooks have recorded, each to the project and host it was recorded with. Sessions
  inactive for 24 hours are marked completed. Sessions from agents that use hooks are skipped while the glab hooks are
  missing, so removing the hooks pauses them. The fallback periodic sync installed by `glab minder setup` runs this, and
  `glab minder doctor` shows the result of its last run.

  Supports Claude Code, OpenCode, Codex, and Cursor sessions. OpenCode sessions are read with `opencode session export`,
  or `opencode export` before OpenCode 2. With `--all`, it also finds and syncs the sessions of Codex and Cursor, when
  they are enabled with `glab minder setup --agents`, by scanning their transcripts, for repositories on GitLab hosts
  glab is logged in to.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab minder audit sync [--flags]

  EXAMPLES

    # Sync the current agent session to GitLab
    $ glab minder audit sync

    # Sync and mark the session as completed
    $ glab minder audit sync --complete

    # Sync against a specific project
    $ glab minder audit sync -R my-group/my-project

    # Sync every recorded session that has unsynced activity
    $ glab minder audit sync --all

  FLAGS

    --all       Sync all sessions recorded by the hooks. Used by the fallback periodic sync.
    --complete  Mark the session as completed. Used by the SessionEnd hook.
    -h --help   Show help for this command.
    --hook      Read the session from the stdin of this agent's hook, and sync it in the background: codex. Used by the Codex Stop hook.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --silent    Suppress all output. Used when invoked from hooks.

```

## glab minder doctor

<!-- help-capture: 206ebab4f:ff0141836d7d -->

```text

  Check that AI governance is correctly configured on this machine.

  Verifies:

  - Authentication: glab is authenticated with a valid token
  - glab in PATH: the binary is findable so hooks will work
  - Agent session hooks: if Claude Code sessions are synced, the Stop and SessionEnd hooks are installed
  - OpenCode plugin: if OpenCode sessions are synced, the glab plugin is installed and up to date
  - API connectivity: can reach the GitLab API
  - Fallback periodic sync: whether the scheduled job is installed and loaded, whether the glab binary it runs still
  exists and is the same build as this glab, and the result of its last run

  Outputs a clear remediation command for any check that fails.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab minder doctor [--flags]

  EXAMPLES

    # Check AI agent governance configuration on this machine
    $ glab minder doctor

  FLAGS

    -h --help  Show help for this command.

```

## glab minder setup

<!-- help-capture: 206ebab4f:db86c27d9ec7 -->

```text

  Configure the current machine for AI governance session capture.

  Choose the agents to sync with `--agents`. Without it, setup syncs the agents set up by an earlier run, or Claude Code
  if there are none. For each agent, setup installs:

  - Claude Code (`claude-code`): a Stop hook in `~/.claude/settings.json`, which syncs the session after every agent
  turn, and a SessionEnd hook, which syncs the session and marks it completed.
  - OpenCode (`opencode`), version 1.4 or later: a plugin in `~/.config/opencode/plugins/glab-govern.js` (under
  `$XDG_CONFIG_HOME` when it is set), which syncs the session every time it goes idle. OpenCode loads it for all your
  sessions, in every project. Later setups keep it up to date.
  - Codex (`codex`) and Cursor (`cursor`): nothing. The fallback periodic sync finds their sessions by scanning their
  transcripts in `~/.codex/sessions` and `~/.cursor/projects`, including sessions from before you enabled them, and
  uploads those from repositories on GitLab hosts you are logged in to with glab. Their sessions are marked completed
  once they have been idle for 24 hours.

  Setup also installs the fallback periodic sync: a launchd agent (`~/Library/LaunchAgents/com.gitlab.glab-govern-audit-
  sync.plist`) on macOS, or a systemd user timer (`~/.config/systemd/user/glab-govern-audit-sync.timer`) on Linux.

  The fallback periodic sync runs `glab minder audit sync --all` every 30 minutes, and on Linux also 5 minutes after
  boot, until you remove it. It uploads anything the hooks missed for sessions they have already recorded (see `glab
  minder audit sync --help` for what is uploaded), using your stored glab credentials and the glab configuration
  directory in use when you run setup. Each session goes to the project and host of the Git repository the agent ran in.
  It also marks sessions completed once they have been idle for 24 hours. It pauses sessions from agents that use hooks
  while those hooks are not installed. Pass `--no-fallback-sync` to install only the hooks and plugin, which Codex and
  Cursor cannot be synced without. The fallback periodic sync is not available on Windows.

  Run setup again with `--agents` to add agents. Agents set up by an earlier run stay set up, so to stop syncing an
  agent, run `--uninstall` and then set up the agents you want. Every setup prompt names the agents that are synced.

  Safe to run multiple times: existing hooks are not duplicated, and an existing fallback periodic sync job is replaced.
  Run `glab minder doctor` afterwards to verify the setup.

  Run `glab minder setup --uninstall` to remove everything setup installed: the hooks, the OpenCode plugin, the fallback
  periodic sync job, and Codex and Cursor session syncing. It also forgets the agents you set up, so the next setup
  starts with Claude Code again. Other hooks and settings in `~/.claude/settings.json`, and other OpenCode plugins, are
  left unchanged.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab minder setup [--flags]

  EXAMPLES

    # Sync Claude Code sessions, or the agents set up earlier
    $ glab minder setup

    # Sync OpenCode sessions
    $ glab minder setup --agents opencode

    # Sync Claude Code, OpenCode, and Codex sessions
    $ glab minder setup --agents claude-code,opencode,codex

    # Install only the hooks and plugin, without the fallback periodic sync
    $ glab minder setup --no-fallback-sync

    # Remove everything setup installed
    $ glab minder setup --uninstall

  FLAGS

    --agents            Agents to sync sessions from: claude-code, opencode, codex, cursor. Added to the agents set up by an earlier run. The OpenCode plugin runs for all your OpenCode sessions. Multiple agents can be comma-separated or specified by repeating the flag.
    -h --help           Show help for this command.
    --no-fallback-sync  Install only the hooks and plugin, without the fallback periodic sync job.
    --uninstall         Remove the hooks, the OpenCode plugin, and the fallback periodic sync job, and stop syncing Codex and Cursor sessions.
    -y --yes            Skip confirmation prompt.

```

