---
name: glab-todo
description: Manage your GitLab to-do list from the CLI, including listing pending or completed items and marking items done. Use when reviewing assigned or mentioned work from GitLab notifications, clearing to-dos, or scripting to-do triage. Triggers on todo, to-do, notification list, mark done, assigned items, mentioned items.
---

# glab todo

Manage your GitLab to-do list.

> **Added in glab v1.92.0**

## Quick start

```bash
# List pending to-dos
glab todo list

# Mark one to-do as done
glab todo done 123

# Mark all pending to-dos as done
glab todo done --all
```

## Common workflows

### Review pending work

```bash
glab todo list
glab todo list --action=assigned
glab todo list --type=MergeRequest
```

### Review completed items

```bash
glab todo list --state=done
glab todo list --state=all
```

### Scripted triage

```bash
glab todo list --output=json
```

### Clear to-dos

```bash
glab todo done 123
glab todo done --all
```

## Command reference

See [references/commands.md](references/commands.md) for the captured command surface.
