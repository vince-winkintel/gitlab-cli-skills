---
name: glab-duo
description: Interact with GitLab Duo AI assistant for code suggestions and chat. Use when accessing AI-powered code assistance, getting code suggestions, or chatting with GitLab Duo. Triggers on Duo, AI assistant, code suggestions, AI chat.
---

# glab duo

## Overview

```

  Work with GitLab Duo, our AI-native assistant for the command line.

  The GitLab Duo CLI integrates AI capabilities directly into your terminal
  workflow. It helps you retrieve forgotten Git commands and offers guidance on
  Git operations. You can accomplish specific tasks without switching contexts.

  To interact with the GitLab Duo Agent Platform, use the
  [GitLab Duo CLI](https://docs.gitlab.com/user/gitlab_duo_cli/).

  A unified experience is proposed in
  [epic 20826](https://gitlab.com/groups/gitlab-org/-/work_items/20826).

  USAGE

    glab duo <command> prompt [command] [--flags]

  COMMANDS

    ask <prompt> [--flags]  Generate Git commands from natural language.
    cli [command]           Run the GitLab Duo CLI (EXPERIMENTAL)

  FLAGS

    -h --help               Show help for this command.
```

## Quick start

```bash
glab duo --help
```

## v1.91.0 Changes

### Current command surface

In the current CLI surface, `glab duo` exposes:

```bash
glab duo ask "how do I revert the last commit but keep the changes?"
glab duo cli
```

Use `glab duo ask` for natural-language command help.

Use `glab duo cli` when you specifically want the experimental GitLab Duo CLI surface that `glab` now exposes.

### Important documentation note

Older guidance that recommended `glab duo update` is stale for the current CLI surface and should not be used unless a future `glab` release reintroduces that command in live help.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
