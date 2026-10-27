---
name: glab-config
description: Manage glab CLI configuration settings including defaults, preferences, and per-host settings. Use when configuring glab behavior, setting defaults, or viewing current configuration. Triggers on config, configuration, settings, glab settings, set default.
---

# glab config

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.


## Host selection and output rendering

The configured `host` key is a fallback, not a constraint on repository remotes. Inside a repository, a remote on another host can select that host. Environment host selectors (`GITLAB_HOST`, `GITLAB_URI`, `GL_HOST`, or the corresponding CI auto-login source) remain authoritative; no matching remote produces an error rather than silently switching hosts. Explicit full-URL repository selectors carry their own host. This host-selection rule is separate from normal setting precedence: environment values, non-empty per-host settings/eligible keyring credentials, local config, global config, then defaults.

Global output color is controlled by `GLAB_COLOR=auto|never|always` or the global `color` config key. `always`/`never` override `NO_COLOR`; `auto` detects terminal output and honors legacy color environment behavior. There is no global `--color` CLI flag. `glab mr diff --color` is a separate command-specific option; label color flags set label metadata. For credential-free, uncolored help use `GLAB_COLOR=never glab help <command>`.

`glamour_style` defaults to `auto` and detects the terminal background; explicit `dark`, `light`, `notty`, and custom styles remain available. Existing seeded `dark` defaults can migrate once to `auto`; use an explicit environment style override when deterministic rendering matters. Help retains Fang's indented uppercase headings and can wrap or truncate examples. Preserve exact help output when capturing references, and use supported JSON output rather than parsing terminal formatting. Error text is displayed as written, so punctuation is not a stable parsing contract.

## Overview

<!-- help-capture: 685c1cbd7:09ba68b4d841 -->

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
  - `color`: Set whether glab colors its output. Available options are [auto, never, always]. `auto` detects whether the
  output is a terminal. This key takes precedence over the NO_COLOR environment variable; NO_COLOR applies when this is
  `auto` (or unset). Environment variable: `GLAB_COLOR`.
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
  - `glamour_style`: Set your desired Markdown renderer style. Available options are [auto, dark, light, notty]. `auto`
  detects your terminal's background color. To set a custom style, refer to
  https://github.com/charmbracelet/glamour#styles. Environment variables, first one set wins: `GLAB_GLAMOUR_STYLE`,
  `GLAMOUR_STYLE`.
  - `host`: Default GitLab hostname to use. Inside a repository, a Git remote on another host takes precedence over the
  config key. A host from an environment variable, such as `GITLAB_HOST`, always wins, and glab errors if no remote
  matches it. Also accepted as: `gitlab_host`, `gitlab_uri`, `gl_host`. Environment variables, first one set wins:
  `GITLAB_HOST`, `GITLAB_URI`, `GL_HOST`.
  - `job_token`: CI job token used for Job-Token authentication. Typically populated automatically from CI_JOB_TOKEN
  when CI auto-login is enabled. Scoped per host; set it with `--host`.
  - `no_prompt`: Set to true (1) to disable prompts, or false (0) to enable them. Also accepted as: `prompt_disabled`.
  Environment variables, first one set wins: `GLAB_NO_PROMPT`, `NO_PROMPT`, `PROMPT_DISABLED`.
  - `notify_skill_updates`: Show a notice when an installed agent skill (bundled or remote) has updates available.
  Environment variable: `GLAB_NOTIFY_SKILL_UPDATES`.
  - `orbit_cli_auto_download`: Automatically download the GitLab Orbit CLI binary without prompting (true/false).
  Environment variables, first one set wins: `GLAB_ORBIT_CLI_AUTO_DOWNLOAD`, `ORBIT_CLI_AUTO_DOWNLOAD`.
  - `orbit_cli_auto_run`: Automatically run the GitLab Orbit CLI without prompting (true/false). Set to true to skip the
  confirmation prompt. Environment variables, first one set wins: `GLAB_ORBIT_CLI_AUTO_RUN`, `ORBIT_CLI_AUTO_RUN`.
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

## Quick start

```bash
glab config --help
```

## Per-host proxy configuration

Configure `proxy` for each GitLab host that requires a fixed proxy. This is useful when different GitLab instances (for example gitlab.com versus a self-hosted instance) require different proxy settings.

