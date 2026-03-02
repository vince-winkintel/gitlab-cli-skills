---
name: glab-workitems
description: List and manage GitLab work items (tasks, OKRs, key results, epics). Use when working with GitLab's work item types beyond standard issues. Triggers on work items, tasks, OKRs, key results, epic list, workitems list.
---

# glab workitems

List and manage GitLab work items — the next-generation work tracking format in GitLab that supports tasks, OKRs, key results, epics, and more.

> **Added in glab v1.87.0**

## What Are Work Items?

Work items are GitLab's unified work tracking model. They extend beyond traditional issues to support:
- **Tasks** — sub-tasks within an issue
- **OKRs** — Objectives and Key Results
- **Key Results** — measurable outcomes linked to OKRs
- **Epics** (next-gen) — large bodies of work across milestones
- **Incidents** — linked to incident management

## Quick Start

```bash
# List work items in current project
glab workitems list

# List in a specific project
glab workitems list --repo owner/project

# Output as JSON
glab workitems list --output json
```

## Common Workflows

### List Work Items

```bash
# All work items (default: open)
glab workitems list

# Filter by type
glab workitems list --type Task
glab workitems list --type OKR
glab workitems list --type KeyResult
glab workitems list --type Epic

# Filter by state
glab workitems list --state opened
glab workitems list --state closed

# JSON for scripting
glab workitems list --output json | python3 -c "
import sys, json
items = json.load(sys.stdin)
for item in items:
    print(f\"{item['iid']}: {item['title']} [{item['type']}]\")
"
```

### Use with a Specific Repo or Group

```bash
# Specific repo
glab workitems list --repo mygroup/myproject

# Group-level work items
glab workitems list --group mygroup
```

## Work Items vs Issues

| Feature | Issues | Work Items |
|---|---|---|
| Standard bug/feature tracking | ✅ | ✅ |
| Tasks (sub-tasks) | ❌ | ✅ |
| OKRs / Key Results | ❌ | ✅ |
| Next-gen Epics | ❌ | ✅ |
| CLI support | Full | `list` (v1.87.0) |

Use `glab issue` for standard issue workflows. Use `glab workitems` when working with tasks, OKRs, or next-gen epics.

## Troubleshooting

**"workitems: command not found":**
- Requires glab v1.87.0+. Check with `glab version`.

**Empty results when you expect items:**
- Work items are a separate type from issues. Items created as issues won't appear here unless they've been converted.
- Check the GitLab UI under the project's "Plan > Work Items" sidebar.

**Type filter returns nothing:**
- Not all work item types are enabled on every GitLab instance. GitLab SaaS has broader support than self-managed instances.

## Related Skills

- `glab-issue` — Standard issue management
- `glab-milestone` — Milestones (often used with OKRs)
- `glab-iteration` — Sprint/iteration management
- `glab-incident` — Incident management (a work item type)

## Command Reference

```
glab workitems list [--flags]

Flags:
  --group        Select a group/subgroup
  --output       Format output as: text, json
  --page         Page number
  --per-page     Number of items per page
  --repo         Select a repository
  --state        Filter by state: opened, closed, all
  --type         Filter by work item type
  -h, --help     Show help
```
