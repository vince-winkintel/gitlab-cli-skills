# glab runner-controller - Command Reference

Complete command syntax and help output for all runner-controller commands.

## Table of Contents

- [glab runner-controller](#glab-runner-controller)
- [Controller Management](#controller-management)
  - [create](#create)
  - [list](#list)
  - [update](#update)
  - [delete](#delete)
- [Token Management](#token-management)
  - [token create](#token-create)
  - [token list](#token-list)
  - [token rotate](#token-rotate)
  - [token revoke](#token-revoke)

---

## glab runner-controller

```
Manages runner controllers. This is an admin-only feature.

  This feature is experimental. It might be broken or removed without any prior notice.
  Read more about what experimental features mean at
  https://docs.gitlab.com/policy/development_stages_support/

  Use experimental features at your own risk.

USAGE

  glab runner-controller <command> [command] [--flags]

COMMANDS

  create [--flags]                     Create a runner controller. (EXPERIMENTAL)
  delete <id> [--flags]                Delete a runner controller. (EXPERIMENTAL)
  list [--flags]                       List runner controllers. (EXPERIMENTAL)
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
