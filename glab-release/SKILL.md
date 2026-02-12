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

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
