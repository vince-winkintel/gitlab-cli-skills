---
name: glab-deploy-token
description: List GitLab project or group deploy-token metadata and filter active credentials. Use for glab deploy-token list, deploy token inventory, expiry, revocation status, or scopes; use glab-token for personal, project, or group access-token rotation.
---

# glab deploy-token

Inspect deploy-token metadata for a project or group. `list` (alias `ls`) collects all API pages; `--active` filters out both revoked and expired tokens. Text columns include ID, name, username, scopes, expiry, revoked, and expired. JSON output also clears any secret token value; a listing cannot recover a deploy-token secret.

```bash
# Credential-free command discovery
glab deploy-token --help
glab deploy-token list --help

# Read-only authenticated inventory after confirming the intended host/project
glab deploy-token list --repo group/project --active --output json
glab deploy-token list --group group/subgroup --output json
```

`--repo` and `--group` are mutually exclusive. Group scope works outside a checkout; verify the default/environment host there. Project scope needs a resolvable repository. `--jq` filters JSON. The command group exposes listing only: do not infer create/revoke/rotate commands from access-token management. Listing does not authorize credential changes.

See [references/commands.md](references/commands.md) for complete captured parent and list help.
