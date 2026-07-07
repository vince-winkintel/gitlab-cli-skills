## glab security

```text
Configure GitLab security features for a project.

This feature is an experiment and is not ready for production use.
It might be unstable or removed at any time.
For more information, see
https://docs.gitlab.com/policy/development_stages_support/.

USAGE
  glab security <command> [command] [--flags]

COMMANDS
  config <command> [command] [--flags]  Configure security scan profiles for a project.

FLAGS
  -h --help  Show help for this command.
  -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
```

## glab security config

```text
Enable, disable, or inspect security scan profiles for a project.

A profile bundles a set of security scans, such as SAST, secret
detection, dependency scanning, or container scanning, or post-scan
processing on given scans, like dependency scanning auto remediation.

USAGE
  glab security config <command> [command] [--flags]

COMMANDS
  disable <profile> [--flags]  Disable a security scan profile for a project.
  enable <profile> [--flags]   Enable a security scan profile for a project.
  status <profile> [--flags]   Show the status of a security scan profile for a project.

FLAGS
  -h --help  Show help for this command.
  -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
```

## glab security config enable

```text
Attach a security scan profile to a project.

You must be a Maintainer or Owner of the project.

USAGE
  glab security config enable <profile> [--flags]

EXAMPLES
  # Enable dependency scanning on the current project
  $ glab security config enable dependency_scanning

  # Enable SAST on a specific project
  $ glab security config enable sast -R gitlab-org/cli

  # Enable auto-remediation for vulnerable dependencies
  $ glab security config enable dependency_scanning_post_processing

FLAGS
  -h --help  Show help for this command.
  -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
```

## glab security config disable

```text
Detach a security scan profile from a project.

You must be a Maintainer or Owner of the project.

USAGE
  glab security config disable <profile> [--flags]

EXAMPLES
  # Disable dependency scanning on the current project
  $ glab security config disable dependency_scanning

  # Disable SAST on a specific project
  $ glab security config disable sast -R gitlab-org/cli

  # Disable auto-remediation for vulnerable dependencies
  $ glab security config disable dependency_scanning_post_processing

FLAGS
  -h --help  Show help for this command.
  -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
```

## glab security config status

```text
Show whether a security scan profile is attached to a project and its
current scan status.

USAGE
  glab security config status <profile> [--flags]

EXAMPLES
  # Show dependency scanning status for the current project
  $ glab security config status dependency_scanning

  # Show SAST status for a specific project
  $ glab security config status sast -R gitlab-org/cli

  # Show auto-remediation status for vulnerable dependencies
  $ glab security config status dependency_scanning_post_processing

FLAGS
  -h --help  Show help for this command.
  -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
```
