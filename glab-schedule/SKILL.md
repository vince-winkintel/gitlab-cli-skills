---
name: glab-schedule
description: Manage CI/CD pipeline schedules including create, list, update, delete, and run scheduled pipelines. Use when automating pipelines, setting up cron jobs, or managing scheduled builds. Triggers on schedule, scheduled pipeline, cron, pipeline schedule, automated build.
---

# glab schedule

## Overview

```

  Work with GitLab CI/CD schedules.                                                                                     
         
  USAGE  
         
    glab schedule <command> [command] [--flags]  
            
  COMMANDS  
            
    create [--flags]       Schedule a new pipeline.
    delete <id> [--flags]  Delete the schedule with the specified ID.
    list [--flags]         Get the list of schedules.
    run <id>               Run the specified scheduled pipeline.
    update <id> [--flags]  Update a pipeline schedule.
         
  FLAGS  
         
    -h --help              Show help for this command.
    -R --repo              Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab schedule --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
