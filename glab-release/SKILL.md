---
name: glab-release
description: Manage GitLab releases including create, list, view, delete, download, and upload release assets. Use when publishing software versions, managing release notes, uploading binaries/artifacts, downloading release files, or viewing release history. Triggers on release, version, tag, publish release, release notes, download release.
---

# glab release

## Overview

```

  Manage GitLab releases.                                                                                               
         
  USAGE  
         
    glab release <command> [command] [--flags]  
            
  COMMANDS  
            
    create <tag> [<files>...] [--flags]  Create a new GitLab release, or update an existing one.
    delete <tag> [--flags]               Delete a GitLab release.
    download <tag> [--flags]             Download asset files from a GitLab release.
    list [--flags]                       List releases in a repository.
    upload <tag> [<files>...] [--flags]  Upload release asset files or links to a GitLab release.
    view <tag> [--flags]                 View information about a GitLab release.
         
  FLAGS  
         
    -h --help                            Show help for this command.
    -R --repo                            Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab release --help
```

## v1.89.0 Updates

> **v1.89.0+:** `glab release list` and `glab release view` support `--output json` / `-F json` for structured output, ideal for agent automation.

> **v1.89.0+:** `--notes` and `--notes-file` are now **optional** for `glab release create` and `glab release update`. Previously required.

```bash
# List releases with JSON output (v1.89.0+)
glab release list --output json
glab release list -F json

# View a release with JSON output (v1.89.0+)
glab release view v1.2.0 --output json
glab release view v1.2.0 -F json

# Create a release without notes (v1.89.0+) — notes are now optional
glab release create v1.2.0

# Update a release without notes (v1.89.0+)
glab release update v1.2.0 --name "My Release"
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
