---
name: glab-config
description: Manage glab CLI configuration settings including defaults, preferences, and per-host settings. Use when configuring glab behavior, setting defaults, or viewing current configuration. Triggers on config, configuration, settings, glab settings, set default.
---

# glab config

## Overview

```

  Manage key/value strings.
  Current respected settings:
  - branch_prefix: Prefix used by glab stack for generated branch names.
  - browser: If unset, uses the default browser. Override with environment variable $BROWSER.
  - check_update: Notify about new glab versions. Override with $GLAB_CHECK_UPDATE.
  - display_hyperlinks: Enable terminal hyperlinks. Override with $FORCE_HYPERLINKS.
  - duo_cli_auto_download / duo_cli_auto_run: Skip Duo CLI download/run prompts.
  - editor: If unset, uses the default editor. Override with environment variable $EDITOR.
  - git_protocol: Git protocol, ssh or https.
  - glab_pager: Pager command, such as less -R.
  - glamour_style: Markdown renderer style: dark, light, notty, or a custom glamour style.
  - host: If unset, defaults to `https://gitlab.com`.
  - no_prompt: Disable interactive prompts. Prefer the $GLAB_NO_PROMPT override in automation.
  - notify_skill_updates: Show installed agent-skill update notices. Override with $GLAB_NOTIFY_SKILL_UPDATES.
  - orbit_local_auto_download / orbit_local_auto_run: Skip Orbit local CLI download/run prompts.
  - remote_alias: Preferred Git remote name when multiple remotes exist.
  - show_whats_new: Show the one-time post-upgrade glab whatsnew banner. Override with $GLAB_SHOW_WHATS_NEW.
  - telemetry: Enable usage data to the GitLab instance. Override with $GLAB_SEND_TELEMETRY.
  - token: Your GitLab access token. Defaults to environment variables.
  - visual: Takes precedence over editor. Override with $VISUAL.
  USAGE
    glab config [command] [--flags]
  COMMANDS
    edit [--flags]               Opens the glab configuration file.
    get <key> [--flags]          Prints the value of a given configuration key.
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

A plain `source ~/.config/openclaw/env/gitlab-<agent>.env` updates the current shell but may leave the values unexported. In that case `glab` can miss the env overrides and silently reuse stored auth from `~/.config/glab-cli/config.yml`.

Use distinct GitLab bot/service accounts when agents need distinct visible identities. Multiple PATs on one GitLab user still act as that same user.

## Non-interactive prompts and config validation

Use `GLAB_NO_PROMPT=1` for non-interactive automation that must fail instead of prompting. Upstream docs now prefer the `GLAB_`-prefixed name; older `NO_PROMPT` is deprecated and should not be used in new scripts.

```bash
GLAB_NO_PROMPT=1 glab repo prune --dry-run
```

`glab config set` validates keys against the canonical config schema. If a set operation fails, check the spelling and whether the setting is host-scoped (`--host`) or global (`--global`) rather than forcing an unknown key into the config file.

## Common Settings

```bash
# View current config
glab config get --global

# Set default editor
glab config set editor vim --global

# Set pager
glab config set glab_pager "less -R" --global

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
