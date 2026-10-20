# glab variable help

> Capture key `d43ccacec`: checksum-verified macOS arm64 release binary, source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`, binary archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`. Marked help preserves all renderer output except trailing spaces/tabs; unmarked blocks retain their stated older provenance.

> Help output captured from `glab variable --help` and its subcommands.

```

  Variables store configuration and secrets used by CI/CD pipelines.

  Each subcommand acts on the current project by default. Use
  `--group` to manage a group's variables instead.

  USAGE

    glab variable [command] [--flags]

  COMMANDS

    delete <key> [--flags]          Delete a variable for a project or group.
    export [--flags]                Export variables from a project or group.
    get <key> [--flags]             Get a variable for a project or group.
    import [--flags]                Import variables from a JSON file or standard input.
    list [--flags]                  List variables for a project or group.
    set <key> <value> [--flags]     Create a new variable for a project or group.
    update <key> <value> [--flags]  Update an existing variable for a project or group.

  FLAGS

    -h --help                       Show help for this command.
    -R --repo                       Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## variable delete

```

  Delete a variable for a project or group.

  USAGE

    glab variable delete <key> [--flags]

  EXAMPLES

    $ glab variable delete VAR_NAME
    $ glab variable delete VAR_NAME --scope=prod
    $ glab variable delete VARNAME -g mygroup

  FLAGS

    -g --group  Delete variable from a group.
    -h --help   Show help for this command.
    -R --repo   Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -s --scope  The 'environment_scope' of the variable. Options: all (*), or specific environments. (*)
```

## variable export

```

  Defaults to the current project. Use `--group` to export
  variables for a group. Use `--output` to set the format:
  `json` (default), `env` (KEY=VALUE pairs), or
  `export` (shell export statements).


  USAGE

    glab variable export [--flags]

  EXAMPLES

    glab variable export
    glab variable export --per-page 1000 --page 1
    glab variable export --group gitlab-org
    glab variable export --group gitlab-org --per-page 1000 --page 1
    glab variable export --output json
    glab variable export --output env
    glab variable export --output export

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: json, export, env. (json)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (100)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope     The environment_scope of the variables. Values: '*' (default), or specific environments. (*)

```

## variable get

> Capture `d43ccacec` (key above).

```text

  Prints the value of a single variable by key. Use `--scope` to
  select a variable in a specific environment, or `--group` to read a
  group variable instead.

  By default the command reads one level only. Pass `--inherited` to
  fall back to the groups above the project and then to the instance,
  in the order CI resolves a variable: the project first, then each
  parent group closest first, then instance variables.

  A level that does not define the key, or that you cannot read, is
  skipped. Instance variables apply to every environment, so
  `--scope` does not filter them.


  USAGE

    glab variable get <key> [--flags]

  EXAMPLES

    glab variable get VAR_KEY
    glab variable get -g GROUP VAR_KEY
    glab variable get -s SCOPE VAR_KEY

    # Read the project, then its parent groups, then the instance
    glab variable get --inherited VAR_KEY

  FLAGS

    -g --group   Get variable for a group.
    -h --help    Show help for this command.
    --inherited  If the key is not defined at the selected level, look in the groups above it, then in instance variables.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope   The environment_scope of the variable. Values: all (*), or specific environments. (*)

```

## variable import

```

  The inverse of `glab variable export`. Reads a JSON array of
  variable objects, in the same shape `export --output json` emits.

  The command:

  - Reads from standard input, or from a file with `--input-file`.
  - Imports into the current project by default. Use `--group` to
    import into a group instead.
  - Stops with an error if a variable already exists. Pass
    `--skip-existing` to skip those and continue.

  Hidden variables' values aren't included in `export` output,
  so re-importing one is skipped with a warning. Set its value again
  with `glab variable set --hidden`.


  USAGE

    glab variable import [--flags]

  EXAMPLES

    # Pipe an export straight into an import, to restore the same project
    glab variable export | glab variable import

    # Import variables from a saved file instead of standard input
    glab variable import --input-file variables.json

    # Import into a group instead of the current project
    glab variable export --group gitlab-org | glab variable import --group gitlab-org

    # Skip variables that already exist instead of failing
    glab variable import --input-file variables.json --skip-existing

  FLAGS

    -g --group       Select a group or subgroup. Ignored if a repository argument is set.
    -h --help        Show help for this command.
    -i --input-file  Read the variables JSON from this file instead of standard input.
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --skip-existing  Skip variables that already exist instead of failing.

```

## variable list

```

  List variables for a project or group.

  USAGE

    glab variable list [--flags]

  EXAMPLES

    $ glab variable list
    $ glab variable list -i
    $ glab variable list --per-page 100 --page 1
    $ glab variable list --group gitlab-org
    $ glab variable list --group gitlab-org --per-page 100

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    -i --instance  Display instance variables.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## variable set

```

  Create a new variable for a project or group.

  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    $ glab variable set WITH_ARG "some value"
    $ glab variable set WITH_DESC "some value" --description "some description"
    $ glab variable set FROM_FLAG -v "some value"
    $ glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    $ glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    $ glab variable set FROM_FILE < secret.txt
    $ cat file.txt | glab variable set SERVER_TOKEN
    $ cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.
```

## variable update

> Capture `d43ccacec` (key above).

```text

  You can pass the variable value from standard input. Use `--group`
  to update a variable for a group instead of the current project.
  The `--scope` flag does not apply to group variables.

  Only the attributes you pass are changed. For example, `--protected`,
  `--masked`, `--raw`, `--type` and `--description` keep their
  current values unless you set them. To turn a boolean attribute off, use
  `--protected=false`.


  USAGE

    glab variable update <key> <value> [--flags]

  EXAMPLES

    glab variable update WITH_ARG "some value"
    glab variable update FROM_FLAG -v "some value"
    glab variable update FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable update FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable update FROM_FILE < secret.txt
    cat file.txt | glab variable update SERVER_TOKEN
    cat token.txt | glab variable update GROUP_TOKEN -g mygroup

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```
