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

## Subcommands

This command has no subcommands.