# glab dependency-firewall command reference

> Parent and `package` help output captured from the checksum-verified glab v1.120.0 macOS arm64 release binary; Yarn remains an exact v1.119.0 capture, and unchanged wrapper and `ci-summary` blocks remain exact v1.118.0 captures. Terminal padding and trailing whitespace are removed. Wrapper help uses `glab help dependency-firewall <wrapper>` because wrapper arguments are forwarded to the package-manager binary verbatim. The v1.120.0 release archive SHA-256 is `8769650c49bb5d5ac52156d46e448e87f5570a868fe4e7bfcbd8cc66693c7afb`.

## dependency-firewall

Alias: `df`

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

```text

  Check a single package coordinate against the GitLab Dependency Firewall policy for the current project and report the
  outcome (allow, warning, blocked). No package manager binary is required.

  Supported package URL (PURL) types are `npm`, `pypi`, `maven`, and `gem`. The PURL must include a version, for example
  `pkg:npm/left-pad@1.3.0`.

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

```text

  Run the yarn binary through the GitLab Dependency Firewall. The command checks each package download and upload
  against the policy for the current project, refuses blocked packages, and summarizes the results after the run.

  The command uses your package manager's registry or index configuration, and does not modify it.

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
