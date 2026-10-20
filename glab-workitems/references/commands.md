# glab work-items command reference

> Per-block capture IDs below override older file-level provenance; unmarked blocks retain their existing provenance.

> Help output captured from the checksum-verified glab v1.117.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed. Documented readability substitutions rejoin code spans that the renderer hard-wrapped, such as `--group`.

## work-items

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

> Complete help from the checksum-verified release binary; immutable capture ID `d43ccacec` maps to release/checksum evidence in `VERSION`. Only trailing spaces/tabs are removed; leading indentation, blank lines, uppercase headings, wrapping, truncation, and product spelling (including renderer `Gitlab`) are preserved.

```text

  Use `--type` to specify the kind of work item to create.
  The command uses your repository context to detect scope automatically.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Uploads are project-scoped, so `--attach` cannot be combined with `--
  group`.

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
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title          Add a title for the work item.
    -T --type           Type of work item (epic, incident, issue, key_result, objective, requirement, task, test_case, ticket).

```

## work-items update

> Complete help from the checksum-verified release binary; immutable capture ID `d43ccacec` maps to release/checksum evidence in `VERSION`. Only trailing spaces/tabs are removed; leading indentation, blank lines, uppercase headings, wrapping, truncation, and product spelling (including renderer `Gitlab`) are preserved.

```text

  The command uses your repository context to detect scope automatically.

  Use `--group` to target a group or subgroup. `--group` and `--repo` are mutually exclusive.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Without `--description` the references are added to the description the
  work item already has, instead of replacing it. Uploads are project-scoped, so `--attach` cannot be combined with `--
  group`.

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
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --startdate         Update the start date for the work item.
    -t --title          Update the title for the work item.
    -w --weight         Update the weight value for the work item.

```
