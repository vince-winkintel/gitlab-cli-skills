# glab work-items command reference

> **Help provenance.** An adjacent `help-capture` marker selects only its matching key below; an explicit per-block capture label applies only when no marker is present. Historical unmarked notes never override either selector. Keyed captures use checksum-verified official macOS arm64 glab binaries. Complete renderer output is preserved except trailing spaces/tabs: indentation, blank lines, heading/flag casing, product spelling (including `Gitlab`), examples, wrapping, and truncation are unchanged. Unmarked legacy captures retain the scoped normalization and older-version guidance stated below.
>
> - `2e352a17e`: source commit `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; archive SHA-256 `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.
> - `d43ccacec`: source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`; archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`.
>
> Unmarked blocks retain the checksum-verified v1.117.0 macOS arm64 capture, with terminal padding/trailing whitespace removed and readability substitutions rejoining hard-wrapped code spans. Marked blocks preserve renderer wrapping verbatim.

Copyable selector: `glab work-items list --group group/subgroup` (the help renderer may split `--group` across lines).

## work-items

<!-- help-capture: 2e352a17e:ad2fa97192ca -->

```text

  Work with GitLab work items.

  Work items are the unified GitLab system for planning and tracking work, supporting
  various types including epics, issues, tasks, incidents, and test cases. Work items
  can be organized hierarchically to break down complex work into manageable pieces.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab work-items <command> [command] [--flags]

  COMMANDS

    create [--flags]        Create work items in a project or group. (EXPERIMENTAL)
    delete <iid> [--flags]  Delete a work item in a project or group. (EXPERIMENTAL)
    list [--flags]          List work items in a project or group. (EXPERIMENTAL)
    update <iid> [--flags]  Update work items in a project or group. (EXPERIMENTAL)

  FLAGS

    -h --help               Show help for this command.

```

## work-items create

<!-- help-capture: 2e352a17e:a48a29167334 -->

