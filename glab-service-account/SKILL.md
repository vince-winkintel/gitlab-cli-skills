---
name: glab-service-account
description: Manage GitLab project and group service accounts with glab. Use for scoped inventory, lookup, approved creation, metadata updates, account deletion, and explicitly authorized service-account token creation, rotation, or revocation. Membership changes are separate operations.
---

# glab service-account

Current captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

> **Source provenance:** [official command source](https://gitlab.com/gitlab-org/cli/-/tree/9b430a11f95ec78d87f19be071d1c381d8803630/internal/commands/service-account) at `9b430a11f95ec78d87f19be071d1c381d8803630`; source archive SHA-256 `482b784243e37db8ec1c85478bbfb8199739765d3315ceabe1ef2e4d32e63085`. Bundled reference help uses capture key `9b430a11f` and the official binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`.

Use [captured help and source provenance](references/help-206ebab4f.md) for project/group account inventory and lifecycle operations. Choose the intended host and either `--repo` or `--group` explicitly; these flags are mutually exclusive. Otherwise `GITLAB_GROUP` selects a group, then the current project is the fallback. Confirm the actor and scope before any write.

`list` (`ls`) inventories accounts; `get <id|username>` inspects one. Numeric input always means ID. Project accounts require GitLab 18.11+ and Maintainer/Owner or administrator access. Group accounts require Owner, or on Self-Managed/Dedicated an administrator or an Owner allowed by the instance's top-level-group setting. Getting an account by ID requires GitLab 19.4+; username lookup uses the scoped inventory.

```bash
# Explicit scoped reads
glab service-account list --repo group/project --output json
glab service-account get release-bot --group group/subgroup
```

Obtain explicit approval for the target and fields before `create` or `update`. Creation defaults the name to "Service account user" and lets GitLab generate username/email when omitted. Subgroup creation requires GitLab 18.11+; custom group-account email on creation requires 17.11+. Creating an account is not token issuance or permission to grant memberships.

`update <id|username>` requires at least one of `--name`, `--username`, or `--email`; omitted fields remain unchanged and empty values cannot clear fields. Group updates require GitLab 17.10+, email updates 18.2+. A custom email normally remains unconfirmed until confirmation, except verified top-level-group domains or disabled instance email confirmation. Composite-identity account usernames cannot change.

`delete` (`del`) needs explicit approval for the exact account and affected automation: its tokens stop working, contributions move to the ghost user, and deletion happens in the background. `--yes` is required without a TTY and only bypasses the prompt; it does not supply authorization. Verify eventual removal through scoped inventory, allowing for background deletion. Do not create tokens or alter production automation as part of verification.

## Service-account tokens

The `token` group manages personal access tokens acting as a scoped service account. Each subcommand takes the account ID or username first; numeric account inputs always mean ID. Resolve the account with scoped account inventory and choose a nonempty explicit `--repo` or `--group`; otherwise `GITLAB_GROUP` or checkout context can select the target. Group service-account tokens require GitLab 17.11+; project service accounts require GitLab 18.11+.

`token list <account-id|username>` lists metadata across all pages; `--active` asks for active tokens. Use IDs from that inventory for mutations. `token create <account-id|username> <name>` requires one or more `--scope` values. `token rotate <account-id|username> <token-id|name>` revokes the old value immediately and creates a replacement with the same name, description, and scopes. Creation and rotation default to 30 days at midnight UTC; `--duration` and `--expires-at YYYY-MM-DD` are mutually exclusive, with duration limited to 365 days. `token revoke <account-id|username> <token-id|name>` immediately breaks clients using that token. Token names resolve active tokens only; ambiguous names require an ID.

Obtain explicit user authorization for the exact host, actor, account, token, scopes, expiry, affected clients, and secret destination before creation, rotation, or revocation. These commands do not provide a confirmation barrier. Creation and rotation print the new secret on stdout (JSON includes it too); keep both streams out of agent tool results, chat, tracing, logs, repository files, and artifacts. Use an operator-controlled secret-manager handoff, or stop at help inspection if no protected handoff exists. Never expose returned token values or test by issuing a token. Approve dependent-client updates separately and verify only metadata. The upstream help examples are captured reference text, not authorization to execute them.
