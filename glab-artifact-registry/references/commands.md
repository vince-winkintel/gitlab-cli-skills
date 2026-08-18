# glab artifact-registry command reference

> Help captured from the checksum-verified glab v1.114.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed. The binary renderer's `Gitlab` typo in three `--hostname` descriptions is normalized to the canonical `GitLab`; these blocks are therefore not claimed as byte-for-byte binary output.

## artifact-registry

```text

  Exchange a GitLab credential for a short-lived Artifact Registry access
  token, either to check your access, to hand the token to a caller, or to
  configure a package manager to authenticate against the registry.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry <command> [command] [--flags]

  COMMANDS

    get-token [--flags]  Get a short-lived access token for the GitLab Artifact Registry. (EXPERIMENTAL)
    login [--flags]      Authenticate a package manager against the GitLab Artifact Registry. (EXPERIMENTAL)
    status [--flags]     Check your access to the GitLab Artifact Registry. (EXPERIMENTAL)

  FLAGS

    -h --help            Show help for this command.

```

The `glab ar` alias emits the same help surface.

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
    --hostname   GitLab hostname to request the token from. Defaults to the configured GitLab instance.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)

```

## artifact-registry login

```text

  Configure a package manager to authenticate against the GitLab Artifact
  Registry, using a short-lived access token exchanged from your GitLab
  session.

  With `--docker`, glab is registered as a Docker credential helper
  for the registry, and Docker exchanges a fresh token on every pull or
  push, so `--duration` does not apply.

  Use `--registry` only for a registry the Artifact Registry
  actually backs. The credential helper prefers the artifact registry
  token and falls back to `container_registry_domains` only
  when that exchange fails, so a container registry listed here gets an
  artifact registry token it rejects on every pull.

  Docker runs that credential helper as its own subprocess, which reads
  your credentials from the configuration file and ignores
  `GITLAB_TOKEN`. This command verifies the login the same way, so
  run `glab auth login` first if no token is stored for the host.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry login [--flags]

  EXAMPLES

    # Configure Docker to authenticate against a registry
    glab artifact-registry login --docker --registry registry.example.com

  FLAGS

    --docker    Configure Docker to authenticate against the registry. Writes to $DOCKER_CONFIG, or ~/.docker when it is unset.
    --duration  How long the exchanged token should remain valid. Ignored for now: --docker is the only tool this command configures, and its credential helper mints a fresh token for every request. (0s)
    -h --help   Show help for this command.
    --hostname  GitLab hostname to request the token from. Defaults to the configured GitLab instance.
    --registry  Bare hostname of the registry to authenticate against.

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
    --hostname   GitLab hostname to check. Defaults to the configured GitLab instance.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)

```
