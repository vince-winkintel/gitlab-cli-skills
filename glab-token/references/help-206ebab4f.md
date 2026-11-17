# Captured glab-token help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab token

<!-- help-capture: 206ebab4f:5987febdc8d7 -->

```text

  Create, list, revoke, and rotate access tokens for your user
  account, a project, or a group.


  USAGE

    glab token [command] [--flags]

  COMMANDS

    create <name> [--flags]                   Creates user, group, or project access tokens.
    list [--flags]                            List user, group, or project access tokens.
    revoke <token-name|token-id> [--flags]    Revoke user, group, or project access tokens.
    rotate [<token-name|token-id>] [--flags]  Rotate user, group, or project access tokens.

  FLAGS

    -h --help                                 Show help for this command.
    -R --repo                                 Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab token create

<!-- help-capture: 206ebab4f:f491c443d832 -->

```text

  Creates a new access token for a user, group, or project. Defaults to a
  project access token, unless user or group name is specified.

  The expiration date of the token is calculated by adding the duration
  (default: 30 days) to the current date, with expiration occurring at midnight
  UTC on the calculated date. You can specify a different duration using days (d),
  weeks (w), or hours (h), or provide an explicit end date.

  The name of the token must be unique. The token is printed to stdout.

  Administrators can create full-featured personal access tokens for themselves and for other users.

  Non-administrators can create personal access tokens only for
  themselves (@me). These tokens must use the scope 'k8s_proxy'. For more
  information, see the GitLab documentation for the
  User tokens API.


  USAGE

    glab token create <name> [--flags]

  EXAMPLES

    # Create project access token for current project (default 30 days)
    glab token create --access-level developer --scope read_repository --scope read_registry my-project-token

    # Create project access token with 7 day lifetime
    glab token create --repo user/my-repo --access-level owner --scope api my-project-token --duration 7d

    # Create a group access token expiring in 2 weeks
    glab token create --group group/sub-group --access-level owner --scope api my-group-token --duration 2w

    # Create a personal access token for current user with 90 day lifetime
    glab token create --user @me --scope k8s_proxy my-personal-token --duration 90d

    # (administrator only) Create a personal access token for another user
    glab token create --user johndoe --scope api johns-personal-token --duration 180d

    # Create a token with explicit expiration date
    glab token create --access-level developer --scope api my-token --expires-at 2025-12-31

  FLAGS

    -A --access-level  Access level of the token: one of 'guest', 'reporter', 'developer', 'maintainer', 'owner'. (no)
    --description      Sets the token's description.
    -D --duration      Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at midnight UTC on the calculated date. (30d)
    -E --expires-at    Sets the token's expiration date and time, in YYYY-MM-DD format. If not specified, --duration is used. (0001-01-01)
    -g --group         Create a group access token. Ignored if a user or repository argument is set.
    -h --help          Show help for this command.
    --jq               Filter JSON output with a jq expression.
    -F --output        Format output as 'text' for the token value, 'json' for the actual API token structure. (text)
    -R --repo          Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -S --scope         Scopes for the token. Multiple scopes can be comma-separated or specified by repeating the flag. For a list, see https://docs.gitlab.com/security/tokens/access_token_scopes/. ([read_repository])
    -U --user          Create a personal access token. For the current user, use @me.

```

## glab token list

<!-- help-capture: 206ebab4f:c36c681aedfa -->

```text

  List all tokens for a user, group, or project.

  The output contains the token's meta information, not the actual token value. The output format
  can be "JSON" or "text". The access level property is printed in human-readable form in the text
  output, but displays the integer value in JSON.

  Administrators can list tokens of other users.


  USAGE

    glab token list [--flags]

  EXAMPLES

    # List the current project's access tokens
    glab token list
    glab token list --output json

    # List the project access tokens of a specific project
    glab token list --repo user/my-repo

    # List group access tokens
    glab token list --group group/sub-group

    # List my personal access tokens
    glab token list --user @me

    # Administrators only: list the personal access tokens of another user
    glab token list --user johndoe

  FLAGS

    -a --active  List only the active tokens.
    -g --group   List group access tokens. Ignored if a user or repository argument is set.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. text provides a readable table, json outputs the tokens with metadata. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -U --user    List personal access tokens. Use @me for the current user.

```

## glab token ls

<!-- help-capture: 206ebab4f:c1df64965286 -->

```text

  List all tokens for a user, group, or project.

  The output contains the token's meta information, not the actual token value. The output format
  can be "JSON" or "text". The access level property is printed in human-readable form in the text
  output, but displays the integer value in JSON.

  Administrators can list tokens of other users.


  USAGE

    glab token list [--flags]

  EXAMPLES

    # List the current project's access tokens
    glab token list
    glab token list --output json

    # List the project access tokens of a specific project
    glab token list --repo user/my-repo

    # List group access tokens
    glab token list --group group/sub-group

    # List my personal access tokens
    glab token list --user @me

    # Administrators only: list the personal access tokens of another user
    glab token list --user johndoe

  FLAGS

    -a --active  List only the active tokens.
    -g --group   List group access tokens. Ignored if a user or repository argument is set.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. text provides a readable table, json outputs the tokens with metadata. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -U --user    List personal access tokens. Use @me for the current user.

