---
name: glab-milestone
description: Manage project milestones including create, list, update, view, and close operations. Use when planning releases, tracking milestone progress, or organizing issues/MRs by milestone. Triggers on milestone, release planning, milestone progress, version milestone.
---

# glab milestone

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## Include descendant milestones

Use `glab milestone list --group <group> --include-descendants` to include milestones from subgroups and descendant projects. It cannot be combined with `--project`; select the group explicitly rather than assuming the current project determines a group. `--include-ancestors` is a separate filter. Existing page/per-page boundaries still apply.

## Overview

<!-- help-capture: 9b430a11f:f4bff38dfc18 -->

```text

  Milestones group issues, merge requests, and epics around a shared
  goal or release. Use the subcommands to create, list, edit, delete,
  or look up milestones in the current project, in another project, or
  in a group.


  USAGE

    glab milestone <command> [command] [--flags]

  COMMANDS

    create [--flags]       Create a milestone in a project or group.
    delete <id> [--flags]  Delete a milestone from a project or group.
    edit <id> [--flags]    Edit a milestone in a project or group.
    get [<id>] [--flags]   Get a milestone by ID in a project or group.
    list [--flags]         List milestones in a project or group.

  FLAGS

    -h --help              Show help for this command.
    -R --repo              Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## Quick start

```bash
glab milestone --help
```

## Structured output

`glab milestone list` and `glab milestone get` support `--output json` / `-F json` for structured output, which is useful for agent automation.

```bash
# List milestones with JSON output
glab milestone list --output json
glab milestone list -F json

# Get a specific milestone with JSON output
glab milestone get --output json
glab milestone get -F json
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
