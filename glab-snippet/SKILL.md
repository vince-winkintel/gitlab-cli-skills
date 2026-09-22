---
name: glab-snippet
description: Create GitLab project or personal code snippets with glab. Use when sharing code or text as a new snippet from files or stdin. For viewing, editing, or deleting existing snippets, use the GitLab UI or the snippets API through glab api. Triggers on snippet, gist, code snippet, share code, create snippet.
---

# glab snippet

`glab snippet` creates snippets. It does not provide native view, update, list, or delete subcommands; use the GitLab UI or `glab api` with the project or personal snippets API for those operations.

## Create from files

```bash
# Project snippet in the repository selected by the current checkout
glab snippet create --title "Example" script.py

# Multiple files
glab snippet create --title "Example" app.py requirements.txt

# Personal snippet
glab snippet create --personal --title "Example" script.py
```

Verify the current repository or pass `--repo` before creating a project snippet. Review every input file for secrets because the command uploads its contents.

## Create from stdin

```bash
printf '%s\n' 'package main' | \
  glab snippet create --title "Go example" --filename main.go
```

Use `--filename` when stdin supplies the content. Choose `--visibility public`, `internal`, or `private` deliberately; the default is private.

## Existing snippets

For project snippets, use the [Project snippets API](https://docs.gitlab.com/api/project_snippets/) through `glab api`. For personal snippets, use the [Snippets API](https://docs.gitlab.com/api/snippets/). Read the target first and verify the host, project, snippet ID, and actor before any update or delete request.

## Command reference

See [references/commands.md](references/commands.md) for checksum-verified `glab snippet` and `glab snippet create` help.