```text

  Use `--type` to specify the kind of work item to create.
  The command uses your repository context to detect scope automatically.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Uploads are project-scoped, so `--attach` cannot be combined with `--
  group`.

  `--parent` accepts a work item ID in the current scope, a reference such as `group/project#123`, or a URL.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab work-items create [--flags]

  EXAMPLES

    # Create a work item in the current project
    glab work-items create --type issue

    # Create a work item in a group
    glab work-items create --type epic --group my-group

    # Read the description from a file
    glab work-items create --type issue --title "Add feature" --description-file description.md

    # Read the description from standard input
    cat description.md | glab work-items create --type issue --title "Add feature" --description-file -

    # Attach a screenshot to the description
    glab work-items create --type issue --title "Add feature" --attach ./screenshot.png

    # Create a work item in an iteration
    glab work-items create --type issue --title "Add feature" --iteration 123

    # Create a task under work item 42 in the current project
    glab work-items create --type task --title "Write tests" --parent 42

    # Create a task under a work item in another project
    glab work-items create --type task --title "Write tests" --parent my-group/my-project#42

  FLAGS

    --attach            (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -c --confidential   Mark work item confidential.
    -d --description    Description of the work item. Set to "-" to open an editor.
    --description-file  Read the work item description from a file. Use "-" to read from standard input.
    -g --group          Create work items for a group or subgroup.
    -h --help           Show help for this command.
    --iteration         Add the work item to the iteration with this ID.
    --jq                Filter JSON output with a jq expression.
    -F --output         Format output as: text, json. (text)
    --parent            Set the parent work item by <id>, reference, or URL.
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title          Add a title for the work item.
    -T --type           Type of work item (epic, incident, issue, key_result, objective, requirement, task, test_case, ticket).

```

## work-items update

<!-- help-capture: 2e352a17e:64a4020dc848 -->

```text

  The command uses your repository context to detect scope automatically.

  Use `--group` to target a group or subgroup. `--group` and `--repo` are mutually exclusive.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Without `--description` the references are added to the description the
  work item already has, instead of replacing it. Uploads are project-scoped, so `--attach` cannot be combined with `--
  group`.

  `--parent` accepts a work item ID in the current scope, a reference such as `group/project#123`, or a URL.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab work-items update <iid> [--flags]

  EXAMPLES

    # Update a work item in current project
    glab work-items update 42 --description "this issue tracks a new feature"

    # Update a work item in a group
    glab work-items update 40 --group MYGROUP --description "this epic tracks a new feature"

    # Read the description from a file
    glab work-items update 42 --description-file description.md

    # Read the description from standard input
    cat description.md | glab work-items update 42 --description-file -

    # Add a screenshot to the existing description
    glab work-items update 42 --attach ./screenshot.png

    # Move a work item to another iteration
    glab work-items update 42 --iteration 123

    # Move a work item under work item 40
    glab work-items update 42 --parent 40

    # Move a work item under a work item in another project
    glab work-items update 42 --parent https://gitlab.com/my-group/my-project/-/work_items/40

  FLAGS

    -a --assignee       Update the work item assignee with the supplied GitLab usernames.
    --attach            (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -d --description    Update the description for the work item.
    --description-file  Read the work item description from a file. Use "-" to read from standard input.
    --duedate           Update the due date for the work item.
    -g --group          Update work items for a group or subgroup.
    -h --help           Show help for this command.
    --iteration         Move the work item to the iteration with this ID.
    --jq                Filter JSON output with a jq expression.
    -m --milestone      Update the work item milestone with the title or ID.
    -F --output         Format output as: text, json. (text)
    --parent            Set the parent work item by <id>, reference, or URL.
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --startdate         Update the start date for the work item.
    -t --title          Update the title for the work item.
    -w --weight         Update the weight value for the work item.

```

## work-items list

<!-- help-capture: 2e352a17e:88f67cb9df75 -->

```text

  List work items in a project or group.

  Automatically detects scope from repository context. Use --group flag
  for group-level work items or -R to specify a different project.

  Date filters accept:

  - An absolute date (YYYY-MM-DD). A date without a time is read in the system time zone of the GitLab server.
  - An RFC 3339 timestamp. Use one with an offset, such as 2026-01-01T00:00:00+02:00, for an exact point in time.
  - A relative date: a number followed by d (days), w (weeks), m (months), or y (years). Negative numbers are in the
  past, positive numbers are in the future, and 0d is today. Relative dates resolve to the start of the day in the time
  zone of the GitLab instance. They stay relative, so the same command keeps returning the last 7 days, for example.

  Date filters require GitLab 19.4 or later. Relative dates require GitLab 19.6 or later.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab work-items list [--flags]

  EXAMPLES

    # List first 20 open work items in current project
    glab work-items list

    # List open epics in a group (default: 20 items)
    glab work-items list --type epic -g gitlab-org

    # List first 50 open work items
    glab work-items list --per-page 50 -g gitlab-org

    # Get next page using cursor from previous output
    glab work-items list --after "eyJpZCI6OTk5OX0" -g gitlab-org

    # List closed work items
    glab work-items list --state closed -g gitlab-org

    # List all work items regardless of state
    glab work-items list --state all -g gitlab-org

    # JSON output with pagination metadata
    glab work-items list --output json -g gitlab-org

    # List issues in a specific project
    glab work-items list --type issue -R gitlab-org/cli

    # List work items created in the last 7 days
    glab work-items list --created-after -7d -g gitlab-org

    # List open work items due in the next 2 weeks
    glab work-items list --due-after 0d --due-before 2w -g gitlab-org

    # List work items closed in a fixed date range
    glab work-items list --state closed --closed-after 2026-01-01 --closed-before 2026-04-01 -g gitlab-org

  FLAGS

    --after           Fetch items after this cursor (for pagination)
    --closed-after    Show work items closed on or after <date>. Implies --state closed unless --state is set. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --closed-before   Show work items closed before <date>. Implies --state closed unless --state is set. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --created-after   Show work items created on or after <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --created-before  Show work items created before <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --due-after       Show work items due on or after <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --due-before      Show work items due before <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    -g --group        List work items for a group or subgroup.
    -h --help         Show help for this command.
    --jq              Filter JSON output with a jq expression.
    -F --output       Format output as: text, json. (text)
    -P --per-page     Number of items to list per page (max 100) (20)
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --state           Filter by state: opened, closed, all. (opened)
    -t --type         Filter by work item type (epic, issue, task, etc.) Multiple types can be comma-separated or specified by repeating the flag.
    --updated-after   Show work items updated on or after <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.
    --updated-before  Show work items updated before <date>. Use YYYY-MM-DD, an RFC 3339 timestamp, or a relative date such as -7d, 2w, -1m, or 1y.

```

## work-items delete

<!-- help-capture: 2e352a17e:0ce07ed90f25 -->

```text

  Delete a work item by its internal ID (IID). This action cannot be undone.

  The command behavior depends on context:

  - By default, deletes from the current repository's project.
  - With `--group`, deletes from the specified group.
  - With `--repo`, deletes from the specified project.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab work-items delete <iid> [--flags]

  EXAMPLES

    # Delete a work item by IID from the current project
    glab work-items delete 42

    # Delete a group work item
    glab work-items delete 42 --group my-group

  FLAGS

    -g --group   Delete a work items from a group or subgroup.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```
