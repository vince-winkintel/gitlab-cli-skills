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
