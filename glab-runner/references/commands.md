# glab runner command reference

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

## runner

<!-- help-capture: 685c1cbd7:d1391781da43 -->

```text

  Manages GitLab CI/CD runners for projects, groups, or the entire instance.


  USAGE

    glab runner <command> [command] [--flags]

  COMMANDS

    assign <runner-id> [--flags]    Assign a runner to a project.
    delete <runner-id> [--flags]    Delete a runner.
    jobs <runner-id> [--flags]      List jobs processed by a runner.
    list [--flags]                  List runners.
    managers <runner-id> [--flags]  List runner managers.
    unassign <runner-id> [--flags]  Unassign a runner from a project.
    update <runner-id> [--flags]    Update a runner.

  FLAGS

    -h --help                       Show help for this command.

```

## runner list

<!-- help-capture: 685c1cbd7:b9cf4fbe0add -->

```text

  List runners for a project (default), group, or instance.

  Instance scope requires administrator access.


  USAGE

    glab runner list [--flags]

  EXAMPLES

    # List runners for the current project
    glab runner list

    # List runners for a specific project
    glab runner list -R owner/repo

    # List runners for a group
    glab runner list --group mygroup

    # List runners as JSON
    glab runner list --output json

  FLAGS

    -g --group     List runners for a group. Ignored if -R/--repo is set.
    -h --help      Show help for this command.
    -i --instance  List all runners available to the user (instance scope).
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## runner jobs

<!-- help-capture: 685c1cbd7:49ac3fcbf274 -->

```text

  Lists jobs processed by the specified runner, including jobs that are currently running.

  Requires the Maintainer or Owner role for the project.


  USAGE

    glab runner jobs <runner-id> [--flags]

  EXAMPLES

    # List all jobs for runner 9
    glab runner jobs 9

    # List only running jobs
    glab runner jobs 9 --status running

    # List jobs as JSON
    glab runner jobs 9 --output json

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    --order-by     Order jobs by: id. (id)
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --sort         Sort order: asc or desc. (desc)
    --status       Filter jobs by status: running, success, failed, canceled.

```

