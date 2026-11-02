# glab deploy-token command reference

> **Help provenance.** An adjacent `help-capture` marker selects only its matching key below; an explicit per-block capture label applies only when no marker is present. Historical unmarked notes never override either selector. Keyed captures use checksum-verified official macOS arm64 glab binaries. Complete renderer output is preserved except trailing spaces/tabs: indentation, blank lines, heading/flag casing, product spelling (including `Gitlab`), examples, wrapping, and truncation are unchanged. Unmarked legacy captures retain the scoped normalization and older-version guidance stated below.
>
> - `2e352a17e`: source commit `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; archive SHA-256 `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.
> - `685c1cbd7`: source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`.

## deploy-token

<!-- help-capture: 2e352a17e:29cbd58744ab -->

```text

  Manage the deploy tokens of a project or a group.

  Deploy tokens grant access to a repository, its container registry, and its package registry over HTTPS without being
  tied to a user account. They are commonly used by CI/CD jobs and external systems.

  These commands act on the current project. Use `--repo` to target a different project, or `--group` to act on a group
  instead. If `GITLAB_GROUP` is set and neither flag is given, these commands act on that group.


  USAGE

    glab deploy-token <command> [command] [--flags]

  COMMANDS

    create <name> [--flags]   Create a deploy token.
    get <token-id> [--flags]  Get a deploy token.
    list [--flags]            List deploy tokens.

  FLAGS

    -h --help                 Show help for this command.
    -R --repo                 Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## deploy-token list

<!-- help-capture: 2e352a17e:2b37798e9488 -->

```text

  List the deploy tokens of a project or a group.

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

    # List the current project's deploy tokens as JSON
    glab deploy-token list --output json

  FLAGS

    -a --active  List only the tokens that are neither revoked nor expired.
    -g --group   List the deploy tokens of the group <group> instead of a project.
    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```


## deploy-token create

<!-- help-capture: 2e352a17e:5a2e5b5dad75 -->

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

## deploy-token get

<!-- help-capture: 2e352a17e:2ebef599375e -->

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
