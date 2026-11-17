# Captured glab-deploy-token help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab deploy-token

<!-- help-capture: 206ebab4f:9542c079412c -->

```text

  Manage the deploy tokens of a project or a group.

  Deploy tokens grant access to a repository, its container registry, and its package registry over HTTPS without being
  tied to a user account. They are commonly used by CI/CD jobs and external systems.

  These commands act on the current project. Use `--repo` to target a different project, or `--group` to act on a group
  instead. If `GITLAB_GROUP` is set and neither flag is given, these commands act on that group.


  USAGE

    glab deploy-token <command> [command] [--flags]

  COMMANDS

    create <name> [--flags]      Create a deploy token.
    delete <token-id> [--flags]  Delete a deploy token.
    get <token-id> [--flags]     Get a deploy token.
    list [--flags]               List deploy tokens.

  FLAGS

    -h --help                    Show help for this command.
    -R --repo                    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab deploy-token create

<!-- help-capture: 206ebab4f:e087fd035b68 -->

```text

  Create a deploy token for a project or a group.

  The token value is printed only once, when the token is created, and cannot be retrieved later. Use `--output json` to
  capture it from a script.

  A deploy token authenticates as a username and token pair, so both values from the output are needed to use it.

  The token does not expire unless `--expires-at` is given.

  Every token must be granted at least one scope with `--scope`. For the scopes you can grant, see
  https://docs.gitlab.com/user/project/deploy_tokens/#scope.


  USAGE

    glab deploy-token create <name> [--flags]

  EXAMPLES

    # Create a read-only deploy token for the current project
    glab deploy-token create ci-reader --scope read_repository

    # Create a token that can also pull images from the container registry
    glab deploy-token create ci-reader --scope read_repository --scope read_registry

    # Create a token for a specific project, with a custom username
    glab deploy-token create ci-reader --scope read_repository --username ci-reader --repo user/my-repo

    # Create a token that is valid until the end of 2027
    glab deploy-token create ci-reader --scope read_repository --expires-at 2028-01-01

    # Create a group deploy token
    glab deploy-token create ci-reader --scope read_repository --group group/sub-group

    # Create the token that CI/CD jobs receive as CI_DEPLOY_USER and CI_DEPLOY_PASSWORD
    glab deploy-token create gitlab-deploy-token --scope read_registry

    # Create a token and print its username and value from a script
    glab deploy-token create ci-reader --scope read_repository --output json --jq '"\(.username) \(.token)"'

  FLAGS

    -E --expires-at  Expiry of the token, as YYYY-MM-DD (00:00 UTC) or an RFC 3339 timestamp. The token does not expire if omitted.
    -g --group       Create a deploy token for a `group` instead of a project. Accepts a group ID or full path.
    -h --help        Show help for this command.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as: text, json. (text)
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -S --scope       Scope to grant the token. Multiple scopes can be comma-separated or specified by repeating the flag.
    --username       Username for the token. Defaults to 'gitlab+deploy-token-<id>'.

```

## glab deploy-token del

<!-- help-capture: 206ebab4f:27c38f317167 -->

```text

  Delete a deploy token of a project or a group, by its ID.

  The deletion is permanent and takes effect immediately. Anything authenticating with the token stops working.

  Deleting is not the revoke action from the GitLab UI, which the REST API does not expose. A revoked token stays listed
  and is reported as revoked, while a deleted token is gone from `glab deploy-token list` entirely.

  Token IDs come from `glab deploy-token list`.


  USAGE

    glab deploy-token delete <token-id> [--flags]

  EXAMPLES

    # Delete deploy token 42 of the current project, after confirming
    glab deploy-token delete 42

    # Delete it without a confirmation prompt
    glab deploy-token delete 42 --yes

    # Delete a deploy token of a specific project
    glab deploy-token delete 42 --repo user/my-repo

    # Delete a group's deploy token
    glab deploy-token delete 42 --group group/sub-group

  FLAGS

    -g --group  Delete a deploy token of a `group` instead of a project. Accepts a group ID or full path.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes    Skip the confirmation prompt.

