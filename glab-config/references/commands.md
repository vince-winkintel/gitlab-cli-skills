# glab config help

> Help output captured from the checksum-verified glab v1.116.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

## config

```text

  Manage key/value strings.

  Current respected settings:

  - `api_host`: Configure host for API endpoint. Defaults to the host itself. Also accepted as: `gitlab_api_host`.
  Scoped per host; set it with `--host`.
  - `api_protocol`: What protocol to use to access the API endpoint. Supported values: `http`, `https`. Scoped per host;
  set it with `--host`.
  - `artifact_registry_domains`: The domains of associated Artifact Registries. These are used to configure the Docker
  credential helper. Only list a domain here if it is actually backed by GitLab Artifact Registry: the credential helper
  tries this key first, and a successful token exchange is used as-is, with no fallback to container_registry_domains. A
  container-registry domain listed here by mistake gets an artifact-registry token the registry rejects, and `docker
  pull` hard-fails. Scoped per host; set it with `--host`.
  - `branch_prefix`: Prefix used by `glab stack` when naming generated branches. Defaults to the current user's username
  (from `os/user.Current`), falling back to `glab-stack` if unavailable.
  - `browser`: What browser glab should run when opening links. This global config cannot be overridden by hostname.
  - `ca_cert`: Path to a CA certificate (PEM) used to verify the GitLab server's TLS certificate. Useful for self-signed
  or private certificate authorities. Scoped per host; set it with `--host`.
  - `check_update`: Allow glab to automatically check for updates and notify you when there are new updates.
  - `client_cert`: Path to a client certificate (PEM) used for mutual TLS authentication. Scoped per host; set it with
  `--host`.
  - `client_id`: OAuth application client ID. Required when authenticating with OAuth against a self-managed GitLab
  instance. Scoped per host; set it with `--host`.
  - `client_key`: Path to the private key (PEM) that matches client_cert. Scoped per host; set it with `--host`.
  - `container_registry_domains`: The domains of associated container registries. These are used to configure the Docker
  credential helper. Scoped per host; set it with `--host`.
  - `custom_headers`: Custom HTTP headers to add to all HTTP requests made by glab. Each header must use exactly one of
  value, valueFromEnv, or valueFromCommand. A command must print the complete header value on one line. glab runs it
  once for each process. Scoped per host; set it with `--host`.
  - `debug`: Output more logging information, including underlying Git commands, expanded aliases, and DNS error
  details.
  - `display_hyperlinks`: Whether or not to display hyperlinks in terminal output. Defaults to true (enabled for TTYs).
  Set to false to disable. Force hyperlinks in non-TTY environments by setting FORCE_HYPERLINKS=1.
  - `duo_cli_auto_download`: Automatically download Duo CLI binary without prompting (true/false).
  - `duo_cli_auto_run`: Automatically run GitLab Duo CLI without prompting (true/false). Set to true to skip the
  confirmation prompt.
  - `editor`: What editor glab should run when creating issues, merge requests, etc. This global config cannot be
  overridden by hostname. Also accepted as: `visual`, `glab_editor`.
  - `git_protocol`: What protocol to use when performing Git operations. Supported values: `ssh`, `https`.
  - `glab_pager`: Your desired pager command to use, such as `less -R`. Takes precedence over the PAGER environment
  variable. GLAB_PAGER takes precedence over both.
  - `glamour_style`: Set your desired Markdown renderer style. Available options are [dark, light, notty]. To set a
  custom style, refer to https://github.com/charmbracelet/glamour#styles.
  - `host`: Default GitLab hostname to use. Also accepted as: `gitlab_host`, `gitlab_uri`, `gl_host`.
  - `job_token`: CI job token used for Job-Token authentication. Typically populated automatically from CI_JOB_TOKEN
  when CI auto-login is enabled. Scoped per host; set it with `--host`.
  - `no_prompt`: Set to true (1) to disable prompts, or false (0) to enable them. Also accepted as: `prompt_disabled`.
  - `notify_skill_updates`: Show a notice when an installed agent skill (bundled or remote) has updates available.
  - `orbit_local_auto_download`: Automatically download Orbit local CLI binary without prompting (true/false).
  - `orbit_local_auto_run`: Automatically run Orbit local CLI without prompting (true/false). Set to true to skip the
  confirmation prompt.
  - `proxy`: Custom proxy for this host. Overrides environment proxy settings when set. Scoped per host; set it with `--
  host`.
  - `remote_alias`: Name of the `git remote` that points at the GitLab repository. Used to resolve which remote to
  operate against when multiple are configured. Also accepted as: `git_remote_url_var`, `git_remote_alias`,
  `remote_nickname`, `git_remote_nickname`.
  - `show_whats_new`: Show a one-time post-upgrade banner pointing at `glab whatsnew` when a new version is detected.
  - `skip_tls_verify`: Skip TLS certificate verification when talking to this host (true/false). Empty is treated as
  false. Use only for development; do not enable in production. Scoped per host; set it with `--host`.
  - `ssh_host`: Alternate hostname for SSH Git operations (e.g., `ssh.example.com` or `git.example.com`). Use this when
  SSH uses a different hostname than HTTP/API operations. Only affects SSH cloning and Git operations. Also accepted as:
  `gitlab_ssh_host`. Scoped per host; set it with `--host`.
  - `subfolder`: Subfolder where GitLab is installed (e.g., `gitlab` for https://example.com/gitlab/). Use this when
  GitLab is hosted at a subfolder rather than domain root. Supports nested paths (e.g., `apps/gitlab` for
  https://example.com/apps/gitlab/). Slashes are automatically trimmed, so `gitlab`, `/gitlab`, and `gitlab/` are
  equivalent. Only applies to HTTP/HTTPS operations (API and Git clone). Also accepted as: `gitlab_subfolder`. Scoped
  per host; set it with `--host`.
  - `telemetry`: Set to false (0) to disable sending usage data to your GitLab instance or true (1) to enable. See
  https://docs.gitlab.com/administration/settings/usage_statistics/ for more information.
  - `token`: Your GitLab access token. To get one, read https://docs.gitlab.com/user/profile/personal_access_tokens/.
  Also accepted as: `gitlab_token`, `oauth_token`. Scoped per host; set it with `--host`.
  - `use_keyring`: Store the host's credentials in the operating system's keyring (true/false). Set automatically by
  `glab auth login`, which defaults to `true` when a keyring backend is available. Empty is treated as false (plaintext
  file storage). Scoped per host; set it with `--host`.

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