```bash
# Set the proxy for a specific host
glab config set proxy "http://proxy.example.com:8080" --host gitlab.mycompany.com

# Verify
glab config get proxy --host gitlab.mycompany.com
```

**Precedence:** A configured per-host `proxy` replaces environment-based proxy selection for that host. When it is unset, glab falls back to Go's standard `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` handling. `proxy` is host-scoped; use `--host` rather than writing a top-level value with `--global`.

## Dynamic custom headers for authenticating proxies

For an authenticating proxy or access gateway, add a `custom_headers` list under the exact host entry in the global config. Each item must contain `name` and exactly one source: literal `value`, `valueFromEnv`, or `valueFromCommand`. Prefer `valueFromEnv` or a credential helper command so secrets are not stored directly in YAML.

```yaml
hosts:
  gitlab.example.com:
    custom_headers:
      - name: X-Proxy-Client-ID
        value: public-client-id
      - name: X-Proxy-Client-Secret
        valueFromEnv: PROXY_CLIENT_SECRET
      - name: Proxy-Authorization
        valueFromCommand: proxy-token-helper
```

Use `glab config edit --global` to edit the structured list; do not force it through a scalar `config set` call. A command source is split into an executable and arguments without an implicit shell, runs once per `glab` process with a 30-second timeout, and must print one non-empty line without NUL bytes. Its trimmed result is reused for all requests in that process, including OAuth refresh. If shell expansion is unavoidable, invoke a reviewed shell explicitly; otherwise prefer `valueFromEnv`.

Treat custom header values as credentials. Keep literal secrets out of config, logs, command arguments, and repositories. Verify the host before enabling a header because `glab` attaches configured headers to requests for that host.

## Configuration file search order

glab uses this global config selection:

1. `$GLAB_CONFIG_DIR/config.yml` when `GLAB_CONFIG_DIR` is set. This is an explicit override; glab uses this directory even when no config file exists there yet.
2. Otherwise, the first existing normal candidate wins:
   - `~/.config/glab-cli/config.yml`, retained as the legacy location.
   - `$XDG_CONFIG_HOME/glab-cli/config.yml` (on macOS this defaults to `~/Library/Application Support/glab-cli/config.yml`).
   - `$XDG_CONFIG_DIRS/glab-cli/config.yml` for system-wide defaults. The usual Linux default is `/etc/xdg/glab-cli/config.yml`; on macOS, set `XDG_CONFIG_DIRS` explicitly when relying on system-wide config.

Files are not merged. If both the legacy and platform-specific XDG files exist, glab uses the legacy file and warns. Repository-local settings live in `.git/glab-cli/config.yml`, while per-host settings are stored in the selected global file. Prefer `glab config get`, `set`, and `edit` over directly modifying files, and do not copy stored tokens into logs or version control.

## Locate the active global config

Use `glab config path` instead of hard-coding the global config file location. It prints the path even when the file does not exist yet; `--dir` prints the parent directory.

```bash
glab config path
glab config path --dir
$EDITOR "$(glab config path)"
```

When a sandboxed tool needs permission to let `glab` refresh or rewrite credentials, grant write access to the directory from `glab config path --dir`, not just the `config.yml` file. `glab` writes a temporary file in that directory and then replaces the config file.

## Env-first agent pattern

For agentic setups, prefer per-agent env files over one shared shell profile. Example:

```bash
# ~/.config/openclaw/env/gitlab-reviewer.env
GITLAB_TOKEN=glpat-...
GITLAB_HOST=gitlab.com
```

Keep these env files outside version control, restrict their permissions (for example `chmod 600`), be mindful of backup exposure, and use least-privilege bot/service-account tokens.

Load plain `KEY=value` env files like this so the variables are exported to `glab`:

```bash
set -a
source ~/.config/openclaw/env/gitlab-<agent>.env
set +a
```

A plain `source ~/.config/openclaw/env/gitlab-<agent>.env` updates the current shell but may leave the values unexported. In that case `glab` can miss the env overrides and silently reuse stored auth from the active global config file.

Use distinct GitLab bot/service accounts when agents need distinct visible identities. Multiple PATs on one GitLab user still act as that same user.

## Non-interactive prompts and config validation

