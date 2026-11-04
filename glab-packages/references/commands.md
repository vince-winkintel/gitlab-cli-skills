# glab packages help

> **Current help capture `519ea19f7`.** Official glab v1.128.0 macOS arm64 binary; source commit `519ea19f7d3e9c701a4063f277ae27254bbafdad`; binary archive SHA-256 `541cdde6a0f706b4b69fed9fb558b421a361f63408d072d78ffdf304aee04248`. Only fences with this adjacent key use this provenance. Each complete stdout capture preserves leading spaces, blank lines, Fang uppercase headings, spelling (including `Gitlab`), examples, wrapping, and truncation; only trailing spaces/tabs are removed. Other captures retain their prior provenance and bytes. Current markers override historical unmarked labels.

> Fences with an adjacent `519ea19f7` marker (the `packages` parent and `packages delete`) use the binary provenance above. Only unmarked sections retain their upstream glab v1.111.0 generated-documentation/release-help provenance.

## packages

<!-- help-capture: 519ea19f7:6cbd77d763eb -->

```text

  Upload, download, list, and delete packages in a project's package
  registry, using your existing `glab` authentication.

  `list` and `delete` operate on packages of any type. `upload` and `download`
  are limited to generic packages, which let you store and retrieve
  arbitrary files identified by a package name, version, and file name.


  USAGE

    glab packages <command> [command] [--flags]

  COMMANDS

    delete [<id> | --id <id> | --name <name>] [--flags]                        Delete a package from a project's package registry.
    download --name <package> --version <version> --filename <file> [--flags]  Download a file from a project's package registry.
    list [--flags]                                                             List packages in a project's package registry.
    upload <file> --name <package> --version <version> [--flags]               Upload a file to a project's package registry.

  FLAGS

    -h --help                                                                  Show help for this command.
    -R --repo                                                                  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## packages delete

<!-- help-capture: 519ea19f7:3a96b8e022de -->

```text

  Identify the package by its numeric ID (as a positional argument or with
  `--id`), or by `--name` and `--version`. When using `--name`,
  `--package-type` defaults to `generic`.

  The command asks for confirmation before deleting; use `-y` to skip
  the prompt in scripts.

  By default, the package is removed from the current project. Use `--repo`
  to target another project.


  USAGE

    glab packages delete [<id> | --id <id> | --name <name>] [--flags]

  EXAMPLES

    # Delete a package by ID
    glab packages delete 1
    glab packages delete --id 1

    # Delete a generic package by name and version
    glab packages delete --name example-generic --version 1.0.0

    # Delete a package by name, version and type
    glab packages delete --name example-maven --version 1.0.0 --package-type maven

    # Skip the confirmation prompt
    glab packages delete 1 -y
    glab packages delete --name example-generic --version 1.0.0 --yes

  FLAGS

    -h --help       Show help for this command.
    --id            Id of the package to remove.
    --name          Name of the package to remove.
    --package-type  Type of the package to remove, used with --name. One of: cargo, composer, conan, debian, generic, golang, helm, maven, ml_model, npm, nuget, pypi, rpm, rubygems, terraform_module. (generic)
    -R --repo       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --version       Version of the package.
    -y --yes        Skip the confirmation prompt.

```

Examples:

```bash
# Delete a package by ID
glab packages delete 1

# Skip the confirmation prompt
glab packages delete 1 -y

# Use the 'del' alias
glab packages del 1
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

# Download to an absolute path
glab packages download -n my-package --version 1.0.0 --filename app.zip --path /tmp/downloads/app.zip

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
