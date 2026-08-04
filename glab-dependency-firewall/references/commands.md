# glab dependency-firewall command reference

Source: <https://docs.gitlab.com/cli/dependency-firewall/>

> Help output captured from the checksum-verified release binary.

## dependency-firewall

Alias: `df`

```text
  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall <command> [command] [--flags]

  COMMANDS

    ci-summary                             Summarize Dependency Firewall activity from the CI log.
    configure <package-manager> [--flags]  Configure Dependency Firewall registry URLs for a package manager.

  FLAGS

    -h --help                              Show help for this command.
```

## dependency-firewall configure

```text
  Write a package manager's resolve and deploy registry URLs to
  `.gitlab/df/config.json`.

  Supported package managers: `npm`.

  The file is written relative to the current working directory, so run this
  command from the directory you run the package manager in.

  Only the flags you pass are updated; existing values and unknown keys are
  preserved.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall configure <package-manager> [--flags]

  EXAMPLES

    # Set the resolve (read) and deploy (publish) registry URLs for npm
    glab dependency-firewall configure npm --repo-resolve https://gitlab.com/api/v4/projects/42/packages/npm/ --rep…

    # Update only the resolve URL; the deploy URL is preserved
    glab dependency-firewall configure npm --repo-resolve https://gitlab.com/api/v4/projects/42/packages/npm/

  FLAGS

    -h --help       Show help for this command.
    --repo-deploy   Full registry URL to deploy (publish) packages to.
    --repo-resolve  Full registry URL to resolve (install) packages from.
```

At least one of `--repo-deploy` or `--repo-resolve` is required. The only accepted package-manager positional in this command surface is `npm`.

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

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
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
