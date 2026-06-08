---
name: glab-skills
description: Install, list, and update bundled agent skills for GitLab CLI. Use when installing agent skills, checking available bundled skills, updating installed glab skills, managing skill bundles, or setting up automated workflows. Triggers on skills, agent skills, glab skills, skill install, skill update, skill bundles.
---

# glab skills

## Overview

```

  Install and manage bundled agent skills for GitLab CLI.

  Skills follow the Agent Skills specification and work with
  any compatible agent, including GitLab Duo Agent Platform, Claude Code, Codex,
  and Gemini CLI.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.

  USAGE

    glab skills <command> [command] [--flags]

  COMMANDS

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

# Install bundled agent skills
glab skills install

# List bundled skills
glab skills list

# Update installed bundled skills to the current glab-shipped version
glab skills update
```

## Common workflows

### Installing, listing, and updating bundled skills

```bash
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

The `install` command sets up pre-packaged skill bundles designed to extend glab capabilities for automation and AI agent workflows. Newer `glab` versions also notify when installed bundled skills have updates available; use `glab skills update` to refresh them to the current version shipped with the installed CLI.

## Troubleshooting

**`skills: command not found`:**
- `glab skills` manages CLI skills and extensions.
- Check your version with `glab version`; upgrade if needed.

**Skills install/update fails or hangs:**
- This is an experimental feature and may have rough edges.
- Check your network connection and glab auth status.
- Review `glab skills install --help`, `glab skills list`, and `glab skills update --help` for any updated flags or requirements.

**What skills are available?**
- Run `glab skills list` to see the bundled catalog for your installed `glab` version.

## Related Skills

- `glab-duo` — GitLab Duo AI assistant integration
- `glab-mcp` — Model Context Protocol server for AI integrations
- `glab-auth` — Authentication required for skill installation

## Command reference

```text
glab skills <command> [flags]

glab skills install [name] [flags]
  -h --help  Show help for this command

glab skills list

glab skills update [name] [flags]
  -h --help  Show help for this command
```
