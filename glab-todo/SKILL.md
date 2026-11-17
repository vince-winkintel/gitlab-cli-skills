---
name: glab-todo
description: Manage your GitLab to-do list from the CLI, including listing pending or completed items and marking items done. Use when reviewing assigned or mentioned work from GitLab notifications, clearing to-dos, or scripting to-do triage. Triggers on todo, to-do, notification list, mark done, assigned items, mentioned items.
---

# glab todo

Current captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

Manage your GitLab to-do list.

## Group-scoped items

For a group-scoped to-do without a project, the text table's `Project` column shows the group's full path. Project-scoped items keep their project path; an item with neither has an empty cell. Consumers of JSON must allow an absent/null project and use the group object when present. This display change does not mark items done or expand authorization for completion.

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

See [current captured help](references/help-206ebab4f.md) for the captured command surface.
