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
    cli [command]           Run the GitLab Duo CLI

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

Use `glab duo cli` for the forward-looking GitLab Duo Agent Platform experience. `glab` handles authentication for the Duo CLI after you authenticate once with `glab auth login`.

Prerequisites for the GA path are GitLab 19.2 or later and the GitLab Duo Agent Platform prerequisites. GitLab Self-Managed and Dedicated instances must also allow Duo CLI access. GitLab 18.11 through 19.1 require beta and experimental features to be enabled.

### Installing GitLab Duo CLI

`glab duo cli` supports install, update, and non-interactive confirmation flags:

```bash
# Install GitLab Duo CLI interactively
glab duo cli --install

# Install GitLab Duo CLI non-interactively (auto-confirm)
glab duo cli --install --yes

# Check for and install a Duo CLI update
glab duo cli --update
```

Use `--install` to download and install the GitLab Duo CLI binaries. Use `--yes` to skip confirmation prompts during installation, which is useful for automation and CI/CD pipelines.

To persist prompt behavior, set `duo_cli_auto_download` and `duo_cli_auto_run` with `glab config set ... --global`. All unrecognized arguments and flags after `glab duo cli` pass through to the Duo CLI binary.

### Important documentation note

Guidance that recommends `glab duo update` is stale; the current wrapper form is `glab duo cli --update`. Rely on live help before using any Duo subcommand that is not documented here.

When local CLI help and external documentation diverge during a transition, document the current upstream direction clearly and note compatibility caveats only when they materially affect usage.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
