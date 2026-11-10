---
name: glab-release
description: Manage GitLab releases including create, list, view, delete, download, and upload release assets. Use when publishing software versions, managing release notes, uploading binaries/artifacts, downloading release files, or viewing release history. Triggers on release, version, tag, publish release, release notes, download release.
---

# glab release

> **Help provenance — capture key `519ea19f7`:** checksum-verified official macOS arm64 binary; source commit `519ea19f7d3e9c701a4063f277ae27254bbafdad`; binary archive SHA-256 `541cdde6a0f706b4b69fed9fb558b421a361f63408d072d78ffdf304aee04248`. Applies only to adjacent `519ea19f7` markers. Complete output is preserved except trailing spaces/tabs.

## Existing download destinations

`glab release download` stops if a destination file exists. Choose `--skip-existing` to keep existing files and download missing assets, or approve `--clobber` to replace them; the flags are mutually exclusive. A skipped local file has not been verified against the release. Downloads use a temporary file before replacement, so a failed transfer does not validate or replace the old file. Review the target directory and preserve checksum verification.

## Asset-link validation and creation

`release create` and `release upload` reject null elements such as `[null]` in `--assets-links` before sending requests, reporting the zero-based index. Supply a JSON array of link objects with the intended names, URLs, optional `link_type`, and `direct_asset_path`. Do not combine deprecated `filepath` with `direct_asset_path`; the former alone is aliased with a warning.

For a new release, asset links are sent in the release-creation request, including links for files uploaded beforehand. This makes the release visible with its links immediately; it does not make the entire operation one network request or transactional. File/package uploads can already exist when release creation fails. Updating an existing release and `release upload` still create links separately. Verify existing release/assets before retrying after partial failure.

Creation, upload, update, deletion, tag creation, and milestone closure are operational writes. Obtain approval for the exact project, tag, release notes, asset destinations, and side effects; verify host/actor before execution. `release create` can update an existing release; use `--no-update` when that must be refused.

## List totals and pagination

`glab release list` uses the API-reported total in its text header when available, separate from the number of returned rows. Missing totals must not be treated as proof there are no other pages. JSON contains the requested page's items, not every item counted by the header. Use `--page` and `--per-page` to traverse results explicitly; do not equate JSON array length with the server total.

## Asset transport

Release downloads recognize same-instance Markdown upload asset URLs and fetch them through the authenticated API, including project-ID and namespace/project upload paths. Use the intended host and identity; do not work around an authentication failure by exposing tokens in URLs. Asset uploads can run in parallel, so verify the final release assets instead of depending on upload completion order.

## Overview

<!-- help-capture: 519ea19f7:2fe464ec3878 -->

```text

  A release bundles a Git tag with release notes and downloadable
  assets, such as binaries or source archives.

  Create and update releases, list and view them, upload assets, and
  download or delete releases. Use `--repo` to target a project other
  than the current one.


  USAGE

    glab release <command> [command] [--flags]

  COMMANDS

    create <tag> [<files>...] [--flags]  Create a new GitLab release, or update an existing one.
    delete <tag> [--flags]               Delete a GitLab release.
    download [<tag>] [--flags]           Download asset files from a GitLab release.
    list [--flags]                       List releases in a repository.
    upload <tag> [<files>...] [--flags]  Upload release asset files or links to a GitLab release.
    view [<tag>] [--flags]               View information about a GitLab release.

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## Failed asset downloads

`release download` reports file-close failures as errors and attempts to remove the partial destination after a download or close failure. Existing destinations remain protected by exclusive creation. Removal can also fail, so inspect the intended destination and error before retrying; never delete a pre-existing asset merely to bypass a file-exists error. This cleanup does not roll back other successfully downloaded assets.

## Quick start

```bash
glab release --help
```

## Structured output

`glab release list` and `glab release view` support `--output json` / `-F json` for structured output, which is useful for agent automation.

`--notes` and `--notes-file` are optional for `glab release create`, including when it updates an existing release. Update preservation is independent for each field:

- **Description:** when no notes are supplied by flags or interactive input, keep the existing description even if `--name` is supplied. Explicit notes, including `--notes ""` or an empty notes file, replace the description.
- **Name:** when no name is supplied by flag or interactive input, keep the existing name even if notes are supplied. Explicit `--name ""` falls back to the tag rather than clearing the name. If the existing name is itself empty, omission also falls back to the tag.

Interactive runs can still prompt for these values; omitting a flag alone does not guarantee preservation. Selecting "Leave blank" in the notes prompt preserves an existing description, unlike explicit empty notes. Review intended changes and verify the resulting release after the approved operation; omission does not make the rest of the command read-only.

The tag is optional for `glab release view` and `glab release download`; omit it to target the latest release. Pass an explicit tag in release automation when reproducibility matters.

```bash
# List releases with JSON output
glab release list --output json
glab release list -F json

# View a release with JSON output
glab release view v1.2.0 --output json
glab release view v1.2.0 -F json

# Create a release without notes
glab release create v1.2.0

# Non-interactive update: change the name and preserve existing notes
GLAB_NO_PROMPT=1 glab release create v1.2.0 --name "My Release"
```

## Creating releases in GitLab CI/CD

For a pipeline job, prefer the predefined `CI_JOB_TOKEN` with glab CI auto-login; see [glab-auth](../glab-auth/SKILL.md) for the general mechanism and environment-variable precedence. The Releases API accepts that credential in the `JOB-TOKEN` header:

```bash
GLAB_ENABLE_CI_AUTOLOGIN=true \
  glab release create "$CI_COMMIT_TAG" \
  --notes-file CHANGELOG.md \
  --ref "$CI_COMMIT_SHA"
```

The Milestones API does not accept `CI_JOB_TOKEN`, even when that token can create a release. Use `--no-close-milestone` when milestone closure is outside the approved job scope, or an approved project/group access token with `api` scope when closure is required. A 401/403 during milestone closure with a resolved job token adds this explanation; other errors or token kinds do not get that hint. Milestone-close errors are logged without making this step fail the release command. Release creation or asset uploads may already have succeeded, so a successful exit does not prove milestone closure; inspect both states before retrying.

Do not assign `CI_JOB_TOKEN` to `GITLAB_TOKEN`: glab sends `GITLAB_TOKEN` as `PRIVATE-TOKEN`, which the Releases API rejects for a job token and can surface as `404 Not Found`. When job-token access is insufficient, use an approved project or group access token with `api` scope through `GITLAB_TOKEN`; never print that token.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
