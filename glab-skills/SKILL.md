---
name: glab-skills
description: Inspect bundled agent skills and install, list, or update bundled and curated remote skills for GitLab CLI. Use when printing a bundled skill file, installing agent skills, checking the skill catalog, updating installed skills, or installing the remote Orbit wrapper skill. Triggers on skills, agent skills, glab skills, skill get, skill install, skill update, skill bundles.
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

# Update the installed core skill to the current glab-shipped version
glab skills update glab
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

# Update all installed skills, including curated remote skills
glab skills update --all

# Update one installed skill (bundled or curated remote)
glab skills update <name>
```

`get` writes the requested bundled file to stdout and defaults to `SKILL.md`; it does not install the skill. The `install` command sets up skill bundles for automation and AI agent workflows. Use `glab skills update <name>` or `glab skills update --all` to refresh installed skills from their sources. A name and `--all` are mutually exclusive, and one is required.

glab also notifies when installed bundled skills differ from the versions shipped with the current binary. When update checks run, it can also notify about curated remote skill updates; those checks fetch from GitLab.com on the update-check cadence rather than on every command. Notifications are best-effort and can be disabled with `notify_skill_updates` or `GLAB_NOTIFY_SKILL_UPDATES`. A notice does not update files automatically: review the content and use `glab skills update <name>` or `glab skills update --all` when intended.

### Curated remote Orbit skill

```bash
# Review the catalog before selecting a skill
glab skills list

# Install the remote Orbit wrapper skill into the current project
glab skills install orbit

# Alternatively, choose user scope or a custom parent directory
glab skills install orbit --global
glab skills install orbit --path ./reviewed-skills

# Refresh an installed copy in a standard project/user location
glab skills update orbit
```

`glab skills list` reads the bundled catalog and embedded remote registry without a network request. The `orbit` registry entry fetches the full `skills/orbit-wrapper` tree from the public `gitlab-org/orbit/knowledge-graph` project on GitLab.com, without authentication. Its `latest` ref means the project's default branch, not the latest release tag. The installer rewrites the upstream frontmatter name to `orbit` to match the installation directory. Review the remote content before allowing an agent to use it; it can change independently of the installed glab binary.

The default destination is `.agents/skills/orbit/` at the current Git repository root; `--global` uses `~/.agents/skills/orbit/`, and `--path` resolves relative to the current working directory. Existing skill files require `--force` to overwrite on install. `glab skills update orbit` re-fetches and overwrites changed content in standard locations, while `--all` updates all installed skills there. Custom `--path` locations are not discovered by update; explicitly reinstall into the reviewed custom path with `--force` when intended.

Despite help text that still says “bundled”, `list`, named `install`, and `update` also cover curated remote skills. Unnamed `glab skills install` installs only the bundled core `glab` skill. `glab skills get orbit` cannot print this remote skill: `get` is bundled-only. Installing the remote skill neither downloads nor runs the Orbit executable; managed-binary installation is a separate `glab orbit --install` operation.

## Troubleshooting

**`skills: command not found`:**
- `glab skills` manages CLI skills and extensions.
- Check your version with `glab version`; upgrade if needed.

**Skills install/update fails or hangs:**
- This is an experimental feature and may have rough edges.
- For bundled skills, check destination permissions and the installed catalog; installation does not require network access or glab authentication.
- For curated remote skills such as `orbit`, check connectivity to public `gitlab.com` and the `gitlab-org/orbit/knowledge-graph` project, plus destination permissions. These downloads are unauthenticated; self-managed-only or air-gapped hosts still need access to GitLab.com.
- Review `glab skills get --help`, `glab skills install --help`, `glab skills list`, and `glab skills update --help` for any updated flags or requirements.

**What skills are available?**
- Run `glab skills list` to see the bundled and curated remote catalog for your installed `glab` version.

## Related Skills

- `glab-duo` — GitLab Duo AI assistant integration
- `glab-mcp` — Deprecated glab MCP compatibility; use the [GitLab MCP Server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) for new integrations
- `glab-orbit` — Managed Orbit binary and graph workflows
- `glab-auth` — Authentication for GitLab operations; curated public remote skill downloads do not use it

## Command reference

### skills get

> Complete help from the verified release binary; immutable capture ID `5686d7484` maps to the release and archive checksums in `VERSION`. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

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

> Complete help from the verified release binary; immutable capture ID `5686d7484` maps to the release and archive checksums in `VERSION`. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

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

> Complete help from the verified release binary; immutable capture ID `5686d7484` maps to the release and archive checksums in `VERSION`. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

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

> Complete help from the verified release binary; immutable capture ID `5686d7484` maps to the release and archive checksums in `VERSION`. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

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