```

## glab token new

<!-- help-capture: 206ebab4f:53407c0e5f3b -->

```text

  Creates a new access token for a user, group, or project. Defaults to a
  project access token, unless user or group name is specified.

  The expiration date of the token is calculated by adding the duration
  (default: 30 days) to the current date, with expiration occurring at midnight
  UTC on the calculated date. You can specify a different duration using days (d),
  weeks (w), or hours (h), or provide an explicit end date.

  The name of the token must be unique. The token is printed to stdout.

  Administrators can create full-featured personal access tokens for themselves and for other users.

  Non-administrators can create personal access tokens only for
  themselves (@me). These tokens must use the scope 'k8s_proxy'. For more
  information, see the GitLab documentation for the
  User tokens API.


  USAGE

    glab token create <name> [--flags]

  EXAMPLES

    # Create project access token for current project (default 30 days)
    glab token create --access-level developer --scope read_repository --scope read_registry my-project-token

    # Create project access token with 7 day lifetime
    glab token create --repo user/my-repo --access-level owner --scope api my-project-token --duration 7d

    # Create a group access token expiring in 2 weeks
    glab token create --group group/sub-group --access-level owner --scope api my-group-token --duration 2w

    # Create a personal access token for current user with 90 day lifetime
    glab token create --user @me --scope k8s_proxy my-personal-token --duration 90d

    # (administrator only) Create a personal access token for another user
    glab token create --user johndoe --scope api johns-personal-token --duration 180d

    # Create a token with explicit expiration date
    glab token create --access-level developer --scope api my-token --expires-at 2025-12-31

  FLAGS

    -A --access-level  Access level of the token: one of 'guest', 'reporter', 'developer', 'maintainer', 'owner'. (no)
    --description      Sets the token's description.
    -D --duration      Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at midnight UTC on the calculated date. (30d)
    -E --expires-at    Sets the token's expiration date and time, in YYYY-MM-DD format. If not specified, --duration is used. (0001-01-01)
    -g --group         Create a group access token. Ignored if a user or repository argument is set.
    -h --help          Show help for this command.
    --jq               Filter JSON output with a jq expression.
    -F --output        Format output as 'text' for the token value, 'json' for the actual API token structure. (text)
    -R --repo          Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -S --scope         Scopes for the token. Multiple scopes can be comma-separated or specified by repeating the flag. For a list, see https://docs.gitlab.com/security/tokens/access_token_scopes/. ([read_repository])
    -U --user          Create a personal access token. For the current user, use @me.

```

## glab token revoke

<!-- help-capture: 206ebab4f:a5ae4c8fe5bc -->

```text

  Revoke a user, group or project access token. If multiple tokens with the same name exist, you can specify
  the ID of the token.

  The output format can be either "JSON" or "text". The JSON output will show the meta information of the
  revoked token. The normal text output is a description of the revoked token name and ID.

  Administrators can revoke personal access tokens belonging to other users.


  USAGE

    glab token revoke <token-name|token-id> [--flags]

  EXAMPLES

    # Revoke a project access token of current project
    glab token revoke my-project-token

    # Revoke a project access token of a specific project
    glab token revoke --repo user/my-repo my-project-token

    # Revoke a group access token
    glab token revoke --group group/sub-group my-group-token

    # Revoke my personal access token
    glab token revoke --user @me my-personal-token

    # Revoke a personal access token of another user (administrator only)
    glab token revoke --user johndoe johns-personal-token

  FLAGS

    -g --group   Revoke group access token. Ignored if a user or repository argument is set.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. 'text' provides the name and ID of the revoked token; 'json' outputs the token with metadata. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -U --user    Revoke personal access token. Use @me for the current user.

```

## glab token rm

<!-- help-capture: 206ebab4f:f0fef3013df4 -->

```text

  Revoke a user, group or project access token. If multiple tokens with the same name exist, you can specify
  the ID of the token.

  The output format can be either "JSON" or "text". The JSON output will show the meta information of the
  revoked token. The normal text output is a description of the revoked token name and ID.

  Administrators can revoke personal access tokens belonging to other users.


  USAGE

    glab token revoke <token-name|token-id> [--flags]

  EXAMPLES

    # Revoke a project access token of current project
    glab token revoke my-project-token

    # Revoke a project access token of a specific project
    glab token revoke --repo user/my-repo my-project-token

    # Revoke a group access token
    glab token revoke --group group/sub-group my-group-token

    # Revoke my personal access token
    glab token revoke --user @me my-personal-token

    # Revoke a personal access token of another user (administrator only)
    glab token revoke --user johndoe johns-personal-token

  FLAGS

    -g --group   Revoke group access token. Ignored if a user or repository argument is set.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. 'text' provides the name and ID of the revoked token; 'json' outputs the token with metadata. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -U --user    Revoke personal access token. Use @me for the current user.

