# Captured glab-attestation help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab attestation

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

## glab attestation verify

<!-- help-capture: 206ebab4f:57e5c588029b -->

```text

  Verify the provenance of an artifact built by a GitLab CI/CD pipeline.
  This command checks the artifact's signed attestation against the expected
  GitLab project and pipeline.

  This command requires the cosign binary. To install it, see
  Cosign installation.

  This command works with any GitLab instance. It finds the project and its attestations on the instance from your
  current context: the `GITLAB_HOST` variable, your Git remote, or your glab configuration.

  This command verifies only attestations signed with Sigstore (`SIGSTORE`). It does not yet support attestations signed
  with the project's certificate authority (`LOCAL_CA`).

  For more information about attestations, see:

  - Attestations API
  - SLSA provenance specification
  - SLSA software attestations

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab attestation verify <project-id> <artifact-path> [--flags]

  EXAMPLES

    # Verify attestation for filename.txt in the gitlab-org/gitlab project
    glab attestation verify gitlab-org/gitlab filename.txt

    # Verify attestation for filename.txt in the project with ID 123
    glab attestation verify 123 filename.txt

  FLAGS

    -h --help  Show help for this command.

```

