---
name: glab-packages
description: List GitLab project package registry packages with glab. Use when inspecting packages, filtering GitLab package registry entries by package name/type, paginating package registry results, or using glab packages commands. Triggers on GitLab packages, package registry, glab packages, npm packages in GitLab, Maven packages in GitLab.
---

# glab packages

List packages in a GitLab project's package registry.

> Added in glab v1.103.0. The initial command group provides `list` / `ls` for project package registries.

## Quick start

```bash
# List all packages in the current project
glab packages list

# Alias
glab packages ls

# List packages from another project
glab packages list -R owner/repo
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

## Reference

See [references/commands.md](references/commands.md) for command synopsis and flags.
