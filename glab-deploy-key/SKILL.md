---
name: glab-deploy-key
description: Manage SSH deploy keys for GitLab projects including add, list, and delete operations. Use when setting up deploy keys for CI/CD, managing read-only access, or configuring deployment authentication. Triggers on deploy key, SSH key, deployment key, read-only access.
---

# glab deploy-key

## Overview

```

  Manage deploy keys.                                                                                                   
         
  USAGE  
         
    glab deploy-key <command> [command] [--flags]  
            
  COMMANDS  
            
    add [key-file] [--flags]  Add a deploy key to a GitLab project.
    delete <key-id>           Deletes a single deploy key specified by the ID.
    get <key-id>              Returns a single deploy key specified by the ID.
    list [--flags]            Get a list of deploy keys for the current project.
         
  FLAGS  
         
    -h --help                 Show help for this command.
    -R --repo                 Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab deploy-key --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
