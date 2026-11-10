# glab incident help

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

> **Help provenance.** An adjacent `help-capture` marker selects only its matching key below; an explicit per-block capture label applies only when no marker is present. Historical unmarked notes never override either selector. Keyed captures use checksum-verified official macOS arm64 glab binaries. Complete renderer output is preserved except trailing spaces/tabs: indentation, blank lines, heading/flag casing, product spelling (including `Gitlab`), examples, wrapping, and truncation are unchanged. Unmarked legacy captures retain the scoped normalization and older-version guidance stated below.
>
> - `2e352a17e`: source commit `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; archive SHA-256 `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.
> - `685c1cbd7`: source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`.
> - `d43ccacec`: source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`; archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`.
>
> Historical unmarked captures: explicitly labeled blocks use v1.123.0: source commit `5686d7484e65cb08b6e3b92f86d2ccffb415bdc0`, archive SHA-256 `bf776ea47d3b30410267adab9c870990be274e85f6dccccee4289f5ecf1386df` (v1.13.32 audit entry in `VERSION`). Other earlier refreshed blocks retain v1.117.0 provenance; untouched legacy blocks may retain older padding or inherited-flag wording.

<!-- help-capture: 9b430a11f:f319178d3144 -->

```text

  Incidents track service disruptions and their resolution. List and
  view incidents, comment on them, and subscribe, close, or reopen
  them.

  Use `--repo` to target a project other than the current one.


  USAGE

    glab incident [command] [--flags]

  EXAMPLES

    glab incident list

  COMMANDS

    close [<id> | <url>] [--flags]   Close an incident.
    list [--flags]                   List project incidents.
    note <incident-id> [--flags]     Comment on an incident in GitLab.
    reopen [<id> | <url>] [--flags]  Reopen a resolved incident.
    subscribe <id>                   Subscribe to an incident.
    unsubscribe <id>                 Unsubscribe from an incident.
    view <id> [--flags]              Display the title, body, and other information about an incident.

  FLAGS

    -h --help                        Show help for this command.
    -R --repo                        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

  ARGUMENTS

    Specify an incident in one of the following formats:
    - By number, for example "123"
    - By URL, for example "https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123"

```

## incident close

<!-- help-capture: 2e352a17e:295c388f379d -->

```text

  You can use a full GitLab URL instead of an ID.


  USAGE

    glab incident close [<id> | <url>] [--flags]

  EXAMPLES

    glab incident close 123
    glab incident close https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident list

<!-- help-capture: 685c1cbd7:5ff32bed88ae -->

```text

  Defaults to open items. Use `--group` to list for a group
  instead of the current project.


  USAGE

    glab incident list [--flags]

  EXAMPLES

    glab incident list --all
    glab incident ls --all
    glab incident list --assignee=@me
    glab incident list --milestone release-2.0.0
    glab incident list --updated-after 2026-10-01T00:00:00Z

  FLAGS

    -A --all            Get all incidents.
    -a --assignee       Filter incident by assignee <username>, @me, @none (unassigned), or @any (assigned).
    --author            Filter incident by author <username>.
    -c --closed         Get only closed incidents.
    -C --confidential   Filter by confidential incidents.
    --created-after     Filter incidents created after a certain date (RFC 3339, for example 2026-10-01T00:00:00Z).
    --created-before    Filter incidents created before a certain date (RFC 3339, for example 2026-10-01T00:00:00Z).
    -e --epic           List issues belonging to a given epic (requires --group, no pagination support).
    -g --group          Select a group or subgroup. Ignored if a repo argument is set.
    -h --help           Show help for this command.
    --in                Search in: title, description. (title,description)
    --jq                Filter JSON output with a jq expression.
    -l --label          Filter incident by label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    -m --milestone      Filter incident by milestone <id>.
    --not-assignee      Filter incident by not being assigned to <username>.
    --not-author        Filter incident by not being by author(s) <username>.
    --not-label         Filter incident by lack of label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    --order             Order incident by <field>. Order options: created_at, updated_at, priority, due_date, relative_position, label_priority, milestone_due, popularity, weight. (created_at)
    -O --output         Options: 'text' or 'json'. (text)
    -F --output-format  Options: 'details', 'ids', 'urls'. (details)
    -p --page           Page number. (1)
    -P --per-page       Number of items to list per page. (30)
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --search            Search <string> in the fields defined by '--in'.
    -s --sort           Sort direction for --order field: asc or desc. (desc)
    --updated-after     Filter incidents updated after a certain date (RFC 3339, for example 2026-10-01T00:00:00Z).
    --updated-before    Filter incidents updated before a certain date (RFC 3339, for example 2026-10-01T00:00:00Z).

```

