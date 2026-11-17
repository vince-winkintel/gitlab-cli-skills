# Captured glab-service-account help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab service-account

<!-- help-capture: 206ebab4f:c9c3d822154d -->

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

    create [--flags]                     Create a service account.
    delete <id | username> [--flags]     Delete a service account.
    get <id | username> [--flags]        Get a service account.
    list [--flags]                       List service accounts.
    token <command> [command] [--flags]  Manage the tokens of a service account.
    update <id | username> [--flags]     Update a service account.

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab service-account create

<!-- help-capture: 206ebab4f:703f8a93b175 -->

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

## glab service-account del

<!-- help-capture: 206ebab4f:af8566632e47 -->

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

## glab service-account delete

<!-- help-capture: 206ebab4f:98cf80c29559 -->

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

## glab service-account get

<!-- help-capture: 206ebab4f:eba095b65177 -->

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

## glab service-account list

<!-- help-capture: 206ebab4f:6940030e1e5f -->

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

## glab service-account ls

<!-- help-capture: 206ebab4f:5695a364d9cf -->

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

## glab service-account token

<!-- help-capture: 206ebab4f:b049eb0c5a73 -->

```text

  Manage the personal access tokens of a service account of a project or a group.

  - Every token command takes the service account as its first argument, by ID or username. IDs and usernames come from
  `glab service-account list`.
  - A token acts as the service account, limited to the scopes it was created with.

  Tokens of a group service account require GitLab 17.11 or later.


  USAGE

    glab service-account token <command> [command] [--flags]

  COMMANDS

    create <account-id | username> <name> [--flags]             Create a token for a service account.
    list <account-id | username> [--flags]                      List the tokens of a service account.
    revoke <account-id | username> <token-id | name> [--flags]  Revoke a token of a service account.
    rotate <account-id | username> <token-id | name> [--flags]  Rotate a token of a service account.

  FLAGS

    -h --help                                                   Show help for this command.
    -R --repo                                                   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab service-account token create

<!-- help-capture: 206ebab4f:173bf42187ab -->

```text

  Create a personal access token for a service account of a project or a group.

  - The token value is printed only once and cannot be retrieved later. It is the only output on stdout, and the token
  details go to stderr.
  - At least one scope is required. For the scopes you can grant, see
  https://docs.gitlab.com/security/tokens/access_token_scopes/.
  - The token expires after `--duration`, 30 days by default, at 00:00 UTC. Use `--expires-at` for a specific date
  instead.
  - A numeric account argument is always treated as an ID.


  USAGE

    glab service-account token create <account-id | username> <name> [--flags]

  EXAMPLES

    # Create a token for service account 42 of the current project
    glab service-account token create 42 ci --scope api

    # Create a read-only token that expires in a week, finding the account by its username
    glab service-account token create release-bot ci-reader --scope read_api,read_repository --duration 7d

    # Create a token for a group's service account that expires at the end of 2027
    glab service-account token create 42 deploy --scope api --expires-at 2027-12-31 --group my-group

    # Create a token and store its value in a variable
    TOKEN=$(glab service-account token create 42 ci --scope api)

  FLAGS

    --description    Description of the token.
    -D --duration    Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at midnight UTC on the calculated date. (30d)
    -E --expires-at  Expiry date of the token, as YYYY-MM-DD. The token expires at midnight UTC on that date.
    -g --group       Create a token for a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help        Show help for this command.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as 'text' for the token value, 'json' for the token with its details. (text)
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -S --scope       Scope to grant the token. Multiple scopes can be comma-separated or specified by repeating the flag.

```

## glab service-account token list

<!-- help-capture: 206ebab4f:1893a7d2f4ae -->

```text

  List the personal access tokens of a service account of a project or a group.

  - A numeric account argument is always treated as an ID.
  - Token values are never shown. GitLab returns a token's value only when the token is created or rotated.

  Listing the tokens of a group service account requires GitLab 17.11 or later.


  USAGE

    glab service-account token list <account-id | username> [--flags]

  EXAMPLES

    # List the tokens of service account 42 of the current project
    glab service-account token list 42

    # List only the active tokens, finding the account by its username
    glab service-account token list release-bot --active

    # List the tokens of a group's service account
    glab service-account token list 42 --group my-group

    # Print the names of the active tokens
    glab service-account token list 42 --active --output json --jq '.[].name'

  FLAGS

    -a --active  List only the active tokens.
    -g --group   List the tokens of a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab service-account token revoke

<!-- help-capture: 206ebab4f:1da75247e9ca -->

```text

  Revoke a personal access token of a service account of a project or a group.

  - Anything authenticating with the token stops working immediately.
  - A token name matches active tokens only. If several active tokens share the name, use the token ID instead.
  - Numeric arguments are always treated as IDs. Token IDs and names come from `glab service-account token list`.

  Revoking a token of a group service account requires GitLab 17.11 or later.


  USAGE

    glab service-account token revoke <account-id | username> <token-id | name> [--flags]

  EXAMPLES

    # Revoke token 7 of service account 42 of the current project
    glab service-account token revoke 42 7

    # Revoke a token by its name, finding the account by its username
    glab service-account token revoke release-bot ci

    # Revoke a token of a group's service account
    glab service-account token revoke 42 7 --group my-group

  FLAGS

    -g --group  Revoke a token of a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab service-account token rotate

<!-- help-capture: 206ebab4f:1470951f0a49 -->

```text

  Rotate a personal access token of a service account of a project or a group.

  - Rotating revokes the token and creates a new one with the same name, description, and scopes. Anything using the old
  value stops working immediately.
  - The new token value is printed only once and cannot be retrieved later. It is the only output on stdout, and the
  token details go to stderr.
  - The new token expires after `--duration`, 30 days by default, at 00:00 UTC. Use `--expires-at` for a specific date
  instead.
  - A token name matches active tokens only. If several active tokens share the name, use the token ID instead.
  - Numeric arguments are always treated as IDs. Token IDs and names come from `glab service-account token list`.

  Finding a token by name for a group service account requires GitLab 17.11 or later.


  USAGE

    glab service-account token rotate <account-id | username> <token-id | name> [--flags]

  EXAMPLES

    # Rotate token 7 of service account 42 of the current project
    glab service-account token rotate 42 7

    # Rotate a token by its name for 90 days, finding the account by its username
    glab service-account token rotate release-bot ci --duration 90d

    # Rotate a token of a group's service account until the end of 2027
    glab service-account token rotate 42 7 --expires-at 2027-12-31 --group my-group

    # Rotate a token and store the new value in a variable
    TOKEN=$(glab service-account token rotate 42 ci)

  FLAGS

    -D --duration    Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at midnight UTC on the calculated date. (30d)
    -E --expires-at  Expiry date of the new token, as YYYY-MM-DD. The token expires at midnight UTC on that date.
    -g --group       Rotate a token of a service account of a `group` instead of a project. Accepts a group ID or full path.
    -h --help        Show help for this command.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as 'text' for the token value, 'json' for the token with its details. (text)
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab service-account update

<!-- help-capture: 206ebab4f:a1d7d22196f1 -->

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

