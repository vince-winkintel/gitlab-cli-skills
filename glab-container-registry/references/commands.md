# glab container-registry help

> Command reference captured from upstream glab v1.103.0 generated documentation.

## container-registry repository list

```text
glab container-registry repository list [flags]

Aliases: ls

Options:
  -g, --group string          List container registry repositories for a group.
      --include-tag-details   Fetch digest, size, and creation time for included tags. Makes one API call per tag. Project JSON output only. Implies --include-tags.
      --include-tags          Include tags in the response. Project repositories only.
      --include-tags-count    Include the number of tags in the response. Project repositories only. (default true)
      --jq string             Filter JSON output with a jq expression.
  -F, --output string         Format output as: text, json. (default "text")
  -p, --page int              Page number. (default 1)
  -P, --per-page int          Number of items to list per page. (default 30)
  -R, --repo string           Select another repository.
```

## container-registry repository view

```text
glab container-registry repository view <repository-id> [flags]

Aliases: show

Options:
      --include-tags         Include tags in the response.
      --include-tags-count   Include the number of tags in the response. (default true)
      --jq string            Filter JSON output with a jq expression.
  -F, --output string        Format output as: text, json. (default "text")
  -R, --repo string          Select another repository.
```

## container-registry repository delete

```text
glab container-registry repository delete <repository-id> [flags]

Aliases: del

Options:
  -y, --yes   Skip the confirmation prompt.
  -R, --repo string   Select another repository.
```

## container-registry tag list

```text
glab container-registry tag list <repository-id> [flags]

Aliases: ls

Options:
      --details         Fetch digest, size, and creation time for each tag. Makes one API call per tag.
      --jq string       Filter JSON output with a jq expression.
  -F, --output string   Format output as: text, json. (default "text")
  -p, --page int        Page number. (default 1)
  -P, --per-page int    Number of items to list per page. (default 30)
  -R, --repo string     Select another repository.
```

## container-registry tag view

```text
glab container-registry tag view <repository-id> <tag-name> [flags]

Aliases: show

Options:
      --jq string       Filter JSON output with a jq expression.
  -F, --output string   Format output as: text, json. (default "text")
  -R, --repo string     Select another repository.
```

## container-registry tag delete

```text
glab container-registry tag delete <repository-id> [<tag-name>] [flags]

Aliases: del

Options:
      --keep-n int                 Keep the latest N matching tags. Bulk deletion only; scheduled asynchronously.
      --name-regex-delete string   Regular expression for tag names to delete. Bulk deletion only; scheduled asynchronously.
      --name-regex-keep string     Regular expression for tag names to keep. Bulk deletion only; scheduled asynchronously.
      --older-than string          Delete tags older than the given duration, such as 7d or 1month. Bulk deletion only; scheduled asynchronously.
  -y, --yes                        Skip the confirmation prompt.
  -R, --repo string                Select another repository.
```
