# Captured glab-orbit help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab orbit

<!-- help-capture: 206ebab4f:2f85a0fb2cb5 -->

```text

  Run the GitLab Orbit CLI through glab.

  Coding agents: run `glab orbit --yes skills get orbit` to load the Orbit skill. `--yes` installs the binary without a
  prompt on first use.

  Every command and flag, including `--help`, is forwarded verbatim to the managed Orbit binary. glab downloads,
  verifies, and updates that binary for you on first use. Until the binary is installed, `glab orbit` and `--help` print
  install instructions instead. glab passes your resolved GitLab credential to the binary on every invocation, so remote
  commands such as `glab orbit query` need no separate login.

  glab handles only the `update` command and the `--install`, `--update`, and `--yes` flags itself. Run `glab help
  orbit` to see them.

  Prerequisites:

  - Run `glab auth login` to authenticate.
  - Orbit must be enabled for your namespace (the `knowledge_graph` feature flag).

  Configuration options:

  - `orbit_cli_auto_run`: Skip the run confirmation prompt.
  - `orbit_cli_auto_download`: Skip the download confirmation prompt.

  For more information, see the Orbit documentation.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab orbit [command] [<command>] [--flags]

  EXAMPLES

    # Install the managed binary without running it, or update it
    $ glab orbit --install --yes
    $ glab orbit update

    # Install on first use without a prompt, then load the Orbit skill
    $ glab orbit --yes skills get orbit

    # Show the Orbit binary's own help
    $ glab orbit --help

  COMMANDS

    update [--flags]  Update the GitLab Orbit CLI binary to the latest version. (EXPERIMENTAL)

  FLAGS

    -h --help         Show the Orbit binary's help, or install instructions until the binary is installed.
    --install         Install the Orbit binary without running it.
    --update          Check for and install updates to the binary. Same as the update command.
    -y --yes          Skip confirmation prompts.

  ENVIRONMENT VARIABLES

    - `GLAB_ORBIT_CLI_BINARY_PATH`: Use a local binary instead of the managed one. Skips
      download, version checks, and updates. Can also be set via the `orbit_cli_binary_path`
      configuration key.
    - `ORBIT_CLI_AUTO_DOWNLOAD`: Set to `true` to download the binary without a
      prompt. Required to run in a non-interactive environment such as CI.
    - `ORBIT_CLI_AUTO_RUN`: Set to `true` to run the binary without a prompt.
      Required to run in a non-interactive environment such as CI.

```

## glab orbit update

<!-- help-capture: 206ebab4f:e8250817c49c -->

```text

  Checks for a newer GitLab Orbit CLI version and installs it. If the binary is not installed yet, `glab` downloads the
  latest version.

  Updates do not apply when you use a custom binary set with `GLAB_ORBIT_CLI_BINARY_PATH` or the `orbit_cli_binary_path`
  configuration key.

  `glab orbit --update` does the same thing.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab orbit update [--flags]

  EXAMPLES

    # Update the GitLab Orbit CLI, or download it if not installed
    glab orbit update

    # Skip the download prompt
    glab orbit update --yes

  FLAGS

    -h --help  Show help for this command.
    -y --yes   Skip the download prompt when the binary is not installed.

```

