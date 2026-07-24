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

## Structured output

`glab release list` and `glab release view` support `--output json` / `-F json` for structured output, which is useful for agent automation.

`--notes` and `--notes-file` are optional for `glab release create` and `glab release update`.

```bash
# List releases with JSON output
glab release list --output json
glab release list -F json

# View a release with JSON output
glab release view v1.2.0 --output json
glab release view v1.2.0 -F json

# Create a release without notes
glab release create v1.2.0

# Update a release without notes
glab release update v1.2.0 --name "My Release"
```

## Creating releases in GitLab CI/CD

For a pipeline job, prefer the predefined `CI_JOB_TOKEN` with glab CI auto-login; see [glab-auth](../glab-auth/SKILL.md) for the general mechanism and environment-variable precedence. The Releases API accepts that credential in the `JOB-TOKEN` header:

```bash
GLAB_ENABLE_CI_AUTOLOGIN=true \
  glab release create "$CI_COMMIT_TAG" \
  --notes-file CHANGELOG.md \
  --ref "$CI_COMMIT_SHA"
```

Do not assign `CI_JOB_TOKEN` to `GITLAB_TOKEN`: glab sends `GITLAB_TOKEN` as `PRIVATE-TOKEN`, which the Releases API rejects for a job token and can surface as `404 Not Found`. When job-token access is insufficient, use an approved project or group access token with `api` scope through `GITLAB_TOKEN`; never print that token.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
