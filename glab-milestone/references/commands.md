# glab milestone help

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

> Help output captured from `glab milestone --help`.

<!-- help-capture: 9b430a11f:f4bff38dfc18 -->

```text

  Milestones group issues, merge requests, and epics around a shared
  goal or release. Use the subcommands to create, list, edit, delete,
  or look up milestones in the current project, in another project, or
  in a group.


  USAGE

    glab milestone <command> [command] [--flags]

  COMMANDS

    create [--flags]       Create a milestone in a project or group.
    delete <id> [--flags]  Delete a milestone from a project or group.
    edit <id> [--flags]    Edit a milestone in a project or group.
    get [<id>] [--flags]   Get a milestone by ID in a project or group.
    list [--flags]         List milestones in a project or group.

  FLAGS

    -h --help              Show help for this command.
    -R --repo              Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## milestone create

<!-- help-capture: 9b430a11f:7b5da3d7b54a -->

```text

  The `--title` flag is required.
  Optionally provide a description, due date, and start date.

  By default, the milestone is created in the current project. Use
  `--project` to target a different project, or `--group` to create a
  group-level milestone. `--project` and `--group` are mutually exclusive.


  USAGE

    glab milestone create [--flags]

  EXAMPLES

    # Create a milestone in the current project
    glab milestone create --title='Example title' --due-date='2025-12-16'

    # Create a milestone in a different project
    glab milestone create --title='Q4 release' --due-date='2025-12-16' --project 123

    # Create a milestone in a group
    glab milestone create --title='FY26 planning' --due-date='2026-01-31' --group 456

  FLAGS

    --description  Description of the milestone.
    --due-date     Due date for the milestone. Expected in ISO 8601 format (2025-04-15T08:00:00Z).
    --group        The ID or URL-encoded path of the group.
    -h --help      Show help for this command.
    --project      The ID or URL-encoded path of the project.
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --start-date   Start date for the milestone. Expected in ISO 8601 format (2025-04-15T08:00:00Z).
    --title        Title of the milestone.

```

## milestone delete

<!-- help-capture: 9b430a11f:7aa95d499a87 -->

```text

  Delete a milestone, identified by its numeric ID, from a project or
  group. The milestone is removed; issues, merge requests, and epics
  that referenced it are no longer associated with it.

  By default, the milestone is deleted from the current project. Use
  `--project` to target a different project, or `--group` to delete a
  group-level milestone. `--project` and `--group` are mutually exclusive.


  USAGE

    glab milestone delete <id> [--flags]

  EXAMPLES

    # Delete a milestone from the current project
    glab milestone delete 123

    # Delete a milestone from a different project
    glab milestone delete 123 --project owner/project

    # Delete a group milestone
    glab milestone delete 123 --group example-group

  FLAGS

    --group    The ID or URL-encoded path of the group.
    -h --help  Show help for this command.
    --project  The ID or URL-encoded path of the project.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## milestone edit

<!-- help-capture: 9b430a11f:d370dc77e04f -->

```text

  Edit a milestone, identified by its numeric ID, in a project or group.
  Use the flags to update the title, description, due date, start date,
  or state. Only the fields you specify are updated.

  By default, the milestone is edited in the current project. Use
  `--project` to target a different project, or `--group` to edit a
  group-level milestone. `--project` and `--group` are mutually exclusive.


  USAGE

    glab milestone edit <id> [--flags]

  EXAMPLES

    # Update a milestone's title and due date in the current project
    glab milestone edit 123 --title='Example title' --due-date='2025-12-16'

    # Update a milestone in a different project
    glab milestone edit 123 --title='Q4 release' --due-date='2025-12-16' --project owner/project

    # Update a group milestone
    glab milestone edit 123 --title='FY26 planning' --due-date='2026-01-31' --group 789

  FLAGS

    --description  Description of the milestone.
    --due-date     Due date for the milestone. Expected in ISO 8601 format (2025-04-15T08:00:00Z).
    --group        The ID or URL-encoded path of the group.
    -h --help      Show help for this command.
    --project      The ID or URL-encoded path of the project.
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --start-date   Start date for the milestone. Expected in ISO 8601 format (2025-04-15T08:00:00Z).
    --state        State of the milestone. Can be 'activate' or 'close'.
    --title        Title of the milestone.

```

## milestone get

<!-- help-capture: 9b430a11f:e5049fb3feda -->

```text

  Get information about a single milestone in a project or group,
  identified by its numeric ID. Use `--output json` to format the result
  as JSON for use with other tools.

  By default, the milestone is looked up in the current project. Use
  `--project` to target a different project, or `--group` to look up a
  group-level milestone. `--project` and `--group` are mutually exclusive.


  USAGE

    glab milestone get [<id>] [--flags]

  EXAMPLES

    # Get a milestone from the current project
    glab milestone get 123

    # Get a milestone from a different project
    glab milestone get 123 --project owner/project

    # Get a group milestone
    glab milestone get 123 --group example-group

    # Get a milestone as JSON
    glab milestone get 123 --output json

  FLAGS

    --group      The ID or URL-encoded path of the group.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    --project    The ID or URL-encoded path of the project.
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## milestone list

<!-- help-capture: 9b430a11f:b80c888ab12a -->

```text

  Filter by state with `--state` (`active` or `closed`), by title with `--title`,
  or by free-text search with `--search`. For group milestones, use
  `--include-ancestors` to also include milestones from ancestor groups, and
  `--include-descendants` to also include milestones from subgroups and descendant projects.

  By default, milestones are listed for the current project. Use
  `--project` to target a different project, or `--group` to list
  group-level milestones. `--project` and `--group` are mutually exclusive.

  Use `--output json` to format the result as JSON for use with other tools.


  USAGE

    glab milestone list [--flags]

  EXAMPLES

    # List milestones in a project
    glab milestone list --project 123
    glab milestone list --project owner/project

    # List milestones in a group
    glab milestone list --group example-group

    # List only active milestones in a group
    glab milestone list --group example-group --state active

    # List group milestones, including those from ancestor groups
    glab milestone list --group example-group --include-ancestors

    # List group milestones, including those from subgroups and descendant projects
    glab milestone list --group example-group --include-descendants

    # List milestones as JSON
    glab milestone list --project owner/project --output json

  FLAGS

    --group                The ID or URL-encoded path of the group.
    -h --help              Show help for this command.
    --include-ancestors    Include milestones from all parent groups.
    --include-descendants  Include milestones from all subgroups and descendant projects.
    --jq                   Filter JSON output with a jq expression.
    -F --output            Format output as: text, json. (text)
    -p --page              Page number. (1)
    -P --per-page          Number of items to list per page. (20)
    --project              The ID or URL-encoded path of the project.
    -R --repo              Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --search               Return only milestones with a title or description matching the provided string.
    --show-id              Show IDs in table output.
    --state                Return only 'active' or 'closed' milestones.
    --title                Return only the milestones having the given title.

```

