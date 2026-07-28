# glab securefile help

> Help output captured from `glab securefile --help` and its subcommands.

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

    -h --help                                              Show help for this command.
    -R --repo                                              Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## securefile create

```

  Provide the name to store the file under, followed by the local path
  to the file to upload.

  Secure files are stored outside the project's repository and not in
  version control. Both plain text and binary files are supported, up
  to a maximum size of 5 MB.

  By default, the file is uploaded to the current project. Use `--repo`
  to target another project.


  USAGE

    glab securefile create <name> <path> [--flags]

  EXAMPLES

    # Upload a secure file from a local path
    glab securefile create "newfile.txt" "securefiles/localfile.txt"

    # Upload using the 'upload' alias
    glab securefile upload "newfile.txt" "securefiles/localfile.txt"

    # Upload to another project
    glab securefile create "newfile.txt" "securefiles/localfile.txt" -R owner/repo

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## securefile download

```

  To download a single file, identify it by its numeric ID (as a positional
  argument or with `--id`) or by its name with `--name`. To download every
  secure file in the project, use `--all`.

  Use `--path` to save a single download to a specific filename, or
  `--output-dir` to choose the destination directory when downloading
  multiple files.

  By default, downloaded files are verified against their checksum.
  Use `--no-verify` to skip verification, or `--force-download` to keep
  files even when verification fails. Both options can allow corrupted
  or tampered files; use with caution.

  By default, files are downloaded from the current project. Use
  `--repo` to target another project.


  USAGE

    glab securefile download [<id> | --id <id> | --name <name>] [--flags]

  EXAMPLES

    # Download a file by ID (positional or flag)
    glab securefile download 1
    glab securefile download --id 1

    # Download a file by ID to a specific path
    glab securefile download 1 --path "securefiles/file.txt"

    # Download a file by name to the current directory
    glab securefile download --name my-secure-file.pem

    # Download a file by name to a chosen path
    glab securefile download --name my-secure-file.pem --path securefiles/some-other-name.pem

    # Download without verifying the checksum
    glab securefile download 1 --no-verify

    # Download all secure files in the project
    glab securefile download --all

    # Download all secure files to a specific directory
    glab securefile download --all --output-dir secure_files/

  FLAGS

    --all             Download all of a project's secure files. Files are downloaded with their original name and file extension.
    --force-download  Force download file(s) even if checksum verification fails. Warning: when enabled, this setting allows the download of files that are corrupt or tampered with.
    -h --help         Show help for this command.
    --id              Id of the secure file to download.
    --name            Name of the secure file to download. Saves the file with this name, or to the path specified by --path.
    --no-verify       Do not verify the checksum of the downloaded file(s). Warning: when enabled, this setting allows the download of files that are corrupt or tampered with.
    --output-dir      Output directory for files downloaded with --all. (.)
    -p --path         Path to download the secure file to, including filename and extension. (./downloaded.tmp)
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## securefile get

```

  Get details of a single secure file in a project, identified by its
  numeric ID. The response includes the file's name, checksum, and
  associated metadata.

  This command requires GitLab 18.0 or later.

  By default, the file is looked up in the current project. Use
  `--repo` to target another project.


  USAGE

    glab securefile get <id> [--flags]

  EXAMPLES

    # Get details of a secure file by ID
    glab securefile get 1

    # Get details using the 'show' alias
    glab securefile show 1

    # Get details from another project
    glab securefile get 1 -R owner/repo

  FLAGS

    -h --help  Show help for this command.
    --jq       Filter JSON output with a jq expression.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## securefile list

```

  List the secure files configured for a project. Use `--page` and
  `--per-page` to paginate the result.

  By default, files are listed for the current project. Use `--repo`
  to target another project.


  USAGE

    glab securefile list [--flags]

  EXAMPLES

    # List all secure files in the current project
    glab securefile list

    # Use the 'ls' alias
    glab securefile ls

    # List a specific page
    glab securefile list --page 2

    # List a specific page with a custom page size
    glab securefile list --page 2 --per-page 10

    # List files from another project
    glab securefile list -R owner/repo

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## securefile remove

```
Remove a secure file from a project.

USAGE
  glab securefile remove [<fileID> | --id <id> | --name <name>] [flags]

ALIASES
  rm
  delete

EXAMPLES
  # Remove a secure file by ID
  glab securefile remove 1
  glab securefile remove --id 1

  # Remove a secure file by name
  glab securefile remove --name example.txt

  # Skip the confirmation prompt
  glab securefile remove 1 -y
  glab securefile remove --name example.txt -y

  # Aliases
  glab securefile rm 1
  glab securefile delete --name example.txt

FLAGS
      --id int       ID of the secure file to remove.
      --name string  Name of the secure file to remove.
  -y, --yes          Skip the confirmation prompt.

INHERITED FLAGS
  -h, --help         Show help for this command.
  -R, --repo string  Select another repository. OWNER/REPO, GROUP/NAMESPACE/REPO, full URL, and Git URL are accepted.
```

## securefile update

```

  Update a secure file in a project, identified by its name.
  The command asks for confirmation before updating; use `-y` to skip
  the prompt in scripts.

  By default, the file is updated in the current project. Use `--repo`
  to target another project.

  If the file content is unchanged, no update is performed.

  Updating a secure file changes its ID. When you download the file afterward, reference it by `--name` instead of `--
  id`.


  USAGE

    glab securefile update <name> <path> [--flags]

  EXAMPLES

    # Update a secure file
    glab securefile update "file.txt" securefiles/localfile.txt

    # Skip the confirmation prompt
    glab securefile update "file.txt" securefiles/localfile.txt -y

    # Use the 'overwrite' alias
    glab securefile overwrite "file.txt" securefiles/localfile.txt

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes   Skip the confirmation prompt.

```
