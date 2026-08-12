# glab artifact-registry command reference

> Help captured from the checksum-verified glab v1.113.0 macOS arm64 release binary.

## artifact-registry

```text

  Exchange a GitLab credential for a short-lived Artifact Registry access
  token, either to check your access or to hand the token to a caller.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry <command> [command] [--flags]

  COMMANDS

    get-token [--flags]  Get a short-lived access token for the GitLab Artifact Registry. (EXPERIMENTAL)
    status [--flags]     Check your access to the GitLab Artifact Registry. (EXPERIMENTAL)

  FLAGS

    -h --help            Show help for this command.

```

## artifact-registry get-token

```text

  Exchange a GitLab credential for a short-lived access token scoped to the
  GitLab Artifact Registry. The command prints the bare token to stdout,
  so a shell can capture it directly, for example to feed `docker login`.

  Prerequisites:

  - A GitLab Enterprise Edition (EE) instance on GitLab 19.1 or later.
  - Token exchange enabled on the instance (the
    `gate_token_exchange_endpoint` feature flag).

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry get-token [--flags]

  EXAMPLES

    # Get a token using the default duration
    glab artifact-registry get-token

    # Get a token valid for one hour
    glab artifact-registry get-token --duration 1h

    # Get a token as JSON, including its expiry
    glab artifact-registry get-token --output json

  FLAGS

    --duration   How long the token should remain valid. Must be between 1s and 12h0m0s. (15m0s)
    -h --help    Show help for this command.
    --hostname   Gitlab hostname to request the token from. Defaults to the configured GitLab instance.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)

```

## artifact-registry status

```text

  Exchange a GitLab credential for a short-lived Artifact Registry access
  token, then print the token's issuer, subject, audience, and expiry so
  you can confirm which identity and instance you are authenticated as. No
  credentials are written to disk.

  Prerequisites:

  - A GitLab Enterprise Edition (EE) instance on GitLab 19.1 or later.
  - Token exchange enabled on the instance (the
    `gate_token_exchange_endpoint` feature flag).

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry status [--flags]

  EXAMPLES

    # Show Artifact Registry access status
    glab artifact-registry status

    # Show Artifact Registry access status as JSON
    glab artifact-registry status --output json

  FLAGS

    -h --help    Show help for this command.
    --hostname   Gitlab hostname to check. Defaults to the configured GitLab instance.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)

```
