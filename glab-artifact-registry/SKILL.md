---
name: glab-artifact-registry
description: Exchange GitLab credentials for short-lived Artifact Registry tokens, verify token identity, and configure Docker's credential helper with glab. Use when checking GitLab Artifact Registry access, obtaining an ephemeral registry token, or configuring Docker for a GitLab Artifact Registry. Triggers on artifact registry, glab artifact-registry, glab ar, get-token, token exchange, registry access status, artifact-registry login, Docker credential helper.
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

## Configure Docker credential exchange

`glab artifact-registry login --docker` installs the `docker-credential-glab` shim and registers `glab` under Docker's per-registry `credHelpers`. Docker then exchanges a fresh short-lived token for every pull or push, so `--duration` is currently ignored.

```bash
# Inspect the intended Docker config and stored GitLab identity first
printf 'Docker config: %s\n' "${DOCKER_CONFIG:-$HOME/.docker}/config.json"
glab auth status --hostname gitlab.example.com

# Configure only the verified Artifact Registry hostname
glab artifact-registry login \
  --hostname gitlab.example.com \
  --docker \
  --registry registry.example.com
```

Safety and compatibility rules:

- `--registry` must be a bare hostname, optionally with a port. Do not pass a URL or path.
- The helper subprocess intentionally ignores `GITLAB_TOKEN`. It normally reads a token stored by `glab auth login`; inside a GitLab CI job, it also honors `CI_JOB_TOKEN` when CI auto-login is enabled with `GLAB_ENABLE_CI_AUTOLOGIN=true`. Outside that CI path, store authentication for the selected host before configuring Docker.
- Use this only for a registry actually backed by GitLab Artifact Registry. Misclassifying a normal container registry can make every pull fail because an exchanged Artifact Registry token takes precedence.
- The command writes `${DOCKER_CONFIG:-$HOME/.docker}/config.json`. Review that file's location first. It refuses to replace another per-registry credential helper, preserves existing `docker login` data, and reports when the new helper shadows that data.
- Re-running the command for the same registry is safe and idempotent. After configuration, test a non-destructive pull or registry operation against the intended host without printing credentials.

## Troubleshooting

- **Unsupported or not found:** verify GitLab EE 19.1+ and the `gate_token_exchange_endpoint` feature flag with the instance administrator.
- **Wrong issuer/subject/audience:** stop; re-check `--hostname`, environment-token precedence, and `glab auth status --hostname <host>`.
- **Duration rejected:** use a Go-style duration between `1s` and `12h`.
- **Expired token:** request a new short-lived token; do not persist or attempt to refresh the old one.
- **Stored-token error during Docker setup:** run `glab auth login --hostname <host>`; an environment-only token is not used by the helper.
- **Credential-helper conflict:** inspect Docker's existing `credHelpers` entry and keep the current helper unless the operator explicitly approves a migration.

See [references/commands.md](references/commands.md) for captured command help.
