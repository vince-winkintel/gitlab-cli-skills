# glab stack help

> Complete help captured from the checksum-verified glab v1.122.0 macOS arm64 release binary. Only terminal padding/trailing whitespace is removed; renderer wrapping and example truncation are preserved. Archive SHA-256: `cbdd6e28d35f9eb09aef79ad23d2712d67c9254677a60ed6d701b5362f659fef`. No product-spelling substitutions were needed in these captures.

## stack

```text

  A stack is a series of small, dependent merge requests that together deliver a feature. Reviewers can review and merge
  earlier changes while you keep building on top of them.

  Locally, each diff in the stack is one commit on its own branch, built on the branch of the previous diff. When you
  run `glab stack sync`, each diff becomes a merge request that targets the branch of the previous diff. The first diff
  targets the base branch.

  The `glab stack` commands act on the stack you last created or switched to, regardless of which branch you have
  checked out.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack <command> [command] [--flags]

  EXAMPLES

    glab stack create cool-new-feature
    glab stack sync

  COMMANDS

    amend [--flags]                   Save your changes to an existing diff. (EXPERIMENTAL)
    create                            Create a new stack. (EXPERIMENTAL)
    delete [<stack-name>] [--flags]   Delete a stack. (EXPERIMENTAL)
    first                             Move to the first diff in the stack. (EXPERIMENTAL)
    infer <revision-range> [--flags]  Add diffs to a stack based on a range of commits. (EXPERIMENTAL)
    last                              Move to the last diff in the stack. (EXPERIMENTAL)
    list                              List all diffs in the stack. (EXPERIMENTAL)
    move                              Move to a specific diff in the stack. (EXPERIMENTAL)
    next                              Move to the next diff in the stack. (EXPERIMENTAL)
    prev                              Move to the previous diff in the stack. (EXPERIMENTAL)
    reorder [--flags]                 Reorder a stack of diffs. (EXPERIMENTAL)
    save [--flags]                    Save your changes as a new diff. (EXPERIMENTAL)
    switch [stack-name]               Switch between stacks. (EXPERIMENTAL)
    sync [--flags]                    Push the stack to GitLab, and create or update its merge requests. (EXPERIMENTAL)

  FLAGS

    -h --help                         Show help for this command.
    -R --repo                         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack amend

```text

  Adds your changes to the diff you have checked out. Its merge request updates the next time you run `glab stack sync`,
  which also rebases the diffs after it.

  To create a new diff from your changes instead, use `glab stack save`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack amend [--flags]

  EXAMPLES

    # Amend diff with currently staged changes
    glab stack amend -m "Fix a function"

    # Add specified file to staged changes and amend diff
    glab stack amend newfile -m "forgot to add this"

    # Add all tracked files to staged changes and amend diff
    glab stack amend -a -m "fixed a function in exisiting file"

    # Add all tracked and untracked files to staged changes and amend diff
    glab stack amend . -m "refactored file into new files"

    # Reword the commit message without adding any files
    glab stack amend --reword -m "updated commit message"

  FLAGS

    -a --all          Automatically stage modified and deleted tracked files.
    -d --description  A description of the change.
    -h --help         Show help for this command.
    -m --message      Alias for the description flag.
    --no-verify       Bypass the pre-commit and commit-msg hooks of git-commit(1).
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --reword          Only update the commit message without staging any files.

```

## stack create

```text

  The stack starts empty, and the other `glab stack` commands act on it until you switch. The branch you have checked
  out becomes its base branch, which the first merge request targets, so push it to the remote before you run `glab
  stack sync`. To add diffs, use `glab stack save`.

  This command adds metadata to your `./.git/stacked` directory.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack create [--flags]

  EXAMPLES

    glab stack create cool-new-feature
    glab stack new cool-new-feature

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack delete

```text

  Removes the stack's local metadata from the `.git/stacked` directory.
  Use this command to clean up stacks for merged or abandoned merge requests.
  Branches, commits, and merge requests are not affected.

  If you do not provide a stack name, the command shows a list of stacks for you to choose from.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack delete [<stack-name>] [--flags]

  EXAMPLES

    # Interactively pick from the list of available stacks
    glab stack delete

    # Delete a specific stack by name
    glab stack delete <stack-name>

    # Delete a specific stack without the confirmation prompt
    glab stack delete <stack-name> -y

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes   Skip the confirmation prompt.

```

## stack first

```text

  Checks out the branch of the first diff in the stack.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack first [--flags]

  EXAMPLES

    glab stack first

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack infer

```text

  Opens an editor with the commits in the range for you to choose from.

  When you save and close the file, the command creates one diff for each commit listed in the file and appends them to
  the stack. If there's no stack to add them to, the command creates one first.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack infer <revision-range> [--flags]

  EXAMPLES

    # Commit range syntax is similar to "git rev-list".
    # The start of the range must be a branch name (not a relative ref like HEAD~5).

    # Add diffs from the commits between main and the current branch
    glab stack infer main..HEAD

    # Add diffs from the commits on a feature branch since it diverged from develop
    glab stack infer develop..HEAD

    # If there's no stack to add the diffs to, create one with a specific name
    glab stack infer --name feature-stack main..HEAD

  FLAGS

    -h --help  Show help for this command.
    -n --name  Name for the new stack (used when creating a stack)
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack last

