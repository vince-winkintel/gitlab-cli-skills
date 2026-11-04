# glab dependency-firewall command reference

> **Current help capture `519ea19f7`.** Official glab v1.128.0 macOS arm64 binary; source commit `519ea19f7d3e9c701a4063f277ae27254bbafdad`; binary archive SHA-256 `541cdde6a0f706b4b69fed9fb558b421a361f63408d072d78ffdf304aee04248`. Only fences with this adjacent key use this provenance. Each complete stdout capture preserves leading spaces, blank lines, Fang uppercase headings, spelling (including `Gitlab`), examples, wrapping, and truncation; only trailing spaces/tabs are removed. Other captures retain their prior provenance and bytes. Current markers override historical unmarked labels.

## dependency-firewall

Alias: `df`

<!-- help-capture: 519ea19f7:d3264f05f7ad -->

```text

  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  Each package manager command, like `glab dependency-firewall npm`, runs the package manager binary and forwards every
  argument to it verbatim. While the package manager runs, the command:

  1. Starts a local proxy and routes the package manager's HTTPS traffic through it.
  1. Reads the name and version of each package the package manager downloads or publishes.
  1. Asks GitLab to evaluate the package against the policies for the project in your Git remote.
  1. Refuses blocked packages with a `403 Forbidden` response, and lets allowed and warned packages through.
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

  To reach package registries, the proxy uses the outbound proxy in `HTTPS_PROXY`, including any credentials in its URL,
  and connects directly to the hosts listed in `NO_PROXY`. The `proxy` setting in your glab configuration applies only
  to GitLab API calls.

  Connections to package registries trust the system certificates, the certificate in the `ca_cert` setting for your
  GitLab host, and the CA bundles in `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `PIP_CERT`, `TWINE_CERT`,
  `NODE_EXTRA_CA_CERTS`, `BUNDLE_SSL_CA_CERT`, and `CARGO_HTTP_CAINFO`. GitLab API calls trust only the system
  certificates and `ca_cert`, so if your outbound proxy uses a private certificate authority, set `ca_cert` to that CA
  to cover both. Module downloads by `glab dependency-firewall go` trust only the system certificates or
  `SSL_CERT_FILE`.

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

    bundle <bundle args>  Run Bundler through the GitLab Dependency Firewall. (BETA)
    cargo <cargo args>    Run Cargo through the GitLab Dependency Firewall. (BETA)
    ci-summary            Summarize Dependency Firewall activity from the CI log. (BETA)
    gem <gem args>        Run gem through the GitLab Dependency Firewall. (BETA)
    go <go args>          Run go through the GitLab Dependency Firewall. (BETA)
    gradle <gradle args>  Run Gradle through the GitLab Dependency Firewall. (BETA)
    maven <mvn args>      Run Maven through the GitLab Dependency Firewall. (BETA)
    npm <npm args>        Run npm through the GitLab Dependency Firewall. (BETA)
    package <purl>        Check a package against the GitLab Dependency Firewall. (BETA)
    pip <pip args>        Run Pip through the GitLab Dependency Firewall. (BETA)
    pipenv <pipenv args>  Run Pipenv through the GitLab Dependency Firewall. (BETA)
    pnpm <pnpm args>      Run pnpm through the GitLab Dependency Firewall. (BETA)
    poetry <poetry args>  Run Poetry through the GitLab Dependency Firewall. (BETA)
    twine <twine args>    Run Twine through the GitLab Dependency Firewall. (BETA)
    uv <uv args>          Run uv through the GitLab Dependency Firewall. (BETA)
    yarn <yarn args>      Run Yarn through the GitLab Dependency Firewall. (BETA)

  FLAGS

    -h --help             Show help for this command.

```

## dependency-firewall package

<!-- help-capture: 519ea19f7:dbde48612df4 -->

```text

  Check a single package coordinate against the GitLab Dependency Firewall policy for the current project and report the
  outcome (allow, warning, blocked). No package manager binary is required.

  Supported package URL (PURL) types are `npm`, `pypi`, `maven`, `gem`, `cargo`, and `golang`. The PURL must include a
  version, for example `pkg:npm/left-pad@1.3.0`. For `golang`, the module path keeps its case, for example
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

    # Check a Cargo package version
    glab dependency-firewall package pkg:cargo/serde@1.0.197

    # Check a Go module version
    glab dependency-firewall package pkg:golang/github.com/pkg/errors@v0.9.1

  FLAGS

    -h --help  Show help for this command.

```

## dependency-firewall bundle

<!-- help-capture: 519ea19f7:774d25d5bb73 -->

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

```

## dependency-firewall gem

<!-- help-capture: 519ea19f7:40920e94d79e -->

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

```

## dependency-firewall go

Alias path: `glab help df go` (same captured help).

<!-- help-capture: 519ea19f7:a36f348fb1bc -->

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

```

## dependency-firewall gradle

<!-- help-capture: 519ea19f7:78bc85e01fd0 -->

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

```

## dependency-firewall maven

<!-- help-capture: 519ea19f7:cf57efccc5fa -->

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

```

## dependency-firewall npm

<!-- help-capture: 519ea19f7:fc3f721ce780 -->

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

```

## dependency-firewall pip

<!-- help-capture: 519ea19f7:aeeaa01a5325 -->

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

```

## dependency-firewall pipenv

<!-- help-capture: 519ea19f7:874eeeaa8542 -->

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

```

## dependency-firewall pnpm

<!-- help-capture: 519ea19f7:b76c6b65b028 -->

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

```

## dependency-firewall poetry

<!-- help-capture: 519ea19f7:b9d7ec6e2037 -->

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

```

## dependency-firewall twine

<!-- help-capture: 519ea19f7:0fad828764cc -->

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

```

## dependency-firewall uv

<!-- help-capture: 519ea19f7:768c3ea273f8 -->

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

```

## dependency-firewall yarn

<!-- help-capture: 519ea19f7:c1f3daec4580 -->

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

```

## dependency-firewall ci-summary

<!-- help-capture: 519ea19f7:96d698741e55 -->

```text

  Read `.gitlab/df/ci-log.json` and print blocked and flagged packages
  recorded during a `glab dependency-firewall` run.

  The log is read from the current working directory. Run this command from
  the same directory as the `glab dependency-firewall` run that wrote the
  log, otherwise no activity is reported.

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

```


## dependency-firewall cargo

<!-- help-capture: 519ea19f7:71fc6a46dda0 -->

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

```
