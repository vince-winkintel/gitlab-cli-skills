---
name: glab-alias
description: Create, list, and delete GitLab CLI command aliases and shortcuts. Use when creating custom glab commands, managing CLI shortcuts, or viewing existing aliases. Triggers on alias, shortcut, custom command, CLI alias.
---

# glab alias

## Argument boundaries

Arguments supplied to an alias are passed through without reconstructing them as a shell-joined string. Keep each intended argument quoted at the calling shell; quoted whitespace and special characters remain part of that argument. Explicit shell aliases still execute shell code and require review before use.

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
glab alias list
```

`glab alias list` wraps long rows instead of truncating expansions at a fixed column width, so the complete stored command remains visible. Treat shell aliases as executable code and review the full expansion before running an unfamiliar alias.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
