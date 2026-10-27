# glab artifact-registry command reference

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

> Older capture notes below apply only to fences without the `685c1cbd7` marker.

> Unmarked blocks retain the checksum-verified glab v1.115.0 macOS arm64 capture, with terminal padding/trailing whitespace removed and renderer `Gitlab` normalized to `GitLab`; those blocks are not byte-for-byte output. The refreshed parent and `login` blocks preserve renderer spelling verbatim.

## artifact-registry

<!-- help-capture: 685c1cbd7:b3bbaacb94f5 -->

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

<!-- help-capture: 685c1cbd7:14d9b48a5cbe -->

```text

  Configure a package manager to authenticate against the GitLab Artifact
  Registry, using a short-lived access token exchanged from your GitLab
  session.

  Use the flag for your package manager:

  - `--docker`: registers `glab` as a Docker credential
    helper for the registry.
  - `--maven`: writes a `<server>` block in
    `~/.m2/settings.xml`, or `--config-file`, keyed by
    `--registry-alias`.
    Reference it from a `<repository>` carrying the same
    `<id>`. The token is written in plain text, so keep a
    `--config-file` out of version control.
  - `--gradle`: writes `{alias}Url`,
    `{alias}Username`, and `{alias}Password` in
    `~/.gradle/gradle.properties`, where `{alias}` is
    `--registry-alias`.
  - `--npm`: writes a `//{host}{path}/:_authToken` entry
    in `~/.npmrc`. You still need to point npm at the registry, with a
    `registry=` or `@scope:registry=` line.
  - `--yarn`: writes an `npmRegistries` entry with `npmAuthToken`
    and `npmAlwaysAuth` in `~/.yarnrc.yml`, for Yarn 2 and later. Set
    an `npmRegistryServer` that matches `--registry`. Rewriting the
    file can change its formatting, like indentation, blank lines, and line endings.
  - `--sbt`: writes a `credentials +=` line in
    `~/.sbt/1.0/credentials.sbt`, which sbt 1.x reads, and the
    same line in `2/credentials.sbt` in the sbt 2.x global base,
    which sbt 2.x reads. That base is `~/.config/sbt`, or
    `%LOCALAPPDATA%\sbt` on Windows, unless
    `SBT_CONFIG_HOME` or `XDG_CONFIG_HOME` moves it.
    On Windows it also writes
    `%LOCALAPPDATA%\sbt\credentials.sbt`. The `sbt.bat`
    of sbt 2.x points every build it starts, on either version, at
    that file only, even when `SBT_CONFIG_HOME` is set.
    The `sbt.version` in a project's
    `project/build.properties` decides which file its build
    reads. An sbt started with any other `-Dsbt.global.base`
    reads none of them. An sbt shell or sbt 2.x server that is
    already running keeps the credentials it loaded, so run
    `reload` in it, or `sbt shutdown`, after you log in.
    To write a different file, pass it with `--config-file`. It
    must be a `.sbt` file that sbt loads, not a properties file
    such as `~/.sbt/.credentials`.

  Token lifetime:

  - `--docker` exchanges a fresh token on every pull or push,
    so `--duration` does not apply.
  - Every other flag writes one token, and nothing refreshes it. Run
    the command again before `--duration` elapses. The default
    is 15 minutes and the maximum is 12 hours.

  Credential resolution:

  - Docker runs the credential helper as its own subprocess, which
    reads your credentials from the configuration file and ignores
    `GITLAB_TOKEN`. This command verifies the login the same
    way, so run `glab auth login` first if no token is stored
    for the host.
  - Every other flag does read `GITLAB_TOKEN`. `glab`
    writes the token into each file itself, so the tool can read it
    without fetching credentials itself.

  Registry and alias selection:

  - Use `--registry` only for a registry the Artifact Registry
    actually backs. If you name a container registry here, it receives the
    wrong token and the error only surfaces on the next pull.
  - `--registry-alias` applies to `--maven` and
    `--gradle` only, because `--npm`, `--sbt`,
    and `--yarn` key their entries on `--registry`
    itself.
    For `--gradle`, use an alias that is a valid identifier
    in your build script: the default is derived from the registry
    host and contains hyphens, which Groovy cannot interpolate as
    `${...}`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab artifact-registry login [--flags]

  EXAMPLES

    # Configure Docker to authenticate against a registry
    glab artifact-registry login --docker --registry registry.example.com

    # Configure Maven to authenticate against a registry for two hours
    glab artifact-registry login --maven --registry https://ar.example.com --duration 2h

    # Configure Gradle to authenticate against a registry for two hours
    glab artifact-registry login --gradle --registry https://ar.example.com --duration 2h

    # Configure npm to authenticate against a registry for two hours
    glab artifact-registry login --npm --registry https://ar.example.com --duration 2h

    # Configure Yarn 2 or later to authenticate against a registry for two hours
    glab artifact-registry login --yarn --registry https://ar.example.com --duration 2h

    # Configure sbt to authenticate against a registry for two hours
    glab artifact-registry login --sbt --registry https://ar.example.com --duration 2h

    # Configure Maven through a settings.xml passed to mvn with -s
    glab artifact-registry login --maven --registry https://ar.example.com --config-file ~/.m2/ci-settings.xml

  FLAGS

    --config-file     File to write (Maven/sbt only). Defaults to ~/.m2/settings.xml for --maven and the sbt 1.x and 2.x global bases for --sbt, where it replaces every file --sbt writes.
    --docker          Configure Docker to authenticate against the registry. Writes to $DOCKER_CONFIG, or ~/.docker when it is unset.
    --duration        How long the exchanged token should remain valid. Ignored for --docker. (15m0s)
    --gradle          Configure Gradle to authenticate against the registry. Writes to ~/.gradle/gradle.properties.
    -h --help         Show help for this command.
    --hostname        Gitlab hostname to request the token from. Defaults to the configured GitLab instance.
    --maven           Configure Maven to authenticate against the registry. Writes to ~/.m2/settings.xml.
    --npm             Configure npm to authenticate against the registry. Writes to ~/.npmrc.
    --registry        Registry to authenticate against. For --docker, a bare hostname; for others, typically a URL.
    --registry-alias  Alias/Id to register the registry under (Maven/Gradle only). Defaults to a name derived from --registry.
    --sbt             Configure sbt to authenticate against the registry. Writes credentials.sbt to the sbt 1.x and 2.x global bases.
    --yarn            Configure Yarn 2 or later to authenticate against the registry. Writes to ~/.yarnrc.yml. For Yarn 1, use --npm.

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
