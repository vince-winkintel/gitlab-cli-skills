---
name: glab-config
description: Manage glab CLI configuration settings including defaults, preferences, and per-host settings. Use when configuring glab behavior, setting defaults, or viewing current configuration. Triggers on config, configuration, settings, glab settings, set default.
---

# glab config

## Overview

```

  Manage key/value strings.
  Current respected settings:
  - Global behavior: branch_prefix, browser, check_update, debug, display_hyperlinks,
    duo_cli_auto_download, duo_cli_auto_run, editor, git_protocol, glab_pager,
    glamour_style, host, no_prompt, notify_skill_updates, orbit_local_auto_download,
    orbit_local_auto_run, remote_alias, show_whats_new, and telemetry.
  - Per-host behavior: api_host, api_protocol, artifact_registry_domains, ca_cert,
    client_cert, client_id, client_key, container_registry_domains, custom_headers,
    job_token, proxy, skip_tls_verify, ssh_host, subfolder, token, and use_keyring.
  - Accepted aliases include visual/glab_editor for editor, gitlab_host/gitlab_uri/gl_host
    for host, prompt_disabled for no_prompt, and the aliases shown by `glab config --help`.
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

## Per-host HTTPS proxy configuration

You can configure an HTTPS proxy on a per-host basis. This is useful when different GitLab instances (for example gitlab.com vs a self-hosted instance) require different proxy settings.

```bash
# Set HTTPS proxy for a specific host
glab config set https_proxy "http://proxy.example.com:8080" --host gitlab.mycompany.com

# Set globally (applies to all hosts without a specific override)
glab config set https_proxy "http://proxy.example.com:8080" --global

# Verify
glab config get https_proxy --host gitlab.mycompany.com
```

**Precedence:** Per-host config overrides global config. Global config overrides the `HTTPS_PROXY` / `https_proxy` environment variables.

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
