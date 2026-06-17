---
name: glab-stack
description: Manage stacked merge requests for complex multi-part changes. Use when creating dependent MRs, managing MR stacks, or working with multi-layer changes. Triggers on stack, stacked MRs, dependent MRs, MR stack, stacked changes.
---

# glab stack

## Overview

```

  Stacked diffs are a way of creating small changes that build upon each other to ultimately deliver a feature. This
  kind of workflow can be used to accelerate development time by continuing to build upon your changes, while earlier
  changes in the stack are reviewed and updated based on feedback.
  This feature is experimental. It might be broken or removed without any prior notice.
  Read more about what experimental features mean at
  https://docs.gitlab.com/policy/development_stages_support/
  Use experimental features at your own risk.
  USAGE
    glab stack <command> [command] [--flags]
  EXAMPLES
    $ glab stack create cool-new-feature
    $ glab stack sync
  COMMANDS
    amend [--flags]      Save more changes to a stacked diff. (EXPERIMENTAL)
    create               Create a new stacked diff. (EXPERIMENTAL)
    first                Moves to the first diff in the stack. (EXPERIMENTAL)
    infer <revision-range>  Add layers to a stack based on a range of commits. (EXPERIMENTAL)
    last                 Moves to the last diff in the stack. (EXPERIMENTAL)
    list                 Lists all entries in the stack. (EXPERIMENTAL)
    move                 Moves to any selected entry in the stack. (EXPERIMENTAL)
    next                 Moves to the next diff in the stack. (EXPERIMENTAL)
    prev                 Moves to the previous diff in the stack. (EXPERIMENTAL)
    reorder              Reorder a stack of merge requests. (EXPERIMENTAL)
    save [--flags]       Save your progress within a stacked diff. (EXPERIMENTAL)
    switch [stack-name]  Switch between stacks. (EXPERIMENTAL)
    sync                 Sync and submit progress on a stacked diff. (EXPERIMENTAL)
  FLAGS
    -h --help            Show help for this command.
    -R --repo            Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## Quick start

```bash
glab stack --help
```

## Current behavior

`glab stack infer <revision-range>` creates or appends stack layers from selected commits in a Git revision range. The start of the range must resolve to a branch name, not a relative ref such as `HEAD~5`, because the base branch is recorded in stack metadata.

```bash
# Infer stack layers from commits between main and the current branch
glab stack infer main..HEAD

# Infer from a feature branch that diverged from develop
glab stack infer develop..HEAD

# Create a new stack with a specific name
glab stack infer --name feature-stack main..HEAD
```

`glab stack sync` supports `--update-base`, `--assignee`, `--label`, `--reviewer`, and `--skip-mr-creation`.

```bash
# Sync stack and rebase onto the latest base branch
glab stack sync --update-base

# Sync/push existing stack work without opening MRs for branches that do not have one yet
glab stack sync --skip-mr-creation

# Sync stack and set MR metadata during submission
glab stack sync --assignee @owner --reviewer @reviewer --label backend

# Multiple reviewers can be repeated or comma-separated
glab stack sync --reviewer user1 --reviewer user2
glab stack sync --reviewer user1,user2
```

Use `--update-base` when the base branch (for example `main`) has moved and you want to rebase the entire stack before pushing.

Use `--skip-mr-creation` when you want to push amended stack branches and clean up merged/closed entries but intentionally avoid opening new merge requests for stack layers that do not have one yet.

Use `--assignee`, `--reviewer`, and `--label` when you want `glab stack sync` to submit the stack's merge requests with ownership and routing metadata in the same step.

`glab stack switch` can now be run without a stack name to choose interactively from all stacks. Pass the stack name for non-interactive automation.

`glab stack amend` and `glab stack save` support `--no-verify` to bypass local `pre-commit` and `commit-msg` hooks for the underlying Git commit. Treat it like `git commit --no-verify`: use only when the skipped hooks are understood and intentionally bypassed.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
