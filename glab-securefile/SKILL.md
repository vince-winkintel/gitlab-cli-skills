---
name: glab-securefile
description: Manage secure files for CI/CD including upload, update, download, list, and delete operations. Use when storing or replacing sensitive files for pipelines, managing certificates, or handling secure configuration files. Triggers on secure file, CI secrets, certificates, overwrite secure file, secure config.
---

# glab securefile

## Overview

```

  Store up to 100 files for secure use in CI/CD pipelines. Secure files are                                             
  stored outside of your project's repository, not in version control.                                                  
  It is safe to store sensitive information in these files. Both plain text                                             
  and binary files are supported, but they must be smaller than 5 MB.                                                   
                                                                                                                        
         
  USAGE  
         
    glab securefile <command> [command] [--flags]  
            
  COMMANDS  
            
    create <name> <path>                                   Upload a new secure file to a project.
    download [<id> | --id <id> | --name <name>] [--flags]  Download one or more secure files from a project.
    get <id> [--flags]                                     Get details of a secure file by ID.
    list [--flags]                                         List secure files in a project.
    remove [<id> | --id <id> | --name <name>] [--flags]    Remove a secure file from a project.
    update <name> <path> [--flags]                         Update a secure file in a project.
         
  FLAGS  
         
    -h --help                          Show help for this command.
    -R --repo                          Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab securefile --help
```

## Removing secure files

Secure-file deletion accepts a positional numeric ID, `--id`, or an exact file name via `--name`:

```bash
# Interactive confirmation
glab securefile remove 1
glab securefile remove --id 1
glab securefile remove --name signing-certificate.p12

# Approved non-interactive deletion
glab securefile remove --name signing-certificate.p12 --yes
```

Deletion is permanent. In non-interactive environments, `--yes` / `-y` is required. Resolve and verify the intended project with `-R/--repo` before deleting, and prefer an ID when duplicate or ambiguous naming is possible.

## Updating secure files

Update a secure file by its exact stored name and a local replacement path. The command asks for confirmation unless `--yes` / `-y` is set; `overwrite` is an alias.

```bash
# Interactive update
glab securefile update signing-certificate.p12 ./replacement.p12

# Approved non-interactive update in an explicit project
glab securefile update signing-certificate.p12 ./replacement.p12 \
  -R group/project --yes
```

No update occurs when the content is unchanged. A successful update changes the secure file's ID, so subsequent workflows should resolve/download it by `--name` or refresh the ID instead of reusing a stale ID. Confirm the target project, file name, and replacement path before bypassing the prompt.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
