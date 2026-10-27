# glab deploy-token command reference

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

## deploy-token

<!-- help-capture: 685c1cbd7:b2451dbebbf9 -->

```text

  Manage the deploy tokens of a project or a group.

  Deploy tokens grant access to a repository, its container registry, and its package registry over HTTPS without being
  tied to a user account. They are commonly used by CI/CD jobs and external systems.

  These commands act on the current project. Use `--repo` to target a different project, or `--group` to act on a group
  instead.


  USAGE

    glab deploy-token <command> [command] [--flags]

  COMMANDS

    list [--flags]  List deploy tokens.

  FLAGS

    -h --help       Show help for this command.
    -R --repo       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## deploy-token list

<!-- help-capture: 685c1cbd7:1957f29337b5 -->

```text

  List the deploy tokens of a project or a group.

  The output never contains the token value. A token value is shown only once, when the token is created.

  Tokens are listed with their expiry, and whether they have been revoked or have expired. Pass `--active` to list only
  the tokens that are still usable.


  USAGE

    glab deploy-token list [--flags]

  EXAMPLES

    # List the current project's deploy tokens
    glab deploy-token list

    # List the deploy tokens of a specific project
    glab deploy-token list --repo user/my-repo

    # List only the tokens that are neither revoked nor expired
    glab deploy-token list --active

    # List a group's deploy tokens
    glab deploy-token list --group group/sub-group

    # List the current project's deploy tokens as JSON
    glab deploy-token list --output json

  FLAGS

    -a --active  List only the tokens that are neither revoked nor expired.
    -g --group   List the deploy tokens of the group <group> instead of a project.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

