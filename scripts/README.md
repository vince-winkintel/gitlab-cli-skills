# GitLab CLI Scripts

Automation scripts for common GitLab CLI workflows.

## Available Scripts

### `mr-review-workflow.sh`

Automated MR review: checkout → run tests → approve if passed.

```bash
./scripts/mr-review-workflow.sh <MR_ID> [test_command]

# Examples
./scripts/mr-review-workflow.sh 123
./scripts/mr-review-workflow.sh 123 "pnpm test"
./scripts/mr-review-workflow.sh 123 "cargo test"
```

**What it does:**
1. Checks out the MR locally
2. Runs your test command (default: `npm test`)
3. If tests pass: adds approval comment + approves MR
4. If tests fail: adds failure comment with details

### `create-mr-from-issue.sh`

Create branch from issue with proper naming.

```bash
./scripts/create-mr-from-issue.sh <ISSUE_ID> [--create-mr]

# Examples
./scripts/create-mr-from-issue.sh 456
./scripts/create-mr-from-issue.sh 456 --create-mr  # Also creates draft MR
```

**What it does:**
1. Fetches issue title
2. Creates branch named `<issue-id>-<slugified-title>`
3. Optionally creates draft MR linked to the issue

### `ci-debug.sh`

Debug CI failures by showing failed job logs.

```bash
./scripts/ci-debug.sh <PIPELINE_ID>

# Example
./scripts/ci-debug.sh 987654
```

**What it does:**
1. Lists all failed jobs in the pipeline
2. Shows last 50 lines of each failed job's log
3. Provides next steps for debugging

### `post-inline-comment.py`

Post inline code review comments at specific line numbers in MR diffs, with automatic recovery when GitLab requires computed `line_code` anchors.

```bash
./scripts/post-inline-comment.py --project <group/project> --mr <mr_iid> --file <file_path> --line <line_number> --body <comment_text>

# Examples
./scripts/post-inline-comment.py --project owner/repo --mr 42 --file "src/main.js" --line 100 --body "Bug: Add null check"
./scripts/post-inline-comment.py --project owner/repo --mr 42 --file "lib/util.py" --line 25 --body "**Performance**: Use dict comprehension"
```

**What it does:**
1. Fetches MR metadata (current SHAs) and all MR diff pages
2. Tries the normal inline discussion payload first
3. If GitLab returns a `line_code` validation error, computes the diff `line_code` and retries with `position[line_range][start/end][line_code]`
4. Preserves the diff's actual `old_path`/`new_path` metadata so renamed files anchor correctly
5. Reports whether the comment landed inline and whether the retry path was needed

**Documentation:** See `scripts/README-inline-comments.md` for detailed usage and integration examples.

### `batch-label-issues.sh`

Apply label to multiple issues at once.

```bash
./scripts/batch-label-issues.sh <label> <issue_id1> [issue_id2] ...

# Examples
./scripts/batch-label-issues.sh bug 100 101 102
./scripts/batch-label-issues.sh "priority::high" 200 201
```

**What it does:**
1. Applies the specified label to all listed issues
2. Shows progress for each issue
3. Reports success/failure summary

### `sync-fork.sh`

Sync your fork with upstream repository.

```bash
./scripts/sync-fork.sh [branch] [upstream_remote]

# Examples
./scripts/sync-fork.sh                    # Syncs main with upstream
./scripts/sync-fork.sh develop            # Syncs develop with upstream
./scripts/sync-fork.sh main my-upstream   # Custom upstream remote name
```

**What it does:**
1. Fetches from upstream remote
2. Merges upstream changes into local branch
3. Pushes to your fork's origin

## Usage Tips

**Make scripts available globally:**
```bash
# Add to your PATH
export PATH="$PATH:/path/to/gitlab-cli-skills/scripts"

# Or create aliases
alias mr-review="/path/to/gitlab-cli-skills/scripts/mr-review-workflow.sh"
alias ci-debug="/path/to/gitlab-cli-skills/scripts/ci-debug.sh"
```

**Use with OpenClaw:**

The agent can execute these scripts directly:
```
"Run the MR review workflow for MR 123"
"Debug the failed CI pipeline 456789"
"Create a branch for issue 789 and draft MR"
```

## Requirements

- `glab` CLI installed and authenticated
- `git` for branch/fork operations
- Test framework for `mr-review-workflow.sh` (npm, pnpm, cargo, etc.)

## Token Efficiency

These scripts are designed for OpenClaw's progressive disclosure pattern:
- Scripts execute without loading into context
- Only script output consumes tokens
- Deterministic behavior vs AI-generated code
- Reusable across multiple tasks
