---
name: gitlab-cli-skills
description: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations via terminal. Use when user mentions GitLab CLI, glab commands, GitLab automation, MR/issue management via CLI, CI/CD pipeline commands, repo operations, authentication setup, or any GitLab terminal operations. Routes to specialized sub-skills for auth, CI, MRs, issues, releases, repos, and 30+ other glab commands. Triggers on glab, GitLab CLI, GitLab commands, GitLab terminal, GitLab automation.
metadata: {"openclaw": {"requires": {"bins": ["glab"], "anyBins": ["cosign"]}, "install": [{"id": "brew", "kind": "brew", "formula": "glab", "bins": ["glab"], "label": "Install glab (brew)"}, {"id": "download", "kind": "download", "url": "https://gitlab.com/gitlab-org/cli/-/releases", "label": "Download glab binary"}]}}
requirements:
  binaries:
    - glab
  binaries_optional:
    - cosign
  notes: |
    Requires GitLab authentication via 'glab auth login' (stores token in ~/.config/glab-cli/config.yml).
    Some features may access sensitive files: SSH keys (~/.ssh/id_rsa for DPoP), Docker config (~/.docker/config.json for registry auth).
    Review auth workflows and script contents before autonomous use.
openclaw:
  requires:
    credentials:
      - name: GITLAB_TOKEN
        description: >
          GitLab personal access token with 'api' scope. Used by automation
          scripts (e.g. post-inline-comment.py) to post MR comments via the
          REST API. If not set, scripts fall back to reading the token from
          glab CLI config (~/.config/glab-cli/config.yml).
        required: false
        fallback: glab config (set via glab auth login)
    network:
      - description: Outbound HTTPS to your GitLab instance (default https://gitlab.com)
        scope: authenticated API calls only; HTTPS enforced; token never sent over HTTP
    write_access:
      - description: >
          Scripts in this skill can post comments, resolve threads, and approve
          merge requests on your behalf. Review scripts/post-inline-comment.py
          before use in automated or agentic contexts.
---

# GitLab CLI Skills

Comprehensive GitLab CLI (glab) command reference and workflows.

## Quick start

```bash
# First time setup
glab auth login

# Common operations
glab mr create --fill              # Create MR from current branch
glab issue create                  # Create issue
glab ci view                       # View pipeline status
glab repo view --web              # Open repo in browser
```

## Multi-agent identity note

When you want different agents to appear as different GitLab users, give each agent its own GitLab bot/service account. Multiple personal access tokens on the same GitLab user still act as that same visible identity.

A practical pattern is one env file per agent, for example `~/.config/openclaw/env/gitlab-reviewer.env` and `~/.config/openclaw/env/gitlab-release.env`. If those files use plain `KEY=value` lines, load them with exported vars before running `glab`:

```bash
set -a
source ~/.config/openclaw/env/gitlab-<agent>.env
set +a
```

Plain `source` updates the current shell but may not export variables to child processes such as `glab`. If the token/host vars are not exported, `glab` may silently fall back to shared stored auth from `~/.config/glab-cli/config.yml`, which can make the wrong account appear to perform the action.

## Skill organization

This skill routes to specialized sub-skills by GitLab domain:

**Core Workflows:**
- `glab-mr` - Merge requests: create, review, approve, merge
- `glab-issue` - Issues: create, list, update, close, comment
- `glab-ci` - CI/CD: pipelines, jobs, logs, artifacts
- `glab-repo` - Repositories: clone, create, fork, manage

**Project Management:**
- `glab-milestone` - Release planning and milestone tracking
- `glab-iteration` - Sprint/iteration management
- `glab-label` - Label management and organization
- `glab-release` - Software releases and versioning

**Authentication & Config:**
- `glab-auth` - Login, logout, Docker registry auth
- `glab-config` - CLI configuration and defaults
- `glab-ssh-key` - SSH key management
- `glab-gpg-key` - GPG keys for commit signing
- `glab-token` - Personal and project access tokens

**CI/CD Management:**
- `glab-job` - Individual job operations
- `glab-schedule` - Scheduled pipelines and cron jobs
- `glab-variable` - CI/CD variables and secrets
- `glab-securefile` - Secure files for pipelines
- `glab-runner` - Runner management: list, assign/unassign, inspect jobs/managers, pause/unpause, delete (added v1.87.0; expanded in v1.90.0)
- `glab-runner-controller` - Runner controller, scope, and token management (EXPERIMENTAL, admin-only)

**Collaboration:**
- `glab-user` - User profiles and information
- `glab-snippet` - Code snippets (GitLab gists)
- `glab-incident` - Incident management
- `glab-workitems` - Work items: tasks, OKRs, key results, next-gen epics (added v1.87.0)

**Advanced:**
- `glab-api` - Direct REST API calls
- `glab-cluster` - Kubernetes cluster integration
- `glab-deploy-key` - Deploy keys for automation
- `glab-quick-actions` - GitLab slash command quick actions for batching state changes
- `glab-stack` - Stacked/dependent merge requests
- `glab-opentofu` - Terraform/OpenTofu state management

**Utilities:**
- `glab-alias` - Custom command aliases
- `glab-completion` - Shell autocompletion
- `glab-help` - Command help and documentation
- `glab-version` - Version information
- `glab-check-update` - Update checker
- `glab-changelog` - Changelog generation
- `glab-attestation` - Software supply chain security
- `glab-duo` - GitLab Duo AI assistant
- `glab-mcp` - Model Context Protocol server for AI assistant integration (EXPERIMENTAL)

## v1.90.0 Updates

Key user-facing changes in `glab` v1.90.0 that affect this skill set:

- **`glab-auth`**: `glab auth login` adds `--web`, `--container-registry-domains`, and `--ssh-hostname`; CI auto-login is now GA.
- **`glab-mr`**: `glab mr create` adds `--auto-merge`; `glab mr note` now has `list`, `resolve`, and `reopen` subcommands in addition to note-posting flags.
- **`glab-runner`**: adds `jobs`, `managers`, and `update --pause|--unpause`.
- **`glab-runner-controller`**: adds `get` and shifts runner scope management under `scope list|create|delete`.

## v1.89.0 Updates

> **v1.89.0+:** 18 commands across 12 sub-skills now support `--output json` / `-F json` for structured output — raw GitLab API responses ideal for agent/automation parsing. Affected sub-skills: `glab-release`, `glab-ci`, `glab-milestone`, `glab-schedule`, `glab-mr`, `glab-repo`, `glab-label`, `glab-deploy-key`, `glab-ssh-key`, `glab-gpg-key`, `glab-cluster`, `glab-opentofu`.

Other v1.89.0 changes:
- **`glab-auth`**: `glab auth login` now prompts for SSH hostname separately from API hostname on self-hosted instances
- **`glab-stack`**: `glab stack sync --update-base` flag added to rebase stack onto updated base branch
- **`glab-release`**: `--notes` / `--notes-file` are now optional for `glab release create` and `glab release update`

## When to use glab vs web UI

**Use glab when:**
- Automating GitLab operations in scripts
- Working in terminal-centric workflows
- Batch operations (multiple MRs/issues)
- Integration with other CLI tools
- CI/CD pipeline workflows
- Faster navigation without browser context switching

**Use web UI when:**
- Complex diff review with inline comments
- Visual merge conflict resolution
- Configuring repo settings and permissions
- Advanced search/filtering across projects
- Reviewing security scanning results
- Managing group/instance-level settings

## Common workflows

### Daily development

```bash
# Start work on issue
glab issue view 123
git checkout -b 123-feature-name

# Create MR when ready
glab mr create --fill --draft

# Mark ready for review
glab mr update --ready

# Merge after approval
glab mr merge --when-pipeline-succeeds --remove-source-branch
```

### Code review

```bash
# List your review queue
glab mr list --reviewer=@me --state=opened

# Review an MR
glab mr checkout 456
glab mr diff
npm test

# Approve
glab mr approve 456
glab mr note 456 -m "LGTM! Nice work on the error handling."
```

### CI/CD debugging

```bash
# Check pipeline status
glab ci status

# View failed jobs
glab ci view

# Get job logs
glab ci trace <job-id>

# Retry failed job
glab ci retry <job-id>
```

## Decision Trees

### "Should I create an MR or work on an issue first?"

```
Need to track work?
├─ Yes → Create issue first (glab issue create)
│         Then: glab mr for <issue-id>
└─ No → Direct MR (glab mr create --fill)
```

**Use `glab issue create` + `glab mr for` when:**
- Work needs discussion/approval before coding
- Tracking feature requests or bugs
- Sprint planning and assignment
- Want issue to auto-close when MR merges

**Use `glab mr create` directly when:**
- Quick fixes or typos
- Working from existing issue
- Hotfixes or urgent changes

### "Which CI command should I use?"

```
What do you need?
├─ Overall pipeline status → glab ci status
├─ Visual pipeline view → glab ci view
├─ Specific job logs → glab ci trace <job-id>
├─ Download build artifacts → glab ci artifact <ref> <job-name>
├─ Validate config file → glab ci lint
├─ Trigger new run → glab ci run
└─ List all pipelines → glab ci list
```

**Quick reference:**
- Pipeline-level: `glab ci status`, `glab ci view`, `glab ci run`
- Job-level: `glab ci trace`, `glab job retry`, `glab job view`
- Artifacts: `glab ci artifact` (by pipeline) or job artifacts via `glab job`

### "Clone or fork?"

```
What's your relationship to the repo?
├─ You have write access → glab repo clone group/project
├─ Contributing to someone else's project:
│   ├─ One-time contribution → glab repo fork + work + MR
│   └─ Ongoing contributions → glab repo fork, then sync regularly
└─ Just reading/exploring → glab repo clone (or view --web)
```

**Fork when:**
- You don't have write access to the original repo
- Contributing to open source projects
- Experimenting without affecting the original
- Need your own copy for long-term work

**Clone when:**
- You're a project member with write access
- Working on organization/team repositories
- No need for a personal copy

### "Project vs group labels?"

```
Where should the label live?
├─ Used across multiple projects → glab label create --group <group>
└─ Specific to one project → glab label create (in project directory)
```

**Group-level labels:**
- Consistent labeling across organization
- Examples: priority::high, type::bug, status::blocked
- Managed centrally, inherited by projects

**Project-level labels:**
- Project-specific workflows
- Examples: needs-ux-review, deploy-to-staging
- Managed by project maintainers

## Related Skills

**MR and Issue workflows:**
- Start with `glab-issue` to create/track work
- Use `glab-mr` to create MR that closes issue
- Script: `scripts/create-mr-from-issue.sh` automates this

**CI/CD debugging:**
- Use `glab-ci` for pipeline-level operations
- Use `glab-job` for individual job operations
- Script: `scripts/ci-debug.sh` for quick failure diagnosis

**Repository operations:**
- Use `glab-repo` for repository management
- Use `glab-auth` for authentication setup
- Script: `scripts/sync-fork.sh` for fork synchronization

**Configuration:**
- Use `glab-auth` for initial authentication
- Use `glab-config` to set defaults and preferences
- Use `glab-alias` for custom shortcuts

