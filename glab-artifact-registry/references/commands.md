# glab artifact-registry command reference

> Help captured from the checksum-verified glab v1.113.0 macOS arm64 release binary.

## artifact-registry

```text
Exchange a GitLab credential for a short-lived Artifact Registry access token,
either to check your access or to hand the token to a caller.

This feature is an experiment and is not ready for production use.

Usage:
  glab artifact-registry <command> [command] [--flags]

Commands:
  get-token [--flags]  Get a short-lived access token for the GitLab Artifact Registry. (EXPERIMENTAL)
  status [--flags]     Check your access to the GitLab Artifact Registry. (EXPERIMENTAL)
```

## artifact-registry get-token

```text
Exchange a GitLab credential for a short-lived access token scoped to the
GitLab Artifact Registry. The command prints the bare token to stdout.

Prerequisites:
- GitLab Enterprise Edition (EE) 19.1 or later.
- Token exchange enabled (`gate_token_exchange_endpoint`).

Usage:
  glab artifact-registry get-token [--flags]

Flags:
  --duration   How long the token should remain valid. Must be between 1s and 12h0m0s. (15m0s)
  -h --help    Show help for this command.
  --hostname   Gitlab hostname to request the token from. Defaults to the configured GitLab instance.
  --jq         Filter JSON output with a jq expression.
  -F --output  Format output as: text, json. (text)
```

## artifact-registry status

```text
Exchange a GitLab credential for a short-lived Artifact Registry access token,
then print the token's issuer, subject, audience, and expiry so you can confirm
which identity and instance you are authenticated as. No credentials are
written to disk.

Prerequisites:
- GitLab Enterprise Edition (EE) 19.1 or later.
- Token exchange enabled (`gate_token_exchange_endpoint`).

Usage:
  glab artifact-registry status [--flags]

Flags:
  -h --help    Show help for this command.
  --hostname   Gitlab hostname to check. Defaults to the configured GitLab instance.
  --jq         Filter JSON output with a jq expression.
  -F --output  Format output as: text, json. (text)
```
