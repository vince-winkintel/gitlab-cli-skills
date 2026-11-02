---
name: glab-deploy-token
description: Use when inspecting or creating GitLab project or group deploy tokens, including metadata, active inventory, expiry, scopes, and one-time secret handling. Use glab-token for personal, project, or group access-token rotation.
---

# glab deploy-token

Manage deploy-token metadata and explicitly approved creation for a project or group. Deploy tokens authenticate with a username/token pair and are separate from personal, project, and group access tokens.

## Inspect metadata

`list` (alias `ls`) collects all API pages; `--active` filters out both revoked and expired tokens. `get <token-id>` selects one numeric ID from the inventory. Both commands clear the token value before JSON serialization; text output contains metadata only. Neither recovers a secret. `--output json` and `--jq` support structured metadata selection.

```bash
# Credential-free discovery
glab deploy-token --help
glab deploy-token create --help
glab deploy-token get --help
```

For an approved authenticated metadata read, select the intended host and either `--repo <project-path>` or `--group <group-id-or-path>`; these flags are mutually exclusive. Group scope works outside a checkout, where default/environment host selection matters. Inside a checkout its repository host can still determine the group API host. Project scope requires a resolvable repository. Confirm the target and actor before any operation.

## Create with a protected secret handoff

`create <name>` requires at least one `--scope` (`-S`), repeated or comma-separated. The server validates granted scopes. `--username` defaults to `gitlab+deploy-token-<id>`; `--expires-at` (`-E`) accepts YYYY-MM-DD at midnight UTC or an RFC 3339 timestamp. Omitting expiry creates a non-expiring token. Prefer the minimum approved scopes and a bounded expiry. The special name `gitlab-deploy-token` can expose the pair to CI/CD as `CI_DEPLOY_USER` and `CI_DEPLOY_PASSWORD`; approve that distribution scope too.

Creation has no confirmation prompt and prints the one-time secret in both text and JSON output. It is excluded from glab's MCP tools. Before creation, obtain explicit approval for the host, project/group, actor, name, scopes, expiry, username, and secret destination. Arrange a trusted operator-controlled secret-manager handoff that keeps both output streams out of agent tool results, terminal recording, shell tracing, logs, artifacts, and repository files. If that path is unavailable, stop after help inspection and let the operator perform the approved creation privately. Never run creation as a connectivity test, echo a secret, put it in command arguments, or collect it into a task report.

Conceptual syntax only: `glab deploy-token create <name> --scope <approved-scope> --expires-at <approved-expiry> --repo <project-path>`. The resulting `<deploy-username>` and `<deploy-token-secret>` are placeholders, not values to substitute into task output. The exact upstream help includes examples that print secrets; those are reference output, not permission to execute them. A lost secret cannot be retrieved with `get`; approve a separate credential replacement and dependent-system update instead of silently creating another token. This command group does not expose revoke or rotate.

See [references/commands.md](references/commands.md) for complete captured parent, create, get, and list help.
