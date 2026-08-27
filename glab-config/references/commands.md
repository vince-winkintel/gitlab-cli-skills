# glab config help

> Help output captured from the checksum-verified glab v1.115.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

## config

```text

  Manage key/value strings.

  Current respected settings:

  - `branch_prefix`: Prefix used by `glab stack` when naming generated branches. Defaults to the current user's username
  (from `os/user.Current`), falling back to `glab-stack` if unavailable.
  - `browser`: If unset, uses the default browser. Override with environment variable `$BROWSER`.
  - `check_update`: If true, notifies of new versions of glab. Defaults to `true`. Override with environment variable
  `$GLAB_CHECK_UPDATE`.
  - `display_hyperlinks`: If `false`, disables hyperlinks in terminal output. Defaults to `true`. Override with
  environment variable `$FORCE_HYPERLINKS`.
  - `duo_cli_auto_download`: If `true`, automatically downloads the Duo CLI binary without prompting.
  - `duo_cli_auto_run`: If `true`, automatically runs GitLab Duo CLI without prompting.
  - `editor`: If unset, uses the default editor. Override with environment variable `$EDITOR`.
  - `git_protocol`: Protocol used for Git operations. Supported values: `ssh`, `https`. Defaults to `ssh`.
  - `glab_pager`: Your desired pager command to use, such as `less -R`.
  - `glamour_style`: Your desired Markdown renderer style. Options are dark, light, notty. Custom styles are available
  using glamour.
  - `host`: If unset, defaults to `https://gitlab.com`.
  - `no_prompt`: If `true`, disables interactive prompts. Defaults to `false`. Override with environment variable
  `$NO_PROMPT`.
  - `notify_skill_updates`: If `true`, shows a notice when an installed agent skill has updates available. Defaults to
  `true`. Override with environment variable `$GLAB_NOTIFY_SKILL_UPDATES`.
  - `orbit_local_auto_download`: If `true`, automatically downloads the Orbit local CLI binary without prompting.
  - `orbit_local_auto_run`: If `true`, automatically runs Orbit local CLI without prompting.
  - `remote_alias`: Name of the `git remote` that points at the GitLab repository. Used to resolve which remote to
  operate against when multiple are configured.
  - `show_whats_new`: If true, shows a one-time post-upgrade banner pointing at `glab whatsnew` when a new version is
  detected. Defaults to `true`. Override with environment variable `$GLAB_SHOW_WHATS_NEW`.
  - `telemetry`: If `false`, disables sending usage data to your GitLab instance. Defaults to `true`. Override with
  environment variable `$GLAB_SEND_TELEMETRY`.
  - `token`: Your GitLab access token. Defaults to environment variables.
  - `visual`: Takes precedence over `editor`. If unset, uses the default editor. Override with environment variable
  `$VISUAL`.

  Configuration file locations follow the XDG Base Directory specification.
  For the full search order and platform-specific paths, see configuration.


  USAGE

    glab config [command] [--flags]

  COMMANDS

    edit [--flags]               Opens the glab configuration file.
    get <key> [--flags]          Prints the value of a given configuration key.
    path [--flags]               Print the location of the global configuration file.
    set <key> <value> [--flags]  Updates configuration with the value of a given key.

  FLAGS

    -g --global                  Use global config file.
    -h --help                    Show help for this command.

```

## config edit

```text

  The command uses the following order when choosing the editor to use:

  1. `glab_editor` field in the configuration file.
  1. `VISUAL` environment variable.
  1. `EDITOR` environment variable.


  USAGE

    glab config edit [--flags]

  EXAMPLES

    # Open the configuration file with the default editor
    glab config edit

    # Open the configuration file with vim
    EDITOR=vim glab config edit

    # Set vim to be used for all future 'glab config edit' invocations
    glab config set editor vim
    glab config edit

    # Open the local configuration file with the default editor
    glab config edit -l

  FLAGS

    -h --help   Show help for this command.
    -l --local  Open '.git/glab-cli/config.yml' file instead of the global '~/.config/glab-cli/config.yml' file.

```

## config get

```text

  By default, the lookup order is: environment variables, then the local
  repository configuration, then the global configuration. Use `--global` to
  read only from the global configuration file, or `--host` to read a
  per-host setting.

  If the key is not set, nothing is printed.


  USAGE

    glab config get <key> [--flags]

  EXAMPLES

    $ glab config get editor
    vim

    $ glab config get glamour_style
    notty

  FLAGS

    -g --global  Read from global config file (~/.config/glab-cli/config.yml). (default checks 'Environment variables → Local → Global')
    -h --help    Show help for this command.
    --host       Get per-host setting.

```

## config path

```text

  Print where `glab` reads and writes its global configuration. The location depends on the platform and whether a
  legacy configuration directory exists, so use this command instead of hard-coding a path.

  The command prints the path even if the file does not exist yet, so it is safe to run before the first `glab auth
  login`.

  Use `--dir` to print the parent directory. Grant write access to that directory rather than to `config.yml` alone,
  because `glab` writes a temporary file in that directory first and then replaces `config.yml` with it.

  Repository-local settings live in the repository's `.git/glab-cli/config.yml` and this command does not report them.

  If no user configuration file exists, `glab` falls back to a read-only system-wide one. This command always reports
  the user location.


  USAGE

    glab config path [--flags]

  EXAMPLES

    # Print the path to the global configuration file
    glab config path

    # Print the directory that holds the configuration file
    glab config path --dir

    # Open the configuration file in an editor
    $EDITOR "$(glab config path)"

  FLAGS

    --dir      Print the configuration directory instead of the configuration file.
    -h --help  Show help for this command.

```

## config set

```text

  Use `glab config set --global` to write to the global configuration.
  Specifying the `--host` flag also saves to the global configuration file.


  USAGE

    glab config set <key> <value> [--flags]

  EXAMPLES

    glab config set editor vim
    glab config set token xxxxx --host gitlab.com
    glab config set check_update false --global

  FLAGS

    -g --global  Write to global '~/.config/glab-cli/config.yml' file rather than the repository's '.git/glab-cli/config.yml' file.
    -h --help    Show help for this command.
    --host       Set per-host setting.

```
