# glab dependency-firewall command reference

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

> Older capture notes below apply only to fences without the `685c1cbd7` marker.

> Capture key `d43ccacec`: checksum-verified macOS arm64 release binary, source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`, binary archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`. Marked help preserves all renderer output except trailing spaces/tabs; unmarked blocks retain their stated older provenance.

> Unmarked wrapper and `ci-summary` blocks retain their exact prior captures; the Cargo block follows its `d43ccacec` marker, and the other unmarked wrappers remain from the earlier capture documented in `VERSION`. Wrapper help uses `glab help dependency-firewall <wrapper>` so no package manager is launched.

## dependency-firewall

Alias: `df`

<!-- help-capture: 685c1cbd7:a4957900ddcc -->

```text

  Commands to configure GitLab Dependency Firewall for local package
  managers, run local package managers with a summary of blocked or
  flagged packages, and view activity during the current session.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall <command> [command] [--flags]

  COMMANDS

    bundle <bundle args>  Run Bundler through the GitLab Dependency Firewall. (EXPERIMENTAL)
    cargo <cargo args>    Run Cargo through the GitLab Dependency Firewall. (EXPERIMENTAL)
    ci-summary            Summarize Dependency Firewall activity from the CI log. (EXPERIMENTAL)
    gem <gem args>        Run gem through the GitLab Dependency Firewall. (EXPERIMENTAL)
    gradle <gradle args>  Run Gradle through the GitLab Dependency Firewall. (EXPERIMENTAL)
    maven <mvn args>      Run Maven through the GitLab Dependency Firewall. (EXPERIMENTAL)
    npm <npm args>        Run npm through the GitLab Dependency Firewall. (EXPERIMENTAL)
    package <purl>        Check a package against the GitLab Dependency Firewall. (EXPERIMENTAL)
    pip <pip args>        Run Pip through the GitLab Dependency Firewall. (EXPERIMENTAL)
    pipenv <pipenv args>  Run Pipenv through the GitLab Dependency Firewall. (EXPERIMENTAL)
    pnpm <pnpm args>      Run pnpm through the GitLab Dependency Firewall. (EXPERIMENTAL)
    poetry <poetry args>  Run Poetry through the GitLab Dependency Firewall. (EXPERIMENTAL)
    twine <twine args>    Run Twine through the GitLab Dependency Firewall. (EXPERIMENTAL)
    uv <uv args>          Run uv through the GitLab Dependency Firewall. (EXPERIMENTAL)
    yarn <yarn args>      Run Yarn through the GitLab Dependency Firewall. (EXPERIMENTAL)

  FLAGS

    -h --help             Show help for this command.

```

## dependency-firewall package

<!-- help-capture: 685c1cbd7:deaca3a6fcd2 -->

```text

  Check a single package coordinate against the GitLab Dependency Firewall policy for the current project and report the
  outcome (allow, warning, blocked). No package manager binary is required.

  Supported package URL (PURL) types are `npm`, `pypi`, `maven`, `gem`, `cargo`, and `golang`. The PURL must include a
  version, for example `pkg:npm/left-pad@1.3.0`. For `golang`, the module path keeps its case, for example
  `pkg:golang/github.com/BurntSushi/toml@v1.4.0`.

  This command does not write to the CI log at `.gitlab/df/ci-log.json`, so `glab dependency-firewall ci-summary` does
  not include its result.

  Exit codes:

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | Allow or warning. |
  | `1` | Misconfiguration or transport error. |
  | `3` | Blocked. |

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
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

```text

  Run the Bundler binary (`bundle`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `bundle` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall bundle <bundle args> [--flags]

  EXAMPLES

    # Install dependencies through the Dependency Firewall
    glab dependency-firewall bundle install

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall gem

```text

  Run the gem binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your configured sources, and does not modify `~/.gemrc` or your sources.

  All arguments are forwarded to `gem` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gem <gem args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall gem install rake

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall gradle

```text

  Run the Gradle binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `gradle` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall gradle <gradle args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall gradle build

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall maven

```text

  Run the Maven binary (`mvn`) through the GitLab Dependency Firewall. The command checks each package download and
  upload against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `mvn` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall maven <mvn args> [--flags]

  EXAMPLES

    # Build a project through the Dependency Firewall
    glab dependency-firewall maven verify

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall npm

```text

  Run the npm binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to npm verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall npm <npm args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall npm install left-pad

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall pip

```text

  Run the Pip binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `pip` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pip <pip args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pip install requests

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall pipenv

```text

  Run the Pipenv binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `pipenv` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
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

```text

  Run the pnpm binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `pnpm` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall pnpm <pnpm args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall pnpm install left-pad

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall poetry

```text

  Run the Poetry binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `poetry` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall poetry <poetry args> [--flags]

  EXAMPLES

    # Add a package through the Dependency Firewall
    glab dependency-firewall poetry add requests

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall twine

```text

  Run the Twine binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `twine` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
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

```text

  Run the uv binary through the GitLab Dependency Firewall. The command checks each package download and upload against
  the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `uv` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall uv <uv args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall uv pip install requests

  FLAGS

    -h --help  Show help for this command.
```

## dependency-firewall yarn

<!-- help-capture: 685c1cbd7:5c0ecefd19e4 -->

```text

  Run the yarn binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  This command requires Yarn 3.2 or later, or Yarn Classic (1.x). It refuses Yarn 2.x through 3.1, because those
  versions cannot stop a `.yarnrc.yml` file from routing registry traffic around the firewall. During the run, Yarn
  ignores per-host `networkSettings` from every `.yarnrc.yml` file, so every request goes through the firewall.

  All arguments are forwarded to `yarn` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab dependency-firewall yarn <yarn args> [--flags]

  EXAMPLES

    # Install a package through the Dependency Firewall
    glab dependency-firewall yarn add left-pad

  FLAGS

    -h --help  Show help for this command.

```

## dependency-firewall ci-summary

```text

  Read `.gitlab/df/ci-log.json` and print blocked and flagged packages
  recorded during a `glab dependency-firewall` run.

  The log is read from the current working directory. Run this command from
  the same directory as the `glab dependency-firewall` run that wrote the
  log, otherwise no activity is reported.

  | Exit code | Meaning |
  |-----------|---------|
  | `0` | No blocked entries in the log (allow-only or warnings). |
  | `1` | The log could not be read. |
  | `3` | At least one entry in the log is blocked. |

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
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

> Capture `d43ccacec` (key above).

```text

  Run the Cargo binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

  All arguments are forwarded to `cargo` verbatim.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
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
