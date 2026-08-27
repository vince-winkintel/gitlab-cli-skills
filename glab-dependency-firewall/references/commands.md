# glab dependency-firewall command reference

> Help output captured from the checksum-verified glab v1.115.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

## dependency-firewall

Alias: `df`

```text

  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall <command> [command] [--flags]

  COMMANDS

    ci-summary  Summarize Dependency Firewall activity from the CI log. (EXPERIMENTAL)

  FLAGS

    -h --help   Show help for this command.

```

## dependency-firewall ci-summary

```text

  Read `.gitlab/df/ci-log.json` and print blocked and flagged packages
  recorded during a `glab dependency-firewall` run.

  The log is read from the current working directory. Run this command from
  the same directory as the `glab dependency-firewall` run that wrote the
  log, otherwise no activity is reported.

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | No blocked entries in the log (allow-only or warnings). |
  | `1` | The log could not be read. |
  | `3` | At least one entry in the log is blocked. |

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall ci-summary [--flags]

  EXAMPLES

    # Show blocked and flagged packages from the last firewall run
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

```
