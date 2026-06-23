---
name: glab-packages
description: List and upload GitLab project package registry packages with glab. Use when inspecting packages, filtering GitLab package registry entries by package name/type, paginating package registry results, uploading generic package files, or using glab packages commands. Triggers on GitLab packages, package registry, glab packages, npm packages in GitLab, Maven packages in GitLab, generic package upload.
---

# glab packages

List packages in a GitLab project's package registry and upload files as generic packages.

> Added in glab v1.103.0. `glab packages list` / `ls` lists project package registries. glab v1.104.0 added `glab packages upload` / `ul` for generic package uploads.

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

## Reference

See [references/commands.md](references/commands.md) for command synopsis and flags.