```

## glab deploy-token delete

<!-- help-capture: 206ebab4f:c1bf57e1d757 -->

```text

  Delete a deploy token of a project or a group, by its ID.

  The deletion is permanent and takes effect immediately. Anything authenticating with the token stops working.

  Deleting is not the revoke action from the GitLab UI, which the REST API does not expose. A revoked token stays listed
  and is reported as revoked, while a deleted token is gone from `glab deploy-token list` entirely.

  Token IDs come from `glab deploy-token list`.


  USAGE

    glab deploy-token delete <token-id> [--flags]

  EXAMPLES

    # Delete deploy token 42 of the current project, after confirming
    glab deploy-token delete 42

    # Delete it without a confirmation prompt
    glab deploy-token delete 42 --yes

    # Delete a deploy token of a specific project
    glab deploy-token delete 42 --repo user/my-repo

    # Delete a group's deploy token
    glab deploy-token delete 42 --group group/sub-group

  FLAGS

    -g --group  Delete a deploy token of a `group` instead of a project. Accepts a group ID or full path.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes    Skip the confirmation prompt.

```

## glab deploy-token get

<!-- help-capture: 206ebab4f:f0b7dabfa142 -->

```text

  Get a single deploy token of a project or a group, by its ID.

  The output never contains the token value. A token value is shown only once, when the token is created.

  Token IDs come from `glab deploy-token list`.


  USAGE

    glab deploy-token get <token-id> [--flags]

  EXAMPLES

    # Get deploy token 42 of the current project
    glab deploy-token get 42

    # Get a deploy token of a specific project
    glab deploy-token get 42 --repo user/my-repo

    # Get a group's deploy token
    glab deploy-token get 42 --group group/sub-group

    # Get a deploy token as JSON
    glab deploy-token get 42 --output json

  FLAGS

    -g --group   Get a deploy token of the group <group> instead of a project.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab deploy-token list

<!-- help-capture: 206ebab4f:e16d69a1f1e4 -->

```text

  List the deploy tokens of a project, a group, or the instance.

  Pass `--instance` to list every deploy token on the instance. This requires administrator access, and `GITLAB_GROUP`
  does not apply.

  The output never contains the token value. A token value is shown only once, when the token is created.

  Tokens are listed with their expiry, and whether they have been revoked or have expired. Pass `--active` to list only
  the tokens that are still usable.


  USAGE

    glab deploy-token list [--flags]

  EXAMPLES

    # List the current project's deploy tokens
    glab deploy-token list

    # List the deploy tokens of a specific project
    glab deploy-token list --repo user/my-repo

    # List only the tokens that are neither revoked nor expired
    glab deploy-token list --active

    # List a group's deploy tokens
    glab deploy-token list --group group/sub-group

    # List every deploy token on the instance (administrator only)
    glab deploy-token list --instance

    # List the current project's deploy tokens as JSON
    glab deploy-token list --output json

  FLAGS

    -a --active    List only the tokens that are neither revoked nor expired.
    -g --group     List the deploy tokens of the group <group> instead of a project.
    -h --help      Show help for this command.
    -i --instance  List every deploy token on the instance instead of a project or group. Requires administrator access.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab deploy-token ls

<!-- help-capture: 206ebab4f:f89d3d5ed65c -->

```text

  List the deploy tokens of a project, a group, or the instance.

  Pass `--instance` to list every deploy token on the instance. This requires administrator access, and `GITLAB_GROUP`
  does not apply.

  The output never contains the token value. A token value is shown only once, when the token is created.

  Tokens are listed with their expiry, and whether they have been revoked or have expired. Pass `--active` to list only
  the tokens that are still usable.


  USAGE

    glab deploy-token list [--flags]

  EXAMPLES

    # List the current project's deploy tokens
    glab deploy-token list

    # List the deploy tokens of a specific project
    glab deploy-token list --repo user/my-repo

    # List only the tokens that are neither revoked nor expired
    glab deploy-token list --active

    # List a group's deploy tokens
    glab deploy-token list --group group/sub-group

    # List every deploy token on the instance (administrator only)
    glab deploy-token list --instance

    # List the current project's deploy tokens as JSON
    glab deploy-token list --output json

  FLAGS

    -a --active    List only the tokens that are neither revoked nor expired.
    -g --group     List the deploy tokens of the group <group> instead of a project.
    -h --help      Show help for this command.
    -i --instance  List every deploy token on the instance instead of a project or group. Requires administrator access.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

