# glab timelog command reference

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## timelog

<!-- help-capture: 9b430a11f:1d961d3a0fc0 -->

```text

  Time logs are the entries that time tracking records when you log time on an issue or merge request. Use `glab timelog
  list` to see who logged time, on which items, and the total, for a project or group over a date range.

  To log time on an issue, use `glab issue update --spend`.


  USAGE

    glab timelog <command> [command] [--flags]

  COMMANDS

    list [--flags]  List time logged on issues and merge requests.

  FLAGS

    -h --help       Show help for this command.

```

## timelog list

<!-- help-capture: 9b430a11f:e6398526bcae -->

```text

  By default, reports on the current project. Use `--group` to report on a group and its subgroups, or `--repo` to
  report on another project. Entries are listed newest first, followed by the total time spent.

  Dates appear in UTC. Durations use time tracking units: 1 day is 8 hours, 1 week is 5 days, and 1 month is 4 weeks.
  Subtracted time appears as a negative value and reduces the total.

  Omits time logged on issues and merge requests you cannot view.


  USAGE

    glab timelog list [--flags]

  EXAMPLES

    # List all time logged in the current project
    glab timelog list

    # List the time you logged in a group and its subgroups since the start of the month
    glab timelog list --group gitlab-org --user @me --start-date 2026-10-01

    # List the time logged in another project on a single day
    glab timelog list -R gitlab-org/cli --start-date 2026-10-14 --end-date 2026-10-14

    # Total the seconds logged per user
    glab timelog list --output json --jq 'group_by(.user.username) | map({user: .[0].user.username, seconds: map(.t…

  FLAGS

    --end-date    List time logged on or before this date, in `YYYY-MM-DD` format.
    -g --group    List time logged in a group and its subgroups.
    -h --help     Show help for this command.
    --jq          Filter JSON output with a jq expression.
    -F --output   Format output as: text, json. (text)
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --start-date  List time logged on or after this date, in `YYYY-MM-DD` format.
    --user        List only the time logged by this `username`. Use @me for yourself.

```
