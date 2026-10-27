---
name: glab-config
description: Manage glab CLI configuration settings including defaults, preferences, and per-host settings. Use when configuring glab behavior, setting defaults, or viewing current configuration. Triggers on config, configuration, settings, glab settings, set default.
---

# glab config

## Host selection and output rendering

The configured `host` key is a fallback, not a constraint on repository remotes. Inside a repository, a remote on another host can select that host. Environment host selectors (`GITLAB_HOST`, `GITLAB_URI`, `GL_HOST`, or the corresponding CI auto-login source) remain authoritative; no matching remote produces an error rather than silently switching hosts. Explicit full-URL repository selectors carry their own host. This host-selection rule is separate from normal setting precedence: environment values, non-empty per-host settings/eligible keyring credentials, local config, global config, then defaults.

Global output color is controlled by `GLAB_COLOR=auto|never|always` or the global `color` config key. `always`/`never` override `NO_COLOR`; `auto` detects terminal output and honors legacy color environment behavior. There is no global `--color` CLI flag. `glab mr diff --color` is a separate command-specific option; label color flags set label metadata. For credential-free, uncolored help use `GLAB_COLOR=never glab help <command>`.

`glamour_style` defaults to `auto` and detects the terminal background; explicit `dark`, `light`, `notty`, and custom styles remain available. Existing seeded `dark` defaults can migrate once to `auto`; use an explicit environment style override when deterministic rendering matters. Help retains Fang's indented uppercase headings and can wrap or truncate examples. Preserve exact help output when capturing references, and use supported JSON output rather than parsing terminal formatting. Error text is displayed as written, so punctuation is not a stable parsing contract.

## Overview

Authored synopsis (not a binary capture). The complete captured help, including
per-key environment aliases, scope, and warnings, is in
[references/commands.md](references/commands.md#config).

- Global behavior: `branch_prefix`, `browser`, `check_update`, `color`, `debug`,
  `display_hyperlinks`, `duo_cli_auto_download`, `duo_cli_auto_run`, `editor`,
  `git_protocol`, `glab_pager`, `glamour_style`, `host`, `no_prompt`,
  `notify_skill_updates`, `orbit_cli_auto_download`, `orbit_cli_auto_run`,
  `remote_alias`, `show_whats_new`, and `telemetry`.
- Per-host behavior: `api_host`, `api_protocol`, `artifact_registry_domains`,
  `ca_cert`, `client_cert`, `client_id`, `client_key`, `container_registry_domains`,
  `custom_headers`, `job_token`, `proxy`, `skip_tls_verify`, `ssh_host`, `subfolder`,
  `token`, and `use_keyring`. Select these with `--host <hostname>`.
- Use canonical keys in new automation. Accepted compatibility aliases and their
  environment-variable precedence are documented below and in the full reference.

```text
glab config [command] [--flags]

Commands:
  edit             Open the configuration file
  get <key>        Print a configuration value
  path             Print the global configuration file location
  set <key> <value>  Update a configuration value

Flags:
  -g, --global     Use global configuration
  -h, --help       Show help
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
