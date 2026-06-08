---
name: glab-repo
description: Work with GitLab repositories and projects including clone, create, fork, archive, view, update, delete, search, transfer, and member management. Use when managing repo lifecycle, forking projects, cloning repositories, searching for projects, managing collaborators, or configuring repo settings. Triggers on repository, repo, project, clone, fork, create repo, search projects, collaborators.
---

# glab repo

Work with GitLab repositories and projects.

## Quick start

```bash
# Clone a repository
glab repo clone group/project

# Create new repository
glab repo create my-new-project --public

# Fork a repository
glab repo fork upstream/project

# View repository details
glab repo view

# Add a Git remote from a GitLab project reference
glab repo remote add group/project --name upstream

# Prune local branches whose MRs have been merged
glab repo prune --dry-run
glab repo prune --yes

# Search for repositories
glab repo search "keyword"
```

## Common workflows

### Starting new project

1. **Create repository:**
   ```bash
   glab repo create my-project \
     --public \
     --description "My awesome project"

   # Create with README
   glab repo create my-project \
     --public \
     --readme
   ```

   **Note:** `glab repo create --readme` clones the newly created repository instead of using `git init`, ensuring a clean local copy with the initial README.

2. **Clone locally (if not using --readme):**
   ```bash
   glab repo clone my-username/my-project
   cd my-project
   ```

3. **Initialize with content:**
   ```bash
   echo "# My Project" > README.md
   git add README.md
   git commit -m "Initial commit"
   git push -u origin main
   ```

### Forking workflow

1. **Fork upstream repository:**
   ```bash
   glab repo fork upstream-group/project
   ```

2. **Clone your fork:**
   ```bash
   glab repo clone my-username/project
   cd project
   ```

3. **Add upstream remote:**
   ```bash
   glab repo remote add upstream-group/project --name upstream
   ```

   `glab repo remote add <namespace/project>` resolves a GitLab project reference and adds the appropriate Git remote URL. The default remote name is the first path component (`upstream-group` in the example); override it with `--name` / `-n`. Use `--protocol ssh|https` / `-p` to override the `git_protocol` config.

   ```bash
   glab repo remote add alice/my-project
   glab repo remote add alice/my-project --name upstream
   glab repo remote add group/subgroup/my-project --protocol ssh
   ```

4. **Keep fork in sync:**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

**Automated sync:**

Use the sync script for one-command fork updates:
```bash
scripts/sync-fork.sh main
scripts/sync-fork.sh develop upstream
```

This automatically: fetches → merges → pushes to origin.

### Repository management

**View repository info:**
```bash
glab repo view
glab repo view group/project  # Specific repo
glab repo view --web          # Open in browser
```

**Update repository settings:**
```bash
glab repo update \
  --description "Updated description" \
  --default-branch develop
```

**Archive repository:**
```bash
glab repo archive download main  # Downloads .tar.gz
glab repo archive download main --format zip
```

**Transfer to new namespace:**
```bash
glab repo transfer my-project --target-namespace new-group
```

**Delete repository:**
```bash
glab repo delete group/project
```

### Local branch pruning

`glab repo prune` deletes **local** Git branches whose GitLab merge requests have been merged. It never deletes remote branches on GitLab, and it skips protected branches, the default branch, and the branch currently checked out.

```bash
# Preview branches that would be deleted
glab repo prune --dry-run

# Delete branches after confirmation
glab repo prune

# Delete without confirmation after reviewing the dry run
glab repo prune --yes

# Exclude additional branches by exact name or glob; comma-separate or repeat
glab repo prune --exclude wip-*,demo-branch

# Faster local-Git detection; misses squash/rebase merges that are not fast-forward ancestry
glab repo prune --merged
```

Prefer the default GitLab-backed mode for correctness: it queries merge requests for each local branch and handles squash/rebase merge cases better than plain `git branch --merged`. Use `--merged` only when the faster fast-forward-only check is acceptable.

### Member management

**List collaborators:**
```bash
glab repo members list
```

**Add member:**
```bash
glab repo members add @username --access-level maintainer
```

**Remove member:**
```bash
glab repo members remove @username
```

**Update member access:**
```bash
glab repo members update @username --access-level developer
```

### Bulk operations

**Clone all repos in a group:**
```bash
glab repo clone -g my-group
```

**Search and clone:**
```bash
glab repo search "api" --per-page 10
# Then clone specific result
glab repo clone group/api-project
```

**List your repositories:**
```bash
glab repo list
glab repo list --member          # Only where you're a member
glab repo list --mine            # Only repos you own
```

## Troubleshooting

**Clone fails with permission error:**
- Verify you have access: `glab repo view group/project`
- Check authentication: `glab auth status`
- For private repos, ensure you're logged in with correct account

**Fork operation fails:**
- Check if fork already exists in your namespace
- Verify you have permission to fork (some repos disable forking)
- Try with explicit namespace: `glab repo fork --fork-path username/new-name`

**Transfer fails:**
- Verify you have owner/maintainer access
- Check target namespace exists and you have create permissions
- Some projects may have transfer protections enabled

**Group clone fails:**
- Verify group exists and you have access
- Check you have enough disk space
- Large groups may time out - clone specific repos instead

## Related Skills

**Authentication and access:**
- See `glab-auth` for login and authentication setup
- See `glab-ssh-key` for SSH key management
- See `glab-deploy-key` for deployment authentication

**Project configuration:**
- See `glab-config` for CLI defaults and settings
- See `glab-variable` for CI/CD variables

**Fork synchronization:**
- Script: `scripts/sync-fork.sh` automates upstream sync

## Structured output

`glab repo contributors` supports `--output json` / `-F json` for structured output, which is useful for agent automation.

```bash
# List contributors with JSON output
glab repo contributors --output json
glab repo contributors -F json
```

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `clone` - Clone repository or group
- `create` - Create new project
- `fork` - Fork repository
- `view` - View project details
- `update` - Update project settings
- `delete` - Delete project
- `search` - Search for projects
- `list` - List repositories
- `transfer` - Transfer to new namespace
- `archive` - Download repository archive
- `contributors` - List contributors
- `members` - Manage project members
- `mirror` - Configure repository mirroring
- `remote` - Manage Git remotes using GitLab project references
- `prune` - Delete local branches whose GitLab merge requests are merged
- `publish` - Publish project resources
