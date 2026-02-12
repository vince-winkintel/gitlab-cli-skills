---
name: glab-label
description: Manage GitLab labels including create, list, update, and delete operations at project and group level. Use when organizing issues/MRs with labels, creating label taxonomies, or managing label colors/descriptions. Triggers on label, tag, issue label, create label, manage labels.
---

# glab label

Manage labels at project and group level.

## Quick start

```bash
# Create project label
glab label create --name bug --color "#FF0000"

# Create group label
glab label create --group my-group --name priority::high --color "#FF6B00"

# List labels
glab label list

# Update label
glab label edit bug --color "#CC0000" --description "Software defects"

# Delete label
glab label delete bug
```

## Decision: Project vs Group Labels?

```
Where should this label live?
├─ Used across multiple projects in a group
│  └─ Group-level: glab label create --group <group> --name <label>
└─ Specific to one project
   └─ Project-level: glab label create --name <label>
```

**Use group-level labels when:**
- You want consistent labeling across all projects in a group
- Managing organization-wide workflows
- Examples: `priority::high`, `type::bug`, `status::blocked`
- Reduces duplication and ensures consistency

**Use project-level labels when:**
- Label is specific to project workflow
- Team wants control over their own labels
- Examples: `needs-ux-review`, `deploy-to-staging`, `legacy-code`

## Common workflows

### Creating a label taxonomy

**Set up priority labels (group-level):**
```bash
glab label create --group engineering --name "priority::critical" --color "#FF0000"
glab label create --group engineering --name "priority::high" --color "#FF6B00"
glab label create --group engineering --name "priority::medium" --color "#FFA500"
glab label create --group engineering --name "priority::low" --color "#FFFF00"
```

**Set up type labels (group-level):**
```bash
glab label create --group engineering --name "type::bug" --color "#FF0000"
glab label create --group engineering --name "type::feature" --color "#00FF00"
glab label create --group engineering --name "type::maintenance" --color "#0000FF"
```

### Managing project-specific labels

**Create workflow labels:**
```bash
glab label create --name "needs-review" --color "#428BCA"
glab label create --name "ready-to-merge" --color "#5CB85C"
glab label create --name "blocked" --color "#D9534F"
```

### Bulk operations

**List all labels to review:**
```bash
glab label list --per-page 100 > labels.txt
```

**Delete deprecated labels:**
```bash
glab label delete old-label-1
glab label delete old-label-2
```

## Related Skills

**Using labels:**
- See `glab-issue` for applying labels to issues
- See `glab-mr` for applying labels to merge requests
- Script: `scripts/batch-label-issues.sh` for bulk labeling

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `create` - Create label (project or group)
- `list` - List labels
- `edit` - Update label properties
- `delete` - Delete label
- `get` - View single label details
