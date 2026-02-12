---
name: glab-runner-controller
description: Manage GitLab runner controllers and authentication tokens. Create, update, delete controllers; generate, rotate, and revoke tokens. Admin-only experimental feature for managing runner controller lifecycle. Triggers on runner controller, controller token, experimental runner, admin runner.
---

# glab-runner-controller

Manage GitLab runner controllers and their authentication tokens.

## ⚠️ Experimental Feature

**Status:** EXPERIMENTAL (Admin-only)
- This feature may be broken or removed without prior notice
- Use at your own risk
- Requires GitLab admin privileges
- See: https://docs.gitlab.com/policy/development_stages_support/

## What It Does

Runner controllers manage the orchestration of GitLab Runners in your infrastructure. This skill provides commands to:
- Create and configure runner controllers
- Manage controller lifecycle (list, update, delete)
- Generate and rotate authentication tokens
- Revoke compromised tokens

## Common Workflows

### Create Runner Controller

```bash
# Create with default settings
glab runner-controller create

# Create with description
glab runner-controller create --description "Production runners"

# Create enabled controller
glab runner-controller create --description "Prod" --state enabled
```

**States:**
- `disabled` - Controller exists but inactive
- `enabled` - Controller is active (default)
- `dry_run` - Test mode (no actual runner execution)

### List and View Controllers

```bash
# List all controllers
glab runner-controller list

# List with pagination
glab runner-controller list --page 2 --per-page 50

# Output as JSON
glab runner-controller list --output json
```

### Update Controller

```bash
# Update description
glab runner-controller update 42 --description "Updated name"

# Change state
glab runner-controller update 42 --state disabled

# Update both
glab runner-controller update 42 --description "Prod" --state enabled
```

### Delete Controller

```bash
# Delete with confirmation prompt
glab runner-controller delete 42

# Delete without confirmation
glab runner-controller delete 42 --force
```

## Token Management Workflows

### Token Lifecycle

**Create → Rotate → Revoke** is the typical token lifecycle for security best practices.

#### 1. Create Token

```bash
# Create token for controller 42
glab runner-controller token create 42

# Create with description
glab runner-controller token create 42 --description "production"

# Output as JSON (for automation)
glab runner-controller token create 42 --output json
```

**Important:** Save the token value immediately - it's only shown once at creation.

#### 2. List Tokens

```bash
# List all tokens for controller 42
glab runner-controller token list 42

# List as JSON
glab runner-controller token list 42 --output json

# Paginate
glab runner-controller token list 42 --page 1 --per-page 20
```

#### 3. Rotate Token

Rotation generates a new token and invalidates the old one.

```bash
# Rotate token 1 (with confirmation)
glab runner-controller token rotate 42 1

# Rotate without confirmation
glab runner-controller token rotate 42 1 --force

# Rotate and output as JSON
glab runner-controller token rotate 42 1 --force --output json
```

**Use cases:**
- Scheduled rotation (security policy compliance)
- Token compromise response
- Key rotation before employee departure

#### 4. Revoke Token

```bash
# Revoke token 1 (with confirmation)
glab runner-controller token revoke 42 1

# Revoke without confirmation
glab runner-controller token revoke 42 1 --force
```

**When to revoke:**
- Token compromised or leaked
- Controller decommissioned
- Access no longer needed

### Token Security Best Practices

1. **Rotate regularly** - Set up scheduled rotation (e.g., every 90 days)
2. **Use descriptions** - Track token purpose and owner
3. **Revoke immediately** when compromised
4. **Never commit tokens** to version control
5. **Use `--output json`** for automation (parse token value securely)

## Decision Tree: Controller State Selection

```
Do you need the controller active?
├─ Yes → --state enabled
├─ Testing configuration? → --state dry_run
└─ No (maintenance/setup) → --state disabled
```

## Troubleshooting

**"Permission denied" or "403 Forbidden":**
- Runner controller commands require GitLab admin privileges
- Verify you're authenticated as an admin user
- Check `glab auth status` to confirm current user

**"Runner controller not found":**
- Verify controller ID with `glab runner-controller list`
- Controller may have been deleted
- Check if you have access to the correct GitLab instance

**Token creation fails:**
- Ensure controller exists and is enabled
- Verify admin privileges
- Check GitLab instance version (experimental features may require recent versions)

**Token rotation shows old token still works:**
- Token invalidation may take a few seconds to propagate
- Wait 10-30 seconds and test again
- Check controller state (disabled controllers don't enforce token validation)

**Cannot delete controller:**
- Check if controller has active runners
- May need to decommission runners first
- Use `--force` to override (⚠️ destructive)

**Experimental feature not available:**
- Verify glab version: `glab version` (requires v1.83.0+)
- Check if feature flag is enabled on GitLab instance
- Confirm GitLab instance version supports runner controllers

**Pagination not working:**
- Default page size is 30
- Use `--per-page` to adjust (max varies by instance)
- Use `--page` to navigate through results

## Related Skills

**CI/CD & Runners:**
- `glab-ci` - View and manage CI/CD pipelines and jobs
- `glab-job` - Retry, cancel, view logs for individual jobs

**Repository Management:**
- `glab-repo` - Manage repositories (runner controllers are instance-level)

**Authentication:**
- `glab-auth` - Login and authentication management

## Command Reference

For complete command syntax and all available flags, see:
- [references/commands.md](references/commands.md)
