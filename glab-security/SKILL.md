---
name: glab-security
description: Configure GitLab project security scan profiles with glab. Use when enabling or disabling SAST, dependency scanning, secret detection, dependency-scanning auto-remediation, business_logic, skillguard, triage_and_remediation presets, or custom profile IDs; or checking scan-type status, including container_scanning. Triggers on GitLab security config, security scan profile, enable SAST, dependency scanning, secret detection, container scanning status, business logic, SkillGuard, triage and remediation, glab security.
---

# glab security

Configure GitLab security features for a project.

> Experimental upstream command surface: verify live `glab security --help` before relying on it in production automation.

## Common commands

```bash
# Show security command help
glab security --help

# Enable a scan profile on the current project
glab security config enable dependency_scanning

# Enable SAST on a specific project
glab security config enable sast -R gitlab-org/cli

# Check profile status
glab security config status dependency_scanning

# Disable a scan profile
glab security config disable dependency_scanning

# Disable dependency scanning auto-remediation
glab security config disable dependency_scanning_post_processing
```

## Profile identifiers versus scan types

`enable` and `disable` take a profile identifier: `secret_detection`, `sast`, `dependency_scanning`, `dependency_scanning_post_processing`, `business_logic`, `skillguard`, or a triage preset (`triage_and_remediation_conservative`, `triage_and_remediation_standard`, `triage_and_remediation_proactive`). For a custom profile, pass the numeric part of its ID, such as `123` from `gid://gitlab/Security::ScanProfile/123`.

`status` instead matches a scan type, case-insensitively. Use the shared types above, `container_scanning`, or `triage_and_remediation` for any triage preset. It does not look up a custom numeric profile ID or a triage preset identifier: use the profile's scan type. `NOT_CONFIGURED` from an unmatched string does not prove a particular custom profile is absent. The status scan-type list does not imply that every type is an enable/disable profile identifier; verify instance availability before approving a change.

## Operational guidance

- Enabling or disabling a profile requires at least the Maintainer role or the Security Manager role for the target project.
- Use `-R/--repo` for explicit targeting in agents and scripts; otherwise `glab` resolves the project from the current git remote.
- Treat `enable` and `disable` as project-configuration writes. Confirm the target project and requested profile before changing state.
- Prefer `status` before and after a change so the user can see the current scan/profile state.

## Safe workflow

```bash
PROFILE_ID=triage_and_remediation_standard
SCAN_TYPE=triage_and_remediation
PROJECT=group/project

# 1. Inspect current state
glab security config status "$SCAN_TYPE" -R "$PROJECT"

# 2. Confirm requested change with the user, then apply
glab security config enable "$PROFILE_ID" -R "$PROJECT"

# 3. Verify
glab security config status "$SCAN_TYPE" -R "$PROJECT"
```

For a custom `PROFILE_ID`, set `SCAN_TYPE` to that profile's scan type. The status check reports scan-type state, not proof that a particular numeric ID or triage preset is attached; verify the exact attachment separately when that identity matters.

## Subcommands

See [references/commands.md](references/commands.md) for the current captured `--help` output.
