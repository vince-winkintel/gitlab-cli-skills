---
name: gitlab-cli-skills
description: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations via terminal. Use when user mentions GitLab CLI, glab commands, GitLab automation, MR/issue management via CLI, CI/CD pipeline commands, repo operations, authentication setup, or any GitLab terminal operations. Routes to specialized sub-skills for auth, CI, MRs, issues, releases, repos, and 30+ other glab commands. Triggers on glab, GitLab CLI, GitLab commands, GitLab terminal, GitLab automation.
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

**Collaboration:**
- `glab-user` - User profiles and information
- `glab-snippet` - Code snippets (GitLab gists)
- `glab-incident` - Incident management

**Advanced:**
- `glab-api` - Direct REST API calls
- `glab-cluster` - Kubernetes cluster integration
- `glab-deploy-key` - Deploy keys for automation
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
- `glab-mcp` - Managed Cluster Platform

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
