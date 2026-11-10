# glab service-account command reference

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## service-account

<!-- help-capture: 9b430a11f:abed5abf6391 -->

```text

  Manage the service accounts of a project or a group.

  Service accounts are user accounts that represent a non-human entity, such as a CI/CD job, a script, or an external
  system, rather than a person.

  These commands act on the current project. Use `--repo` to target a different project, or `--group` to act on a group
  instead. If `GITLAB_GROUP` is set and neither flag is given, these commands act on that group.

  Group service accounts require the Owner role for the group. On GitLab Self-Managed and GitLab Dedicated, they require
  an administrator, or the Owner role when an administrator has turned on the setting to allow top-level group Owners to
  create service accounts.

  Project service accounts require the Maintainer or Owner role for the project, or an administrator. They require
  GitLab 18.11 or later.


  USAGE

    glab service-account <command> [command] [--flags]

  COMMANDS

    create [--flags]                  Create a service account.
    delete <id | username> [--flags]  Delete a service account.
    get <id | username> [--flags]     Get a service account.
    list [--flags]                    List service accounts.
    update <id | username> [--flags]  Update a service account.

  FLAGS

    -h --help                         Show help for this command.
    -R --repo                         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## service-account create

<!-- help-capture: 9b430a11f:0251d8a47199 -->

```text

  Create a service account for a project or a group.

  - Every flag is optional. Without `--name`, the account is named "Service account user". Without `--username` or `--
  email`, GitLab generates them.
  - A custom email address must be confirmed before the account uses it, unless the top-level group has a matching
  verified domain or email confirmation is turned off on the instance. Until then, the address is shown as the
  unconfirmed email.
  - A service account created in a top-level group can be invited to any group or project on the instance. One created
  in a subgroup can be invited only to that subgroup and its descendants.

  Creating a service account in a subgroup requires GitLab 18.11 or later. Setting `--email` for a group service account
  requires GitLab 17.11 or later.


  USAGE

    glab service-account create [--flags]

  EXAMPLES

    # Create a service account for the current project
    glab service-account create --name "Release bot"

    # Create it with a chosen username and email address
    glab service-account create --name "Release bot" --username release-bot --email release-bot@example.com

    # Create a service account for a specific project
    glab service-account create --name "Release bot" --repo user/my-repo

    # Create a group service account
    glab service-account create --name "Release bot" --group my-group

    # Create a service account and print its ID from a script
    glab service-account create --name "Release bot" --output json --jq '.id'

  FLAGS

    --email      Email address of the service account.
    -g --group   Create a service account for a `group` instead of a project. Accepts a group ID or full path.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    --name       Name of the service account.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --username   The service account's `username`.

```

## service-account delete

<!-- help-capture: 9b430a11f:0e72c3cbf6a4 -->

```text

  Delete a service account of a project or a group, by its ID or username.

  The account's contributions, such as merge requests and comments, are moved to the ghost user. Anything authenticating
  with the account's tokens stops working.

  GitLab deletes the account in the background, so it can still appear in `glab service-account list` for a short time.

  A numeric argument is always treated as an ID. IDs and usernames come from `glab service-account list`.


  USAGE

    glab service-account delete <id | username> [--flags]

  EXAMPLES

    # Delete service account 42 of the current project, after confirming
    glab service-account delete 42

    # Delete it without a confirmation prompt
    glab service-account delete 42 --yes

    # Delete a service account by its username
    glab service-account delete release-bot

    # Delete a service account of a specific project
    glab service-account delete 42 --repo user/my-repo

    # Delete a group's service account
    glab service-account delete 42 --group my-group

  FLAGS

    -g --group  Delete a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes    Skip the confirmation prompt.

```

## service-account get

<!-- help-capture: 9b430a11f:e3a7a3303658 -->

```text

  Get a single service account of a project or a group, by its ID or username.

  A numeric argument is always treated as an ID. IDs and usernames come from `glab service-account list`.

  Getting a service account by ID requires GitLab 19.4 or later.


  USAGE

    glab service-account get <id | username> [--flags]

  EXAMPLES

    # Get service account 42 of the current project
    glab service-account get 42

    # Get a service account by its username
    glab service-account get service_account_project_123_abc

    # Get a service account of a specific project
    glab service-account get 42 --repo user/my-repo

    # Get a group's service account
    glab service-account get 42 --group my-group

    # Print the service account's email address
    glab service-account get 42 --output json --jq '.email'

  FLAGS

    -g --group   Get a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## service-account list

<!-- help-capture: 9b430a11f:abd4691e8155 -->

```text

  List the service accounts of a project or a group.


  USAGE

    glab service-account list [--flags]

  EXAMPLES

    # List the current project's service accounts
    glab service-account list

    # List the service accounts of a specific project
    glab service-account list --repo user/my-repo

    # List a group's service accounts
    glab service-account list --group my-group

    # Print the ID and username of each service account
    glab service-account list --output json --jq '.[] | "\(.id) \(.username)"'

  FLAGS

    -g --group   List the service accounts of a `group` instead of a project. Accepts a group ID or full path.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## service-account update

<!-- help-capture: 9b430a11f:64d2cae2cbd0 -->

```text

  Update the name, username, or email address of a service account of a project or a group, by its ID or username.

  - Only the given fields change. At least one of `--name`, `--username`, or `--email` is required.
  - A field cannot be cleared, so an empty value is rejected.
  - A numeric argument is always treated as an ID. IDs and usernames come from `glab service-account list`.
  - A new custom email address must be confirmed before the account uses it, unless the top-level group has a matching
  verified domain or email confirmation is turned off on the instance. Until then, the address is shown as the
  unconfirmed email.
  - The username of a service account associated with a composite identity cannot be changed.

  Updating a group service account requires GitLab 17.10 or later. Changing the email address requires GitLab 18.2 or
  later.


  USAGE

    glab service-account update <id | username> [--flags]

  EXAMPLES

    # Rename service account 42 of the current project
    glab service-account update 42 --name "Release bot"

    # Change the username of a service account, found by its current username
    glab service-account update release-bot --username release-bot-2

    # Change the email address of a service account of a specific project
    glab service-account update 42 --email release-bot@example.com --repo user/my-repo

    # Rename a group's service account
    glab service-account update 42 --name "Release bot" --group my-group

  FLAGS

    --email      New email address of the service account.
    -g --group   Update a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    --name       New name of the service account.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --username   New `username` of the service account.

```
