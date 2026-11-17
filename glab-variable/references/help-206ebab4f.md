# Captured glab-variable help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab var

<!-- help-capture: 206ebab4f:467180b07ca5 -->

```text

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
    -R --repo                       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab var create

<!-- help-capture: 206ebab4f:14f3d5856ea0 -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab var delete

<!-- help-capture: 206ebab4f:0ae719add1c3 -->

```text

  Deletes a variable by key. Use `--group` to delete a group
  variable instead of a project variable.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.


  USAGE

    glab variable delete <key> [--flags]

  EXAMPLES

    glab variable delete VAR_NAME
    glab variable delete VAR_NAME --scope=prod
    glab variable delete VARNAME -g mygroup

    # Delete a group variable in the production environment.
    glab variable delete VARNAME -g mygroup --scope=prod

  FLAGS

    -g --group  Delete variable from a group.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope  The 'environment_scope' of the variable. Options: all (*), or specific environments. (*)

```

## glab var ex

<!-- help-capture: 206ebab4f:86077885cb01 -->

```text

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

## glab var export

<!-- help-capture: 206ebab4f:11079d7a630f -->

```text

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

## glab var get

<!-- help-capture: 206ebab4f:66741fe3cff0 -->

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

## glab var im

<!-- help-capture: 206ebab4f:8dd15eb7240b -->

```text

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

## glab var import

<!-- help-capture: 206ebab4f:65dc7e49f2f7 -->

```text

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

## glab var list

<!-- help-capture: 206ebab4f:91839e7c8f1b -->

```text

  Defaults to the current project. Use `--group` to list variables
  for a group, or `--instance` to list instance variables.


  USAGE

    glab variable list [--flags]

  EXAMPLES

    glab variable list
    glab variable list -i
    glab variable list --per-page 100 --page 1
    glab variable list --group gitlab-org
    glab variable list --group gitlab-org --per-page 100

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    -i --instance  Display instance variables.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab var ls

<!-- help-capture: 206ebab4f:6ca65759bd59 -->

```text

  Defaults to the current project. Use `--group` to list variables
  for a group, or `--instance` to list instance variables.


  USAGE

    glab variable list [--flags]

  EXAMPLES

    glab variable list
    glab variable list -i
    glab variable list --per-page 100 --page 1
    glab variable list --group gitlab-org
    glab variable list --group gitlab-org --per-page 100

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    -i --instance  Display instance variables.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab var new

<!-- help-capture: 206ebab4f:eff1ff225c48 -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab var remove

<!-- help-capture: 206ebab4f:bfd40483ae6f -->

```text

  Deletes a variable by key. Use `--group` to delete a group
  variable instead of a project variable.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.


  USAGE

    glab variable delete <key> [--flags]

  EXAMPLES

    glab variable delete VAR_NAME
    glab variable delete VAR_NAME --scope=prod
    glab variable delete VARNAME -g mygroup

    # Delete a group variable in the production environment.
    glab variable delete VARNAME -g mygroup --scope=prod

  FLAGS

    -g --group  Delete variable from a group.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope  The 'environment_scope' of the variable. Options: all (*), or specific environments. (*)

```

## glab var set

<!-- help-capture: 206ebab4f:acab842d13ff -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab var update

<!-- help-capture: 206ebab4f:48f204a1cded -->

```text

  You can pass the variable value from standard input. Use `--group`
  to update a variable for a group instead of the current project.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.

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

    # Update a group variable in the production environment.
    glab variable update GROUP_TOKEN -g mygroup --scope prod --value "some value"

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

## glab variable

<!-- help-capture: 206ebab4f:0e323ff1e4fd -->

```text

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
    -R --repo                       Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab variable create

<!-- help-capture: 206ebab4f:22f46f801237 -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab variable delete

<!-- help-capture: 206ebab4f:6ac5fdf79ec7 -->

```text

  Deletes a variable by key. Use `--group` to delete a group
  variable instead of a project variable.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.


  USAGE

    glab variable delete <key> [--flags]

  EXAMPLES

    glab variable delete VAR_NAME
    glab variable delete VAR_NAME --scope=prod
    glab variable delete VARNAME -g mygroup

    # Delete a group variable in the production environment.
    glab variable delete VARNAME -g mygroup --scope=prod

  FLAGS

    -g --group  Delete variable from a group.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope  The 'environment_scope' of the variable. Options: all (*), or specific environments. (*)

