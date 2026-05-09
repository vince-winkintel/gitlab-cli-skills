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

## Command surface guidance

Upstream `glab` now hides and deprecates `glab duo ask`.

Treat `glab duo ask` as legacy guidance only for older installed versions that still expose it in live help. For current forward-looking documentation, prefer:

```bash
glab duo cli
```

Use `glab duo cli` when you specifically want the experimental GitLab Duo CLI surface that `glab` now exposes.

### Installing GitLab Duo CLI (v1.95.0+)

Starting in glab v1.95.0, `glab duo cli` gained `--install` and `--yes` flags:

```bash
# Install GitLab Duo CLI interactively
glab duo cli --install

# Install GitLab Duo CLI non-interactively (auto-confirm)
glab duo cli --install --yes
```

Use `--install` to download and install the GitLab Duo CLI binaries. Use `--yes` to skip confirmation prompts during installation, which is useful for automation and CI/CD pipelines.

### Important documentation note

Older guidance that recommended `glab duo update` is stale and should not be used unless a future `glab` release reintroduces that command in live help.

When release notes and local CLI help diverge during a transition, document the current upstream direction clearly and note compatibility caveats only when they materially affect usage.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
