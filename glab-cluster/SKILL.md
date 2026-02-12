---
name: glab-cluster
description: Manage GitLab Kubernetes clusters and agent integrations. Use when connecting clusters, managing cluster agents, or working with Kubernetes integration. Triggers on cluster, Kubernetes, k8s, cluster agent, connect cluster.
---

# glab cluster

## Overview

```

  Manage GitLab Agents for Kubernetes and their clusters.                                                               
         
  USAGE  
         
    glab cluster <command> [command] [--flags]  
            
  COMMANDS  
            
    agent <command> [command] [--flags]  Manage GitLab Agents for Kubernetes.
    graph [--flags]                      Queries the Kubernetes object graph, using the GitLab Agent for Kubernetes. (EXPERIMENTAL)
         
  FLAGS  
         
    -h --help                            Show help for this command.
    -R --repo                            Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab cluster --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
