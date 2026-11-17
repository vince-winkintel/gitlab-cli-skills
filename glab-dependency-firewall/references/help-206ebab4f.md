# Captured glab-dependency-firewall help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab dependency-firewall

<!-- help-capture: 206ebab4f:37d4b91bf678 -->

````text

  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  Each package manager command, like `glab dependency-firewall npm`, runs the package manager binary and forwards every
  argument to it verbatim. While the package manager runs, the command:

  1. Starts a local proxy and routes the package manager's HTTPS traffic through it.
  1. Reads the name and version of each package the package manager downloads or publishes.
  1. Asks GitLab to evaluate the package against the policies for the project in your Git remote.
  1. Refuses blocked packages with a `403` response that gives the block reason, and lets allowed and warned packages
  through.
  1. Records blocked and warned packages in `.gitlab/df/ci-log.json` and prints a summary.

  When the package manager finishes, the command prints a summary of the packages that matched your policies. A `✖`
  marks a blocked package, and a `▲` marks a package with a warning. If no package matched, the command prints no
  summary. A run with at least one blocked package prints the summary to standard error. A run with only warnings prints
  it to standard output.

  Evaluation results are cached for the length of a run, so a package that appears many times in a dependency tree is
  evaluated once.

  If GitLab can't evaluate a package, the command blocks it. If the Dependency Firewall isn't evaluating the project,
  the command allows every package.

  The command does not change your registry configuration. For the length of the run, it sets environment variables that
  route the package manager's traffic through the proxy and make the package manager trust the proxy certificate. Your
  existing CA bundles stay trusted.

  To reach package registries, the proxy uses the outbound proxy in `HTTPS_PROXY`, including any credentials in its URL.
  For plain-HTTP registries it uses `HTTP_PROXY` instead, when that's set. For npm and pnpm, `HTTPS_PROXY` takes
  precedence over `HTTP_PROXY` for plain-HTTP registries too, matching those tools. It connects directly to the hosts
  listed in `NO_PROXY`. The `proxy` setting in your glab configuration applies only to GitLab API calls.

  If an `https://` outbound proxy requires a client certificate, the proxy presents the certificate in the `client_cert`
  setting for your GitLab host to it. Package registries never receive that certificate, and module downloads by `glab
  dependency-firewall go` don't present it.

  Some package managers have proxy environment variables of their own, such as `npm_config_https_proxy`,
  `YARN_HTTPS_PROXY`, `PIP_PROXY`, and `CARGO_HTTP_PROXY`. The proxy reads those variables first, so for those package
  managers the outbound proxy can differ from `HTTPS_PROXY` and `HTTP_PROXY`. A proxy from Yarn's or pip's own settings
  also applies to hosts in `NO_PROXY`, as it does in those tools.

  For npm, Yarn, pip, pipenv, and cargo, the proxy also reads the same settings from your user and global config files,
  such as `~/.npmrc`, `~/.yarnrc`, `~/.yarnrc.yml`, `pip.conf`, and `$CARGO_HOME/config.toml`. For Maven and Gradle, it
  reads the proxy settings in your user and global config files first, such as `~/.m2/settings.xml` and
  `~/.gradle/gradle.properties`. It doesn't read proxy settings from files inside the project, such as a `.npmrc` or
  `.cargo/config.toml` in the repository, or a user or global config file stored there. Outside a Git repository, the
  working directory and everything under it count as the project.

  A proxy from Maven's or Gradle's settings also applies to hosts in `NO_PROXY`, as it does in those tools, but not to
  the hosts in its `nonProxyHosts` or `http.nonProxyHosts` setting. Maven proxy passwords encrypted with `settings-
  security.xml` are not supported.

  Connections to package registries trust the system certificates, the certificate in the `ca_cert` setting for your
  GitLab host, and the CA bundles in `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `PIP_CERT`, `TWINE_CERT`,
  `NODE_EXTRA_CA_CERTS`, `BUNDLE_SSL_CA_CERT`, and `CARGO_HTTP_CAINFO`. GitLab API calls trust only the system
  certificates and `ca_cert`, so if your outbound proxy uses a private certificate authority, set `ca_cert` to that CA
  to cover both. `glab dependency-firewall go` uses the same outbound proxy and certificates for module downloads from a
  module proxy. On macOS, on Windows, and when only `SSL_CERT_DIR` is set, `go` keeps its own trust for them. Modules
  that `go` fetches directly from version control use the certificate and proxy settings of `go` and `git`.

  Maven and Gradle registry connections also trust the JVM truststore set with `-Djavax.net.ssl.trustStore` in
  `MAVEN_OPTS`, `GRADLE_OPTS`, `JAVA_OPTS`, `JAVA_TOOL_OPTIONS`, `JDK_JAVA_OPTIONS`, or `.mvn/jvm.config`. Without that
  option, they trust the default truststore of the JDK in `JAVA_HOME`. When the option names a file that does not exist
  or cannot be opened, they trust that JDK's `cacerts` instead, as the JVM does. Only PKCS#12 truststores are read. When
  the command opens a truststore that one of these options names but cannot use it, for example a JKS truststore, it
  prints a warning. A JDK default truststore in JKS format, which JDK 17 and earlier ship, is skipped without a warning.

  Maven registry connections also trust a truststore set with `-Djavax.net.ssl.trustStore` in the `mvn` arguments,
  `MAVEN_ARGS`, or `.mvn/maven.config`, unless one of the options above sets the same property, as on Maven 4. On Maven
  3, such an option replaces the truststore the command gives Maven, so Maven cannot trust the proxy and the run fails.
  On the `gradle` command line, it does the same to Gradle. The command warns in both cases. Set it in `MAVEN_OPTS` or
  `GRADLE_OPTS` instead.

  A truststore set in `_JAVA_OPTIONS`, or for Maven in `MAVEN_DEBUG_OPTS` or, on Maven 4, `.mvn/jvm.config`, replaces
  the truststore the command gives Maven or Gradle, so they cannot trust the proxy and the run fails. Set it in
  `MAVEN_OPTS` or `GRADLE_OPTS` instead. The command warns about `_JAVA_OPTIONS` and `MAVEN_DEBUG_OPTS`.

  The command writes `.gitlab/df/ci-log.json` to the working directory on every run, including local runs. Add
  `.gitlab/df/` to your `.gitignore` file.

  To run a package manager command in a GitLab CI/CD job, set `GLAB_ENABLE_CI_AUTOLOGIN` to `true` so the command signs
  in with the CI/CD job token. When the firewall blocks a package, the install fails, and so does the job. For more
  information, see CI/CD auto-login.

  ```yaml
  install:
    variables:
      GLAB_ENABLE_CI_AUTOLOGIN: "true"
    script:
      - glab dependency-firewall npm ci
  ```

  Package manager commands exit with the following codes:

  | Exit code | Meaning |
  |-----------|---------|
  | The package manager exit code | The package manager ran and exited. |
  | `1` | The package manager was not found on your `PATH` or could not start. |
  | `130` | The run was interrupted or stopped, for example, with Control+C or when a CI/CD job is canceled. |

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall <command> [command] [--flags]

  COMMANDS

    bundle <bundle args>           Run Bundler through the GitLab Dependency Firewall. (BETA)
    cargo <cargo args>             Run Cargo through the GitLab Dependency Firewall. (BETA)
    ci-summary                     Summarize Dependency Firewall activity from the CI log. (BETA)
    gem <gem args>                 Run gem through the GitLab Dependency Firewall. (BETA)
    go <go args>                   Run go through the GitLab Dependency Firewall. (BETA)
    gradle <gradle args>           Run Gradle through the GitLab Dependency Firewall. (BETA)
    job-proxy <command> [command]  Run one Dependency Firewall proxy for a whole CI/CD job. (EXPERIMENTAL)
    maven <mvn args>               Run Maven through the GitLab Dependency Firewall. (BETA)
    npm <npm args>                 Run npm through the GitLab Dependency Firewall. (BETA)
    package <purl>                 Check a package against the GitLab Dependency Firewall. (BETA)
    pip <pip args>                 Run Pip through the GitLab Dependency Firewall. (BETA)
    pipenv <pipenv args>           Run Pipenv through the GitLab Dependency Firewall. (BETA)
    pnpm <pnpm args>               Run pnpm through the GitLab Dependency Firewall. (BETA)
    poetry <poetry args>           Run Poetry through the GitLab Dependency Firewall. (BETA)
    twine <twine args>             Run Twine through the GitLab Dependency Firewall. (BETA)
    uv <uv args>                   Run uv through the GitLab Dependency Firewall. (BETA)
    yarn <yarn args>               Run Yarn through the GitLab Dependency Firewall. (BETA)

  FLAGS

    -h --help                      Show help for this command.

````

## glab dependency-firewall bundle

<!-- help-capture: 206ebab4f:3e2b230a8a04 -->

```text

  Run the Bundler binary (`bundle`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  When a bundle is already vendored, Bundler installs from `vendor/bundle/` and the firewall does not check those
  packages. Clear that directory, or run `bundle install --force`, to check them again.

  All arguments are forwarded to `bundle` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall bundle <bundle args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall bundle install

    # Update dependencies through the Dependency Firewall
    glab dependency-firewall bundle update

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab dependency-firewall cargo

<!-- help-capture: 206ebab4f:5b028a02b366 -->

```text

  Run the Cargo binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `cargo` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall cargo <cargo args> [--flags]

  EXAMPLES

    # Fetch dependencies through the Dependency Firewall
    glab dependency-firewall cargo fetch

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    CARGO_HTTP_PROXY: proxy setting for cargo. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files ($CARGO_HOME/config.toml, ~/.gitconfig). glab doesn't read proxy settings from files inside the project.

```

## glab dependency-firewall ci-summary

<!-- help-capture: 206ebab4f:1195d223aed1 -->

````text

  Read `.gitlab/df/ci-log.json` and print blocked and flagged packages
  recorded during a `glab dependency-firewall` run.

  The log is read from the current working directory and, when set, from the
  directory in `GLAB_DF_CI_LOG_DIR`. Run this command from the same directory
  as the `glab dependency-firewall` run that wrote the log, otherwise no
  activity is reported. The job-level proxy sets `GLAB_DF_CI_LOG_DIR`, so jobs
  that use it can run this command from any directory.

  To fail a CI/CD job when any package was blocked, run this command as the
  last command in `script`. This catches a block even when a package
  manager continues after a refused download. In `after_script`, the
  command prints the report but can't fail the job, because GitLab ignores
  `after_script` exit codes.

  ```yaml
  install:
    variables:
      GLAB_ENABLE_CI_AUTOLOGIN: "true"
    script:
      - glab dependency-firewall npm ci
      - glab dependency-firewall pip install -r requirements.txt
      - glab dependency-firewall ci-summary
  ```

  Entries accumulate across runs, and the command never clears them. A block
  from an earlier run keeps the command exiting with `3` until you delete
  `.gitlab/df/ci-log.json`.

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | No blocked entries in the log (allow-only or warnings). |
  | `1` | The log could not be read. |
  | `3` | At least one entry in the log is blocked. |

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall ci-summary [--flags]

  EXAMPLES

    # Show blocked and flagged packages from the last firewall run
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_CI_LOG_DIR: a directory whose .gitlab/df/ci-log.json is read in addition to the working directory's. The job-level proxy sets it.

````

## glab dependency-firewall gem

<!-- help-capture: 206ebab4f:7e160f2ed207 -->

```text

  Run the gem binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your configured sources, and does not modify `~/.gemrc` or your sources.

  All arguments are forwarded to `gem` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gem <gem args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall gem install rake

    # Download a package without installing it through the Dependency Firewall
    glab dependency-firewall gem fetch rake

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab dependency-firewall go

<!-- help-capture: 206ebab4f:2b5d995ef78b -->

```text

  Run the go binary through the GitLab Dependency Firewall. The command checks each module download against the policy
  for the current project, refuses blocked modules, and summarizes the results after the run.

  Module downloads go through a Go module proxy that the command starts on `127.0.0.1` for the run. No certificate is
  involved, so your system trust store is not changed.

  For the run, `GOPROXY` points at that proxy, `GONOPROXY` is `none`, and `GO111MODULE` is `on`, so every module
  download is checked. Private modules matched by `GOPRIVATE` are also checked, then fetched the way your configuration
  fetches them.

  If you set `GOPROXY=off`, the command keeps it.

  Allowed modules are downloaded through your configured `GOPROXY`, from the environment or the `go env` file, in list
  order and with its fallbacks. Credentials for that proxy come from your `.netrc` file, `GOAUTH`, or the URL itself. A
  `GOSUMDB` with its own URL is reached through the proxy the command starts; credentials for that URL must be in the
  URL itself, because `.netrc` and `GOAUTH` apply only to `GOPROXY`.

  The command checks only modules that `go` downloads during the run:

  - Modules already in your module cache are not checked. In CI, point `GOMODCACHE` at an empty directory to check every
  module.
  - Vendored code and `replace` directives that point at a local path are not checked.
  - Go toolchain downloads are not checked by policy. `go` verifies them against the checksum database.

  Module paths and versions, including private ones, are sent to the policy API and written to `.gitlab/df/ci-log.json`.
  CI jobs that upload that file publish them with the job's artifacts.

  Tests that make HTTPS requests can fail certificate checks under this command. Run `go test` outside the firewall if
  your tests reach the network.

  All arguments are forwarded to `go` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall go <go args> [--flags]

  EXAMPLES

    # Download modules through the Dependency Firewall
    glab dependency-firewall go mod download

    # Add a dependency, checking it against the policy first
    glab dependency-firewall go get github.com/pkg/errors@v0.9.1

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    NO_PROXY: hosts glab reaches directly instead of through HTTPS_PROXY.

```

## glab dependency-firewall gradle

<!-- help-capture: 206ebab4f:da87bf72afc6 -->

```text

  Run the Gradle binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  The command runs `gradle` from your `PATH`. The Gradle Wrapper (`./gradlew`) is not supported.

  Gradle does not download artifacts already cached in `~/.gradle/caches/`, so the firewall does not check them. Clear
  the cache to check them again.

  All arguments are forwarded to `gradle` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gradle <gradle args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall gradle build

    # List dependencies through the Dependency Firewall
    glab dependency-firewall gradle dependencies

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    glab reads the proxy settings for gradle from your user and global config files first ($GRADLE_USER_HOME/gradle.properties, the Gradle installation's gradle.properties), so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab doesn't read proxy settings from files inside the project. glab also reads them from -D options on the gradle command line.

```

## glab dependency-firewall job-proxy

<!-- help-capture: 206ebab4f:7e7612e878a2 -->

```text

  Run a single Dependency Firewall inspection proxy for the length of a CI/CD job and route every tool in the job
  through it, instead of wrapping each package-manager command with `glab dependency-firewall npm` and the like.

  Start it once at the beginning of the job, in `before_script`, and evaluate its output with `eval`. The output sets
  the environment variables that route the job's package managers through the proxy and make them trust its certificate.

  The proxy checks each package the job downloads or publishes against the policy for the current project, refuses
  blocked packages, and records blocked and flagged packages in `.gitlab/df/ci-log.json`. Run `glab dependency-firewall
  ci-summary` as the last command in `script`, not in `after_script`, to fail the job when a package was blocked. GitLab
  ignores the exit code of `after_script`.

  Unlike the per-command wrappers, the job-level proxy also covers tools that are not package managers (for example a
  raw `curl` of a tarball), because the whole job's HTTP and HTTPS traffic is routed through it. Traffic that isn't a
  package download, such as a call to a service container, is forwarded unchanged.

  The command preserves your existing configuration. It keeps your `NO_PROXY` and, when a corporate egress proxy is
  configured through `HTTPS_PROXY`, chains to it. It adds the proxy certificate to your trust rather than replacing it:
  it installs the certificate into the system trust store and, for tools that read a CA bundle instead, writes a bundle
  that is your existing trust plus the proxy certificate.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall job-proxy <command> [command] [--flags]

  COMMANDS

    start      Start the job-level proxy and print shell exports to route the job through it.
    stop       Stop the job-level proxy started by `job-proxy start`.

  FLAGS

    -h --help  Show help for this command.

```

## glab dependency-firewall job-proxy serve

<!-- help-capture: 206ebab4f:044b6fc8d56e -->

```text

  Run the job-level proxy in the foreground (internal).

  USAGE

    glab dependency-firewall job-proxy serve [--flags]

  FLAGS

    -h --help    Show help for this command.
    --state-dir  Directory for the proxy's runtime state.

```

## glab dependency-firewall job-proxy start

<!-- help-capture: 206ebab4f:b9e78a8157e1 -->

```text

  Start the job-level Dependency Firewall proxy as a background process and print `export` lines that route the current
  shell through it. Evaluate the output so the exports apply to the rest of the job.

  If the proxy cannot start, the command prints `false`, so the `eval` fails and a CI/CD job (which runs with `set -e`)
  stops instead of running without the firewall.


  USAGE

    glab dependency-firewall job-proxy start [--flags]

  EXAMPLES

    # In before_script: route the rest of the CI/CD job through the proxy
    eval "$(glab dependency-firewall job-proxy start)"

    # As the last command in script: fail the job if a package was blocked
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory for the proxy's runtime state (address, pid, CA). Set it to pin a known location; otherwise start creates a fresh per-user directory and exports this variable so `job-proxy stop` finds the same proxy.

```

## glab dependency-firewall job-proxy stop

<!-- help-capture: 206ebab4f:f2e6b963965f -->

```text

  Stop the job-level Dependency Firewall proxy that `job-proxy start` started in this shell. You do not usually need it
  in a CI/CD job, because the proxy stops when the job's container stops.


  USAGE

    glab dependency-firewall job-proxy stop [--flags]

  EXAMPLES

    # Stop the proxy before the job ends
    glab dependency-firewall job-proxy stop

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory holding the proxy's runtime state, as exported by `job-proxy start`. stop requires it to find the proxy to stop.

```

## glab dependency-firewall maven

<!-- help-capture: 206ebab4f:2f06891ef987 -->

```text

  Run the Maven binary (`mvn`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  The command checks `.jar`, `.pom`, `.aar`, and `.war` files, including timestamped snapshot files. It does not check
  checksum and signature files (`.md5`, `.sha1`, `.sha256`, `.sha512`, and `.asc`).

  The command runs `mvn` from your `PATH`. The Maven Wrapper (`./mvnw`) is not supported.

  Maven does not download artifacts already cached in `~/.m2/repository/`, so the firewall does not check them. Clear
  the cache to check them again.

  All arguments are forwarded to `mvn` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall maven <mvn args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall maven verify

    # Resolve dependencies through the Dependency Firewall
    glab dependency-firewall maven dependency:resolve

    # Deploy a project through the Dependency Firewall
    glab dependency-firewall maven deploy

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    glab reads the proxy settings for maven from your user and global config files first (~/.m2/settings.xml, ${maven.home}/conf/settings.xml), so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab doesn't read proxy settings from files inside the project. glab doesn't support proxy passwords encrypted with settings-security.xml.

```

## glab dependency-firewall npm

<!-- help-capture: 206ebab4f:3521cb008802 -->

```text

  Run the npm binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to npm verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall npm <npm args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall npm install

    # Install a package through the Dependency Firewall
    glab dependency-firewall npm install left-pad

    # Clean install from the lockfile through the Dependency Firewall
    glab dependency-firewall npm ci

    # Publish a package through the Dependency Firewall
    glab dependency-firewall npm publish

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries, plain-HTTP registries included. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries when HTTPS_PROXY is unset.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    npm_config_https_proxy, npm_config_proxy: proxy settings for npm. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (~/.npmrc, $PREFIX/etc/npmrc). glab doesn't read proxy settings from files inside the project.

```

## glab dependency-firewall package

<!-- help-capture: 206ebab4f:904550aae7d3 -->

```text

  Check a single package coordinate against the GitLab Dependency Firewall policy for the current project and report the
  outcome (allow, warning, blocked). No package manager binary is required.

  Supported package URL (PURL) types are `npm`, `pypi`, `maven`, `gem`, `nuget`, `cargo`, and `golang`. The PURL must
  include a version, for example `pkg:npm/left-pad@1.3.0`. For `golang`, the module path keeps its case, for example
  `pkg:golang/github.com/BurntSushi/toml@v1.4.0`.

  An allowed package prints one line, for example, `left-pad@1.3.0: allowed by the Dependency Firewall.` A warned or
  blocked package prints the same summary as the package manager commands.

  This command does not write to the CI log at `.gitlab/df/ci-log.json`, so `glab dependency-firewall ci-summary` does
  not include its result.

  Exit codes:

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | Allowed or warned, or the Dependency Firewall is not evaluating the project. |
  | `1` | The PURL is invalid or has no version, the project or credentials can't be resolved, or the request to GitLab
  failed. |
  | `3` | Blocked. |

  An exit code of `0` does not always mean GitLab checked the package. If the Dependency Firewall is not evaluating the
  project, the command prints a line that ends with `the Dependency Firewall is not evaluating this project; allowing.`

  Unlike the package manager commands, this command does not block the package when the request to GitLab fails. It
  exits with `1` instead.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall package <purl> [--flags]

  EXAMPLES

    # Check an npm package version
    glab dependency-firewall package pkg:npm/left-pad@1.3.0

    # Check a PyPI package version
    glab dependency-firewall package pkg:pypi/requests@2.31.0

    # Check a Maven package version
    glab dependency-firewall package pkg:maven/org.slf4j/slf4j-api@2.0.13

    # Check a RubyGems package version
    glab dependency-firewall package pkg:gem/rails@7.1.3

    # Check a NuGet package version
    glab dependency-firewall package pkg:nuget/Newtonsoft.Json@13.0.1

    # Check a Cargo package version
    glab dependency-firewall package pkg:cargo/serde@1.0.197

    # Check a Go module version
    glab dependency-firewall package pkg:golang/github.com/pkg/errors@v0.9.1

  FLAGS

    -h --help  Show help for this command.

```

## glab dependency-firewall pip

<!-- help-capture: 206ebab4f:635c469dfb44 -->

```text

  Run the Pip binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `pip` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pip <pip args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pip install requests

    # Install from a requirements file through the Dependency Firewall
    glab dependency-firewall pip install -r requirements.txt

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    PIP_PROXY: proxy setting for pip. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (pip.conf, $PIP_CONFIG_FILE). glab doesn't read proxy settings from files inside the project.

```

## glab dependency-firewall pipenv

<!-- help-capture: 206ebab4f:c38c00422aed -->

```text

  Run the Pipenv binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `pipenv` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pipenv <pipenv args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pipenv install requests

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    PIP_PROXY: proxy setting for pipenv. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (pip.conf, $PIP_CONFIG_FILE). glab doesn't read proxy settings from files inside the project.

```

## glab dependency-firewall pnpm

<!-- help-capture: 206ebab4f:7652bd8e7d4d -->

```text

  Run the pnpm binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `pnpm` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pnpm <pnpm args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall pnpm install

    # Add a package through the Dependency Firewall
    glab dependency-firewall pnpm add left-pad

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries, plain-HTTP registries included. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries when HTTPS_PROXY is unset.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    npm_config_https_proxy, npm_config_proxy: proxy settings for pnpm. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY.

```

## glab dependency-firewall poetry

<!-- help-capture: 206ebab4f:cefb8550a366 -->

```text

  Run the Poetry binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `poetry` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall poetry <poetry args> [--flags]

  EXAMPLES

    # Add a package through the Dependency Firewall
    glab dependency-firewall poetry add requests

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall poetry install

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab dependency-firewall session

<!-- help-capture: 206ebab4f:95e1e7eb2e4e -->

```text

  Run a single Dependency Firewall inspection proxy for the length of a CI/CD job and route every tool in the job
  through it, instead of wrapping each package-manager command with `glab dependency-firewall npm` and the like.

  Start it once at the beginning of the job, in `before_script`, and evaluate its output with `eval`. The output sets
  the environment variables that route the job's package managers through the proxy and make them trust its certificate.

  The proxy checks each package the job downloads or publishes against the policy for the current project, refuses
  blocked packages, and records blocked and flagged packages in `.gitlab/df/ci-log.json`. Run `glab dependency-firewall
  ci-summary` as the last command in `script`, not in `after_script`, to fail the job when a package was blocked. GitLab
  ignores the exit code of `after_script`.

  Unlike the per-command wrappers, the job-level proxy also covers tools that are not package managers (for example a
  raw `curl` of a tarball), because the whole job's HTTP and HTTPS traffic is routed through it. Traffic that isn't a
  package download, such as a call to a service container, is forwarded unchanged.

  The command preserves your existing configuration. It keeps your `NO_PROXY` and, when a corporate egress proxy is
  configured through `HTTPS_PROXY`, chains to it. It adds the proxy certificate to your trust rather than replacing it:
  it installs the certificate into the system trust store and, for tools that read a CA bundle instead, writes a bundle
  that is your existing trust plus the proxy certificate.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall job-proxy <command> [command] [--flags]

  COMMANDS

    start      Start the job-level proxy and print shell exports to route the job through it.
    stop       Stop the job-level proxy started by `job-proxy start`.

  FLAGS

    -h --help  Show help for this command.

```

## glab dependency-firewall session serve

<!-- help-capture: 206ebab4f:c5e2aa9e5024 -->

```text

  Run the job-level proxy in the foreground (internal).

  USAGE

    glab dependency-firewall job-proxy serve [--flags]

  FLAGS

    -h --help    Show help for this command.
    --state-dir  Directory for the proxy's runtime state.

```

## glab dependency-firewall session start

<!-- help-capture: 206ebab4f:57d45dafc9d6 -->

```text

  Start the job-level Dependency Firewall proxy as a background process and print `export` lines that route the current
  shell through it. Evaluate the output so the exports apply to the rest of the job.

  If the proxy cannot start, the command prints `false`, so the `eval` fails and a CI/CD job (which runs with `set -e`)
  stops instead of running without the firewall.


  USAGE

    glab dependency-firewall job-proxy start [--flags]

  EXAMPLES

    # In before_script: route the rest of the CI/CD job through the proxy
    eval "$(glab dependency-firewall job-proxy start)"

    # As the last command in script: fail the job if a package was blocked
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory for the proxy's runtime state (address, pid, CA). Set it to pin a known location; otherwise start creates a fresh per-user directory and exports this variable so `job-proxy stop` finds the same proxy.

```

## glab dependency-firewall session stop

<!-- help-capture: 206ebab4f:3e6c836929ab -->

```text

  Stop the job-level Dependency Firewall proxy that `job-proxy start` started in this shell. You do not usually need it
  in a CI/CD job, because the proxy stops when the job's container stops.


  USAGE

    glab dependency-firewall job-proxy stop [--flags]

  EXAMPLES

    # Stop the proxy before the job ends
    glab dependency-firewall job-proxy stop

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory holding the proxy's runtime state, as exported by `job-proxy start`. stop requires it to find the proxy to stop.

```

## glab dependency-firewall twine

<!-- help-capture: 206ebab4f:6760415bd06a -->

```text

  Run the Twine binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `twine` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall twine <twine args> [--flags]

  EXAMPLES

    # Upload a package through the Dependency Firewall
    glab dependency-firewall twine upload dist/*

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab dependency-firewall uv

<!-- help-capture: 206ebab4f:cf0eb6457a01 -->

```text

  Run the uv binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `uv` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall uv <uv args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall uv pip install requests

    # Sync the project environment through the Dependency Firewall
    glab dependency-firewall uv sync

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab dependency-firewall yarn

<!-- help-capture: 206ebab4f:f346f7918448 -->

```text

  Run the yarn binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  This command requires Yarn 3.2 or later, or Yarn Classic (1.x). It refuses Yarn 2.x through 3.1, because those
  versions cannot stop a `.yarnrc.yml` file from routing registry traffic around the firewall. During the run, Yarn
  ignores per-host `networkSettings` from every `.yarnrc.yml` file, so every request goes through the firewall.

  All arguments are forwarded to `yarn` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall yarn <yarn args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall yarn install

    # Add a package through the Dependency Firewall
    glab dependency-firewall yarn add left-pad

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    YARN_HTTPS_PROXY, YARN_PROXY, npm_config_https_proxy, npm_config_proxy: proxy settings for yarn. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (~/.yarnrc, ~/.npmrc, $PREFIX/etc/yarnrc, $PREFIX/etc/npmrc, ~/.yarnrc.yml). glab doesn't read proxy settings from files inside the project. For Yarn 2 and later, glab reads only YARN_HTTPS_PROXY and ~/.yarnrc.yml.

```

## glab df

<!-- help-capture: 206ebab4f:48e94568c0c6 -->

````text

  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  Each package manager command, like `glab dependency-firewall npm`, runs the package manager binary and forwards every
  argument to it verbatim. While the package manager runs, the command:

  1. Starts a local proxy and routes the package manager's HTTPS traffic through it.
  1. Reads the name and version of each package the package manager downloads or publishes.
  1. Asks GitLab to evaluate the package against the policies for the project in your Git remote.
  1. Refuses blocked packages with a `403` response that gives the block reason, and lets allowed and warned packages
  through.
  1. Records blocked and warned packages in `.gitlab/df/ci-log.json` and prints a summary.

  When the package manager finishes, the command prints a summary of the packages that matched your policies. A `✖`
  marks a blocked package, and a `▲` marks a package with a warning. If no package matched, the command prints no
  summary. A run with at least one blocked package prints the summary to standard error. A run with only warnings prints
  it to standard output.

  Evaluation results are cached for the length of a run, so a package that appears many times in a dependency tree is
  evaluated once.

  If GitLab can't evaluate a package, the command blocks it. If the Dependency Firewall isn't evaluating the project,
  the command allows every package.

  The command does not change your registry configuration. For the length of the run, it sets environment variables that
  route the package manager's traffic through the proxy and make the package manager trust the proxy certificate. Your
  existing CA bundles stay trusted.

  To reach package registries, the proxy uses the outbound proxy in `HTTPS_PROXY`, including any credentials in its URL.
  For plain-HTTP registries it uses `HTTP_PROXY` instead, when that's set. For npm and pnpm, `HTTPS_PROXY` takes
  precedence over `HTTP_PROXY` for plain-HTTP registries too, matching those tools. It connects directly to the hosts
  listed in `NO_PROXY`. The `proxy` setting in your glab configuration applies only to GitLab API calls.

  If an `https://` outbound proxy requires a client certificate, the proxy presents the certificate in the `client_cert`
  setting for your GitLab host to it. Package registries never receive that certificate, and module downloads by `glab
  dependency-firewall go` don't present it.

  Some package managers have proxy environment variables of their own, such as `npm_config_https_proxy`,
  `YARN_HTTPS_PROXY`, `PIP_PROXY`, and `CARGO_HTTP_PROXY`. The proxy reads those variables first, so for those package
  managers the outbound proxy can differ from `HTTPS_PROXY` and `HTTP_PROXY`. A proxy from Yarn's or pip's own settings
  also applies to hosts in `NO_PROXY`, as it does in those tools.

  For npm, Yarn, pip, pipenv, and cargo, the proxy also reads the same settings from your user and global config files,
  such as `~/.npmrc`, `~/.yarnrc`, `~/.yarnrc.yml`, `pip.conf`, and `$CARGO_HOME/config.toml`. For Maven and Gradle, it
  reads the proxy settings in your user and global config files first, such as `~/.m2/settings.xml` and
  `~/.gradle/gradle.properties`. It doesn't read proxy settings from files inside the project, such as a `.npmrc` or
  `.cargo/config.toml` in the repository, or a user or global config file stored there. Outside a Git repository, the
  working directory and everything under it count as the project.

  A proxy from Maven's or Gradle's settings also applies to hosts in `NO_PROXY`, as it does in those tools, but not to
  the hosts in its `nonProxyHosts` or `http.nonProxyHosts` setting. Maven proxy passwords encrypted with `settings-
  security.xml` are not supported.

  Connections to package registries trust the system certificates, the certificate in the `ca_cert` setting for your
  GitLab host, and the CA bundles in `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `PIP_CERT`, `TWINE_CERT`,
  `NODE_EXTRA_CA_CERTS`, `BUNDLE_SSL_CA_CERT`, and `CARGO_HTTP_CAINFO`. GitLab API calls trust only the system
  certificates and `ca_cert`, so if your outbound proxy uses a private certificate authority, set `ca_cert` to that CA
  to cover both. `glab dependency-firewall go` uses the same outbound proxy and certificates for module downloads from a
  module proxy. On macOS, on Windows, and when only `SSL_CERT_DIR` is set, `go` keeps its own trust for them. Modules
  that `go` fetches directly from version control use the certificate and proxy settings of `go` and `git`.

  Maven and Gradle registry connections also trust the JVM truststore set with `-Djavax.net.ssl.trustStore` in
  `MAVEN_OPTS`, `GRADLE_OPTS`, `JAVA_OPTS`, `JAVA_TOOL_OPTIONS`, `JDK_JAVA_OPTIONS`, or `.mvn/jvm.config`. Without that
  option, they trust the default truststore of the JDK in `JAVA_HOME`. When the option names a file that does not exist
  or cannot be opened, they trust that JDK's `cacerts` instead, as the JVM does. Only PKCS#12 truststores are read. When
  the command opens a truststore that one of these options names but cannot use it, for example a JKS truststore, it
  prints a warning. A JDK default truststore in JKS format, which JDK 17 and earlier ship, is skipped without a warning.

  Maven registry connections also trust a truststore set with `-Djavax.net.ssl.trustStore` in the `mvn` arguments,
  `MAVEN_ARGS`, or `.mvn/maven.config`, unless one of the options above sets the same property, as on Maven 4. On Maven
  3, such an option replaces the truststore the command gives Maven, so Maven cannot trust the proxy and the run fails.
  On the `gradle` command line, it does the same to Gradle. The command warns in both cases. Set it in `MAVEN_OPTS` or
  `GRADLE_OPTS` instead.

  A truststore set in `_JAVA_OPTIONS`, or for Maven in `MAVEN_DEBUG_OPTS` or, on Maven 4, `.mvn/jvm.config`, replaces
  the truststore the command gives Maven or Gradle, so they cannot trust the proxy and the run fails. Set it in
  `MAVEN_OPTS` or `GRADLE_OPTS` instead. The command warns about `_JAVA_OPTIONS` and `MAVEN_DEBUG_OPTS`.

  The command writes `.gitlab/df/ci-log.json` to the working directory on every run, including local runs. Add
  `.gitlab/df/` to your `.gitignore` file.

  To run a package manager command in a GitLab CI/CD job, set `GLAB_ENABLE_CI_AUTOLOGIN` to `true` so the command signs
  in with the CI/CD job token. When the firewall blocks a package, the install fails, and so does the job. For more
  information, see CI/CD auto-login.

  ```yaml
  install:
    variables:
      GLAB_ENABLE_CI_AUTOLOGIN: "true"
    script:
      - glab dependency-firewall npm ci
  ```

  Package manager commands exit with the following codes:

  | Exit code | Meaning |
  |-----------|---------|
  | The package manager exit code | The package manager ran and exited. |
  | `1` | The package manager was not found on your `PATH` or could not start. |
  | `130` | The run was interrupted or stopped, for example, with Control+C or when a CI/CD job is canceled. |

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall <command> [command] [--flags]

  COMMANDS

    bundle <bundle args>           Run Bundler through the GitLab Dependency Firewall. (BETA)
    cargo <cargo args>             Run Cargo through the GitLab Dependency Firewall. (BETA)
    ci-summary                     Summarize Dependency Firewall activity from the CI log. (BETA)
    gem <gem args>                 Run gem through the GitLab Dependency Firewall. (BETA)
    go <go args>                   Run go through the GitLab Dependency Firewall. (BETA)
    gradle <gradle args>           Run Gradle through the GitLab Dependency Firewall. (BETA)
    job-proxy <command> [command]  Run one Dependency Firewall proxy for a whole CI/CD job. (EXPERIMENTAL)
    maven <mvn args>               Run Maven through the GitLab Dependency Firewall. (BETA)
    npm <npm args>                 Run npm through the GitLab Dependency Firewall. (BETA)
    package <purl>                 Check a package against the GitLab Dependency Firewall. (BETA)
    pip <pip args>                 Run Pip through the GitLab Dependency Firewall. (BETA)
    pipenv <pipenv args>           Run Pipenv through the GitLab Dependency Firewall. (BETA)
    pnpm <pnpm args>               Run pnpm through the GitLab Dependency Firewall. (BETA)
    poetry <poetry args>           Run Poetry through the GitLab Dependency Firewall. (BETA)
    twine <twine args>             Run Twine through the GitLab Dependency Firewall. (BETA)
    uv <uv args>                   Run uv through the GitLab Dependency Firewall. (BETA)
    yarn <yarn args>               Run Yarn through the GitLab Dependency Firewall. (BETA)

  FLAGS

    -h --help                      Show help for this command.

````

## glab df bundle

<!-- help-capture: 206ebab4f:a67ef7b4a8d1 -->

```text

  Run the Bundler binary (`bundle`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  When a bundle is already vendored, Bundler installs from `vendor/bundle/` and the firewall does not check those
  packages. Clear that directory, or run `bundle install --force`, to check them again.

  All arguments are forwarded to `bundle` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall bundle <bundle args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall bundle install

    # Update dependencies through the Dependency Firewall
    glab dependency-firewall bundle update

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab df cargo

<!-- help-capture: 206ebab4f:45065b90f548 -->

```text

  Run the Cargo binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `cargo` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall cargo <cargo args> [--flags]

  EXAMPLES

    # Fetch dependencies through the Dependency Firewall
    glab dependency-firewall cargo fetch

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    CARGO_HTTP_PROXY: proxy setting for cargo. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files ($CARGO_HOME/config.toml, ~/.gitconfig). glab doesn't read proxy settings from files inside the project.

```

## glab df ci-summary

<!-- help-capture: 206ebab4f:8606007a9a84 -->

````text

  Read `.gitlab/df/ci-log.json` and print blocked and flagged packages
  recorded during a `glab dependency-firewall` run.

  The log is read from the current working directory and, when set, from the
  directory in `GLAB_DF_CI_LOG_DIR`. Run this command from the same directory
  as the `glab dependency-firewall` run that wrote the log, otherwise no
  activity is reported. The job-level proxy sets `GLAB_DF_CI_LOG_DIR`, so jobs
  that use it can run this command from any directory.

  To fail a CI/CD job when any package was blocked, run this command as the
  last command in `script`. This catches a block even when a package
  manager continues after a refused download. In `after_script`, the
  command prints the report but can't fail the job, because GitLab ignores
  `after_script` exit codes.

  ```yaml
  install:
    variables:
      GLAB_ENABLE_CI_AUTOLOGIN: "true"
    script:
      - glab dependency-firewall npm ci
      - glab dependency-firewall pip install -r requirements.txt
      - glab dependency-firewall ci-summary
  ```

  Entries accumulate across runs, and the command never clears them. A block
  from an earlier run keeps the command exiting with `3` until you delete
  `.gitlab/df/ci-log.json`.

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | No blocked entries in the log (allow-only or warnings). |
  | `1` | The log could not be read. |
  | `3` | At least one entry in the log is blocked. |

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall ci-summary [--flags]

  EXAMPLES

    # Show blocked and flagged packages from the last firewall run
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_CI_LOG_DIR: a directory whose .gitlab/df/ci-log.json is read in addition to the working directory's. The job-level proxy sets it.

````

## glab df gem

<!-- help-capture: 206ebab4f:80811ebf235e -->

```text

  Run the gem binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your configured sources, and does not modify `~/.gemrc` or your sources.

  All arguments are forwarded to `gem` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gem <gem args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall gem install rake

    # Download a package without installing it through the Dependency Firewall
    glab dependency-firewall gem fetch rake

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab df go

<!-- help-capture: 206ebab4f:100d136ce70f -->

```text

  Run the go binary through the GitLab Dependency Firewall. The command checks each module download against the policy
  for the current project, refuses blocked modules, and summarizes the results after the run.

  Module downloads go through a Go module proxy that the command starts on `127.0.0.1` for the run. No certificate is
  involved, so your system trust store is not changed.

  For the run, `GOPROXY` points at that proxy, `GONOPROXY` is `none`, and `GO111MODULE` is `on`, so every module
  download is checked. Private modules matched by `GOPRIVATE` are also checked, then fetched the way your configuration
  fetches them.

  If you set `GOPROXY=off`, the command keeps it.

  Allowed modules are downloaded through your configured `GOPROXY`, from the environment or the `go env` file, in list
  order and with its fallbacks. Credentials for that proxy come from your `.netrc` file, `GOAUTH`, or the URL itself. A
  `GOSUMDB` with its own URL is reached through the proxy the command starts; credentials for that URL must be in the
  URL itself, because `.netrc` and `GOAUTH` apply only to `GOPROXY`.

  The command checks only modules that `go` downloads during the run:

  - Modules already in your module cache are not checked. In CI, point `GOMODCACHE` at an empty directory to check every
  module.
  - Vendored code and `replace` directives that point at a local path are not checked.
  - Go toolchain downloads are not checked by policy. `go` verifies them against the checksum database.

  Module paths and versions, including private ones, are sent to the policy API and written to `.gitlab/df/ci-log.json`.
  CI jobs that upload that file publish them with the job's artifacts.

  Tests that make HTTPS requests can fail certificate checks under this command. Run `go test` outside the firewall if
  your tests reach the network.

  All arguments are forwarded to `go` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall go <go args> [--flags]

  EXAMPLES

    # Download modules through the Dependency Firewall
    glab dependency-firewall go mod download

    # Add a dependency, checking it against the policy first
    glab dependency-firewall go get github.com/pkg/errors@v0.9.1

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    NO_PROXY: hosts glab reaches directly instead of through HTTPS_PROXY.

```

## glab df gradle

<!-- help-capture: 206ebab4f:67cc31ed10f7 -->

```text

  Run the Gradle binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  The command runs `gradle` from your `PATH`. The Gradle Wrapper (`./gradlew`) is not supported.

  Gradle does not download artifacts already cached in `~/.gradle/caches/`, so the firewall does not check them. Clear
  the cache to check them again.

  All arguments are forwarded to `gradle` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gradle <gradle args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall gradle build

    # List dependencies through the Dependency Firewall
    glab dependency-firewall gradle dependencies

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    glab reads the proxy settings for gradle from your user and global config files first ($GRADLE_USER_HOME/gradle.properties, the Gradle installation's gradle.properties), so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab doesn't read proxy settings from files inside the project. glab also reads them from -D options on the gradle command line.

```

## glab df job-proxy

<!-- help-capture: 206ebab4f:6b25db2369c9 -->

```text

  Run a single Dependency Firewall inspection proxy for the length of a CI/CD job and route every tool in the job
  through it, instead of wrapping each package-manager command with `glab dependency-firewall npm` and the like.

  Start it once at the beginning of the job, in `before_script`, and evaluate its output with `eval`. The output sets
  the environment variables that route the job's package managers through the proxy and make them trust its certificate.

  The proxy checks each package the job downloads or publishes against the policy for the current project, refuses
  blocked packages, and records blocked and flagged packages in `.gitlab/df/ci-log.json`. Run `glab dependency-firewall
  ci-summary` as the last command in `script`, not in `after_script`, to fail the job when a package was blocked. GitLab
  ignores the exit code of `after_script`.

  Unlike the per-command wrappers, the job-level proxy also covers tools that are not package managers (for example a
  raw `curl` of a tarball), because the whole job's HTTP and HTTPS traffic is routed through it. Traffic that isn't a
  package download, such as a call to a service container, is forwarded unchanged.

  The command preserves your existing configuration. It keeps your `NO_PROXY` and, when a corporate egress proxy is
  configured through `HTTPS_PROXY`, chains to it. It adds the proxy certificate to your trust rather than replacing it:
  it installs the certificate into the system trust store and, for tools that read a CA bundle instead, writes a bundle
  that is your existing trust plus the proxy certificate.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall job-proxy <command> [command] [--flags]

  COMMANDS

    start      Start the job-level proxy and print shell exports to route the job through it.
    stop       Stop the job-level proxy started by `job-proxy start`.

  FLAGS

    -h --help  Show help for this command.

```

## glab df job-proxy serve

<!-- help-capture: 206ebab4f:1291d651e811 -->

```text

  Run the job-level proxy in the foreground (internal).

  USAGE

    glab dependency-firewall job-proxy serve [--flags]

  FLAGS

    -h --help    Show help for this command.
    --state-dir  Directory for the proxy's runtime state.

```

## glab df job-proxy start

<!-- help-capture: 206ebab4f:124bc8a7c28c -->

```text

  Start the job-level Dependency Firewall proxy as a background process and print `export` lines that route the current
  shell through it. Evaluate the output so the exports apply to the rest of the job.

  If the proxy cannot start, the command prints `false`, so the `eval` fails and a CI/CD job (which runs with `set -e`)
  stops instead of running without the firewall.


  USAGE

    glab dependency-firewall job-proxy start [--flags]

  EXAMPLES

    # In before_script: route the rest of the CI/CD job through the proxy
    eval "$(glab dependency-firewall job-proxy start)"

    # As the last command in script: fail the job if a package was blocked
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory for the proxy's runtime state (address, pid, CA). Set it to pin a known location; otherwise start creates a fresh per-user directory and exports this variable so `job-proxy stop` finds the same proxy.

```

## glab df job-proxy stop

<!-- help-capture: 206ebab4f:8941d94ef98e -->

```text

  Stop the job-level Dependency Firewall proxy that `job-proxy start` started in this shell. You do not usually need it
  in a CI/CD job, because the proxy stops when the job's container stops.


  USAGE

    glab dependency-firewall job-proxy stop [--flags]

  EXAMPLES

    # Stop the proxy before the job ends
    glab dependency-firewall job-proxy stop

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory holding the proxy's runtime state, as exported by `job-proxy start`. stop requires it to find the proxy to stop.

```

## glab df maven

<!-- help-capture: 206ebab4f:916415b0b5fe -->

```text

  Run the Maven binary (`mvn`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  The command checks `.jar`, `.pom`, `.aar`, and `.war` files, including timestamped snapshot files. It does not check
  checksum and signature files (`.md5`, `.sha1`, `.sha256`, `.sha512`, and `.asc`).

  The command runs `mvn` from your `PATH`. The Maven Wrapper (`./mvnw`) is not supported.

  Maven does not download artifacts already cached in `~/.m2/repository/`, so the firewall does not check them. Clear
  the cache to check them again.

  All arguments are forwarded to `mvn` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall maven <mvn args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall maven verify

    # Resolve dependencies through the Dependency Firewall
    glab dependency-firewall maven dependency:resolve

    # Deploy a project through the Dependency Firewall
    glab dependency-firewall maven deploy

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    glab reads the proxy settings for maven from your user and global config files first (~/.m2/settings.xml, ${maven.home}/conf/settings.xml), so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab doesn't read proxy settings from files inside the project. glab doesn't support proxy passwords encrypted with settings-security.xml.

```

## glab df npm

<!-- help-capture: 206ebab4f:72e00b7666dc -->

```text

  Run the npm binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to npm verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall npm <npm args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall npm install

    # Install a package through the Dependency Firewall
    glab dependency-firewall npm install left-pad

    # Clean install from the lockfile through the Dependency Firewall
    glab dependency-firewall npm ci

    # Publish a package through the Dependency Firewall
    glab dependency-firewall npm publish

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries, plain-HTTP registries included. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries when HTTPS_PROXY is unset.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    npm_config_https_proxy, npm_config_proxy: proxy settings for npm. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (~/.npmrc, $PREFIX/etc/npmrc). glab doesn't read proxy settings from files inside the project.

```

## glab df package

<!-- help-capture: 206ebab4f:6d9ef7487145 -->

```text

  Check a single package coordinate against the GitLab Dependency Firewall policy for the current project and report the
  outcome (allow, warning, blocked). No package manager binary is required.

  Supported package URL (PURL) types are `npm`, `pypi`, `maven`, `gem`, `nuget`, `cargo`, and `golang`. The PURL must
  include a version, for example `pkg:npm/left-pad@1.3.0`. For `golang`, the module path keeps its case, for example
  `pkg:golang/github.com/BurntSushi/toml@v1.4.0`.

  An allowed package prints one line, for example, `left-pad@1.3.0: allowed by the Dependency Firewall.` A warned or
  blocked package prints the same summary as the package manager commands.

  This command does not write to the CI log at `.gitlab/df/ci-log.json`, so `glab dependency-firewall ci-summary` does
  not include its result.

  Exit codes:

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | Allowed or warned, or the Dependency Firewall is not evaluating the project. |
  | `1` | The PURL is invalid or has no version, the project or credentials can't be resolved, or the request to GitLab
  failed. |
  | `3` | Blocked. |

  An exit code of `0` does not always mean GitLab checked the package. If the Dependency Firewall is not evaluating the
  project, the command prints a line that ends with `the Dependency Firewall is not evaluating this project; allowing.`

  Unlike the package manager commands, this command does not block the package when the request to GitLab fails. It
  exits with `1` instead.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall package <purl> [--flags]

  EXAMPLES

    # Check an npm package version
    glab dependency-firewall package pkg:npm/left-pad@1.3.0

    # Check a PyPI package version
    glab dependency-firewall package pkg:pypi/requests@2.31.0

    # Check a Maven package version
    glab dependency-firewall package pkg:maven/org.slf4j/slf4j-api@2.0.13

    # Check a RubyGems package version
    glab dependency-firewall package pkg:gem/rails@7.1.3

    # Check a NuGet package version
    glab dependency-firewall package pkg:nuget/Newtonsoft.Json@13.0.1

    # Check a Cargo package version
    glab dependency-firewall package pkg:cargo/serde@1.0.197

    # Check a Go module version
    glab dependency-firewall package pkg:golang/github.com/pkg/errors@v0.9.1

  FLAGS

    -h --help  Show help for this command.

```

## glab df pip

<!-- help-capture: 206ebab4f:503522212be3 -->

```text

  Run the Pip binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `pip` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pip <pip args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pip install requests

    # Install from a requirements file through the Dependency Firewall
    glab dependency-firewall pip install -r requirements.txt

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    PIP_PROXY: proxy setting for pip. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (pip.conf, $PIP_CONFIG_FILE). glab doesn't read proxy settings from files inside the project.

```

## glab df pipenv

<!-- help-capture: 206ebab4f:28f7887cd46d -->

```text

  Run the Pipenv binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `pipenv` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pipenv <pipenv args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pipenv install requests

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    PIP_PROXY: proxy setting for pipenv. glab reads it first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (pip.conf, $PIP_CONFIG_FILE). glab doesn't read proxy settings from files inside the project.

```

## glab df pnpm

<!-- help-capture: 206ebab4f:df779e1e8799 -->

```text

  Run the pnpm binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `pnpm` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pnpm <pnpm args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall pnpm install

    # Add a package through the Dependency Firewall
    glab dependency-firewall pnpm add left-pad

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries, plain-HTTP registries included. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries when HTTPS_PROXY is unset.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    npm_config_https_proxy, npm_config_proxy: proxy settings for pnpm. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY.

```

## glab df poetry

<!-- help-capture: 206ebab4f:847e2b9daac3 -->

```text

  Run the Poetry binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `poetry` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall poetry <poetry args> [--flags]

  EXAMPLES

    # Add a package through the Dependency Firewall
    glab dependency-firewall poetry add requests

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall poetry install

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab df session

<!-- help-capture: 206ebab4f:e423946c7617 -->

```text

  Run a single Dependency Firewall inspection proxy for the length of a CI/CD job and route every tool in the job
  through it, instead of wrapping each package-manager command with `glab dependency-firewall npm` and the like.

  Start it once at the beginning of the job, in `before_script`, and evaluate its output with `eval`. The output sets
  the environment variables that route the job's package managers through the proxy and make them trust its certificate.

  The proxy checks each package the job downloads or publishes against the policy for the current project, refuses
  blocked packages, and records blocked and flagged packages in `.gitlab/df/ci-log.json`. Run `glab dependency-firewall
  ci-summary` as the last command in `script`, not in `after_script`, to fail the job when a package was blocked. GitLab
  ignores the exit code of `after_script`.

  Unlike the per-command wrappers, the job-level proxy also covers tools that are not package managers (for example a
  raw `curl` of a tarball), because the whole job's HTTP and HTTPS traffic is routed through it. Traffic that isn't a
  package download, such as a call to a service container, is forwarded unchanged.

  The command preserves your existing configuration. It keeps your `NO_PROXY` and, when a corporate egress proxy is
  configured through `HTTPS_PROXY`, chains to it. It adds the proxy certificate to your trust rather than replacing it:
  it installs the certificate into the system trust store and, for tools that read a CA bundle instead, writes a bundle
  that is your existing trust plus the proxy certificate.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall job-proxy <command> [command] [--flags]

  COMMANDS

    start      Start the job-level proxy and print shell exports to route the job through it.
    stop       Stop the job-level proxy started by `job-proxy start`.

  FLAGS

    -h --help  Show help for this command.

```

## glab df session serve

<!-- help-capture: 206ebab4f:25a86fc9f2da -->

```text

  Run the job-level proxy in the foreground (internal).

  USAGE

    glab dependency-firewall job-proxy serve [--flags]

  FLAGS

    -h --help    Show help for this command.
    --state-dir  Directory for the proxy's runtime state.

```

## glab df session start

<!-- help-capture: 206ebab4f:ef7fc42b37a9 -->

```text

  Start the job-level Dependency Firewall proxy as a background process and print `export` lines that route the current
  shell through it. Evaluate the output so the exports apply to the rest of the job.

  If the proxy cannot start, the command prints `false`, so the `eval` fails and a CI/CD job (which runs with `set -e`)
  stops instead of running without the firewall.


  USAGE

    glab dependency-firewall job-proxy start [--flags]

  EXAMPLES

    # In before_script: route the rest of the CI/CD job through the proxy
    eval "$(glab dependency-firewall job-proxy start)"

    # As the last command in script: fail the job if a package was blocked
    glab dependency-firewall ci-summary

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory for the proxy's runtime state (address, pid, CA). Set it to pin a known location; otherwise start creates a fresh per-user directory and exports this variable so `job-proxy stop` finds the same proxy.

```

## glab df session stop

<!-- help-capture: 206ebab4f:124222fda4f9 -->

```text

  Stop the job-level Dependency Firewall proxy that `job-proxy start` started in this shell. You do not usually need it
  in a CI/CD job, because the proxy stops when the job's container stops.


  USAGE

    glab dependency-firewall job-proxy stop [--flags]

  EXAMPLES

    # Stop the proxy before the job ends
    glab dependency-firewall job-proxy stop

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    GLAB_DF_JOB_PROXY_STATE_DIR: directory holding the proxy's runtime state, as exported by `job-proxy start`. stop requires it to find the proxy to stop.

```

## glab df twine

<!-- help-capture: 206ebab4f:d2e0d9770f76 -->

```text

  Run the Twine binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `twine` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall twine <twine args> [--flags]

  EXAMPLES

    # Upload a package through the Dependency Firewall
    glab dependency-firewall twine upload dist/*

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab df uv

<!-- help-capture: 206ebab4f:b0e0702ea464 -->

```text

  Run the uv binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  Package names are normalized as described in PEP 503, so `Flask_Login` and `flask-login` are treated as the same
  package.

  All arguments are forwarded to `uv` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall uv <uv args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall uv pip install requests

    # Sync the project environment through the Dependency Firewall
    glab dependency-firewall uv sync

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.

```

## glab df yarn

<!-- help-capture: 206ebab4f:b80dcd3fbf65 -->

```text

  Run the yarn binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  This command requires Yarn 3.2 or later, or Yarn Classic (1.x). It refuses Yarn 2.x through 3.1, because those
  versions cannot stop a `.yarnrc.yml` file from routing registry traffic around the firewall. During the run, Yarn
  ignores per-host `networkSettings` from every `.yarnrc.yml` file, so every request goes through the firewall.

  All arguments are forwarded to `yarn` verbatim.

  This feature is in beta and might not be ready for production use.
  It might be unstable and breaking changes can occur outside of major releases.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall yarn <yarn args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall yarn install

    # Add a package through the Dependency Firewall
    glab dependency-firewall yarn add left-pad

  FLAGS

    -h --help  Show help for this command.

  ENVIRONMENT VARIABLES

    HTTPS_PROXY: outbound proxy glab uses to reach package registries. Credentials in the URL are sent to the proxy.
    HTTP_PROXY: outbound proxy for plain-HTTP registries. When it's unset, glab uses HTTPS_PROXY.
    NO_PROXY: hosts glab reaches directly instead of through an outbound proxy.
    YARN_HTTPS_PROXY, YARN_PROXY, npm_config_https_proxy, npm_config_proxy: proxy settings for yarn. glab reads them first, so the outbound proxy can differ from HTTPS_PROXY and HTTP_PROXY. glab also reads the same settings from your user and global config files (~/.yarnrc, ~/.npmrc, $PREFIX/etc/yarnrc, $PREFIX/etc/npmrc, ~/.yarnrc.yml). glab doesn't read proxy settings from files inside the project. For Yarn 2 and later, glab reads only YARN_HTTPS_PROXY and ~/.yarnrc.yml.

```

