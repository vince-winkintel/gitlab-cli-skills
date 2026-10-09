# glab iteration help

> Complete help captured from the checksum-verified glab v1.122.0 macOS arm64 release binary. Only terminal padding/trailing whitespace is removed; renderer wrapping and example truncation are preserved. Archive SHA-256: `cbdd6e28d35f9eb09aef79ad23d2712d67c9254677a60ed6d701b5362f659fef`. No product-spelling substitutions were needed in these captures.

## iteration

```text

  Iterations are time-boxed periods, similar to sprints, that group
  issues and merge requests in a project or group.

  List the iterations for the current project, or use the `--group`
  flag to list a group's iterations instead.


  USAGE

    glab iteration <command> [command] [--flags]

  COMMANDS

    list [--flags]  List project iterations.

  FLAGS

    -h --help       Show help for this command.
    -R --repo       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## iteration list

```text

  By default, lists the iterations for the current project. Use
  `--group` to list a group's iterations instead, or `--repo` to
  target a project other than the current one.


  USAGE

    glab iteration list [--flags]

  EXAMPLES

    glab iteration list
    glab iteration ls
    glab iteration list -R owner/repository
    glab iteration list -g mygroup

  FLAGS

    -g --group     List iterations for a group.
    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```