```

## glab token rot

<!-- help-capture: 206ebab4f:696eb5925f7e -->

```text

  Rotating a token revokes the existing token and creates a new one
  with a new secret value and expiration date.
  The old token stops working immediately, so you must update any client that uses
  it with the new value that this command returns.

  If multiple tokens share the same name, specify the token ID to select the correct one.

  The token expires at 00:00 UTC on a date calculated by adding the duration to today's date.
  The default duration is 30 days. You can specify a different duration in days (`d`),
  weeks (`w`), or hours (`h`).
  The `--duration` and `--expires-at` flags are mutually exclusive.

  Administrators can rotate personal access tokens that belong to other users.

  Use `--self` to rotate the token currently used for authentication. This command requires GitLab 17.9 or later.
  glab replaces the stored copy of that token for the host, in the keyring or the config file, so your next command
  keeps working. A token from an environment variable can't be updated, so glab warns on stderr and you must export the
  new value.


  USAGE

    glab token rotate [<token-name|token-id>] [--flags]

  EXAMPLES

    # Rotate project access token of current project (default 30 days)
    glab token rotate my-project-token

    # Rotate project access token with explicit expiration date
    glab token rotate --repo user/repo my-project-token --expires-at 2025-08-08

    # Rotate group access token with 7 day lifetime
    glab token rotate --group group/sub-group my-group-token --duration 7d

    # Rotate personal access token with 2 week lifetime
    glab token rotate --user @me my-personal-token --duration 2w

    # Rotate a personal access token of another user (administrator only)
    glab token rotate --user johndoe johns-personal-token --duration 90d

    # Rotate the current authentication token
    glab token rotate --self --duration 90d

  FLAGS

    -D --duration    Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at 00:00 UTC on the calculated date. (30d)
    -E --expires-at  Sets the token's expiration date and time, in YYYY-MM-DD format. If not specified, --duration is used. (0001-01-01)
    -g --group       Rotate group access token. Ignored if a user or repository argument is set.
    -h --help        Show help for this command.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as: text, json. 'text' provides the new token value; 'json' outputs the token with metadata. (text)
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --self           Rotate the access token currently used for authentication.
    -U --user        Rotate personal access token. Use @me for the current user.

```

## glab token rotate

<!-- help-capture: 206ebab4f:be03a98df5a6 -->

```text

  Rotating a token revokes the existing token and creates a new one
  with a new secret value and expiration date.
  The old token stops working immediately, so you must update any client that uses
  it with the new value that this command returns.

  If multiple tokens share the same name, specify the token ID to select the correct one.

  The token expires at 00:00 UTC on a date calculated by adding the duration to today's date.
  The default duration is 30 days. You can specify a different duration in days (`d`),
  weeks (`w`), or hours (`h`).
  The `--duration` and `--expires-at` flags are mutually exclusive.

  Administrators can rotate personal access tokens that belong to other users.

  Use `--self` to rotate the token currently used for authentication. This command requires GitLab 17.9 or later.
  glab replaces the stored copy of that token for the host, in the keyring or the config file, so your next command
  keeps working. A token from an environment variable can't be updated, so glab warns on stderr and you must export the
  new value.


  USAGE

    glab token rotate [<token-name|token-id>] [--flags]

  EXAMPLES

    # Rotate project access token of current project (default 30 days)
    glab token rotate my-project-token

    # Rotate project access token with explicit expiration date
    glab token rotate --repo user/repo my-project-token --expires-at 2025-08-08

    # Rotate group access token with 7 day lifetime
    glab token rotate --group group/sub-group my-group-token --duration 7d

    # Rotate personal access token with 2 week lifetime
    glab token rotate --user @me my-personal-token --duration 2w

    # Rotate a personal access token of another user (administrator only)
    glab token rotate --user johndoe johns-personal-token --duration 90d

    # Rotate the current authentication token
    glab token rotate --self --duration 90d

  FLAGS

    -D --duration    Sets the token lifetime in days. Accepts: days (30d), weeks (4w), or hours in multiples of 24 (24h, 168h, 720h). Maximum: 365d. The token expires at 00:00 UTC on the calculated date. (30d)
    -E --expires-at  Sets the token's expiration date and time, in YYYY-MM-DD format. If not specified, --duration is used. (0001-01-01)
    -g --group       Rotate group access token. Ignored if a user or repository argument is set.
    -h --help        Show help for this command.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as: text, json. 'text' provides the new token value; 'json' outputs the token with metadata. (text)
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --self           Rotate the access token currently used for authentication.
    -U --user        Rotate personal access token. Use @me for the current user.

```

