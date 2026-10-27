# glab opentofu help

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

> Every help fence in this file is marked with capture key `685c1cbd7` and was rechecked against that binary.

<!-- help-capture: 685c1cbd7:bd8225589b41 -->

```text

  Manage OpenTofu and Terraform state stored in the GitLab-managed
  state backend.

  Initialize a working directory against a GitLab-managed state, and
  list, lock, unlock, download, or delete states.


  USAGE

    glab opentofu <command> [command] [--flags]

  COMMANDS

    init <state> [--flags]               Initialize OpenTofu or Terraform.
    state <command> [command] [--flags]  Work with the OpenTofu or Terraform states.

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## opentofu init

<!-- help-capture: 685c1cbd7:7db03955c79f -->

```text

  Configures the GitLab HTTP backend for OpenTofu or Terraform state
  and runs `tofu init`. You must run this command from a GitLab
  project repository.

  If glab is installed as a snap, it cannot run OpenTofu or Terraform
  binaries installed on the host or by other snaps. Place the binary in
  your home directory and pass its path with `--binary`.


  USAGE

    glab opentofu init <state> [--flags]

  EXAMPLES

    # Initialize state with name production in working directory
    glab opentofu init production

    # Initialize state with name production in infra/ directory
    glab opentofu init production -d infra/

    # Initialize state with name production with Terraform
    glab opentofu init production -b terraform

    # Initialize state with name production with reconfiguring state
    glab opentofu init production -- -reconfigure

  FLAGS

    -b --binary     Name or path of the OpenTofu or Terraform binary to use for the initialization. (tofu)
    -d --directory  Directory of the OpenTofu or Terraform project to initialize. (.)
    -h --help       Show help for this command.
    -R --repo       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## opentofu state

<!-- help-capture: 685c1cbd7:2f8bc9d9c834 -->

```text

  List the states in the current project, lock or unlock a state to
  control concurrent access, download a state as JSON, or delete a
  state or one of its versions.


  USAGE

    glab opentofu state <command> [command] [--flags]

  COMMANDS

    delete <state> [<serial>] [--flags]  Delete a state or a specific version of a state.
    download <state> [<serial>]          Download the given state and output as JSON to stdout.
    list [--flags]                       List states.
    lock <state>                         Lock the given state.
    unlock <state>                       Unlock the given state.

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