## incident note

<!-- help-capture: 9b430a11f:1c82a9c9375d -->

```text

  Without `--message`, opens an editor at a terminal, and otherwise reads the comment from standard input, such as when
  input is piped or redirected.

  `--attach` uploads a file and references it at the end of the comment. Repeat the flag for more than one file, or pass
  `-` to read the file from standard input. An attachment is content on its own, so a comment with only `--attach` does
  not prompt for a body. When standard input is not a terminal, it is read as the comment body, unless `--attach -`
  reads the file from standard input. The command waits until standard input closes, so to post only the attachment from
  a script, redirect standard input from `/dev/null`.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab incident note <incident-id> [--flags]

  EXAMPLES

    # Comment on incident 123, opening an editor for the message
    glab incident note 123

    # Comment with the message given inline
    glab incident note 123 --message "Looking into this now."

    # Create an internal note, visible only to project members
    glab incident note 123 --message "Rotating the leaked token now." --internal

    # Attach a screenshot alongside the message
    glab incident note 123 --message "Here is the repro." --attach ./screenshot.png

    # Attach an image piped from the clipboard
    pngpaste - | glab incident note 123 --attach -

    # Comment with the message read from a file
    glab incident note 123 < comment.md

  FLAGS

    --attach      (Experimental) Upload a file and reference it at the end of the comment. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -h --help     Show help for this command.
    --internal    Create the note as an internal note, visible only to project members.
    -m --message  Message text.
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident reopen

<!-- help-capture: 2e352a17e:39f706377ed8 -->

```text

  You can use a full GitLab URL instead of an ID.


  USAGE

    glab incident reopen [<id> | <url>] [--flags]

  EXAMPLES

    glab incident reopen 123
    glab incident open 123
    glab incident reopen https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident subscribe

<!-- help-capture: 2e352a17e:04752f1e4d7f -->

```text

  You receive notifications when the incident is updated, commented on,
  or has its state changed.


  USAGE

    glab incident subscribe <id> [--flags]

  EXAMPLES

    glab incident subscribe 123
    glab incident sub 123
    glab incident subscribe https://gitlab.com/OWNER/REPO/-/issues/incident/123

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident unsubscribe

<!-- help-capture: 2e352a17e:749ab6cfb465 -->

```text

  You no longer receive notifications about updates to the incident.


  USAGE

    glab incident unsubscribe <id> [--flags]

  EXAMPLES

    glab incident unsubscribe 123
    glab incident unsub 123
    glab incident unsubscribe https://gitlab.com/OWNER/REPO/-/issues/incident/123

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident view

<!-- help-capture: 9b430a11f:284429aac09c -->

```text

  You can use a full GitLab URL instead of an ID. Use `--web`
  to open in a browser.


  USAGE

    glab incident view <id> [--flags]

  EXAMPLES

    glab incident view 123
    glab incident show 123
    glab incident view --web 123
    glab incident view --comments 123
    glab incident view https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123

  FLAGS

    -c --comments     Show incident comments and activities.
    -h --help         Show help for this command.
    --jq              Filter JSON output with a jq expression.
    -F --output       Format output as: text, json. (text)
    -p --page         Page number. (1)
    -P --per-page     Number of items to list per page. (20)
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --system-logs  Show system activities and logs.
    -w --web          Open incident in a browser. Uses the default browser, or the browser specified in the $BROWSER variable.

```
