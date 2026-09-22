# glab snippet help

> Help output captured from the checksum-verified glab v1.119.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed. The release archive SHA-256 is `d9cddd1dbe9a8bea8d5709f90a9ac13c3dd3eb0d0e94e3bc4fae6b27abd6a3db`.

## snippet

```text

  Snippets store and share small pieces of code or text. A snippet can
  belong to a project, or to your personal account when you pass
  `--personal`.

  To view and edit existing snippets, use the GitLab UI or `glab api` with the Project snippets API or personal Snippets
  API.


  USAGE

    glab snippet <command> [command] [--flags]

  EXAMPLES

    glab snippet create --title "Title of the snippet" --filename "main.go"

  COMMANDS

    create  -t <title> <file1>                                        [<file2>...] [--flags]  Create a new snippet.
    glab snippet create  -t <title> -f <filename>  # reads from stdin

  FLAGS

    -h --help                                                                                 Show help for this command.
    -R --repo                                                                                 Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## snippet create

```text

  Provide one or more file paths to upload, or pass `--filename` and
  pipe content from standard input.

  Snippets are created in the current project by default. Use
  `--personal` to create the snippet in your personal account instead,
  and `--visibility` to control who can see it.


  USAGE

    glab snippet create -t <title> <file1> glab snippet create -t <title> -f <filename> # reads from stdin
    [<file2>...] [--flags]

  EXAMPLES

    glab snippet create script.py --title "Title of the snippet"
    echo "package main" | glab snippet new --title "Title of the snippet" --filename "main.go"
    glab snippet create -t Title -f "different.go" -d Description main.go
    glab snippet create -t Title -f "different.go" -d Description --filename different.go main.go
    glab snippet create --personal --title "Personal snippet" script.py

  FLAGS

    -d --description  Description of the snippet. Set to "-" to open an editor.
    -f --filename     Filename of the snippet in GitLab.
    -h --help         Show help for this command.
    -p --personal     Create a personal snippet.
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title        (Required) Title of the snippet.
    -v --visibility   Limit by visibility: 'public', 'internal', or 'private'. (private)

```
