---
name: glab-help
description: Display help information for glab commands and subcommands. Use when learning glab commands, viewing command syntax, or getting usage examples. Triggers on help, command help, usage, glab help.
---

# glab help

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## Renderer and capture fidelity

Fang renders uppercase sections such as `USAGE`, `COMMANDS`, `FLAGS`, `ARGUMENTS`, and `ENVIRONMENT VARIABLES`; annotation-provided argument/environment sections are part of complete help. Do not reconstruct Cobra-style output from source or silently omit these sections.

Current keyed binary captures preserve complete stdout with only trailing spaces/tabs removed. Earlier documentation may normalize product spelling to canonical GitLab; those legacy blocks retain that normalization and provenance and are not described as byte-exact captures. Unchanged historical captures are not re-stamped. For managed external commands and package-manager wrappers, inspect the parent renderer with `glab help <command>` rather than forwarding `--help` to another program.

## Overview

<!-- help-capture: 9b430a11f:5cb2e7ea7a8c -->

```text

  Help provides help for any command in the application.
  Simply type glab help [path to command] for full details.

  USAGE

    glab help [command] [--flags]

  FLAGS

    -h --help  Show help for this command.

```

## Quick start

```bash
glab help --help
```

## Subcommands

This command has no subcommands.