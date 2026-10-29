---
name: glab-cluster
description: Manage GitLab Kubernetes clusters and agent integrations. Use when connecting clusters, managing cluster agents, or working with Kubernetes integration. Triggers on cluster, Kubernetes, k8s, cluster agent, connect cluster.
---

# glab cluster

> Only blocks marked `4dd0d32d1` were captured in this refresh from the checksum-verified binary identified in `VERSION`. Complete help is preserved, including leading whitespace, blank lines, wrapping/truncation, and product spelling (`Gitlab` included); only trailing spaces/tabs are removed. Other blocks retain their individual prior provenance.

## Overview

<!-- help-capture: 4dd0d32d1:ed5b0c665871 -->

```text

  Agents connect your cluster to GitLab, enabling pull-based deployments
  and secure access to the Kubernetes API.


  USAGE

    glab cluster <command> [command] [--flags]

  COMMANDS

    agent <command> [command] [--flags]  Manage GitLab Agents for Kubernetes.
    graph [--flags]                      Query the Kubernetes object graph using the GitLab Agent for Kubernetes. (EXPERIMENTAL)

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## Quick start

```bash
glab cluster --help
```

## Structured output

`glab cluster agent list` and `glab cluster agent token list` support `--output json` / `-F json` for structured output, which is useful for agent automation.

```bash
# List cluster agents with JSON output
glab cluster agent list --output json
glab cluster agent list -F json

# List agent tokens with JSON output
glab cluster agent token list <agent-id> --output json
glab cluster agent token list <agent-id> -F json
```

`glab cluster agent list` uses the API-reported total in its text header when available, separately from the current page's row count. JSON remains the requested page of agents. Traverse `--page` / `--per-page` explicitly; neither a page's JSON length nor missing total metadata proves there are no further results. This total change applies to the agent list, not the agent-token list.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.

## Snap kubeconfig access

The snap uses the manual-connect `dot-kube-config` plug, scoped to `~/.kube/config` and `~/.kube/config.lock`, rather than the whole `.kube` directory. A different kubeconfig path can remain inaccessible under confinement. Connecting the plug or updating kubeconfig changes local permissions/configuration and requires approval; do not treat CLI help as permission to connect it or modify a cluster.
