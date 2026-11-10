---
name: glab-service-account
description: Manage GitLab project and group service accounts with glab. Use for scoped inventory, lookup, approved creation, metadata updates, or account deletion; service-account tokens and memberships are separate operations.
---

# glab service-account

> **Source provenance:** [official command source](https://gitlab.com/gitlab-org/cli/-/tree/9b430a11f95ec78d87f19be071d1c381d8803630/internal/commands/service-account) at `9b430a11f95ec78d87f19be071d1c381d8803630`; source archive SHA-256 `482b784243e37db8ec1c85478bbfb8199739765d3315ceabe1ef2e4d32e63085`. Bundled reference help uses capture key `9b430a11f` and the official binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`.

Use [complete command help and source provenance](references/commands.md) for project/group account inventory and lifecycle operations. Choose the intended host and either `--repo` or `--group` explicitly; these flags are mutually exclusive. Otherwise `GITLAB_GROUP` selects a group, then the current project is the fallback. Confirm the actor and scope before any write.

`list` (`ls`) inventories accounts; `get <id|username>` inspects one. Numeric input always means ID. Project accounts require GitLab 18.11+ and Maintainer/Owner or administrator access. Group accounts require Owner, or on Self-Managed/Dedicated an administrator or an Owner allowed by the instance's top-level-group setting. Getting an account by ID requires GitLab 19.4+; username lookup uses the scoped inventory.

```bash
# Explicit scoped reads
glab service-account list --repo group/project --output json
glab service-account get release-bot --group group/subgroup
```

Obtain explicit approval for the target and fields before `create` or `update`. Creation defaults the name to "Service account user" and lets GitLab generate username/email when omitted. Subgroup creation requires GitLab 18.11+; custom group-account email on creation requires 17.11+. Creating an account is not token issuance or permission to grant memberships.

`update <id|username>` requires at least one of `--name`, `--username`, or `--email`; omitted fields remain unchanged and empty values cannot clear fields. Group updates require GitLab 17.10+, email updates 18.2+. A custom email normally remains unconfirmed until confirmation, except verified top-level-group domains or disabled instance email confirmation. Composite-identity account usernames cannot change.

`delete` (`del`) needs explicit approval for the exact account and affected automation: its tokens stop working, contributions move to the ghost user, and deletion happens in the background. `--yes` is required without a TTY and only bypasses the prompt; it does not supply authorization. Verify eventual removal through scoped inventory, allowing for background deletion. Do not create tokens or alter production automation as part of verification.
