# Captured glab-todo help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab todo

<!-- help-capture: 206ebab4f:eee4da49d2de -->

```text

  Your to-do list collects the items that need your attention, such as
  issues and merge requests where you were assigned, mentioned, or
  asked to review.

  List pending items, then mark them as done individually or all at once.


  USAGE

    glab todo <command> [command] [--flags]

  EXAMPLES

    glab todo list
    glab todo done 123
    glab todo done --all

  COMMANDS

    done [<id>] [--flags]  Mark a to-do item as done.
    list [--flags]         List your to-do items.

  FLAGS

    -h --help              Show help for this command.

```

## glab todo done

<!-- help-capture: 206ebab4f:4ba4732bb964 -->

```text

  Pass a to-do item's ID to mark that single item as done, or use
  `--all` to mark every pending item as done at once.

  Find item IDs with `glab todo list`.


  USAGE

    glab todo done [<id>] [--flags]

  EXAMPLES

    glab todo done 123
    glab todo done --all

  FLAGS

    --all      Mark all pending to-do items as done.
    -h --help  Show help for this command.

```

## glab todo list

<!-- help-capture: 206ebab4f:864bbb0e53ef -->

```text

  By default, lists your pending to-do items. Use `--state` to
  show done or all items instead.

  Narrow the results with `--action` to filter by why an item was
  created, or `--type` to filter by its target type.


  USAGE

    glab todo list [--flags]

  EXAMPLES

    glab todo list
    glab todo list --state=done
    glab todo list --action=assigned
    glab todo list --type=MergeRequest
    glab todo list --output=json

  FLAGS

    -a --action    Filter by action: assigned, mentioned, build_failed, marked, approval_required, directly_addressed.
    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -s --state     Filter by state: pending, done, all. (pending)
    -t --type      Filter by target type: Issue, MergeRequest.

```

## glab todo ls

<!-- help-capture: 206ebab4f:3545e3be2142 -->

```text

  By default, lists your pending to-do items. Use `--state` to
  show done or all items instead.

  Narrow the results with `--action` to filter by why an item was
  created, or `--type` to filter by its target type.


  USAGE

    glab todo list [--flags]

  EXAMPLES

    glab todo list
    glab todo list --state=done
    glab todo list --action=assigned
    glab todo list --type=MergeRequest
    glab todo list --output=json

  FLAGS

    -a --action    Filter by action: assigned, mentioned, build_failed, marked, approval_required, directly_addressed.
    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -s --state     Filter by state: pending, done, all. (pending)
    -t --type      Filter by target type: Issue, MergeRequest.

```

