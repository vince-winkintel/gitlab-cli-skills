---
name: glab-container-registry
description: Manage GitLab container registry repositories and tags with glab. Use when listing, viewing, or deleting container registry repositories/tags, cleaning old image tags, inspecting tag metadata, or using glab container-registry commands. Triggers on container registry, registry repository, registry tags, image tags, glab container-registry.
---

# glab container-registry

Manage GitLab container registry repositories and tags from the CLI.

> Added in glab v1.103.0. Repository IDs come from registry repository list/view output, not from Git repository project IDs.

## Common workflows

```bash
# List registry repositories for the current project
glab container-registry repository list

# List repositories for another project
glab container-registry repository list -R gitlab-org/cli

# List repositories for a group
glab container-registry repository list --group gitlab-org

# Include tag counts/tags in project repository output
glab container-registry repository list --include-tags-count --include-tags

# JSON output for automation
glab container-registry repository list --output json --jq '.[].id'
```

## Repository commands

```bash
# View a registry repository
glab container-registry repository view <repository-id>

# Include tags in the repository response
glab container-registry repository view <repository-id> --include-tags

# Delete a repository and all images/tags published to it (destructive)
glab container-registry repository delete <repository-id>
glab container-registry repository delete <repository-id> --yes
```

Aliases: `repository ls`, `repository show`, and `repository del`.

## Tag commands

```bash
# List tags for a registry repository
glab container-registry tag list <repository-id>

# List tags for a repository in another project
glab container-registry tag list <repository-id> -R owner/repo

# Include digest, size, and creation time for each tag
glab container-registry tag list <repository-id> --details

# View a specific tag
glab container-registry tag view <repository-id> <tag-name>

# Delete one tag (destructive)
glab container-registry tag delete <repository-id> <tag-name>
glab container-registry tag delete <repository-id> <tag-name> --yes
```

Aliases: `tag ls`, `tag show`, and `tag del`.

## Bulk tag cleanup

Bulk deletion is scheduled asynchronously by GitLab. Matching tags may remain visible until the background deletion job completes.

```bash
# Schedule tags matching a regex for deletion
glab container-registry tag delete <repository-id> \
  --name-regex-delete '^release-.*' \
  --yes

# Delete old tags while keeping the 10 most recent matching tags
glab container-registry tag delete <repository-id> \
  --name-regex-delete '.*' \
  --keep-n 10 \
  --older-than 30d \
  --yes

# Keep tags matching a regex during bulk deletion
glab container-registry tag delete <repository-id> \
  --name-regex-delete '.*' \
  --name-regex-keep '^stable$|^latest$' \
  --yes
```

Bulk flags:
- `--name-regex-delete <regex>` — tag names to delete.
- `--name-regex-keep <regex>` — tag names to keep.
- `--keep-n <n>` — keep latest N matching tags.
- `--older-than <duration>` — delete tags older than durations like `7d` or `1month`.

## Safety notes

- Treat repository/tag delete commands as destructive; omit `--yes` unless the target IDs and regexes have been reviewed.
- Use `--output json` and `--jq` for scripts instead of parsing tables.
- Use `-R/--repo` whenever running outside the target project's checkout.

## Reference

See [references/commands.md](references/commands.md) for command synopsis and flags.
