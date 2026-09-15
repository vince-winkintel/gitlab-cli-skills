# glab config help

> Help output captured from the checksum-verified glab v1.118.0 macOS arm64 release binary (`glab 1.118.0 (570955d42)`). Terminal padding and trailing whitespace are removed. The release archive SHA-256 is `d289e2ba48f85cc0639cb77e4ea78c14d222d099e8d545c7bb687ba779255f47`.

## config

```text

  Manage key/value strings.

  Current respected settings:

  - `api_host`: Configure host for API endpoint. Defaults to the host itself. Also accepted as: `gitlab_api_host`.
  Scoped per host; set it with `--host`. Environment variable: `GITLAB_API_HOST`.
  - `api_protocol`: What protocol to use to access the API endpoint. Supported values: `http`, `https`. Scoped per host;
  set it with `--host`. Environment variables, first one set wins: `GLAB_API_PROTOCOL`, `API_PROTOCOL`.
  - `artifact_registry_domains`: The domains of associated Artifact Registries. These are used to configure the Docker
  credential helper. Only list a domain here if it is actually backed by GitLab Artifact Registry: the credential helper
  tries this key first, and a successful token exchange is used as-is, with no fallback to container_registry_domains. A
  container-registry domain listed here by mistake gets an artifact-registry token the registry rejects, and `docker
  pull` hard-fails. Scoped per host; set it with `--host`. Environment variables, first one set wins:
  `GLAB_ARTIFACT_REGISTRY_DOMAINS`, `ARTIFACT_REGISTRY_DOMAINS`.
  - `branch_prefix`: Prefix used by `glab stack` when naming generated branches. Defaults to the current user's username
  (from `os/user.Current`), falling back to `glab-stack` if unavailable. Environment variables, first one set wins:
  `GLAB_BRANCH_PREFIX`, `BRANCH_PREFIX`.
  - `browser`: What browser glab should run when opening links. This global config cannot be overridden by hostname.
  Environment variables, first one set wins: `GLAB_BROWSER`, `BROWSER`.
  - `ca_cert`: Path to a CA certificate (PEM) used to verify the GitLab server's TLS certificate. Useful for self-signed
  or private certificate authorities. Scoped per host; set it with `--host`. Environment variables, first one set wins:
  `GLAB_CA_CERT`, `CA_CERT`.
  - `check_update`: Allow glab to automatically check for updates and notify you when there are new updates. Setting the
  environment variable to true also forces a check, bypassing the once-a-day interval. Environment variables, first one
  set wins: `GLAB_CHECK_UPDATE`, `CHECK_UPDATE`.
  - `client_cert`: Path to a client certificate (PEM) used for mutual TLS authentication. Scoped per host; set it with
  `--host`. Environment variables, first one set wins: `GLAB_CLIENT_CERT`, `CLIENT_CERT`.
  - `client_id`: OAuth application client ID. Required when authenticating with OAuth against a self-managed GitLab
  instance. Scoped per host; set it with `--host`. Environment variable: `GITLAB_CLIENT_ID`.
  - `client_key`: Path to the private key (PEM) that matches client_cert. Scoped per host; set it with `--host`.
  Environment variables, first one set wins: `GLAB_CLIENT_KEY`, `CLIENT_KEY`.
  - `container_registry_domains`: The domains of associated container registries. These are used to configure the Docker
  credential helper. Scoped per host; set it with `--host`. Environment variables, first one set wins:
  `GLAB_CONTAINER_REGISTRY_DOMAINS`, `CONTAINER_REGISTRY_DOMAINS`.
  - `custom_headers`: Custom HTTP headers to add to all HTTP requests made by glab. Each header must use exactly one of
  value, valueFromEnv, or valueFromCommand. A command must print the complete header value on one line. glab runs it
  once for each process. Scoped per host; set it with `--host`.
  - `debug`: Output more logging information, including underlying Git commands, expanded aliases, and DNS error
  details. Environment variable: `GLAB_DEBUG`.
  - `display_hyperlinks`: Whether or not to display hyperlinks in terminal output. Defaults to true (enabled for TTYs).
  Set to false to disable. Force hyperlinks in non-TTY environments by setting FORCE_HYPERLINKS=1. Environment
  variables, first one set wins: `GLAB_DISPLAY_HYPERLINKS`, `DISPLAY_HYPERLINKS`.
  - `duo_cli_auto_download`: Automatically download Duo CLI binary without prompting (true/false). Environment
  variables, first one set wins: `GLAB_DUO_CLI_AUTO_DOWNLOAD`, `DUO_CLI_AUTO_DOWNLOAD`.
  - `duo_cli_auto_run`: Automatically run GitLab Duo CLI without prompting (true/false). Set to true to skip the
  confirmation prompt. Environment variables, first one set wins: `GLAB_DUO_CLI_AUTO_RUN`, `DUO_CLI_AUTO_RUN`.
  - `editor`: What editor glab should run when creating issues, merge requests, etc. This global config cannot be
  overridden by hostname. Also accepted as: `visual`, `glab_editor`. Environment variables, first one set wins:
  `GLAB_EDITOR`, `VISUAL`, `EDITOR`.
  - `git_protocol`: What protocol to use when performing Git operations. Supported values: `ssh`, `https`. Environment
  variables, first one set wins: `GLAB_GIT_PROTOCOL`, `GIT_PROTOCOL`.
  - `glab_pager`: Your desired pager command to use, such as `less -R`. Takes precedence over the PAGER environment
  variable. GLAB_PAGER takes precedence over both. Environment variable: `GLAB_PAGER`.
  - `glamour_style`: Set your desired Markdown renderer style. Available options are [dark, light, notty]. To set a
  custom style, refer to https://github.com/charmbracelet/glamour#styles. Environment variables, first one set wins:
  `GLAB_GLAMOUR_STYLE`, `GLAMOUR_STYLE`.
  - `host`: Default GitLab hostname to use. Also accepted as: `gitlab_host`, `gitlab_uri`, `gl_host`. Environment
  variables, first one set wins: `GITLAB_HOST`, `GITLAB_URI`, `GL_HOST`.
  - `job_token`: CI job token used for Job-Token authentication. Typically populated automatically from CI_JOB_TOKEN
  when CI auto-login is enabled. Scoped per host; set it with `--host`.
  - `no_prompt`: Set to true (1) to disable prompts, or false (0) to enable them. Also accepted as: `prompt_disabled`.
  Environment variables, first one set wins: `GLAB_NO_PROMPT`, `NO_PROMPT`, `PROMPT_DISABLED`.
  - `notify_skill_updates`: Show a notice when an installed agent skill (bundled or remote) has updates available.
  Environment variable: `GLAB_NOTIFY_SKILL_UPDATES`.
  - `orbit_local_auto_download`: Automatically download Orbit local CLI binary without prompting (true/false).
  Environment variables, first one set wins: `GLAB_ORBIT_LOCAL_AUTO_DOWNLOAD`, `ORBIT_LOCAL_AUTO_DOWNLOAD`.
  - `orbit_local_auto_run`: Automatically run Orbit local CLI without prompting (true/false). Set to true to skip the
  confirmation prompt. Environment variables, first one set wins: `GLAB_ORBIT_LOCAL_AUTO_RUN`, `ORBIT_LOCAL_AUTO_RUN`.
  - `proxy`: Custom proxy for this host. Overrides environment proxy settings when set. Scoped per host; set it with `--
  host`. Environment variables, first one set wins: `GLAB_PROXY`, `PROXY`.
  - `remote_alias`: Name of the `git remote` that points at the GitLab repository. Used to resolve which remote to
  operate against when multiple are configured. Also accepted as: `git_remote_url_var`, `git_remote_alias`,
  `remote_nickname`, `git_remote_nickname`. Environment variables, first one set wins: `GLAB_REMOTE_ALIAS`,
  `GIT_REMOTE_URL_VAR`, `GIT_REMOTE_ALIAS`, `REMOTE_ALIAS`, `REMOTE_NICKNAME`, `GIT_REMOTE_NICKNAME`.
  - `show_whats_new`: Show a one-time post-upgrade banner pointing at `glab whatsnew` when a new version is detected.
  Environment variable: `GLAB_SHOW_WHATS_NEW`.
  - `skip_tls_verify`: Skip TLS certificate verification when talking to this host (true/false). Empty is treated as
  false. Use only for development; do not enable in production. Scoped per host; set it with `--host`. Environment
  variables, first one set wins: `GLAB_SKIP_TLS_VERIFY`, `SKIP_TLS_VERIFY`.
  - `ssh_host`: Alternate hostname for SSH Git operations (e.g., `ssh.example.com` or `git.example.com`). Use this when
  SSH uses a different hostname than HTTP/API operations. Only affects SSH cloning and Git operations. Also accepted as:
  `gitlab_ssh_host`. Scoped per host; set it with `--host`. Environment variable: `GITLAB_SSH_HOST`.
  - `subfolder`: Subfolder where GitLab is installed (e.g., `gitlab` for https://example.com/gitlab/). Use this when
  GitLab is hosted at a subfolder rather than domain root. Supports nested paths (e.g., `apps/gitlab` for
  https://example.com/apps/gitlab/). Slashes are automatically trimmed, so `gitlab`, `/gitlab`, and `gitlab/` are
  equivalent. Only applies to HTTP/HTTPS operations (API and Git clone). Also accepted as: `gitlab_subfolder`. Scoped
  per host; set it with `--host`. Environment variable: `GITLAB_SUBFOLDER`.
  - `telemetry`: Set to false (0) to disable sending usage data to your GitLab instance or true (1) to enable. See
  https://docs.gitlab.com/administration/settings/usage_statistics/ for more information. Environment variable:
  `GLAB_SEND_TELEMETRY`.
  - `token`: Your GitLab access token. To get one, read https://docs.gitlab.com/user/profile/personal_access_tokens/.
  Also accepted as: `gitlab_token`, `oauth_token`. Scoped per host; set it with `--host`. Environment variables, first
  one set wins: `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, `OAUTH_TOKEN`.
  - `use_keyring`: Store the host's credentials in the operating system's keyring (true/false). Set automatically by
  `glab auth login`, which defaults to `true` when a keyring backend is available. Empty is treated as false (plaintext
  file storage). Scoped per host; set it with `--host`. Environment variables, first one set wins: `GLAB_USE_KEYRING`,
  `USE_KEYRING`.

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
