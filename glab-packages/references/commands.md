# glab packages help

> Command reference captured from upstream glab v1.106.0 generated documentation.

## packages delete

```text
Delete a package from a project's package registry.

glab packages delete <id> [flags]

Aliases: rm

Options:
  -y, --yes             Skip the confirmation prompt.
  -R, --repo string     Select another repository.
```

Examples:

```bash
# Delete a package by ID
glab packages delete 1

# Skip the confirmation prompt
glab packages delete 1 -y

# Use the 'rm' alias
glab packages rm 1
```

## packages download

```text
Download a file from a project's package registry.

glab packages download --name <package> --version <version> --filename <file> [flags]

Aliases: dl

Options:
      --filename string   Name of the file within the package to download.
      --force             Overwrite the target file if it already exists.
  -n, --name string       Name of the package.
      --no-verify         Do not verify the checksum of the downloaded file. Warning: when enabled, this setting allows the download of files that are corrupt or tampered with.
  -p, --path string       Directory to save the file in (keeps its original name) or a full file path to rename it. Defaults to the original name in the current directory.
      --version string    Version of the package.
  -R, --repo string       Select another repository.
```

Examples:

```bash
# Download a package file to the current directory
glab packages download --name my-package --version 1.0.0 --filename app.zip

# Download into a directory, keeping the original file name
glab packages download -n my-package --version 1.0.0 --filename app.zip --path ./downloads/

# Download to an exact path, renaming the file
glab packages download -n my-package --version 1.0.0 --filename app.zip --path ./downloads/renamed.zip

# Download without verifying the checksum
glab packages download -n my-package --version 1.0.0 --filename app.zip --no-verify

# Overwrite an existing file
glab packages download -n my-package --version 1.0.0 --filename app.zip --force

# Use the 'dl' alias and target another project
glab packages dl -n my-package --version 1.0.0 --filename app.zip -R owner/repo
```

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
