---
name: glab-job
description: Work with individual CI/CD jobs including view, retry, cancel, trace logs, and download artifacts. Use when debugging job failures, viewing job logs, retrying jobs, or managing job execution. Triggers on job, CI job, job logs, retry job, job artifacts.
---

# glab job

## Overview

```

  Work with GitLab CI/CD jobs.                                                                                          
         
  USAGE  
         
    glab job <command> [command] [--flags]  
            
  COMMANDS  
            
    artifact <refName> <jobName> [--flags]  Download all artifacts from the last pipeline.
         
  FLAGS  
         
    -h --help                               Show help for this command.
    -R --repo                               Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab job --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
