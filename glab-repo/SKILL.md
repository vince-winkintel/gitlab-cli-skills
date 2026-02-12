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
   ```

2. **Clone locally:**
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
   git remote add upstream https://gitlab.com/upstream-group/project.git
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
- `publish` - Publish project resources
