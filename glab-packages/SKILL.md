---
name: glab-packages
description: List, upload, download, and delete GitLab project package registry packages with glab. Use when inspecting packages, filtering GitLab package registry entries by package name/type, paginating package registry results, uploading or downloading generic package files, deleting packages, or using glab packages commands. Triggers on GitLab packages, package registry, glab packages, npm packages in GitLab, Maven packages in GitLab, generic package upload, generic package download, delete package.
---

# glab packages

List packages in a GitLab project's package registry, upload/download generic package files, and delete package registry entries by ID.

> Added in glab v1.103.0. `glab packages list` / `ls` lists project package registries. glab v1.104.0 added `glab packages upload` / `ul` for generic package uploads. glab v1.106.0 added `glab packages download` / `dl` for generic package downloads and `glab packages delete` / `rm` for package deletion by numeric ID.

## Quick start

```bash
# List all packages in the current project
glab packages list

# Alias
glab packages ls

# List packages from another project
glab packages list -R owner/repo

# Upload a file as a generic package version
glab packages upload ./build/app.zip --name my-package --version 1.0.0

# Download a generic package file
glab packages download --name my-package --version 1.0.0 --filename app.zip

# Delete a package by numeric ID after listing packages
glab packages delete 12345 --yes
```

## Filtering

```bash
# Filter by package name substring
glab packages list --name my-package

# Filter by package type
glab packages list --package-type npm
glab packages list --package-type maven
glab packages list --package-type generic
```

Supported package types from glab help:

```text
composer, conan, debian, generic, golang, helm, maven, npm, nuget, pypi, terraform_module
```

## Pagination and automation

```bash
# Select a page and page size
glab packages list --page 2 --per-page 10

# JSON output filtering is available through the global --jq support on this command
glab packages list --jq '.[].name'
```

Use `-R/--repo` when running outside the target project's Git checkout. Prefer structured output/`--jq` for scripts rather than parsing text tables.

## Upload generic package files

```bash
# Upload a local file under its original filename
glab packages upload ./build/app.zip --name my-package --version 1.0.0

# Store the uploaded file under a different package filename
glab packages upload ./build/app.zip --name my-package --version 1.0.0 --filename release.zip

# Alias and explicit target project
glab packages ul ./build/app.zip -n my-package --version 1.0.0 -R owner/repo
```

Upload stores the file as a **generic** package in the target project's package registry. `--name` and `--version` are required; `--filename` defaults to the local file basename. Use `-R/--repo` for uploads outside the target project checkout.

## Download generic package files

```bash
# Download a package file to the current directory
glab packages download --name my-package --version 1.0.0 --filename app.zip

# Download into a directory, keeping the original file name
glab packages download -n my-package --version 1.0.0 --filename app.zip --path ./downloads/

# Download to an exact path, renaming the file
glab packages download -n my-package --version 1.0.0 --filename app.zip --path ./downloads/renamed.zip

# Skip checksum verification only when you intentionally accept the integrity risk
glab packages download -n my-package --version 1.0.0 --filename app.zip --no-verify

# Alias, overwrite an existing target, and explicit project targeting
glab packages dl -n my-package --version 1.0.0 --filename app.zip --force -R owner/repo
```

Download is limited to **generic** package files and requires `--name`, `--version`, and `--filename`. By default glab verifies the downloaded file against registry checksum metadata and fails if the destination already exists. Use `--path` for a directory or exact output filename, `--force` to overwrite, and `--no-verify` only when checksum verification is intentionally bypassed.

## Delete packages

```bash
# Find the package ID first
glab packages list --name my-package

# Delete by numeric package ID; prompts for confirmation
glab packages delete 12345

# Skip confirmation for automation after independently confirming the ID
glab packages delete 12345 --yes

# Alias
glab packages rm 12345
```

Delete operates on a package's numeric ID, not the package name/version. Use `glab packages list` (preferably with JSON/`--jq` in scripts) to identify the ID, then pass `--yes` only when the target package has been verified.

## Reference

See [references/commands.md](references/commands.md) for command synopsis and flags.
