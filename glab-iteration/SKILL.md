---
name: glab-iteration
description: Manage GitLab iterations for project planning and sprint management. Use when creating iterations, assigning issues to sprints, or viewing iteration progress. Triggers on iteration, sprint, iteration planning, sprint planning.
---

# glab iteration

## Overview

```

  Retrieve iteration information.                                                                                       
         
  USAGE  
         
    glab iteration <command> [command] [--flags]  
            
  COMMANDS  
            
    list [--flags]  List project iterations
         
  FLAGS  
         
    -h --help       Show help for this command.
    -R --repo       Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab iteration --help
```

## Subcommands

`glab iteration list` reports the server's real total in its text header, not just the number of iterations on the current page. Do not treat the header total as proof that all records were returned: choose the intended `--page`/`--per-page` and count returned JSON records separately for automation.

```bash
glab iteration list --output json --page 1 --per-page 30
```

See [references/commands.md](references/commands.md) for full `--help` output.