```

## glab variable ex

<!-- help-capture: 206ebab4f:43d806b6ea4f -->

```text

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

## glab variable export

<!-- help-capture: 206ebab4f:6092fa3bc2ae -->

```text

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

## glab variable get

<!-- help-capture: 206ebab4f:769a27934f7f -->

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

## glab variable im

<!-- help-capture: 206ebab4f:17f53a0536da -->

```text

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

## glab variable import

<!-- help-capture: 206ebab4f:e1d8130c8a31 -->

```text

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

## glab variable list

<!-- help-capture: 206ebab4f:04e9764f9afc -->

```text

  Defaults to the current project. Use `--group` to list variables
  for a group, or `--instance` to list instance variables.


  USAGE

    glab variable list [--flags]

  EXAMPLES

    glab variable list
    glab variable list -i
    glab variable list --per-page 100 --page 1
    glab variable list --group gitlab-org
    glab variable list --group gitlab-org --per-page 100

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    -i --instance  Display instance variables.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab variable ls

<!-- help-capture: 206ebab4f:f089af79c34f -->

```text

  Defaults to the current project. Use `--group` to list variables
  for a group, or `--instance` to list instance variables.


  USAGE

    glab variable list [--flags]

  EXAMPLES

    glab variable list
    glab variable list -i
    glab variable list --per-page 100 --page 1
    glab variable list --group gitlab-org
    glab variable list --group gitlab-org --per-page 100

  FLAGS

    -g --group     Select a group or subgroup. Ignored if a repository argument is set.
    -h --help      Show help for this command.
    -i --instance  Display instance variables.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab variable new

<!-- help-capture: 206ebab4f:96ef227c280a -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab variable remove

<!-- help-capture: 206ebab4f:c1b7832fb79a -->

```text

  Deletes a variable by key. Use `--group` to delete a group
  variable instead of a project variable.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.


  USAGE

    glab variable delete <key> [--flags]

  EXAMPLES

    glab variable delete VAR_NAME
    glab variable delete VAR_NAME --scope=prod
    glab variable delete VARNAME -g mygroup

    # Delete a group variable in the production environment.
    glab variable delete VARNAME -g mygroup --scope=prod

  FLAGS

    -g --group  Delete variable from a group.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope  The 'environment_scope' of the variable. Options: all (*), or specific environments. (*)

```

## glab variable set

<!-- help-capture: 206ebab4f:35c0034e326b -->

```text

  You can pass the variable value from standard input. Use `--group`
  to set a variable for a group instead of the current project.


  USAGE

    glab variable set <key> <value> [--flags]

  EXAMPLES

    glab variable set WITH_ARG "some value"
    glab variable set WITH_DESC "some value" --description "some description"
    glab variable set FROM_FLAG -v "some value"
    glab variable set FROM_ENV_WITH_ARG "${ENV_VAR}"
    glab variable set FROM_ENV_WITH_FLAG -v"${ENV_VAR}"
    glab variable set FROM_FILE < secret.txt
    cat file.txt | glab variable set SERVER_TOKEN
    cat token.txt | glab variable set GROUP_TOKEN -g mygroup --scope=prod

  FLAGS

    -d --description  Set description of a variable.
    -g --group        Set variable for a group.
    -h --help         Show help for this command.
    --hidden          Whether the variable is hidden.
    -m --masked       Whether the variable is masked.
    -p --protected    Whether the variable is protected.
    -r --raw          Whether the variable is treated as a raw string.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -s --scope        The environment_scope of the variable. Values: all (*), or specific environments. (*)
    -t --type         The type of a variable: env_var, file. (env_var)
    -v --value        The value of a variable.

```

## glab variable update

<!-- help-capture: 206ebab4f:88743fd97856 -->

```text

  You can pass the variable value from standard input. Use `--group`
  to update a variable for a group instead of the current project.

  Use `--scope` to select the environment scope of the project or
  group variable. The default scope is `*`. Environment scopes for
  group variables require GitLab Premium or Ultimate.

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

    # Update a group variable in the production environment.
    glab variable update GROUP_TOKEN -g mygroup --scope prod --value "some value"

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

