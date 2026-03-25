---
name: glab-config
description: Manage glab CLI configuration settings including defaults, preferences, and per-host settings. Use when configuring glab behavior, setting defaults, or viewing current configuration. Triggers on config, configuration, settings, glab settings, set default.
---

# glab config

## Overview

```

  Manage key/value strings.                                                                                             
                                                                                                                        
  Current respected settings:                                                                                           
                                                                                                                        
  - browser: If unset, uses the default browser. Override with environment variable $BROWSER.                           
  - check_update: If true, notifies of new versions of glab. Defaults to true. Override with environment variable       
  $GLAB_CHECK_UPDATE.                                                                                                   
  - display_hyperlinks: If true, and using a TTY, outputs hyperlinks for issues and merge request lists. Defaults to    
  false.                                                                                                                
  - editor: If unset, uses the default editor. Override with environment variable $EDITOR.                              
  - glab_pager: Your desired pager command to use, such as 'less -R'.                                                   
  - glamour_style: Your desired Markdown renderer style. Options are dark, light, notty. Custom styles are available    
  using [glamour](https://github.com/charmbracelet/glamour#styles).                                                     
  - host: If unset, defaults to `https://gitlab.com`.                                                                   
  - token: Your GitLab access token. Defaults to environment variables.                                                 
  - visual: Takes precedence over 'editor'. If unset, uses the default editor. Override with environment variable       
  $VISUAL.                                                                                                              
                                                                                                                        
         
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

## v1.86.0 Changes

### Per-host HTTPS proxy configuration
As of v1.86.0, you can configure an HTTPS proxy on a per-host basis. This is useful when different GitLab instances (e.g. gitlab.com vs a self-hosted instance) require different proxy settings.

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

# Set default host
glab config set host https://gitlab.mycompany.com --global
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
