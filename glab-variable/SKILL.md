---
name: glab-variable
description: Manage CI/CD variables at project and group level including create, update, import, export, list, and delete operations. Use when setting environment variables for pipelines, managing secrets, migrating variables, or configuring CI/CD variables. Triggers on variable, CI variable, environment variable, secrets, variable import, CI/CD config.
---

# glab variable

## Overview

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

## Quick start

```bash
glab variable --help
```

## Export and import variables

`glab variable import` consumes the same JSON array shape emitted by `glab variable export --output json`. It reads standard input by default or a file passed with `--input-file` / `-i`.

```bash
# Preview and preserve an export before importing it elsewhere
glab variable export --output json > variables.json
glab variable import --input-file variables.json -R group/target-project

# Pipe between groups
glab variable export --group source-group |
  glab variable import --group target-group

# Continue when target variables already exist
glab variable import --input-file variables.json --skip-existing
```

Import stops when a target variable already exists unless `--skip-existing` is set. Hidden variable values are omitted from exports, so those entries are skipped with a warning during import; recreate their values explicitly with `glab variable set --hidden` from an approved secret source. Treat export files as sensitive, keep them out of version control, and verify the target project or group before importing.

## Masked and hidden group variables

`glab variable set` now sends `--masked` and `--hidden` correctly for group-level variables. Use explicit flags, verify the target group, and never print the value during confirmation:

```bash
glab variable set DEPLOY_TOKEN "$DEPLOY_TOKEN" \
  --group group/subgroup \
  --masked \
  --hidden \
  --protected

# Verify metadata without exposing the value
glab variable get DEPLOY_TOKEN --group group/subgroup --output json
```

Masking and hiding are server-enforced properties, not substitutes for least privilege or rotation. If GitLab rejects a value because it does not satisfy masking rules, do not weaken the setting silently; fix the value format or get explicit operator approval for a different policy.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
