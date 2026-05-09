---
name: glab-skills
description: Install and manage bundled agent skills for GitLab CLI. Use when installing agent skills, managing skill bundles, or setting up automated workflows. Triggers on skills, agent skills, glab skills, skill install, skill bundles.
---

# glab skills

## Overview

```

  Install and manage bundled agent skills for GitLab CLI.

  This feature is experimental and provides a way to install pre-packaged
  skills and workflows that extend glab functionality for AI agents and
  automation use cases.

  USAGE

    glab skills <command> [--flags]

  COMMANDS

    install [flags]  Install bundled agent skills (EXPERIMENTAL)

  FLAGS

    -h --help        Show help for this command.
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
```

## Common workflows

### Installing bundled skills

```bash
# Install agent skills interactively
glab skills install

# Check installation status
glab skills install --help
```

The `install` command downloads and sets up pre-packaged skill bundles designed to extend glab capabilities for automation and AI agent workflows.

## Troubleshooting

**`skills: command not found`:**
- `glab skills` was added in glab v1.95.0.
- Check your version with `glab version`; upgrade if needed.

**Skills install fails or hangs:**
- This is an experimental feature and may have rough edges.
- Check your network connection and glab auth status.
- Review `glab skills install --help` for any updated flags or requirements.

**What skills are available?**
- The upstream skill bundle catalog is not yet publicly documented.
- Run `glab skills install` to see interactive prompts or available bundles.

## Related Skills

- `glab-duo` — GitLab Duo AI assistant integration
- `glab-mcp` — Model Context Protocol server for AI integrations
- `glab-auth` — Authentication required for skill installation

## Command reference

```text
glab skills <command> [flags]

glab skills install [flags]
  -h --help  Show help for this command
```
