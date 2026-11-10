---
name: glab-alias
description: Create, list, and delete GitLab CLI command aliases and shortcuts. Use when creating custom glab commands, managing CLI shortcuts, or viewing existing aliases. Triggers on alias, shortcut, custom command, CLI alias.
---

# glab alias

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## Shell completion boundaries

Shell completion for `alias delete` suggests configured alias names. `alias set` does not complete arbitrary shell commands or file paths. Inspect the alias expansion before approving any persistent alias write; completion is not proof that a shell expansion is safe.

## Argument boundaries

Arguments supplied to an alias are passed through without reconstructing them as a shell-joined string. Keep each intended argument quoted at the calling shell; quoted whitespace and special characters remain part of that argument. Explicit shell aliases still execute shell code and require review before use.

## Overview

<!-- help-capture: 9b430a11f:6cdbed27d9b0 -->

```text

  Aliases are shortcuts for longer glab commands. Use aliases to save
  keystrokes for commands you run often, or to compose shell pipelines
  around glab commands.


  USAGE

    glab alias [command] [--flags]

  COMMANDS

    delete <alias name> [--flags]           Delete an alias.
    list [--flags]                          List aliases.
    set <alias name> '<command>' [--flags]  Set an alias for a longer command.

  FLAGS

    -h --help                               Show help for this command.

```

## Quick start

```bash
glab alias --help
glab alias list
```

`glab alias list` wraps long rows instead of truncating expansions at a fixed column width, so the complete stored command remains visible. Treat shell aliases as executable code and review the full expansion before running an unfamiliar alias.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
