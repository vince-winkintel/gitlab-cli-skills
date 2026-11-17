---
name: glab-attestation
description: Work with GitLab attestations for software supply chain security including artifact verification and provenance. Use when verifying software artifacts, managing attestations, or working with supply chain security. Triggers on attestation, verify artifact, provenance, supply chain security.
---

# glab attestation

Current captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

> **Help provenance — capture key `206ebab4f`:** official macOS arm64 release binary, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`. Applies only to adjacent `206ebab4f` markers; complete binary stdout is preserved except trailing spaces/tabs. Historical references retain their own provenance. This attribution is kept inline for single-file exports that omit references and VERSION.

## Select the instance and signing format

`verify <project-id> <artifact-path>` supports Sigstore (`SIGSTORE`) attestations from any GitLab instance, using the host resolved from `GITLAB_HOST`, the Git remote, or glab configuration. Confirm the trusted host and project before reading attestations. The verifier derives the expected OIDC issuer and project identity prefix from the project's returned web URL, then invokes the separately installed `cosign` binary to check the artifact and bundle. It does not support project-CA (`LOCAL_CA`) attestations. Do not weaken certificate identity checks or install tools as part of passive help inspection.

## Overview

<!-- help-capture: 206ebab4f:185d975484f3 -->

```text

  Manage software attestations for artifacts built in GitLab CI/CD pipelines.
  An attestation is a signed statement about an artifact, such as a provenance
  statement that records how the artifact was built.

  Use this command to verify that an artifact was built by the expected
  GitLab project and pipeline.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab attestation <command> [command] [--flags]

  EXAMPLES

    # Verify attestation for filename.txt in the gitlab-org/gitlab project
    glab attestation verify gitlab-org/gitlab filename.txt

    # Verify attestation for filename.txt in the project with ID 123
    glab attestation verify 123 filename.txt

  COMMANDS

    verify <project-id> <artifact-path>  Verify the provenance of a specific artifact or file. (EXPERIMENTAL)

  FLAGS

    -h --help                            Show help for this command.

  ARGUMENTS

    Specify a project in one of the following formats:
    - By number, for example "123"
    - By path, for example "gitlab-org/cli"

```

## Quick start

```bash
glab attestation --help
```

## Subcommands

See [current command help](references/help-206ebab4f.md) for captured `--help` output. Earlier captures remain in [the historical reference](references/commands.md).
