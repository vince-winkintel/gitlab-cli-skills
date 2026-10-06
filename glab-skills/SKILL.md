---
name: glab-skills
description: Inspect, install, list, and update bundled agent skills for GitLab CLI. Use when printing a bundled skill file without installing it, installing agent skills, checking available bundled skills, updating installed glab skills, or managing skill bundles. Triggers on skills, agent skills, glab skills, skill get, skill install, skill update, skill bundles.
---

# glab skills

## Overview

> Help captured from the checksum-verified macOS arm64 release binary. Terminal padding and trailing whitespace are removed; release provenance is recorded in `VERSION`.

```text

  Install the bundled glab agent skills so that AI agents can discover
  and use glab effectively.

  Skills follow the Agent Skills specification and work with
  any compatible agent, including GitLab Duo Agent Platform, Claude Code, Codex,
  and Gemini CLI.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab skills <command> [command] [--flags]

  COMMANDS

    get <name> [<path>]       Print a bundled agent skill file. (EXPERIMENTAL)
    install [name] [--flags]  Install glab's bundled agent skills. (EXPERIMENTAL)
    list                      List the available bundled agent skills. (EXPERIMENTAL)
    update [name] [--flags]   Update installed agent skills to the current shipped version. (EXPERIMENTAL)

  FLAGS

    -h --help                 Show help for this command.

```

## ⚠️ Experimental Feature

`glab skills` is marked **EXPERIMENTAL** upstream:
- command shape and functionality may change
- skill bundle format is not yet stable
- availability may vary by glab version
- use for exploration and prototyping, not production workflows

See: https://docs.gitlab.com/policy/development_stages_support/

## Quick start

```bash
# View available skills commands
glab skills --help

# Inspect a bundled skill without installing it
glab skills get glab

# Install bundled agent skills
glab skills install

# List bundled skills
glab skills list

# Update installed bundled skills to the current glab-shipped version
glab skills update
```

## Common workflows

### Inspecting, installing, listing, and updating bundled skills

```bash
# Print the bundled skill manifest without installing it
glab skills get glab

# Print a supporting file relative to a bundled skill root
glab skills get <name> references/<file>.md

# Install agent skills interactively
glab skills install

# Install a named bundled skill when supported by the shipped catalog
glab skills install <name>

# List available bundled skills
glab skills list

# Update all installed bundled skills
glab skills update

# Update one installed bundled skill
glab skills update <name>
```

`get` writes the requested bundled file to stdout and defaults to `SKILL.md`; it does not install the skill. The `install` command sets up pre-packaged skill bundles designed to extend glab capabilities for automation and AI agent workflows. Newer `glab` versions also notify when installed bundled skills have updates available; use `glab skills update` to refresh them to the current version shipped with the installed CLI.

## Troubleshooting

**`skills: command not found`:**
- `glab skills` manages CLI skills and extensions.
- Check your version with `glab version`; upgrade if needed.

**Skills install/update fails or hangs:**
- This is an experimental feature and may have rough edges.
- Check your network connection and glab auth status.
- Review `glab skills get --help`, `glab skills install --help`, `glab skills list`, and `glab skills update --help` for any updated flags or requirements.

**What skills are available?**
- Run `glab skills list` to see the bundled catalog for your installed `glab` version.

## Related Skills

- `glab-duo` — GitLab Duo AI assistant integration
- `glab-mcp` — Model Context Protocol server for AI integrations
- `glab-auth` — Authentication required for skill installation

## Command reference

### skills get

```text

  Print a file from an agent skill bundled with this glab binary without installing it.

  The path is relative to the skill root and defaults to `SKILL.md`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab skills get <name> [<path>] [--flags]

  EXAMPLES

    # Print the manifest for the bundled glab skill
    glab skills get glab

    # Print the other bundled skill
    glab skills get glab-stack

    # For skills that ship supporting files, use the path form
    # glab skills get <name> references/<file>.md

  FLAGS

    -h --help  Show help for this command.
```

### skills install

```text

  Install bundled `SKILL.md` files to `.agents/skills/`, the
  cross-agent standard defined by the Agent Skills specification. This works
  with GitLab Duo Agent Platform, Claude Code, Codex, Gemini CLI, and any
  other compliant agent.

  By default, only the core `glab` skill is installed. Pass a positional
  `name` argument to install a specific bundled skill instead. Run
  `glab skills list` to see what is available.

  Install scope:

  - By default, skills are installed for the current project, in `.agents/skills/`
    at the root of the current Git repository.
  - Use `--global` to install skills for the current user, in
    `~/.agents/skills/`.
  - Use `--path` to install skills to a custom directory. The path is resolved
    relative to the current working directory, not the repository root.

  To overwrite an existing skill file, use `--force`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab skills install [name] [--flags]

  EXAMPLES

    # Install the core glab skill in the current project (default)
    glab skills install

    # Install a specific bundled skill by name
    glab skills install glab-stack

    # Install the core skill globally (user scope)
    glab skills install --global

    # Install a skill to a custom directory
    glab skills install glab-stack --path /path/to/skills

    # Overwrite an existing skill file
    glab skills install --force

  FLAGS

    -f --force   Overwrite existing skill files.
    -g --global  Install skills at user scope (~/.agents/skills/).
    -h --help    Show help for this command.
    --path       Install skills to the directory at <path>.
```

### skills list

```text

  List the agent skills bundled with glab. Use the name of a skill with
  'glab skills install <name>' to install just that one.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab skills list [--flags]

  EXAMPLES

    # List every bundled skill with its description
    glab skills list

  FLAGS

    -h --help  Show help for this command.
```

### skills update

```text

  Re-fetch installed agent skills from their source (bundled in this
  glab binary, or the curated remote registry) and overwrite the on-disk
  copy if it differs.

  By default, updates only the named skill in every well-known location
  it is installed (the current project's '.agents/skills/' and the
  user-scope '~/.agents/skills/'). Use --all to update every installed
  skill in those locations.

  Skills whose on-disk content already matches the source are left alone.
  Skills installed via 'glab skills install --path' are not considered —
  update only knows about the two well-known locations.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab skills update [name] [--flags]

  EXAMPLES

    # Update the bundled glab skill in every location it is installed
    glab skills update glab

    # Update every installed skill
    glab skills update --all

  FLAGS

    --all      Update every installed skill.
    -h --help  Show help for this command.
```
