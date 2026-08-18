---
name: glab-duo
description: Install and run GitLab Duo CLI through glab in interactive or headless mode. Use when accessing GitLab Duo Agent Platform from the terminal, running a bounded headless goal, or managing the wrapped Duo CLI binary. Triggers on Duo, GitLab Duo CLI, glab duo cli, AI assistant, headless goal, autonomous coding.
---

# glab duo

## Overview

`glab duo` is centered on the GitLab Duo Agent Platform. The current visible command surface exposes `glab duo cli`; the legacy `glab duo ask` command is hidden and deprecated.

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

### Interactive and headless modes

```bash
# Interactive, multi-prompt session with build and plan modes
glab duo cli

# One bounded prompt for a runner, script, or automated workflow
glab duo cli run --goal "Fix the failing tests in this project"

# Wrapper help versus the installed Duo CLI's own command surface
glab duo cli --help
glab duo cli help
```

Use headless `run --goal` only with a bounded task, an isolated working tree, explicit stop conditions, and an independent review of the resulting changes. `glab` passes unknown arguments and flags through to the Duo CLI binary, so verify the installed Duo CLI's own `help` before relying on forwarded options.

To persist wrapper prompt behavior, set `duo_cli_auto_download` and `duo_cli_auto_run` with `glab config set ... --global`. `--yes` skips confirmation prompts for the current invocation.

### Important documentation note

Guidance that recommends `glab duo update` is stale; the current wrapper form is `glab duo cli --update`. Rely on live help before using any Duo subcommand that is not documented here.

When local CLI help and external documentation diverge during a transition, document the current upstream direction clearly and note compatibility caveats only when they materially affect usage.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
