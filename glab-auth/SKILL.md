---
name: glab-auth
description: Manage GitLab CLI authentication including login/logout, check auth status, switch accounts, and configure Docker registry access. Use when setting up glab for first time, troubleshooting auth issues, switching GitLab instances/accounts, or configuring Docker to pull from GitLab registry. Triggers on auth, login, logout, authentication, credentials, token, Docker registry.
---

# glab auth

Manage GitLab CLI authentication.

## Quick start

```bash
# Interactive login
glab auth login

# Browser/OAuth login without the prompt (v1.90.0+)
glab auth login --hostname gitlab.com --web

# Check current auth status
glab auth status

# Login to different instance
glab auth login --hostname gitlab.company.com

# Logout
glab auth logout
```

## Workflows

### First-time setup

1. Run `glab auth login`
2. Choose authentication method (token or browser)
3. Follow prompts for your GitLab instance
4. Verify with `glab auth status`

> **v1.90.0+:** `glab auth login` supports a more complete setup flow:
> - `--ssh-hostname` to explicitly set a different SSH endpoint for self-hosted instances
> - `--web` to skip the login-type prompt and go straight to browser/OAuth auth
> - `--container-registry-domains` to preconfigure registry / dependency-proxy domains during login
>
> Example: API hostname `gitlab.company.com`, SSH hostname `ssh.company.com`

### v1.90.0 Login Flag Examples

```bash
# Self-managed GitLab with separate API and SSH endpoints
glab auth login \
  --hostname gitlab.company.com \
  --ssh-hostname ssh.company.com

# Skip prompts and go straight to browser/OAuth auth
glab auth login --hostname gitlab.com --web

# Preconfigure multiple registry / dependency proxy domains during login
glab auth login \
  --hostname gitlab.com \
  --web \
  --container-registry-domains "registry.gitlab.com,gitlab.com"
```

**CI auto-login (GA in v1.90.0):** when enabled, token environment variables such as `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, or `OAUTH_TOKEN` still take precedence over stored credentials and `CI_JOB_TOKEN`.

### Agentic and multi-account setups

If you need different agents to show up as different GitLab users, use distinct GitLab bot/service accounts. Multiple PATs on one GitLab user are useful for rotation or scope separation, but they do **not** create distinct visible identities.

Use the **Actor identity** for actor-authored GitLab comments, replies, approvals, and other writes. Use an **agent identity** only when the GitLab action is explicitly that agent's own work product. Pick the intended visible actor before the first write.

A good operational pattern is one env file per actor:

```bash
# ~/.config/openclaw/env/gitlab-reviewer.env
GITLAB_TOKEN=glpat-...
GITLAB_HOST=gitlab.com
```

Keep these env files outside version control, restrict their permissions (for example `chmod 600`), be mindful of backup exposure, and prefer least-privilege bot/service-account tokens. In a reused shell, clear stale GitLab auth vars first or start a fresh shell.

If the file uses plain `KEY=value` lines, load it with exported vars before running `glab`:

```bash
unset GITLAB_TOKEN GITLAB_ACCESS_TOKEN OAUTH_TOKEN GITLAB_HOST
set -a
source ~/.config/openclaw/env/gitlab-<actor>.env
set +a
```

Why this matters:
- plain `source` does not necessarily export variables to child processes
- `glab` only sees env vars that are exported
- if `glab` cannot see the env token, it may silently fall back to shared stored auth in `~/.config/glab-cli/config.yml`
- if another env file was sourced earlier in the same shell/session, identity can be sticky in ways that are unsafe for writes unless you deliberately switch and verify

That fallback/shared-auth behavior is convenient for humans, but in multi-agent automation it can cause the wrong GitLab account to post comments, create MRs, or approve work.

### Required pre-flight before any GitLab write

Run this immediately before any GitLab write, including `glab mr note`, review submission or approval, thread replies, and any `glab api` `POST`/`PATCH`/`PUT`/`DELETE` call:

```bash
glab auth status --hostname "$GITLAB_HOST"
glab api --hostname "$GITLAB_HOST" user
```

This assumes the target actor env file set `GITLAB_HOST` for the exact GitLab instance you intend to modify. Do not write until both commands clearly show the intended visible actor on that host.

### Wrong-identity remediation

If a comment or reply was posted under the wrong identity:

1. Stop posting.
2. Delete the mistaken comment or reply if cleanup is needed.
3. `unset GITLAB_TOKEN GITLAB_ACCESS_TOKEN OAUTH_TOKEN GITLAB_HOST` or start a fresh shell.
4. Source the correct env file with `set -a; source ...; set +a`.
5. Rerun `glab auth status --hostname "$GITLAB_HOST"` and `glab api --hostname "$GITLAB_HOST" user`.
6. Repost under the correct actor.
7. Verify the thread no longer shows the wrong visible author for the replacement message.

If the wrong-identity write changed state beyond a comment or reply, re-auth as above and then use the matching GitLab reversal for that write under the correct actor and host, such as unapproving an MR or issuing the compensating `glab api --hostname "$GITLAB_HOST"` mutation for the exact resource that was changed.

### Switching accounts/instances

1. **Logout from current:**
   ```bash
   glab auth logout
   ```

2. **Login to new instance:**
   ```bash
   glab auth login --hostname gitlab.company.com
   ```

3. **Verify:**
   ```bash
   glab auth status --hostname gitlab.company.com
   ```

### Docker registry access

1. **Configure Docker helper:**
   ```bash
   glab auth configure-docker
   ```

2. **Verify Docker can authenticate:**
   ```bash
   docker login registry.gitlab.com
   ```

3. **Pull private images:**
   ```bash
   docker pull registry.gitlab.com/group/project/image:tag
   ```

## Troubleshooting

**"401 Unauthorized" errors:**
- Check status: `glab auth status`
- Verify token hasn't expired (check GitLab settings)
- Re-authenticate: `glab auth login`

**Re-login still looks stuck after changing auth method (v1.92.0):**
- If you switched from browser/OAuth login to token-based login and `glab` still appears to use stale stored credentials, run `glab auth login` again instead of assuming the config must be edited manually.
- After re-login, verify with `glab auth status` before retrying the failing command.

**Env-token auth failures (v1.91.0 troubleshooting):**
- If `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, or `OAUTH_TOKEN` is exported, it overrides stored credentials.
- If auth suddenly fails, check whether an env token is being picked up before assuming your saved login is broken.
- These failures can affect both read operations and writes, not just write pre-flight checks.
- Verify the active actor and token path with `glab auth status` and `glab api user` before any GitLab write.
- In multi-agent shells, deliberately re-source the intended env file with `set -a; source ...; set +a` before retrying.

**Multiple instances:**
- Use `--hostname` flag to specify instance
- Each instance maintains separate auth

**Docker authentication fails:**
- Re-run: `glab auth configure-docker`
- Check Docker config: `cat ~/.docker/config.json`
- Verify helper is set: `"credHelpers": { "registry.gitlab.com": "glab-cli" }`

## Subcommands

See [references/commands.md](references/commands.md) for detailed flag documentation:
- `login` - Authenticate with GitLab instance
- `logout` - Log out of GitLab instance
- `status` - View authentication status
- `configure-docker` - Configure Docker to use GitLab registry
- `docker-helper` - Docker credential helper
- `dpop-gen` - Generate DPoP token

## Related Skills

**Initial setup:**
- After authentication, see `glab-config` to set CLI defaults
- See `glab-ssh-key` for SSH key management
- See `glab-gpg-key` for commit signing setup

**Repository operations:**
- See `glab-repo` for cloning repositories
- Authentication required before first clone/push
