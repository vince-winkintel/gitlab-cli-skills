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

# Browser/OAuth login without the prompt
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

> `glab auth login` supports a complete setup flow:
> - `--ssh-hostname` to explicitly set a different SSH endpoint for self-hosted instances
> - `--web` to skip the login-type prompt and go straight to browser/OAuth auth
> - `--container-registry-domains` to preconfigure registry / dependency-proxy domains during login
>
> Example: API hostname `gitlab.company.com`, SSH hostname `ssh.company.com`

For personal access tokens, glab requires at least `api` and `write_repository`. GitLab 18.9 introduced `https://<host>/-/user_settings/personal_access_tokens/legacy/new?scopes=api,write_repository`; that route does not exist on earlier releases. GitLab 18.8 and earlier use `https://<host>/-/user_settings/personal_access_tokens?scopes=api,write_repository` instead. Use the URL for the target instance rather than assuming the current GitLab.com route exists on an older self-managed server.

### Login flag examples

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

# Explicitly opt out of keyring storage (stores the token as plaintext)
glab auth login --hostname gitlab.company.com --insecure-storage \
  --stdin < approved-token-file
```

### Credential storage

On a normal workstation, `glab auth login` stores credentials in the operating system keyring by default when one is available: macOS Keychain, Windows Credential Manager, or Linux Secret Service. The old `--use-keyring` flag is deprecated because keyring storage is now the default. Re-running login migrates a credential previously stored as plaintext in the config file into the keyring.

Use `--insecure-storage` only when plaintext config-file storage is explicitly required and its risk is accepted. If no keyring backend is available, glab warns and falls back to the config file. In CI (`GITLAB_CI` or `CI` is set), glab defaults to config-file storage because keyrings are usually unavailable or ephemeral; prefer environment credentials rather than persisting a login there.

If a keyring is locked, unavailable, or denies access, glab reports the credential-read failure directly. Fix keyring access or re-authenticate instead of treating the resulting error as an invalid token.

glab checks whether refreshed OAuth credentials can be saved before it refreshes the token, and serializes credential writes across concurrent `glab` processes. If multiple agents or shells share one config directory, prefer separate config directories per actor for isolation, but do not add external file locks around `glab` itself.

In a sandbox such as Claude Code, `glab` must be allowed to write the directory from `glab config path --dir`, not only the `config.yml` file. `glab` writes a temporary file beside the config and then replaces the original. On snap installs, connect keyring access with `sudo snap connect glab:password-manager-service` if encrypted credential storage is required; otherwise `glab auth login` can fall back to plaintext config storage.

When re-authenticating interactively, `glab` preserves saved per-host values such as a custom API host, SSH host, and container-registry domains unless you explicitly override them with flags or prompts. Verify these values after re-authentication instead of deleting the config preemptively:

```bash
glab config get api_host --host gitlab.company.com
glab config get ssh_host --host gitlab.company.com
glab config get container_registry_domains --host gitlab.company.com
```

Non-interactive login also persists explicitly supplied `--git-protocol` and `--api-protocol` values in the host configuration. This applies to token/stdin and other prompt-free login paths, so automation can configure the protocols in the same login operation instead of requiring a later config edit. Verify the resulting host entry before relying on it:

```bash
glab auth login --hostname gitlab.company.com --stdin \
  --git-protocol ssh --api-protocol https < approved-token-file
glab config get git_protocol --host gitlab.company.com
glab config get api_protocol --host gitlab.company.com
```

Keep token files outside version control and do not print their contents.

**CI auto-login:** `GLAB_ENABLE_CI_AUTOLOGIN=true` lets glab use `CI_JOB_TOKEN` in GitLab CI/CD without a stored login. `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, and `OAUTH_TOKEN` still take precedence, so leave them unset when the intended credential is `CI_JOB_TOKEN`. Use explicit env tokens instead when a command needs a project, group, or personal access token.

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
- if `glab` cannot see the env token, it may silently fall back to shared stored auth in the active global config file
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

`configure-docker` adds glab only for the configured GitLab registry domains.
It preserves unrelated Docker credential helpers and refuses to replace a
different helper already assigned to the same domain. If a domain has legacy
credentials from `docker login`, glab warns that the helper takes precedence;
after verifying helper-based access, use the exact suggested `docker logout
<domain>` command to remove the shadowed entry. Back up and review
`$DOCKER_CONFIG/config.json` before repairing conflicts manually.

## Troubleshooting

**"401 Unauthorized" errors:**
- Check status: `glab auth status`
- Verify token hasn't expired (check GitLab settings)
- Re-authenticate: `glab auth login`

**Re-login still looks stuck after changing auth method:**
- If you switched from browser/OAuth login to token-based login and `glab` still appears to use stale stored credentials, run `glab auth login` again instead of assuming the config must be edited manually.
- After re-login, verify with `glab auth status` before retrying the failing command.

**Env-token auth failures:**
- If `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, or `OAUTH_TOKEN` is exported, it overrides stored credentials.
- `GITLAB_TOKEN` and `GITLAB_ACCESS_TOKEN` are treated as personal access tokens independently of a stored OAuth profile, so a temporary PAT does not inherit or refresh saved OAuth state.
- If the host is configured for OAuth but an environment variable contains an OAuth access token, set `GLAB_IS_OAUTH2=true`; otherwise glab sends the environment token as a personal access token. `glab auth status` reports this scheme mismatch after a 401.
- If auth suddenly fails, check whether an env token is being picked up before assuming your saved login is broken. `glab auth login` and `glab auth status` warn when this precedence applies.
- Run `type glab` to distinguish a wrapper that intentionally injects a token (for example, a 1Password shell plugin alias) from a plain executable path. A wrapper can be expected and need no action; a plain path means the token came from the shell profile, current environment, or CI variables.
- These failures can affect both read operations and writes, not just write pre-flight checks.
- Verify the active actor and token path with `glab auth status` and `glab api user` before any GitLab write.
- In multi-agent shells, deliberately re-source the intended env file with `set -a; source ...; set +a` before retrying.

**Self-managed OAuth URL or refresh problems:**
- Re-authenticate with the full configured host/subfolder; browser OAuth includes the configured subfolder in its authorization URL.
- A re-authentication response that omits a replacement refresh token preserves the existing refresh token instead of clearing it.
- If refresh fails with `invalid_grant`, re-run `glab auth login`; a revoked/expired OAuth grant or an earlier failed credential save can leave stored OAuth credentials stale.
- If OAuth refresh fails inside a sandbox with a credential-save error, grant write access to `glab config path --dir` and re-authenticate. Retrying the same stale token normally will not repair the saved credential.
- Docker and other helpers skip OAuth refresh for hosts authenticated with personal access tokens; check the token type before debugging OAuth state.

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
