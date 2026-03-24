# glab runner-controller - Command Reference

Complete command syntax and help output for all runner-controller commands.

## Table of Contents

- [glab runner-controller](#glab-runner-controller)
- [Controller Management](#controller-management)
  - [create](#create)
  - [get](#get)
  - [list](#list)
  - [update](#update)
  - [delete](#delete)
- [Scope Management](#scope-management)
  - [scope](#scope)
  - [scope list](#scope-list)
  - [scope create](#scope-create)
  - [scope delete](#scope-delete)
- [Token Management](#token-management)
  - [token create](#token-create)
  - [token list](#token-list)
  - [token rotate](#token-rotate)
  - [token revoke](#token-revoke)

---

## glab runner-controller

```
Manages runner controllers. This is an administrator-only feature.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

USAGE

  glab runner-controller <command> [command] [--flags]

COMMANDS

  create [--flags]                     Create a runner controller. (EXPERIMENTAL)
  delete <id> [--flags]                Delete a runner controller. (EXPERIMENTAL)
  get <controller-id> [--flags]        Get details of a runner controller. (EXPERIMENTAL)
  list [--flags]                       List runner controllers. (EXPERIMENTAL)
  scope <command> [command] [--flags]  Manage runner controller scopes. (EXPERIMENTAL)
  token <command> [command] [--flags]  Manage runner controller tokens. (EXPERIMENTAL)
  update <id> [--flags]                Update a runner controller. (EXPERIMENTAL)

FLAGS

  -h --help                            Show help for this command.
```

---

## Controller Management

### create

```
Create a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller create [--flags]

EXAMPLES

  # Create a runner controller with default settings
  $ glab runner-controller create

  # Create a runner controller with a description
  $ glab runner-controller create --description "My controller"

  # Create an enabled runner controller
  $ glab runner-controller create --description "Production" --state enabled

FLAGS

  -d --description  Description of the runner controller.
  -h --help         Show help for this command.
  -F --output       Format output as: text, json. (text)
  --state           State of the runner controller: disabled, enabled, dry_run.
```

### get

```
Retrieves details of a single runner controller, including its
  connection status. This is an administrator-only feature.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

USAGE

  glab runner-controller get <controller-id> [--flags]

EXAMPLES

  # Get runner controller with ID 42
  glab runner-controller get 42

  # Get runner controller as JSON
  glab runner-controller get 42 --output json

FLAGS

  -h --help    Show help for this command.
  -F --output  Format output as: text, json. (text)
```

### list

```
List runner controllers. (EXPERIMENTAL)

USAGE

  glab runner-controller list [--flags]

EXAMPLES

  # List all runner controllers
  $ glab runner-controller list

  # List runner controllers as JSON
  $ glab runner-controller list --output json

FLAGS

  -h --help      Show help for this command.
  -F --output    Format output as: text, json. (text)
  -p --page      Page number. (1)
  -P --per-page  Number of items per page. (30)
```

### update

```
Update a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller update <id> [--flags]

EXAMPLES

  # Update a runner controller's description
  $ glab runner-controller update 42 --description "Updated description"

  # Update a runner controller's state
  $ glab runner-controller update 42 --state enabled

  # Update both description and state
  $ glab runner-controller update 42 --description "Production" --state enabled

FLAGS

  -d --description  Description of the runner controller.
  -h --help         Show help for this command.
  -F --output       Format output as: text, json. (text)
  --state           State of the runner controller: disabled, enabled, dry_run.
```

### delete

```
Delete a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller delete <id> [--flags]

EXAMPLES

  # Delete a runner controller (with confirmation prompt)
  $ glab runner-controller delete 42

  # Delete a runner controller without confirmation
  $ glab runner-controller delete 42 --force

FLAGS

  -f --force  Skip confirmation prompt.
  -h --help   Show help for this command.
```

---

## Scope Management

### scope

```
Manages runner controller scopes. This is an administrator-only feature.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

USAGE

  glab runner-controller scope <command> [command] [--flags]

COMMANDS

  create <controller-id> [--flags]  Create a scope for a runner controller. (EXPERIMENTAL)
  delete <controller-id> [--flags]  Delete a scope from a runner controller. (EXPERIMENTAL)
  list <controller-id> [--flags]    List scopes for a runner controller. (EXPERIMENTAL)

FLAGS

  -h --help                         Show help for this command.
```

### scope list

```
List scopes for a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller scope list <controller-id> [--flags]

EXAMPLES

  # List all scopes for runner controller 42
  glab runner-controller scope list 42

  # List scopes as JSON
  glab runner-controller scope list 42 --output json

FLAGS

  -h --help    Show help for this command.
  -F --output  Format output as: text, json. (text)
```

### scope create

```
Creates a scope for a runner controller. This is an administrator-only feature.

  Use one of the following flags to specify the scope type:

  - --instance: Add an instance-level scope, allowing the runner controller
    to evaluate jobs for all runners in the GitLab instance.
  - --runner <id>: Add a runner-level scope, allowing the runner controller
    to evaluate jobs for a specific instance-level runner. Multiple IDs can
    be comma-separated or specified by repeating the flag.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

USAGE

  glab runner-controller scope create <controller-id> [--flags]

EXAMPLES

  # Add an instance-level scope to runner controller 42
  glab runner-controller scope create 42 --instance

  # Add a runner-level scope for runner 5 to runner controller 42
  glab runner-controller scope create 42 --runner 5

  # Add runner-level scopes for multiple runners
  glab runner-controller scope create 42 --runner 5 --runner 10
  glab runner-controller scope create 42 --runner 5,10

  # Add a runner-level scope and output as JSON
  glab runner-controller scope create 42 --runner 5 --output json

FLAGS

  -h --help    Show help for this command.
  --instance   Add an instance-level scope.
  -F --output  Format output as: text, json. (text)
  --runner     Add a runner-level scope for the specified runner ID. Multiple IDs can be comma-separated or specified by repeating the flag.
```

### scope delete

```
Deletes a scope from a runner controller. This is an administrator-only feature.

  Use one of the following flags to specify the scope type:

  - --instance: Remove an instance-level scope from the runner controller.
  - --runner <id>: Remove a runner-level scope for a specific runner. Multiple IDs
    can be comma-separated or specified by repeating the flag.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

USAGE

  glab runner-controller scope delete <controller-id> [--flags]

EXAMPLES

  # Remove an instance-level scope from runner controller 42 (with confirmation)
  glab runner-controller scope delete 42 --instance

  # Remove an instance-level scope without confirmation
  glab runner-controller scope delete 42 --instance --force

  # Remove a runner-level scope for runner 5 from runner controller 42
  glab runner-controller scope delete 42 --runner 5 --force

  # Remove runner-level scopes for multiple runners
  glab runner-controller scope delete 42 --runner 5 --runner 10 --force
  glab runner-controller scope delete 42 --runner 5,10 --force

FLAGS

  -f --force  Skip confirmation prompt.
  -h --help   Show help for this command.
  --instance  Remove an instance-level scope.
  --runner    Remove a runner-level scope for the specified runner ID. Multiple IDs can be comma-separated or specified by repeating the flag.
```

---

## Token Management

### glab runner-controller token

```
Manages runner controller tokens. This is an admin-only feature.

  This feature is experimental. It might be broken or removed without any prior notice.
  Read more about what experimental features mean at
  https://docs.gitlab.com/policy/development_stages_support/

  Use experimental features at your own risk.

USAGE

  glab runner-controller token <command> [command] [--flags]

COMMANDS

  create <controller-id> [--flags]             Create a token for a runner controller. (EXPERIMENTAL)
  list <controller-id> [--flags]               List tokens of a runner controller. (EXPERIMENTAL)
  revoke <controller-id> <token-id> [--flags]  Revoke a token from a runner controller. (EXPERIMENTAL)
  rotate <controller-id> <token-id> [--flags]  Rotate a token for a runner controller. (EXPERIMENTAL)

FLAGS

  -h --help                                    Show help for this command.
```

### token create

```
Create a token for a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller token create <controller-id> [--flags]

EXAMPLES

  # Create a token for runner controller 42
  $ glab runner-controller token create 42

  # Create a token with a description
  $ glab runner-controller token create 42 --description "production"

  # Create a token and output as JSON
  $ glab runner-controller token create 42 --output json

FLAGS

  -d --description  Description of the token.
  -h --help         Show help for this command.
  -F --output       Format output as: text, json. (text)
```

### token list

```
List tokens of a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller token list <controller-id> [--flags]

EXAMPLES

  # List all tokens of runner controller 42
  $ glab runner-controller token list 42

  # List tokens as JSON
  $ glab runner-controller token list 42 --output json

FLAGS

  -h --help      Show help for this command.
  -F --output    Format output as: text, json. (text)
  -p --page      Page number. (1)
  -P --per-page  Number of items per page. (30)
```

### token rotate

```
Rotate a token for a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller token rotate <controller-id> <token-id> [--flags]

EXAMPLES

  # Rotate token 1 for runner controller 42 (with confirmation prompt)
  $ glab runner-controller token rotate 42 1

  # Rotate without confirmation
  $ glab runner-controller token rotate 42 1 --force

  # Rotate and output as JSON
  $ glab runner-controller token rotate 42 1 --force --output json

FLAGS

  -f --force   Skip confirmation prompt.
  -h --help    Show help for this command.
  -F --output  Format output as: text, json. (text)
```

### token revoke

```
Revoke a token from a runner controller. (EXPERIMENTAL)

USAGE

  glab runner-controller token revoke <controller-id> <token-id> [--flags]

EXAMPLES

  # Revoke token 1 from runner controller 42 (with confirmation prompt)
  $ glab runner-controller token revoke 42 1

  # Revoke without confirmation
  $ glab runner-controller token revoke 42 1 --force

FLAGS

  -f --force  Skip confirmation prompt.
  -h --help   Show help for this command.
```