```text

  Checks out the branch of the last diff in the stack.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack last [--flags]

  EXAMPLES

    glab stack last

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack list

```text

  Shows the branch and description of each diff. To check out a different diff, use `glab stack move`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack list [--flags]

  EXAMPLES

    glab stack list

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack move

```text

  Shows a list of the diffs in the stack, and checks out the branch of the diff you select.

  To work on a different stack, run `glab stack switch` first.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack move [--flags]

  EXAMPLES

    glab stack move

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack next

```text

  Checks out the branch of the next diff in the stack.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack next [--flags]

  EXAMPLES

    glab stack next

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack prev

```text

  Checks out the branch of the previous diff in the stack.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack prev [--flags]

  EXAMPLES

    glab stack prev

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack reorder

```text

  Opens an editor with one diff per line, so you can rearrange them.

  When you save and close the file, each diff's branch is rebased onto the branch of the diff now before it, and each
  moved diff's merge request is retargeted to match. The rebased branches are not pushed automatically, so run `glab
  stack sync` to force-push them and replace the old commits on GitLab.

  If a rebase hits a conflict, resolve it, run `git rebase --continue`, and then run `glab stack reorder --continue`. To
  restore the original order instead, run `glab stack reorder --abort`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack reorder [--flags]

  EXAMPLES

    # Reorder the stack by choosing a new branch order in your editor
    glab stack reorder

    # Continue a reorder after resolving a conflict
    glab stack reorder --continue

    # Abort a reorder and restore the original branch order
    glab stack reorder --abort

  FLAGS

    --abort     Abort a reorder and restore original branch state.
    --continue  Continue a reorder after resolving conflicts.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack save

```text

  Adds a new diff to the end of the stack. It becomes a new merge request the next time you run `glab stack sync`.

  To add your changes to the diff you have checked out instead, use `glab stack amend`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack save [--flags]

  EXAMPLES

    # Save currently staged changes as diff with description
    glab stack save -m "added a function"

    # Add specified file to staged changes and save diff
    glab stack save added_file

    # Add all tracked files to staged changes and save diff
    glab stack save -a -m "added a function to exisiting file"

    # Add all tracked and untracked files to staged changes and save diff
    glab stack save . -m "added new file"

  FLAGS

    -a --all          Automatically stage modified and deleted tracked files.
    -d --description  Description of the change.
    -h --help         Show help for this command.
    -m --message      Alias for the description flag.
    --no-verify       Bypass the pre-commit and commit-msg hooks of git-commit(1).
    -R --repo         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack switch

```text

  If you do not provide a stack name, the command shows a list of stacks for you to choose from.

  After you switch, use `glab stack move` to check out a diff in the new stack.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack switch [stack-name] [--flags]

  EXAMPLES

    # Interactively pick from the list of available stacks.
    glab stack switch

    # Switch to a specific stack by name.
    glab stack switch <stack-name>

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack sync

```text

  Updates GitLab to match your local stack:

  - Creates a merge request for each diff without one, unless `--skip-mr-creation` or `--skip-push` is set. Each merge
  request targets the branch of the previous diff, or the base branch for the first diff.
  - Pulls changes made on GitLab, such as applied suggestions, into any diff whose branch is behind its remote.
  - If you amended a diff since the last sync, rebases the diffs after it. Then, unless `--skip-push` is set, force-
  pushes the stack's branches.
  - Removes diffs with merged merge requests and deletes their local branches. Keeps diffs with closed merge requests.
  - If you're working in a fork, asks whether to push to the fork or the upstream repository.
  - With `--update-base`, rebases the stack onto the latest version of the base branch. Then, unless `--skip-push` is
  set, force-pushes the stack's branches.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack sync [--flags]

  EXAMPLES

    glab stack sync
    glab stack sync --no-verify
    glab stack sync --update-base
    glab stack sync --skip-push
    glab stack sync --skip-mr-creation
    glab stack sync --assignee user1,user2
    glab stack sync --label bug,priority::high
    glab stack sync --reviewer user1 --reviewer user2

  FLAGS

    -a --assignee       Assign merge request to people by their `usernames`. Multiple usernames can be comma-separated or specified by repeating the flag.
    -h --help           Show help for this command.
    -l --label          Add label by `name`. Multiple labels can be comma-separated or specified by repeating the flag.
    --no-verify         Bypass the pre-push hook. (See githooks(5) for more information.)
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --reviewer          Request review from users by their `usernames`. Multiple usernames can be comma-separated or specified by repeating the flag.
    --skip-mr-creation  Skip creating merge requests for branches that don't have one yet.
    --skip-push         Rebase the stack locally without pushing branches or creating merge requests. Still fetches from the remote and calls the GitLab API.
    --update-base       Rebase the stack onto the latest version of the base branch.

```
