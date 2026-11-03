# glab user help

> **Current help capture `519ea19f7`.** Official glab v1.128.0 macOS arm64 binary; source commit `519ea19f7d3e9c701a4063f277ae27254bbafdad`; binary archive SHA-256 `541cdde6a0f706b4b69fed9fb558b421a361f63408d072d78ffdf304aee04248`. Only fences with this adjacent key use this provenance. Each complete stdout capture preserves leading spaces, blank lines, Fang uppercase headings, spelling (including `Gitlab`), examples, wrapping, and truncation; only trailing spaces/tabs are removed. Other captures retain their prior provenance and bytes. Current markers override historical unmarked labels.

> Help output captured from `glab user --help`.

<!-- help-capture: 519ea19f7:f646d51bf9bd -->

```text

  Look up information about GitLab users, such as the events a user has
  generated.


  USAGE

    glab user <command> [command] [--flags]

  COMMANDS

    events [--flags]  View user events.

  FLAGS

    -h --help         Show help for this command.

```

## user events

<!-- help-capture: 519ea19f7:f058cbb96c03 -->

```text

  By default, lists events for the current project. Use `--all` to
  include events from every project you can access.


  USAGE

    glab user events [--flags]

  EXAMPLES

    glab user events
    glab user events --all
    glab user events -F json

  FLAGS

    -a --all       Get events from all projects.
    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: 'text', 'json'. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)

```

