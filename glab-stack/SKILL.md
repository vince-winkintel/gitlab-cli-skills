---
name: glab-stack
description: Manage stacked merge requests for complex multi-part changes. Use when creating dependent MRs, reordering or syncing a stack, recovering a conflicted reorder, or deleting local stack metadata. Triggers on stack, stacked MRs, dependent MRs, MR stack, stacked changes, stack delete, stack reorder.
---

# glab stack

## Overview

A stack is a series of small, dependent merge requests delivering one feature. Locally, each diff is one commit on its own branch, based on the preceding diff's branch. Sync creates an MR targeting the preceding branch; the first diff targets the base branch.

Stack commands operate on the stack last created or switched to, regardless of the currently checked-out branch. Inspect that active stack before a mutation. This feature remains experimental. See [references/commands.md](references/commands.md) for complete checksum-verified parent/subcommand help, including current terminology and examples.

## Quick start

```bash
glab stack --help
```

## Current behavior

Generated stack branches use `{branch_prefix}-{stack-title}-{hash}`. If `branch_prefix` is unset, glab uses the operating system account username (and removes a Windows domain prefix), falling back to `glab-stack` only when user lookup is unavailable. It does not rely on `$USER`; set `glab config set branch_prefix <value>` when automation requires a stable explicit prefix.

`glab stack infer <revision-range>` creates or appends stack layers from selected commits in a Git revision range. The start of the range must resolve to a branch name, not a relative ref such as `HEAD~5`, because the base branch is recorded in stack metadata.

```bash
# Infer stack layers from commits between main and the current branch
glab stack infer main..HEAD

# Infer from a feature branch that diverged from develop
glab stack infer develop..HEAD

# Create a new stack with a specific name
glab stack infer --name feature-stack main..HEAD
```

`glab stack sync` supports `--update-base`, `--assignee`, `--label`, `--reviewer`, `--skip-mr-creation`, and `--skip-push`.

```bash
# Sync stack and rebase onto the latest base branch
glab stack sync --update-base

# Sync/push existing stack work without opening MRs for branches that do not have one yet
glab stack sync --skip-mr-creation

# Fetch and rebase the stack locally without pushing branches or creating MRs
glab stack sync --skip-push

# Sync stack and set MR metadata during submission
glab stack sync --assignee @owner --reviewer @reviewer --label backend

# Multiple reviewers can be repeated or comma-separated
glab stack sync --reviewer user1 --reviewer user2
glab stack sync --reviewer user1,user2
```

Use `--update-base` when the base branch (for example `main`) has moved and you want to rebase the entire stack before pushing.

Use `--skip-mr-creation` when you want to push amended stack branches and clean up merged/closed entries but intentionally avoid opening new merge requests for stack layers that do not have one yet.

Use `--skip-push` when you want to fetch and rebase the stack locally without pushing branches or creating merge requests. This is not an offline mode: glab still fetches from the remote and calls the GitLab API. Review the rewritten local history before a later push.

Use `--assignee`, `--reviewer`, and `--label` when you want `glab stack sync` to submit the stack's merge requests with ownership and routing metadata in the same step.

During stack sync pushes, glab streams Git hook output to stdout/stderr as it runs. Preserve that output in automation logs: a failing pre-push hook is returned as the push error instead of being hidden behind buffered output.

`glab stack switch` can now be run without a stack name to choose interactively from all stacks. Pass the stack name for non-interactive automation.

`glab stack amend` supports `--reword` to update only the stacked commit message without staging files. It cannot be combined with file arguments or `--all`; pass `-m/--message` or `-d/--description`, or let glab open the editor.

```bash
glab stack amend --reword -m "updated commit message"
```

`glab stack amend` and `glab stack save` support `--no-verify` to bypass local `pre-commit` and `commit-msg` hooks for the underlying Git commit. Treat it like `git commit --no-verify`: use only when the skipped hooks are understood and intentionally bypassed.

## Reorder and recovery

`glab stack reorder` opens the current stack order in an editor, rebases each branch onto its new parent, and retargets each diff locally. It does not push; run `glab stack sync` after reviewing the rewritten history to force-push the rebased branches.

```bash
glab stack reorder

# After resolving a rebase conflict and running git rebase --continue
glab stack reorder --continue

# Restore the original branch order instead
glab stack reorder --abort
```

Do not start another reorder while a reorder rebase is in progress. Resolve and continue, or abort, before retrying. Preserve the conflict and rebase output in automation logs.

## Delete local stack metadata

```bash
# Choose a stack interactively
glab stack delete

# Delete a named stack after confirmation
glab stack delete <stack-name>

# Approved non-interactive deletion
glab stack delete <stack-name> --yes
```

Deletion removes only the stack's local stacked-metadata directory. It does not delete branches, commits, or merge requests. Verify the stack name and repository before `--yes`, then confirm the named directory is absent under `$(git rev-parse --git-common-dir)/stacked/`. This read-only check works for both ordinary checkouts and linked worktrees; `glab stack list` only lists layers in the current stack and cannot verify that a different stack was deleted.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
