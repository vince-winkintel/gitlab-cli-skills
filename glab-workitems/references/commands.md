# glab work-items command reference

> Help output captured from the checksum-verified glab v1.115.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

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

```text

  Use `--type` to specify the kind of work item to create.
  The command uses your repository context to detect scope automatically.

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

  FLAGS

    -c --confidential   Mark work item confidential.
    -d --description    Description of the work item. Set to "-" to open an editor.
    --description-file  Read the work item description from a file. Use "-" to read from standard input.
    -g --group          Create work items for a group or subgroup.
    -h --help           Show help for this command.
    --jq                Filter JSON output with a jq expression.
    -F --output         Format output as: text, json. (text)
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title          Add a title for the work item.
    -T --type           Type of work item (epic, incident, issue, key_result, objective, requirement, task, test_case, ticket).

```

## work-items update

```text

  The command uses your repository context to detect scope automatically.

  Use `--group` to target a group or subgroup. `--group` and `--repo` are mutually exclusive.

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

  FLAGS

    -a --assignee       Update the work item assignee with the supplied GitLab usernames.
    -d --description    Update the description for the work item.
    --description-file  Read the work item description from a file. Use "-" to read from standard input.
    --duedate           Update the due date for the work item.
    -g --group          Update work items for a group or subgroup.
    -h --help           Show help for this command.
    --jq                Filter JSON output with a jq expression.
    -m --milestone      Update the work item milestone with the title or ID.
    -F --output         Format output as: text, json. (text)
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --startdate         Update the start date for the work item.
    -t --title          Update the title for the work item.
    -w --weight         Update the weight value for the work item.

```
