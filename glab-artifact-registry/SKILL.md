---
name: glab-artifact-registry
description: Exchange GitLab credentials for short-lived Artifact Registry tokens and verify token identity with glab. Use when checking GitLab Artifact Registry access, obtaining an ephemeral registry token, or feeding a short-lived token to a registry client. Triggers on artifact registry, glab artifact-registry, glab ar, get-token, token exchange, registry access status.
---

# glab artifact-registry

Exchange the active GitLab credential for a short-lived Artifact Registry access token. The command group also accepts the `glab ar` alias. This command group is experimental; verify live help and the target GitLab instance before using it in durable automation.

## Prerequisites

- GitLab Enterprise Edition 19.1 or later.
- The instance administrator enabled the `gate_token_exchange_endpoint` feature flag.
- `glab` is authenticated to the intended hostname.

The token is ephemeral but still a credential. Never print it in logs, store it in a repository, include it in command arguments, or paste it into issue/MR content.

## Check access first

`status` performs the token exchange and prints non-secret identity metadata: issuer, subject, audience, and expiry. Each check mints and immediately discards a server-side token; prefer JSON for automation and do not call it in a tight loop.

```bash
glab artifact-registry status --hostname gitlab.example.com --output json

# Extract only non-secret expiry metadata
glab artifact-registry status \
  --hostname gitlab.example.com \
  --output json \
  --jq '.expires_at'
```

Confirm that the issuer, subject, and audience identify the intended instance, actor, and registry before requesting a token for another process.

## Request a short-lived token

Text output is the bare token on stdout so a shell can capture or pipe it. Default duration is 15 minutes; accepted durations range from 1 second through 12 hours. Use the shortest duration that covers the operation.

```bash
# Avoid command tracing and keep the token only in a process-local variable
set +x
artifact_token="$(glab artifact-registry get-token \
  --hostname gitlab.example.com \
  --duration 15m)"

# Feed via stdin, not as a command-line argument. Obtain the registry host and
# required username from the target registry's documentation or administrator.
printf '%s' "$artifact_token" | \
  docker login <artifact-registry-host> \
    --username '<registry-username>' \
    --password-stdin
unset artifact_token
```

Use `--output json` only when a consumer also needs the expiry. Treat the JSON document as secret because it contains the token. Do not pass `--jq` expressions that print the token into logs.

## Troubleshooting

- **Unsupported or not found:** verify GitLab EE 19.1+ and the `gate_token_exchange_endpoint` feature flag with the instance administrator.
- **Wrong issuer/subject/audience:** stop; re-check `--hostname`, environment-token precedence, and `glab auth status --hostname <host>`.
- **Duration rejected:** use a Go-style duration between `1s` and `12h`.
- **Expired token:** request a new short-lived token; do not persist or attempt to refresh the old one.

See [references/commands.md](references/commands.md) for captured command help.
