# glab duo help

> Complete affected help surfaces captured from the checksum-verified glab v1.114.0 macOS arm64 release binary, with only terminal padding and trailing whitespace removed.

## duo

```text

  Use the GitLab Duo Agent Platform in your terminal. Ask GitLab Duo questions about your codebase and use it to
  autonomously perform actions on your behalf.

  `glab duo cli` installs and runs the GitLab Duo CLI (`duo`) binary. `glab` handles authentication, so you sign in only
  once with `glab auth login`.

  The GitLab Duo CLI requires GitLab 19.2 or later, or GitLab 18.11 to 19.1 with beta and experimental features turned
  on. For all prerequisites and usage, see `glab duo cli --help`.


  USAGE

    glab duo [command] [--flags]

  EXAMPLES

    glab duo cli --install
    glab duo cli
    glab duo cli run --goal "Fix the failing tests in this project"

  COMMANDS

    cli [command] [--flags]  Run the GitLab Duo CLI.

  FLAGS

    -h --help                Show help for this command.

```

## duo cli

```text

  Run the GitLab Duo CLI (`duo`) through `glab`.

  The GitLab Duo CLI brings the GitLab Duo Agent Platform to your terminal. Ask GitLab Duo questions about your codebase
  and use it to autonomously perform actions on your behalf.

  The GitLab Duo CLI runs in two modes:

  - Interactive (default): `glab duo cli` opens a session for multiple prompts, with build and plan modes.
  - Headless: `glab duo cli run --goal "<prompt>"` runs a single prompt and exits. For use in runners, scripts, and
  automated workflows.

  When you use the GitLab Duo CLI through `glab`, `glab` handles authentication for you. You authenticate only once.

  Prerequisites:

  - Use GitLab 19.2 or later.
  - Run `glab auth login` to authenticate.
  - Meet the prerequisites for GitLab Duo Agent Platform.
  - Set a default GitLab Duo namespace, or run the command in a project that has GitLab Duo access.
  - For GitLab Self-Managed and GitLab Dedicated on 19.2 or later, turn on GitLab Duo CLI access. It is on by default.

  Note: If you are on GitLab 18.11 to 19.1, you can use the GitLab Duo CLI by turning on beta and experimental features.

  Configuration options:

  - `duo_cli_auto_run`: Skip the run confirmation prompt.
  - `duo_cli_auto_download`: Skip the download confirmation prompt.

  `glab` passes all other arguments and flags through to the GitLab Duo CLI binary. To see the GitLab Duo CLI commands
  and flags, run `glab duo cli help`.

  For more information, see the GitLab Duo CLI documentation.


  USAGE

    glab duo cli [command] [--flags]

  EXAMPLES

    # Start an interactive GitLab Duo CLI session
    glab duo cli

    # Use the GitLab Duo CLI in headless mode with a single prompt
    glab duo cli run --goal "Fix the failing tests in this project"

    # Pass any command or flag through to the GitLab Duo CLI binary (for example: model, version, run)
    glab duo cli <command>
    glab duo cli --model claude_sonnet_4_6

    # Show GitLab CLI help content
    glab duo cli --help

    # Show GitLab Duo CLI help content, including commands and flags
    glab duo cli help

    # Run without prompts (for use in scripts and non-interactive environments)
    glab duo cli --yes

    # Install the GitLab Duo CLI binary
    glab duo cli --install

    # Install the GitLab Duo CLI binary without prompts
    glab duo cli --install --yes

    # Check for and install updates
    glab duo cli --update

  FLAGS

    -h --help  Show help for this command.
    --install  Install the GitLab Duo CLI binary without running it.
    --update   Check for and install updates to the binary.
    -y --yes   Skip confirmation prompts.

GITLAB DUO CLI
  The GitLab Duo CLI binary is not installed yet. To get started:

    1. glab auth login          # authenticate, once
    2. glab duo cli --install   # download the GitLab Duo CLI binary
    3. glab duo cli             # start an interactive session

  Or run 'glab duo cli' and follow the prompts.
  After it is installed, 'glab duo cli help' shows the GitLab Duo CLI
  commands and flags.
```
