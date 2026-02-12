---
name: glab-alias
description: Create, list, and delete GitLab CLI command aliases and shortcuts. Use when creating custom glab commands, managing CLI shortcuts, or viewing existing aliases. Triggers on alias, shortcut, custom command, CLI alias.
---

# glab alias

## Overview

```

  Create, list, and delete aliases.                                                                                     
         
  USAGE  
         
    glab alias [command] [--flags]  
            
  COMMANDS  
            
    delete <alias name> [--flags]           Delete an alias.
    list [--flags]                          List the available aliases.
    set <alias name> '<command>' [--flags]  Set an alias for a longer command.
         
  FLAGS  
         
    -h --help                               Show help for this command.
```

## Quick start

```bash
glab alias --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
