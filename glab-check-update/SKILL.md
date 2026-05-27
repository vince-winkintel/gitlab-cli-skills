---
name: glab-check-update
description: Check for glab CLI updates and view latest version information. Use when checking if glab is up to date or finding available updates. Triggers on update glab, check version, glab version, CLI update.
---

# glab check-update

## Overview

```

  Checks for the latest version of glab available on GitLab.com.                                                        
                                                                                                                        
  When run explicitly, this command always checks for updates regardless of when the last check occurred.               
                                                                                                                        
  When run automatically after other glab commands, it checks for updates at most once every 24 hours.                  
                                                                                                                        
  To disable the automatic update check entirely, run 'glab config set check_update false'.                             
  To re-enable the automatic update check, run 'glab config set check_update true'.                                     
                                                                                                                        
         
  USAGE  
         
    glab check-update [--flags]  
         
  FLAGS  
         
    -h --help  Show help for this command.
```

## Quick start

```bash
glab check-update --help
```

## Update nudge behavior

`glab check-update` and its `glab update` alias always check when invoked explicitly. Automatic checks after other commands remain throttled to at most once every 24 hours and can be disabled with `glab config set check_update false`.

In glab v1.100.0+, the update nudge is install-aware and agent-aware: when glab can detect the install method, it includes the matching upgrade command, and when a coding-agent environment is detected, it emits a compact bracketed line suitable for agents to relay instead of a multi-line human prompt. If the install method is unknown, expect only the release-notes URL rather than a guessed upgrade command.

## Subcommands

This command has no subcommands.
