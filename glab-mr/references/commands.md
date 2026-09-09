# glab mr help

> Affected help output refreshed from the checksum-verified glab v1.117.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

## Table of Contents

**Most Used Commands:**
- [mr approve](#mr-approve) - Approve merge requests
- [mr checkout](#mr-checkout) - Check out an MR locally
- [mr create](#mr-create) - Create new MR
- [mr diff](#mr-diff) - View changes in MR
- [mr list](#mr-list) - List merge requests
- [mr merge](#mr-merge) - Merge/accept MR
- [mr note](#mr-note) - Add comment to MR
- [mr view](#mr-view) - Display MR details

**All Commands:**
- [mr approve](#mr-approve) | [mr approvers](#mr-approvers) | [mr checkout](#mr-checkout) | [mr close](#mr-close)
- [mr create](#mr-create) | [mr delete](#mr-delete) | [mr diff](#mr-diff) | [mr for](#mr-for)
- [mr issues](#mr-issues) | [mr list](#mr-list) | [mr merge](#mr-merge) | [mr note](#mr-note)
- [mr note create](#mr-note-create) | [mr note update](#mr-note-update) | [mr note list](#mr-note-list)
- [mr rebase](#mr-rebase) | [mr reopen](#mr-reopen) | [mr revoke](#mr-revoke) | [mr subscribe](#mr-subscribe)
- [mr todo](#mr-todo) | [mr unsubscribe](#mr-unsubscribe) | [mr update](#mr-update) | [mr view](#mr-view)

---

## Overview

```

  Create, view, and manage merge requests.

  USAGE

    glab mr <command> [command] [--flags]

  EXAMPLES

    $ glab mr create --fill --label bugfix
    $ glab mr merge 123
    $ glab mr note -m "needs to do X before it can be merged" branch-foo

  COMMANDS

    approve {<id> | <branch>} [--flags]           Approve merge requests.
    approvers [<id> | <branch>] [--flags]         List eligible approvers for merge requests in any state.
    checkout [<id> | <branch> | <url>] [--flags]  Check out an open merge request.
    close [<id> | <branch>]                       Close a merge request.
    create [--flags]                              Create a new merge request.
    delete [<id> | <branch>]                      Delete a merge request.
    diff [<id> | <branch>] [--flags]              View changes in a merge request.
    for [--flags]                                 Create a new merge request for an issue.
    issues [<id> | <branch>]                      Get issues related to a particular merge request.
    list [--flags]                                List merge requests.
    merge {<id> | <branch>} [--flags]             Merge or accept a merge request.
    note [<id> | <branch>] [--flags]              Add a comment or note to a merge request.
    rebase [<id> | <branch>] [--flags]            Rebase the source branch of a merge request against its target branch.
    reopen [<id>... | <branch>...]                Reopen a merge request.
    revoke [<id> | <branch>]                      Revoke approval on a merge request.
    subscribe [<id> | <branch>]                   Subscribe to a merge request.
    todo [<id> | <branch>]                        Add a to-do item to merge request.
    unsubscribe [<id> | <branch>]                 Unsubscribe from a merge request.
    update [<id> | <branch>] [--flags]            Update a merge request.
    view {<id> | <branch>} [--flags]              Display the title, body, and other information about a merge request.

  FLAGS

    -h --help                                     Show help for this command.
    -R --repo                                     Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr approve

```

  Approve merge requests.

  USAGE

    glab mr approve {<id> | <branch>} [--flags]

  EXAMPLES

    $ glab mr approve 235
    $ glab mr approve 123 345
    $ glab mr approve branch-1
    $ glab mr approve branch-2 branch-3

    # Finds open merge request from current branch and approves it
    $ glab mr approve

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -s --sha   Sha, which must match the SHA of the HEAD commit of the merge request.
```

## mr approvers

```

  List eligible approvers for merge requests in any state.

  USAGE

    glab mr approvers [<id> | <branch>] [--flags]

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr checkout

```

  Check out an open merge request.

  USAGE

    glab mr checkout [<id> | <branch> | <url>] [--flags]

  EXAMPLES

    $ glab mr checkout 1
    $ glab mr checkout branch
    $ glab mr checkout 12 --branch todo-fix
    $ glab mr checkout new-feature --set-upstream-to=upstream/main
    $ glab mr checkout https://gitlab.com/gitlab-org/cli/-/merge_requests/1234

    # Uses the checked-out branch
    $ glab mr checkout

  FLAGS

    -b --branch           Check out merge request with name <branch>.
    -h --help             Show help for this command.
    -R --repo             Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -u --set-upstream-to  Set tracking of checked-out branch to [REMOTE/]BRANCH.
```

## mr close

```

  Close a merge request.

  USAGE

    glab mr close [<id> | <branch>] [--flags]

  EXAMPLES

    $ glab mr close 1

    # Close multiple merge requests at once
    $ glab mr close 1 2 3 4

    # Use the checked-out branch
    $ glab mr close

    $ glab mr close branch
    $ glab mr close username:branch
    $ glab mr close branch -R another/repo

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr create

```

  Defaults to the current branch as the source branch. Use `--fill`
  to automatically fill the title and description from the commit history. Use
  `--draft` to create a draft merge request.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Files upload to the target project, so the references resolve even for
  a merge request from a fork.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

  The `--recover` flag is an experiment: it might be unstable or
  removed at any time, and is not ready for production use. For more
  information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mr create [--flags]

  EXAMPLES

    # Create a merge request interactively from the current branch
    glab mr new

    # Assign a user and set a title without prompting for description
    glab mr create -a username -t "fix annoying bug"

    # Fill title and description from commits, mark as draft, add a label
    glab mr create -f --draft --label RFC

    # Fill from commits and preview the compare page in the browser
    glab mr create --fill --web

    # Fill from commits, expand each commit body into the description
    glab mr create --fill --fill-commit-body --yes

    # Use a merge request template for the description
    glab mr create -t "Fix login bug" --template bug_fix
    glab mr create -t "Security patch" --template security_fix.md --yes

    # Create against another project without a local clone. All inputs must be passed as flags; no --push, --fill, …
    glab mr create --repo group/project --source-branch feature-branch --target-branch main --title "Add feature" -…

    # Create a fork merge request from your fork into the upstream project, without a local clone.
    glab mr create --repo upstream/project --head your-namespace/project --source-branch feature-branch --target-br…

    # Read the description from a file
    glab mr create -t "Fix login bug" --description-file description.md

    # Read the description from standard input
    cat description.md | glab mr create -t "Fix login bug" --description-file -

    # Attach a screenshot to the description
    glab mr create -t "Fix login bug" -d "Before and after:" --attach ./before.png --attach ./after.png

  FLAGS

    --allow-collaboration   Allow commits from other members. Set to true/false to override project defaults, or omit to use project settings.
    -a --assignee           Assign merge request to people by their `usernames`. Multiple usernames can be comma-separated or specified by repeating the flag.
    --attach                (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    --auto-merge            Set the merge request to merge when all merge checks pass.
    --copy-issue-labels     Copy labels from issue to the merge request. Used with --related-issue.
    --create-source-branch  Create a source branch if it does not exist.
    -d --description        Supply a description for the merge request. Set to "-" to open an editor.
    --description-file      Read the merge request description from a file. Use "-" to read from standard input.
    --draft                 Mark merge request as a draft.
    -f --fill               Do not prompt for title or description, and just use commit info. Sets `push` to `true`, and pushes the branch.
    --fill-commit-body      Fill description with each commit body when multiple commits. Can only be used with --fill.
    -H --head               Select another head repository using the `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format, the project ID, or the full URL.
    -h --help               Show help for this command.
    -l --label              Add label by name. Multiple labels can be comma-separated or specified by repeating the flag.
    -m --milestone          The global ID or title of a milestone to assign.
    --no-editor             Don't open editor to enter a description. If true, uses prompt. Defaults to false.
    --push                  Push committed changes after creating merge request. Make sure you have committed changes.
    --recover               Save the options to a file if the merge request creation fails. If the file exists, the options are loaded from the recovery file. (EXPERIMENTAL)
    -i --related-issue      Create a merge request for an issue. If --title is not provided, uses the issue title.
    --remove-source-branch  Remove source branch on merge. Set to true/false to override project defaults, or omit to use project settings.
    -R --repo               Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --reviewer              Request review from users by their `usernames`. Multiple usernames can be comma-separated or specified by repeating the flag.
    --signoff               Append a DCO signoff to the merge request description.
    -s --source-branch      Create a merge request from this branch. Default is the current branch.
    --squash-before-merge   Squash commits into a single commit when merging. Set to true/false to override project defaults, or omit to use project settings.
    -b --target-branch      The target or base branch into which you want your code merged into.
    --template              Name of a template in '.gitlab/merge_request_templates/' to pre-populate the description. The '.md' extension is optional. Templates are loaded from the local repository only.
    -t --title              Supply a title for the merge request.
    -w --web                Continue merge request creation in a browser.
    --wip                   Mark merge request as a draft. Alternative to --draft.
    -y --yes                Skip submission confirmation prompt. Use --fill to skip all optional prompts.

```

## mr delete

```

  Delete a merge request.

  USAGE

    glab mr delete [<id> | <branch>] [--flags]

  EXAMPLES

    $ glab mr delete 123

    # Delete multiple merge requests by ID and branch name
    $ glab mr delete 123 branch-name 789

    # Delete merge requests !1, !2, !3, !4, !5
    $ glab mr delete 1,2,branch-related-to-mr-3,4,5

    $ glab mr del 123
    $ glab mr delete branch

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr diff

```

  View changes in a merge request.

  USAGE

    glab mr diff [<id> | <branch>] [--flags]

  EXAMPLES

    $ glab mr diff 123
    $ glab mr diff branch

    # Get merge request from current branch
    $ glab mr diff

    $ glab mr diff 123 --color=never

  FLAGS

    --color    Use color in diff output: always, never, auto. (auto)
    -h --help  Show help for this command.
    --raw      Use raw diff format that can be piped to commands
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr for

```
Command "for" is deprecated, use `glab mr create --related-issue <issueID>`

  Create a new merge request for an issue.

  USAGE

    glab mr for [--flags]

  EXAMPLES

    # Create merge request for issue 34
    $ glab mr for 34

    # Create merge request for issue 34 and mark as work in progress
    $ glab mr for 34 --wip

    $ glab mr new-for 34
    $ glab mr create-for 34

  FLAGS

    --allow-collaboration   Allow commits from other members.
    -a --assignee           Assign merge request to people by their IDs. Multiple values should be comma-separated.
    --draft                 Mark merge request as a draft. (true)
    -h --help               Show help for this command.
    -l --label              Add label by name. Multiple labels should be comma-separated.
    -m --milestone          Add milestone by <id> for this merge request. (-1)
    --remove-source-branch  Remove source branch on merge.
    -R --repo               Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -b --target-branch      The target or base branch into which you want your code merged.
    --wip                   Mark merge request as a work in progress. Overrides --draft.
    --with-labels           Copy labels from issue to the merge request.
```

## mr issues

```

  Get issues related to a particular merge request.

  USAGE

    glab mr issues [<id> | <branch>] [--flags]

  EXAMPLES

    # List issues for merge request 46
    $ glab mr issues 46
    $ glab mr issues branch

    # Use the checked-out branch
    $ glab mr issues

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr list

```

  List merge requests.

  USAGE

    glab mr list [--flags]

  EXAMPLES

    $ glab mr list --all
    $ glab mr ls -a
    $ glab mr list --assignee=@me
    $ glab mr list --reviewer=@me
    $ glab mr list --source-branch=new-feature
    $ glab mr list --target-branch=main
    $ glab mr list --search "this adds feature X"
    $ glab mr list --label needs-review
    $ glab mr list --not-label waiting-maintainer-feedback,subsystem-x
    $ glab mr list -M --per-page 10
    $ glab mr list --draft
    $ glab mr list --not-draft

  FLAGS

    -A --all            Get all merge requests.
    -a --assignee       Get only merge requests assigned to users. Multiple users can be comma-separated or specified by repeating the flag.
    --author            Filter merge request by author <username>.
    -c --closed         Get only closed merge requests.
    --created-after     Filter merge requests created after a certain date (ISO 8601 format).
    --created-before    Filter merge requests created after a certain date (ISO 8601 format).
    -d --draft          Filter by draft merge requests.
    -g --group          Select a group/subgroup. This option is ignored if a repo argument is set.
    -h --help           Show help for this command.
    -l --label          Filter merge request by label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    -M --merged         Get only merged merge requests.
    -m --milestone      Filter merge request by milestone <id>.
    --not-draft         Filter by non-draft merge requests.
    --not-label         Filter merge requests by not having label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    -o --order          Order merge requests by <field>. Order options: created_at, updated_at, merged_at, title, priority, label_priority, milestone_due, and popularity.
    -F --output         Format output as: text, json. (text)
    -p --page           Page number. (1)
    -P --per-page       Number of items to list per page. (30)
    -R --repo           Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -r --reviewer       Get only merge requests with users as reviewer. Multiple users can be comma-separated or specified by repeating the flag.
    --search            Filter by <string> in title and description.
    -S --sort           Sort direction for --order field: asc or desc.
    -s --source-branch  Filter by source branch <name>.
    -t --target-branch  Filter by target branch <name>.
```

## mr merge

```

  Defaults to the currently checked-out branch. When a pipeline is running,
  auto-merge is enabled by default. Pass `--auto-merge=false` to
  merge immediately. Use `--squash` or `--rebase` to control
  the merge strategy, or `--remove-source-branch` to delete the
  source branch after merging.


  USAGE

    glab mr merge [<id | branch>] [--flags]

  EXAMPLES

    # Merge a merge request
    glab mr merge 235
    glab mr accept 235

    # Finds open merge request from current branch
    glab mr merge

  FLAGS

    --auto-merge               Set auto-merge. (true)
    -h --help                  Show help for this command.
    -m --message               Custom merge commit message.
    -r --rebase                Rebase the commits onto the base branch.
    -d --remove-source-branch  Remove source branch on merge.
    -R --repo                  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --sha                      Merge only if the HEAD of the source branch matches this SHA. Use to ensure that only reviewed commits are merged.
    -s --squash                Squash commits on merge.
    --squash-message           Custom squash commit message.
    -y --yes                   Skip submission confirmation prompt.
```

## mr note

```

  Manage comments and discussions on a merge request.

  USAGE

    glab mr note [command] [<id> | <branch>] [--flags]

  EXAMPLES

    # Add a comment to merge request with ID 123
    glab mr note 123 -m "Looks good to me!"

    # Add a comment to the merge request for the current branch
    glab mr note -m "LGTM"

    # Open your editor to compose a multi-line comment
    glab mr note 123

    # Resolve a discussion by note ID
    glab mr note 123 --resolve 3107030349

    # Unresolve a discussion by note ID
    glab mr note 123 --unresolve 3107030349

  COMMANDS

    list [<id> | <branch>] [--flags]            List merge request discussions. (EXPERIMENTAL)
    reopen  <discussion-id> [<id> | <branch>]   Reopen a discussion on a merge request. (EXPERIMENTAL)
    resolve  <discussion-id> [<id> | <branch>]  Resolve a discussion on a merge request. (EXPERIMENTAL)

  FLAGS

    -h --help                                   Show help for this command.
    -m --message                                Comment or note message.
    -R --repo                                   Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    --unique                                    Don't create a comment or note if it already exists.
```

## mr note create

```text

  Add a comment to a merge request. By default, the command creates the comment
  as a new discussion thread.

  Use `--resolvable=false` to create a non-resolvable note instead.
  Non-resolvable notes do not block merging when the project requires
  **All threads must be resolved**. Use this option for automation or status
  updates that do not need a human to resolve them.

  Use `--reply` to add a note to an existing discussion thread instead of
  starting a new one. The value can be a full discussion ID or a unique
  prefix of at least 8 characters. Find discussion IDs with
  `glab mr note list`. Human-readable output uses
  eight characters before the ellipsis, for example
  `[discussion: abc12345…]`; pass
  only those characters, for example `--reply abc12345`. To get a
  full ID, use the `id` field of each discussion object:
  `glab mr note list -F json | jq -r '.[].id'`.

  Use `--file` to place a diff comment on a specific file in the latest
  merge request diff version. Combine with `--line` (new side) or
  `--old-line` (old/removed side) to target a specific line. Omit
  both flags for a file-level comment.

  The flag rules are:

  - `--line` and `--old-line` require `--file`, and
  cannot be used together.
  - `--file`, `--reply`, and `--unique` are mutually
  exclusive.
  - `--resolvable=false` cannot be combined with `--reply`
  or `--file` (and by extension `--line` or
  `--old-line`).
  - `--attach` and `--unique` are mutually exclusive,
  because every upload gets a fresh URL and so an attached comment can
  never match an existing one.

  `--attach` uploads a file and references it at the end of the comment. Repeat the flag for more than one file, or pass
  `-` to read the file from standard input. An attachment is content on its own, so a comment with only `--attach`
  neither prompts nor reads a body from stdin.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mr note create [<id> | <branch>] [--flags]

  EXAMPLES

    # Add a comment to merge request 123
    glab mr note create 123 -m "Looks good to me!"

    # Add a comment to the current branch's merge request
    glab mr note create -m "LGTM"

    # Open editor to compose the message
    glab mr note create 123

    # Pipe from stdin
    echo "LGTM" | glab mr note create 123

    # Read the body from a file
    glab mr note create 123 < plan.md

    # Skip if already posted
    glab mr note create 123 -m "LGTM" --unique

    # Create a non-resolvable note, for example for bot or CI status updates
    glab mr note create 123 -m "Build status: green" --resolvable=false

    # Reply to an existing discussion thread
    glab mr note create 123 --reply abc12345 -m "I agree!"

    # Add a diff comment on line 42 of main.go
    glab mr note create 123 --file main.go --line 42 -m "Needs refactoring"

    # Add a diff comment on lines 10-15 (multiline range)
    glab mr note create 123 --file main.go --line 10:15 -m "Extract this block"

    # Add a diff comment on a removed line (old side)
    glab mr note create 123 --file main.go --old-line 7 -m "Why was this removed?"

    # Add a file-level diff comment (no line specified)
    glab mr note create 123 --file main.go -m "General comment on this file"

    # Attach a screenshot alongside the message
    glab mr note create 123 -m "Renders wrong here." --attach ./screenshot.png

    # Attach an image piped from the clipboard
    pngpaste - | glab mr note create 123 --attach -

  FLAGS

    --attach      (Experimental) Upload a file and reference it at the end of the comment. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    --file        File path for a diff comment, like <path/to/file>. Targets the latest merge request diff version.
    -h --help     Show help for this command.
    --line        Line in the new version. A single line number, like 42, or a range, like 10:15.
    -m --message  Comment or note message.
    --old-line    Line in the old version, for commenting on a removed line.
    --reply       Reply to an existing discussion. Accepts a full discussion ID or a unique prefix of at least 8 characters.
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --resolvable  Create the note as a resolvable discussion thread. Set to false to create a non-resolvable note. (true)
    --unique      Don't create a note if a note with the same body already exists. Reads all merge request comments first.

```

## mr note update

```text

  Replace the body of an existing note on a merge request.

  `<note-id>` is a numeric note ID, not a hex discussion ID.
  You can find note IDs with:

  - `glab mr note list -F json` (the `.id` field)
  - Note URLs: `.../merge_requests/1#note_12345`

  You can change only the note body. You cannot move the position of diff notes.

  `--attach` uploads a file and references it at the end of the note. Repeat the flag for more than one file, or pass `-
  ` to read the file from standard input. Without `--message` the references are added to the body the note already has,
  instead of replacing it.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mr note update <note-id> [<id> | <branch>] [--flags]

  EXAMPLES

    # Update note 12345 on merge request 1 with a new message
    glab mr note update 1 12345 -m "Updated comment"

    # Update a note on the current branch's merge request, composing in an editor
    glab mr note update 12345

    # Pipe the new body from stdin
    echo "new body" | glab mr note update 1 12345

    # Add a screenshot to the existing note body
    glab mr note update 1 12345 --attach ./screenshot.png

  FLAGS

    --attach      (Experimental) Upload a file and reference it at the end of the note. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -h --help     Show help for this command.
    -m --message  New note body. If omitted, opens an editor or reads from stdin.
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## mr note list

```
Fetches and displays merge request discussions.
Human-readable output shows an eight-character prefix for each non-system
discussion. Use the characters before the ellipsis with
`glab mr note create --reply`. JSON output preserves the full discussion ID in
the `id` field of each discussion object. Extract it with:
`glab mr note list -F json | jq -r '.[].id'`.
Supports filtering by note type, resolution state, and file path.
Supports JSON output for scripting.

USAGE
  glab mr note list [<id> | <branch>] [flags]

EXAMPLES
  # List all discussions on the current branch's MR
  glab mr note list

  # List diff comments only
  glab mr note list --type diff

  # List unresolved discussions
  glab mr note list --state unresolved

  # List discussions on a specific file
  glab mr note list --file src/main.go

  # JSON output for scripting
  glab mr note list -F json | jq '.[].notes[].body'

  # List discussions on MR 123
  glab mr note list 123

FLAGS
      --file string    Show only diff notes on this file path.
  -F, --output string  Format output as: text, json. (default "text")
      --jq string      Filter JSON output with a jq expression.
      --state string   Resolution state: all, resolved, unresolved. (default "all")
  -t, --type string    Note type: all, general, diff, system. (default "all")

INHERITED FLAGS
  -h, --help           Show help for this command.
  -R, --repo string    Select another repository. OWNER/REPO, GROUP/NAMESPACE/REPO, full URL, and Git URL are accepted.
```

## mr rebase

```

  If you don't have permission to push to the merge request's source branch, you'll get a 403 Forbidden response.


  USAGE

    glab mr rebase [<id> | <branch>] [--flags]

  EXAMPLES

    # Rebase merge request 123
    $ glab mr rebase 123

    # Rebase current branch
    $ glab mr rebase

    # Rebase merge request from branch
    $ glab mr rebase branch
    $ glab mr rebase branch --skip-ci

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    --skip-ci  Rebase merge request while skipping CI/CD pipeline.
```

## mr reopen

```

  Reopen a merge request.

  USAGE

    glab mr reopen [<id>... | <branch>...] [--flags]

  EXAMPLES

    # Reopen merge request 123
    $ glab mr reopen 123

    # Reopen merge requests 123, 456, and 789
    $ glab mr reopen 123 456 789

    # Reopen merge requests from branches branch-1 and branch-2
    $ glab mr reopen branch-1 branch-2

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr revoke

```

  Revoke approval on a merge request.

  USAGE

    glab mr revoke [<id> | <branch>] [--flags]

  EXAMPLES

    # Revoke approval on a merge request
    $ glab mr revoke 123
    $ glab mr unapprove 123
    $ glab mr revoke branch

    # Revoke approval on the currently checked out branch
    $ glab mr revoke
    # Revoke approval on merge request 123 on branch 456
    $ glab mr revoke 123 branch 456

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr subscribe

```

  Subscribe to a merge request.

  USAGE

    glab mr subscribe [<id> | <branch>] [--flags]

  EXAMPLES

    # Subscribe to a merge request
    $ glab mr subscribe 123
    $ glab mr sub 123
    $ glab mr subscribe branch

    # Subscribe to multiple merge requests
    $ glab mr subscribe 123 branch

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr todo

```

  Add a to-do item to merge request.

  USAGE

    glab mr todo [<id> | <branch>] [--flags]

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr unsubscribe

```

  Unsubscribe from a merge request.

  USAGE

    glab mr unsubscribe [<id> | <branch>] [--flags]

  EXAMPLES

    # Unsubscribe from a merge request
    $ glab mr unsubscribe 123
    $ glab mr unsub 123
    $ glab mr unsubscribe branch

    # Unsubscribe from multiple merge requests
    $ glab mr unsubscribe 123 branch

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## mr update

```

  Defaults to the currently checked-out branch. Use `--fill` to
  automatically fill the title and description from the commit history.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Without `--description` the references are added to the description the
  merge request already has, instead of replacing it.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mr update [<id> | <branch>] [--flags]

  EXAMPLES

    # Mark a merge request as ready
    glab mr update 23 --ready

    # Mark a merge request as draft
    glab mr update 23 --draft

    # Updates the merge request for the current branch
    glab mr update --draft

    # Update merge request with commit information
    glab mr update 23 --fill --fill-commit-body --yes

    # Read the description from a file
    glab mr update 23 --description-file description.md

    # Read the description from standard input
    cat description.md | glab mr update 23 --description-file -

    # Add a screenshot to the existing description
    glab mr update 23 --attach ./screenshot.png

  FLAGS

    -a --assignee           Assign users via username. Prefix with '!' or '-' to remove from existing assignees, '+' to add. Otherwise, replace existing assignees with given users. Multiple usernames can be comma-separated or specified by repeating the flag.
    --attach                (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -d --description        Merge request description. Set to "-" to open an editor.
    --description-file      Read the merge request description from a file. Use "-" to read from standard input.
    --draft                 Mark merge request as a draft.
    -f --fill               Do not prompt for title or body, and just use commit info.
    --fill-commit-body      Fill body with each commit body when multiple commits. Can only be used with --fill.
    -h --help               Show help for this command.
    -l --label              Add labels.
    --lock-discussion       Lock discussion on merge request.
    -m --milestone          Title of the milestone to assign. Set to "" or 0 to unassign.
    -r --ready              Mark merge request as ready to be reviewed and merged.
    --remove-source-branch  Toggles the removal of the source branch on merge.
    -R --repo               Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --reviewer              Request review from users by their usernames. Prefix with '!' or '-' to remove from existing reviewers, '+' to add. Otherwise, replace existing reviewers with given users. Multiple usernames can be comma-separated or specified by repeating the flag.
    --squash-before-merge   Toggles the option to squash commits into a single commit when merging.
    --target-branch         Set target branch.
    -t --title              Title of merge request.
    --unassign              Unassign all users.
    -u --unlabel            Remove labels.
    --unlock-discussion     Unlock discussion on merge request.
    --wip                   Mark merge request as a work in progress. Alternative to --draft.
    -y --yes                Skip confirmation prompt.

```

## mr view

> Captured from the checksum-verified glab v1.114.0 macOS arm64 release binary, with only terminal padding and trailing whitespace removed.

```text

  You can use a branch name or ID. Use `--web` to open in a browser.


  USAGE

    glab mr view [<id | branch>] [--flags]

  EXAMPLES

    glab mr view 123
    glab mr view branch-name
    glab mr view 123 --comments
    glab mr view 123 --web

  FLAGS

    -c --comments     Show merge request comments and activities.
    -h --help         Show help for this command.
    --jq              Filter JSON output with a jq expression.
    -F --output       Format output as: text, json. (text)
    -p --page         Page number.
    -P --per-page     Number of items to list per page. (20)
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --resolved        Show only resolved discussions (implies --comments).
    -s --system-logs  Show system activities and logs.
    --unresolved      Show only unresolved discussions (implies --comments).
    -w --web          Open merge request in a browser. Uses default browser or browser specified in BROWSER variable.
```
