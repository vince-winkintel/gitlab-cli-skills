# glab todo help

> Help surface based on the `glab` v1.92.0 documentation.

## todo

```
Manage your to-do list.

Examples

glab todo list
glab todo done 123
glab todo done --all

Subcommands

done
list
```

## todo list

```
List your to-do items.

glab todo list [flags]

Aliases

ls

Examples

glab todo list
glab todo list --state=done
glab todo list --action=assigned
glab todo list --type=MergeRequest
glab todo list --output=json

Options

  -a, --action string   Filter by action: assigned, mentioned, build_failed, marked, approval_required, directly_addressed.
  -F, --output string   Format output as: text, json. (default "text")
  -p, --page int        Page number. (default 1)
  -P, --per-page int    Number of items to list per page. (default 30)
  -s, --state string    Filter by state: pending, done, all. (default "pending")
  -t, --type string     Filter by target type: Issue, MergeRequest.
  -h, --help            Show help for this command.
```

## todo done

```
Mark a to-do item as done.

glab todo done [<id>] [flags]

Examples

glab todo done 123
glab todo done --all

Options

      --all   Mark all pending to-do items as done.
  -h, --help  Show help for this command.
```
