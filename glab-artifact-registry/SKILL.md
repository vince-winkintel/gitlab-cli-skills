---
name: glab-artifact-registry
description: Exchange GitLab credentials for short-lived Artifact Registry tokens, verify token identity, and configure package-manager authentication with glab. Use when checking GitLab Artifact Registry access, obtaining an ephemeral registry token, or configuring Docker, Maven, Gradle, npm, Yarn, or sbt for a GitLab Artifact Registry. Triggers on artifact registry, glab artifact-registry, glab ar, get-token, token exchange, registry access status, artifact-registry login, Docker credential helper, Maven registry, Gradle registry, npm auth, sbt credentials.
---

# glab artifact-registry

Exchange the active GitLab credential for a short-lived Artifact Registry access token. The command group also accepts the `glab ar` alias. This command group is experimental; verify live help and the target GitLab instance before using it in durable automation.

## Maven and sbt destination files

`login --config-file <path>` applies only to `--maven` or `--sbt`; other package-manager modes reject it, as does an explicitly empty path. It writes only that file, leaving the default destinations alone. Approve the token exchange and exact destination before running login; these files contain a live credential and must stay outside repositories and logs. A project-specific Maven settings file must also be selected by the consuming build, for example with Maven's `--settings` option. For sbt with `-Dsbt.global.base`, select the `credentials.sbt` file inside that actual base.

Without `--config-file`, sbt writes `~/.sbt/1.0/credentials.sbt` plus `<base>/2/credentials.sbt`. For sbt 2.x, `<base>` uses the first valid absolute override: `SBT_CONFIG_HOME`, then `XDG_CONFIG_HOME/sbt` on macOS/Linux or `%LOCALAPPDATA%\sbt` on Windows, then `~/.config/sbt` as the fallback. On Windows, glab uses `LOCALAPPDATA` instead of `XDG_CONFIG_HOME`; it does not consult `XDG_CONFIG_HOME` for this base. Blank or relative overrides are skipped with a warning because sbt can resolve them differently. On Windows, absolute `LOCALAPPDATA` also gets `sbt/credentials.sbt` for the sbt 2.x batch launcher. Inspect every reported destination: a later write can fail after an earlier file already received the token.

Credentials use realm `artifact-registry`, username `__token__`, and the lowercased hostname without its port. Existing matching active entries are refreshed. An already-running sbt shell/server keeps its old credentials until `reload` or `sbt shutdown`; refresh the token and reload before retrying an expired-token build.

```bash
# After approving the exchange and the destination outside version control
glab artifact-registry login --maven --registry https://ar.example.com \
  --registry-alias gitlab-ar --config-file /secure/build-settings.xml
glab artifact-registry login --sbt --registry https://ar.example.com \
  --config-file /secure/sbt-global/credentials.sbt
```

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

## Configure package-manager authentication

`glab artifact-registry login` configures exactly one package manager per run:

- `--docker` installs the `docker-credential-glab` shim and registers `glab` under Docker's per-registry `credHelpers`.
- `--maven` writes a `<server>` block to `~/.m2/settings.xml`, keyed by `--registry-alias`; the consuming `<repository>` must use the same `<id>`.
- `--gradle` writes `{alias}Url`, `{alias}Username`, and `{alias}Password` to `~/.gradle/gradle.properties`, where `{alias}` is `--registry-alias`.
- `--npm` writes a `//{host}{path}/:_authToken` entry to `~/.npmrc`; you must still configure `registry=` or `@scope:registry=` to point npm at the registry.
- `--yarn` configures Yarn 2 or later in `~/.yarnrc.yml`: an `npmRegistries` entry holds `npmAuthToken` and `npmAlwaysAuth`. Set a matching `npmRegistryServer` separately. For Yarn 1 use `--npm`. Existing `npmScopes` credentials can override the registry token; inspect the warning and review the scope before changing it. Rewriting YAML can change formatting.
- `--sbt` writes credentials for both sbt 1.x and 2.x; see [destination and reload rules above](#maven-and-sbt-destination-files). `--config-file` selects one file instead.

```bash
# Inspect the intended Docker config and stored GitLab identity first
printf 'Docker config: %s\n' "${DOCKER_CONFIG:-$HOME/.docker}/config.json"
glab auth status --hostname gitlab.example.com

# Configure only the verified Artifact Registry hostname
glab artifact-registry login \
  --hostname gitlab.example.com \
  --docker \
  --registry registry.example.com

# Configure Maven for a two-hour token
glab artifact-registry login \
  --hostname gitlab.example.com \
  --maven \
  --registry https://ar.example.com \
  --registry-alias gitlab-ar \
  --duration 2h
```

Safety and compatibility rules:

- For `--docker`, `--registry` must be a bare hostname, optionally with a port. For Maven, Gradle, npm, Yarn, and sbt, `--registry` is typically a URL.
- Docker exchanges a fresh token for every pull or push, so `--duration` does not apply. Maven, Gradle, npm, Yarn, and sbt receive one static token; rerun the command before `--duration` elapses.
- The Docker helper subprocess intentionally ignores `GITLAB_TOKEN`. It normally reads a token stored by `glab auth login`; inside a GitLab CI job, it also honors `CI_JOB_TOKEN` when CI auto-login is enabled with `GLAB_ENABLE_CI_AUTOLOGIN=true`. Maven, Gradle, npm, Yarn, and sbt login paths can read `GITLAB_TOKEN` because `glab` writes the exchanged token into each tool's config file.
- Use this only for a registry actually backed by GitLab Artifact Registry. Misclassifying a normal container registry can make every pull fail because an exchanged Artifact Registry token takes precedence.
- Review the destination config path before writing: `${DOCKER_CONFIG:-$HOME/.docker}/config.json`, `~/.m2/settings.xml`, `~/.gradle/gradle.properties`, `~/.npmrc`, `~/.yarnrc.yml`, or the sbt destination files listed above (or the explicit `--config-file`).
- `--registry-alias` applies only to Maven and Gradle. For Gradle, choose an alias that is a valid identifier in the build script; the derived default can contain hyphens.
- Re-running the command for the same registry refreshes or replaces the matching entry. After configuration, test a non-destructive package-manager operation against the intended host without printing credentials.

## Troubleshooting

- **Unsupported or not found:** verify GitLab EE 19.1+ and the `gate_token_exchange_endpoint` feature flag with the instance administrator.
- **Wrong issuer/subject/audience:** stop; re-check `--hostname`, environment-token precedence, and `glab auth status --hostname <host>`.
- **Duration rejected:** use a Go-style duration between `1s` and `12h`.
- **Expired token:** request a new short-lived token; do not persist or attempt to refresh the old one.
- **Stored-token error during Docker setup:** run `glab auth login --hostname <host>`; an environment-only token is not used by the Docker helper.
- **Credential-helper conflict:** inspect Docker's existing `credHelpers` entry and keep the current helper unless the operator explicitly approves a migration.
- **Build tool still unauthenticated:** verify the tool reads the file that `glab artifact-registry login` wrote, and that its registry URL or repository ID matches the written key.

See [references/commands.md](references/commands.md) for captured command help.
