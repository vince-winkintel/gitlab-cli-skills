---
name: glab-mr
description: Create, view, manage, approve, and merge GitLab merge requests. Use when working with MRs: creating from branches/issues, reviewing, approving, adding comments, checking out locally, viewing diffs, rebasing, merging, or managing state. Triggers on merge request, MR, pull request, PR, review, approve, merge.
---

# glab mr

Create, view, and manage GitLab merge requests.

## Quick start

```bash
# Create MR from current branch
glab mr create --fill

# List my MRs
glab mr list --assignee=@me

# Review an MR
glab mr checkout 123
glab mr diff
glab mr approve

# Merge an MR
glab mr merge 123 --when-pipeline-succeeds --remove-source-branch
```

## Common workflows

### Creating MRs

**From current branch:**
```bash
glab mr create --fill --label bugfix --assignee @reviewer
```

**From issue:**
```bash
glab mr for 456  # Creates MR linked to issue #456
```

**Draft MR:**
```bash
glab mr create --draft --title "WIP: Feature X"
```

### Review workflow

1. **List pending reviews:**
   ```bash
   glab mr list --reviewer=@me --state=opened
   ```

2. **Checkout and test:**
   ```bash
   glab mr checkout 123
   npm test
   ```

3. **Leave feedback:**
   ```bash
   glab mr note 123 -m "Looks good, one question about the cache logic"
   ```

4. **Approve:**
   ```bash
   glab mr approve 123
   ```

**Automated review workflow:**

For repetitive review tasks, use the automation script:
```bash
scripts/mr-review-workflow.sh 123
scripts/mr-review-workflow.sh 123 "pnpm test"
```

This automatically: checks out → runs tests → posts result → approves if passed.

### Merge strategies

**Auto-merge when pipeline passes:**
```bash
glab mr merge 123 --when-pipeline-succeeds --remove-source-branch
```

**Squash commits:**
```bash
glab mr merge 123 --squash
```

**Rebase before merge:**
```bash
glab mr rebase 123
glab mr merge 123
```

## Troubleshooting

**Merge conflicts:**
- Checkout MR: `glab mr checkout 123`
- Resolve conflicts manually in your editor
- Commit resolution: `git add . && git commit`
- Push: `git push`

**Cannot approve MR:**
- Check if you're the author (can't self-approve in most configs)
- Verify permissions: `glab mr approvers 123`
- Ensure MR is not in draft state

**Pipeline required but not running:**
- Check `.gitlab-ci.yml` exists in branch
- Verify CI/CD is enabled for project
- Trigger manually: `glab ci run`

**"MR already exists" error:**
- List existing MRs from branch: `glab mr list --source-branch <branch>`
- Close old MR if obsolete: `glab mr close <id>`
- Or update existing: `glab mr update <id> --title "New title"`

## Related Skills

**Working with issues:**
- See `glab-issue` for creating/managing issues
- Use `glab mr for <issue-id>` to create MR linked to issue
- Script: `scripts/create-mr-from-issue.sh` automates branch + MR creation

**CI/CD integration:**
- See `glab-ci` for pipeline status before merging
- Use `glab mr merge --when-pipeline-succeeds` for auto-merge

**Automation:**
- Script: `scripts/mr-review-workflow.sh` for automated review + test workflow

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `approve` - Approve merge requests
- `checkout` - Check out an MR locally
- `close` - Close merge request
- `create` - Create new MR
- `delete` - Delete merge request
- `diff` - View changes in MR
- `for` - Create MR for an issue
- `list` - List merge requests
- `merge` - Merge/accept MR
- `note` - Add comment to MR
- `rebase` - Rebase source branch
- `reopen` - Reopen merge request
- `revoke` - Revoke approval
- `subscribe` / `unsubscribe` - Manage notifications
- `todo` - Add to-do item
- `update` - Update MR metadata
- `view` - Display MR details
