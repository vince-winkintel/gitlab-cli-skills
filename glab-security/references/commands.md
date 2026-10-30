## glab security

> Capture key `4dd0d32d1`: checksum-verified official macOS arm64 binary, source commit `4dd0d32d18361db6c1c668eb4ac691c0d6edf255`, archive SHA-256 `11980310aaad2bd9c4e75b5635a60e984da5d0e6245187f2cd6e8db0ec4c5a92`. Only adjacent marked help fences use this provenance; complete renderer output is preserved except trailing spaces/tabs. Other fences retain their stated prior provenance.

<!-- help-capture: 4dd0d32d1:03e81cf1b737 -->

```text

  Use these commands to enable, disable, or inspect the security scans
  attached to a project.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab security <command> [command] [--flags]

  COMMANDS

    config <command> [command] [--flags]  Configure security scan profiles for a project. (EXPERIMENTAL)

  FLAGS

    -h --help                             Show help for this command.
    -R --repo                             Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab security config

<!-- help-capture: 4dd0d32d1:4c508cf28a9b -->

```text

  Enable, disable, or inspect security scan profiles for a project.

  A profile bundles a set of security scans, such as SAST, secret
  detection, dependency scanning, or container scanning, or post-scan
  processing on given scans, like dependency scanning auto remediation.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab security config <command> [command] [--flags]

  COMMANDS

    disable <profile> [--flags]  Disable a security scan profile for a project. (EXPERIMENTAL)
    enable <profile> [--flags]   Enable a security scan profile for a project. (EXPERIMENTAL)
    status <profile> [--flags]   Show the status of a security scan profile for a project. (EXPERIMENTAL)

  FLAGS

    -h --help                    Show help for this command.
    -R --repo                    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab security config enable

<!-- help-capture: 4dd0d32d1:f29d1b4dc4d6 -->

```text

  Attach a security scan profile to a project.

  Prerequisites:

  - At least the Maintainer role or the Security Manager role for the project.

  For `<profile>`, use one of the following identifiers:

  - `secret_detection`: Secret detection.
  - `sast`: SAST.
  - `dependency_scanning`: Dependency scanning.
  - `dependency_scanning_post_processing`: Dependency scanning auto-remediation.
  - `business_logic`: Business logic.
  - `skillguard`: SkillGuard.
  - `triage_and_remediation_conservative`: Automated triage and remediation, Conservative preset.
  - `triage_and_remediation_standard`: Automated triage and remediation, Standard preset.
  - `triage_and_remediation_proactive`: Automated triage and remediation, Proactive preset.
  - For a custom profile, the numeric part of the profile ID. For example,
    `123` for `gid://gitlab/Security::ScanProfile/123`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


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

<!-- help-capture: 4dd0d32d1:c21158d96add -->

```text

  Detach a security scan profile from a project.

  Prerequisites:

  - At least the Maintainer role or the Security Manager role for the project.

  For `<profile>`, use one of the following identifiers:

  - `secret_detection`: Secret detection.
  - `sast`: SAST.
  - `dependency_scanning`: Dependency scanning.
  - `dependency_scanning_post_processing`: Dependency scanning auto-remediation.
  - `business_logic`: Business logic.
  - `skillguard`: SkillGuard.
  - `triage_and_remediation_conservative`: Automated triage and remediation, Conservative preset.
  - `triage_and_remediation_standard`: Automated triage and remediation, Standard preset.
  - `triage_and_remediation_proactive`: Automated triage and remediation, Proactive preset.
  - For a custom profile, the numeric part of the profile ID. For example,
    `123` for `gid://gitlab/Security::ScanProfile/123`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


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

<!-- help-capture: 4dd0d32d1:cd43dd3b2ab3 -->

```text

  Show whether a security scan profile is attached to a project and its
  current scan status.

  For `<profile>`, use one of the following scan types:

  - `secret_detection`: Secret detection.
  - `sast`: SAST.
  - `container_scanning`: Container scanning.
  - `dependency_scanning`: Dependency scanning.
  - `dependency_scanning_post_processing`: Dependency scanning auto-remediation.
  - `business_logic`: Business logic.
  - `skillguard`: SkillGuard.
  - `triage_and_remediation`: Automated triage and remediation, any preset.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


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
