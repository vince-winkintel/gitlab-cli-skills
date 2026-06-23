# glab packages help

> Command reference captured from upstream glab v1.104.0 generated documentation.

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

## packages upload

```text
Upload a file to a project's package registry.

glab packages upload <file> --name <package> --version <version> [flags]

Aliases: ul

Options:
      --filename string   Name to store the file under. Defaults to the local file name.
  -n, --name string       Name of the package.
  -v, --version string    Version of the package.
  -R, --repo string       Select another repository.
```

Examples:

```bash
# Upload a file as version 1.0.0 of package 'my-package'
glab packages upload ./build/app.zip --name my-package --version 1.0.0

# Store the file under a different name
glab packages upload ./build/app.zip --name my-package --version 1.0.0 --filename release.zip

# Use the 'ul' alias and upload to another project
glab packages ul ./build/app.zip -n my-package --version 1.0.0 -R owner/repo
```