Use `GLAB_NO_PROMPT=1` for non-interactive automation that must fail instead of prompting. Upstream docs now prefer the `GLAB_`-prefixed name; older `NO_PROMPT` is deprecated and should not be used in new scripts.

```bash
GLAB_NO_PROMPT=1 glab repo prune --dry-run
```

For configuration-backed environment overrides, use the environment-variable list from the config schema: the first set variable wins, in the order shown per key by `glab config --help` or on the [configuration documentation’s environment-variable section](https://docs.gitlab.com/cli/configuration/#environment-variables), which is generated from the same schema. Prefer the `GLAB_`-prefixed names in new automation when one exists; older names remain compatibility fallbacks later in that same ordered list.

Representative schema-order examples:

- `remote_alias`: `GLAB_REMOTE_ALIAS`, `GIT_REMOTE_URL_VAR`, `GIT_REMOTE_ALIAS`, `REMOTE_ALIAS`, `REMOTE_NICKNAME`, `GIT_REMOTE_NICKNAME`
- `editor`: `GLAB_EDITOR`, `VISUAL`, `EDITOR`
- `check_update`: `GLAB_CHECK_UPDATE`, `CHECK_UPDATE`
- `glamour_style`: `GLAB_GLAMOUR_STYLE`, `GLAMOUR_STYLE`
- `no_prompt`: `GLAB_NO_PROMPT`, `NO_PROMPT`, `PROMPT_DISABLED`
- `api_protocol`: `GLAB_API_PROTOCOL`, `API_PROTOCOL`
- `artifact_registry_domains`: `GLAB_ARTIFACT_REGISTRY_DOMAINS`, `ARTIFACT_REGISTRY_DOMAINS`
- `container_registry_domains`: `GLAB_CONTAINER_REGISTRY_DOMAINS`, `CONTAINER_REGISTRY_DOMAINS`
- `duo_cli_auto_download` and `duo_cli_auto_run`: `GLAB_DUO_CLI_AUTO_DOWNLOAD` / `DUO_CLI_AUTO_DOWNLOAD`, `GLAB_DUO_CLI_AUTO_RUN` / `DUO_CLI_AUTO_RUN`
- `orbit_cli_auto_download` and `orbit_cli_auto_run`: `GLAB_ORBIT_CLI_AUTO_DOWNLOAD` / `ORBIT_CLI_AUTO_DOWNLOAD`, `GLAB_ORBIT_CLI_AUTO_RUN` / `ORBIT_CLI_AUTO_RUN`
- `proxy`, `skip_tls_verify`, and `use_keyring`: `GLAB_PROXY` / `PROXY`, `GLAB_SKIP_TLS_VERIFY` / `SKIP_TLS_VERIFY`, `GLAB_USE_KEYRING` / `USE_KEYRING`

Existing GitLab-specific names such as `GITLAB_HOST`, `GITLAB_API_HOST`, `GITLAB_CLIENT_ID`, `GITLAB_SSH_HOST`, `GITLAB_SUBFOLDER`, and token variables retain their documented names. Do not rename secrets or host selectors speculatively.

`glab config set` validates keys against the canonical config schema. If a set operation fails, check the spelling and whether the setting is host-scoped (`--host`) or global (`--global`) rather than forcing an unknown key into the config file.

Registered aliases are accepted case-insensitively and persist under their canonical key. For example, `glab config set visual nano --global` updates `editor`; both `glab config get visual --global` and `glab config get editor --global` then resolve the same value. Prefer canonical names in new automation even though aliases remain supported.

`glab_pager` and `debug` are valid global settings. `GLAB_PAGER` takes precedence over `glab_pager`, which takes precedence over `PAGER`; `GLAB_DEBUG` can override the persisted debug setting.

## Common Settings

```bash
# View current config
glab config get --global

# Set default editor
glab config set editor vim --global

# Set pager
glab config set glab_pager "less -R" --global

# Enable detailed glab/Git/DNS diagnostics
glab config set debug true --global

# Disable update checks
glab config set check_update false --global

# Select the Git remote glab should prefer
glab config set remote_alias origin --global

# Allow Duo CLI to download and run without wrapper prompts
glab config set duo_cli_auto_download true --global
glab config set duo_cli_auto_run true --global

# Set default host
glab config set host https://gitlab.mycompany.com --global
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
