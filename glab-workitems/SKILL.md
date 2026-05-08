---
name: glab-workitems
description: Create, list, and delete GitLab work items (tasks, OKRs, key results, epics, incidents, test cases). Use when working with GitLab's work item types beyond standard issues. Triggers on work items, work-items, tasks, OKRs, key results, epics, work item create, work item delete.
---

# glab work-items

Create, list, and delete GitLab work items — GitLab's unified work tracking model for tasks, OKRs, key results, epics, incidents, test cases, and related planning objects.

## ⚠️ Experimental Feature

`glab work-items` is still marked **EXPERIMENTAL** upstream:
- command shape may still change
- availability can differ by GitLab version / feature flags
- some work item types are only meaningful at group scope
- use `glab issue` for stable day-to-day issue workflows

See: https://docs.gitlab.com/policy/development_stages_support/

## Quick start

```bash
# List work items in the current project
glab work-items list

# Create a task in the current project
glab work-items create --type task --title "Follow up on flaky pipeline"

# Create a group-scoped epic
glab work-items create --type epic --group my-group --title "Platform rewrite"
```

## Scope model

`glab work-items` uses repository context by default, then lets you override scope explicitly:

- **Current repo context** → project work items in the checked-out repository
- `--repo owner/project` → a different project
- `--group my-group` → group/subgroup work items

This matters because some work item types are commonly project-scoped (`task`, `issue`, `incident`) while others often live at group scope (`epic`, `objective`, `key_result`).

## Common workflows

### List work items

```bash
# First 20 open work items in current project
glab work-items list

# Filter by type
glab work-items list --type epic --group gitlab-org
glab work-items list --type issue --repo gitlab-org/cli

# Closed or all states
glab work-items list --state closed --group gitlab-org
glab work-items list --state all --group gitlab-org

# Increase page size (max 100)
glab work-items list --per-page 50 --group gitlab-org

# Cursor-based pagination
glab work-items list --after "eyJpZCI6OTk5OX0" --group gitlab-org

# JSON output for automation
glab work-items list --output json --group gitlab-org
```

### Create work items

Use `--type` to declare the work item type explicitly.

```bash
# Create a project work item
glab work-items create \
  --type task \
  --title "Audit runner costs" \
  --description "Summarize shared-runner usage before Friday"

# Create a confidential incident
glab work-items create \
  --type incident \
  --title "Investigate production latency spike" \
  --confidential

# Create a group-scoped epic
glab work-items create \
  --type epic \
  --group my-group \
  --title "Q3 platform migration"

# JSON output for scripts
glab work-items create --type issue --title "Backfill docs" --output json
```

Supported upstream type values in v1.94.0 include:
`epic`, `incident`, `issue`, `key_result`, `objective`, `requirement`, `task`, `test_case`, and `ticket`.

### Delete work items

```bash
# Delete by IID in the current project
glab work-items delete 42

# Delete a group work item
glab work-items delete 42 --group my-group

# Delete from another project and return JSON
glab work-items delete 42 --repo mygroup/myproject --output json
```

`delete` is destructive. Double-check whether the IID belongs to the intended project or group before running it.

## Work items vs issues

| Need | Prefer |
|---|---|
| Standard bug / feature issue workflow | `glab issue` |
| Tasks, OKRs, objectives, key results, next-gen epics | `glab work-items` |
| Stable/non-experimental issue automation | `glab issue` |
| Group-scoped planning objects | `glab work-items --group ...` |

Use `glab work-items` when the work type itself matters. Use `glab issue` when you just need standard issue lifecycle commands with the most mature CLI surface.

## Troubleshooting

**`work-items: command not found` or docs show `workitems`:**
- The current upstream command family is `glab work-items` with a hyphen.
- Older `glab workitems` examples are stale.
- Check your version with `glab version`; `work-items` coverage here assumes glab v1.94.0 guidance.

**Create/delete seems unavailable on your machine:**
- Older glab versions only exposed `list`.
- Upgrade glab if you're still on a pre-v1.94 build.

**Type filter returns nothing:**
- Not every GitLab instance exposes every work item type.
- Try the correct scope (`--group` vs `--repo`) for the type you're querying.

**Delete removed the wrong thing:**
- `delete` works by IID within the selected project/group scope.
- Re-run with explicit `--repo` or `--group` so the scope is unambiguous.

## Related Skills

- `glab-issue` — Standard issue workflows
- `glab-milestone` — Milestones often paired with OKRs and planning
- `glab-iteration` — Sprint / iteration planning
- `glab-incident` — Incident-specific workflows

## Command reference

```text
glab work-items <command> [flags]

glab work-items list [flags]
  --after        Cursor for pagination
  --group        Group/subgroup scope
  --output       text|json
  --per-page     Up to 100 items
  --repo         Project scope override
  --state        opened|closed|all
  --type         One or more work item types

glab work-items create [flags]
  --confidential Mark the work item confidential
  --description  Body text (use - to open editor)
  --group        Group/subgroup scope
  --output       text|json
  --repo         Project scope override
  --title        Title for the new work item
  --type         epic|incident|issue|key_result|objective|requirement|task|test_case|ticket

glab work-items delete <iid> [flags]
  --group        Group/subgroup scope
  --output       text|json
  --repo         Project scope override
```
