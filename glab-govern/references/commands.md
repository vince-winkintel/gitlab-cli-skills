# glab govern command reference

> Help output captured from the checksum-verified glab v1.119.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed. The release archive SHA-256 is `d9cddd1dbe9a8bea8d5709f90a9ac13c3dd3eb0d0e94e3bc4fae6b27abd6a3db`.

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

```text

  Configure the current machine for AI agent governance session capture.

  Installs the following:

  - Stop hook in `~/.claude/settings.json`
  - SessionEnd hook in `~/.claude/settings.json`

  The Stop and SessionEnd hooks are the sync mechanism. Safe to run multiple times — existing hooks are not duplicated.
  Run `glab govern doctor` afterwards to verify the setup.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab govern setup [--flags]

  EXAMPLES

    # Configure hooks for AI agent governance
    $ glab govern setup

  FLAGS

    -h --help  Show help for this command.
    -y --yes   Skip confirmation prompt.

```

## govern doctor

```text

  Check that AI agent governance is correctly configured on this machine.

  Verifies:

  - Authentication: glab is authenticated with a valid token
  - glab in PATH: the binary is findable so hooks will work
  - Claude Code hooks: Stop and SessionEnd hooks are installed
  - API connectivity: can reach the GitLab API

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

  Read new entries from the local agent transcript since the last sync
  and POST them to GitLab as audit events.

  Called by the Stop hook after every agent turn. Also used by the
  SessionEnd hook (with --complete) to mark the session as complete.

  Project is resolved from:

  1. --project flag (requires --hostname)
  2. Git remote of the current directory

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
    $ glab govern audit sync --project my-group/my-project --hostname gitlab.com

  FLAGS

    --complete     Mark the session as completed. Used by the SessionEnd hook.
    -h --help      Show help for this command.
    -H --hostname  Gitlab hostname (required with --project).
    -p --project   Project ID or path to sync against.
    --silent       Suppress all output. Used when invoked from hooks.

```
