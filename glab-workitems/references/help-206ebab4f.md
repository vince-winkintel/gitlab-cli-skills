# Captured glab-workitems help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab work-items

<!-- help-capture: 206ebab4f:ef7ac27592bd -->

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

## glab work-items create

<!-- help-capture: 206ebab4f:ed9da64c9449 -->

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

## glab work-items delete

<!-- help-capture: 206ebab4f:d7098ebe1dad -->

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

## glab work-items list

<!-- help-capture: 206ebab4f:5962fce9848f -->

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

## glab work-items ls

<!-- help-capture: 206ebab4f:358e873ba07f -->

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

## glab work-items update

<!-- help-capture: 206ebab4f:6cc5dfffd3de -->

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

    # Set the status of a work item
    glab work-items update 42 --status in-progress

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
    --status            Set the work item status: todo, in-progress, done, wont-do, or duplicate. Needs the status widget, which is Premium and Ultimate only.
    -t --title          Update the title for the work item.
    -w --weight         Update the weight value for the work item.

```

