---
name: glab-opentofu
description: Work with OpenTofu state management in GitLab. Use when managing Terraform/OpenTofu state, configuring state backends, or working with infrastructure as code. Triggers on OpenTofu, Terraform, state management, infrastructure as code, IaC.
---

# glab opentofu

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.


## Snap binary lookup

If a confined snap cannot find `tofu`, `opentofu init` suggests `--binary <path>` for an executable accessible inside the snap. Verify that path and approve initialization before running it; the option does not bypass snap confinement or authorize state/backend writes.

## Overview

<!-- help-capture: 685c1cbd7:bf2745a27d03 -->

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

## Quick start

```bash
glab opentofu --help
```

## Structured output

`glab opentofu state list` supports `--output json` / `-F json` for structured output, which is useful for agent automation.

```bash
# List OpenTofu state with JSON output
glab opentofu state list --output json
glab opentofu state list -F json
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
