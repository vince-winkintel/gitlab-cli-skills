---
name: glab-issue
description: Create, view, update, and manage GitLab issues. Use when working with issue tracking, bug reports, feature requests, or task management. Operations include creating issues, listing with filters, viewing details, adding comments/notes, updating labels/assignees/milestones, closing/reopening, and board management. Triggers on issue, bug, task, ticket, feature request, list issues, create issue.
---

# glab issue

Create, view, update, and manage GitLab issues.

## Quick start

```bash
# Create an issue
glab issue create --title "Fix login bug" --label bug

# List open issues
glab issue list --state opened

# View issue details
glab issue view 123

# Add comment
glab issue note 123 -m "Working on this now"

# Close issue
glab issue close 123
```

## Common workflows

### Bug reporting workflow

1. **Create bug issue:**
   ```bash
   glab issue create \
     --title "Login fails with 500 error" \
     --label bug \
     --label priority::high \
     --assignee @dev-lead
   ```

2. **Add reproduction steps:**
   ```bash
   glab issue note 456 -m "Steps to reproduce:
   1. Navigate to /login
   2. Enter valid credentials
   3. Click submit
   Expected: Dashboard loads
   Actual: 500 error"
   ```

### Issue triage

1. **List untriaged issues:**
   ```bash
   glab issue list --label needs-triage --state opened
   ```

2. **Update labels and assignee:**
   ```bash
   glab issue update 789 \
     --label backend,priority::medium \
     --assignee @backend-team \
     --milestone "Sprint 23"
   ```

3. **Remove triage label:**
   ```bash
   glab issue update 789 --unlabel needs-triage
   ```

**Batch labeling:**

For applying labels to multiple issues at once:
```bash
scripts/batch-label-issues.sh "priority::high" 100 101 102
scripts/batch-label-issues.sh bug 200 201 202 203
```

### Sprint planning

**View current sprint issues:**
```bash
glab issue list --milestone "Sprint 23" --assignee @me
```

**Add to sprint:**
```bash
glab issue update 456 --milestone "Sprint 23"
```

**Board view:**
```bash
glab issue board view
```

### Linking issues to work

**Create MR for issue:**
```bash
glab mr for 456  # Creates MR that closes issue #456
```

**Automated workflow (create branch + draft MR):**
```bash
scripts/create-mr-from-issue.sh 456 --create-mr
```

This automatically: creates branch from issue title → empty commit → pushes → creates draft MR.

**Close via commit/MR:**
```bash
git commit -m "Fix login bug

Closes #456"
```

## Related Skills

**Creating MRs from issues:**
- See `glab-mr` for merge request operations
- Use `glab mr for <issue-id>` to create MR that closes issue
- Script: `scripts/create-mr-from-issue.sh` automates branch creation + draft MR

**Label management:**
- See `glab-label` for creating and managing labels
- Script: `scripts/batch-label-issues.sh` for bulk labeling operations

**Project planning:**
- See `glab-milestone` for release planning
- See `glab-iteration` for sprint/iteration management

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `create` - Create new issue
- `list` - List issues with filters
- `view` - Display issue details
- `note` - Add comment to issue
- `update` - Update title, labels, assignees, milestone
- `close` - Close issue
- `reopen` - Reopen closed issue
- `delete` - Delete issue
- `subscribe` / `unsubscribe` - Manage notifications
- `board` - Work with issue boards
