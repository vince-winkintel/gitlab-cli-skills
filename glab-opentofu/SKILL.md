---
name: glab-opentofu
description: Work with OpenTofu state management in GitLab. Use when managing Terraform/OpenTofu state, configuring state backends, or working with infrastructure as code. Triggers on OpenTofu, Terraform, state management, infrastructure as code, IaC.
---

# glab opentofu

## Overview

```

  Work with the OpenTofu or Terraform integration.                                                                      
         
  USAGE  
         
    glab opentofu <command> [command] [--flags]  
            
  COMMANDS  
            
    init <state> [--flags]               Initialize OpenTofu or Terraform.
    state <command> [command] [--flags]  Work with the OpenTofu or Terraform states.
         
  FLAGS  
         
    -h --help                            Show help for this command.
    -R --repo                            Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab opentofu --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
