# glab packages help

> Command reference captured from upstream glab v1.103.0 generated documentation.

## packages list

```text
List packages in a project's package registry.

glab packages list [flags]

Aliases: ls

Options:
      --jq string             Filter JSON output with a jq expression.
  -n, --name string           Filter packages by name (substring match).
      --package-type string   Package type composer, conan, debian, generic, golang, helm, maven, npm, nuget, pypi, terraform_module
  -p, --page int              Page number. (default 1)
  -P, --per-page int          Number of items to list per page. (default 30)
  -R, --repo string           Select another repository.
```

Examples:

```bash
# List all packages in the current project
glab packages list

# Use the alias
glab packages ls

# Filter by package name
glab packages list --name my-package

# List a specific page with a custom page size
glab packages list --page 2 --per-page 10

# List packages from another project
glab packages list -R owner/repo
```
