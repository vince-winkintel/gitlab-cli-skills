---
name: glab-ssh-key
description: Manage SSH keys for GitLab account including add, list, and delete operations. Use when setting up SSH authentication, managing SSH keys, or configuring Git over SSH. Triggers on SSH key, add SSH key, SSH authentication, Git SSH.
---

# glab ssh-key

## Overview

```

  Manage SSH keys registered with your GitLab account.                                                                  
         
  USAGE  
         
    glab ssh-key <command> [command] [--flags]  
            
  COMMANDS  
            
    add [key-file] [--flags]   Add an SSH key to your GitLab account.
    delete <key-id> [--flags]  Deletes a single SSH key specified by the ID.
    get <key-id> [--flags]     Returns a single SSH key specified by the ID.
    list [--flags]             Get a list of SSH keys for the currently authenticated user.
         
  FLAGS  
         
    -h --help                  Show help for this command.
    -R --repo                  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab ssh-key --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
