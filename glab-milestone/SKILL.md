---
name: glab-milestone
description: Manage project milestones including create, list, update, view, and close operations. Use when planning releases, tracking milestone progress, or organizing issues/MRs by milestone. Triggers on milestone, release planning, milestone progress, version milestone.
---

# glab milestone

## Overview

```

  Manage group or project milestones.                                                                                   
         
  USAGE  
         
    glab milestone <command> [command] [--flags]  
            
  COMMANDS  
            
    create [--flags]  Create a group or project milestone.
    delete [--flags]  Delete a group or project milestone.
    edit [--flags]    Edit a group or project milestone.
    get [--flags]     Get a milestones via an ID for a project or group.
    list [--flags]    Get a list of milestones for a project or group.
         
  FLAGS  
         
    -h --help         Show help for this command.
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab milestone --help
```

## v1.89.0 Updates

> **v1.89.0+:** `glab milestone list` and `glab milestone get` support `--output json` / `-F json` for structured output, ideal for agent automation.

```bash
# List milestones with JSON output (v1.89.0+)
glab milestone list --output json
glab milestone list -F json

# Get a specific milestone with JSON output (v1.89.0+)
glab milestone get --output json
glab milestone get -F json
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
