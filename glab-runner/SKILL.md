---
name: glab-runner
description: Manage GitLab CI/CD runners — list, assign, unassign, inspect recent jobs and managers, pause/unpause via update, and delete runners at project, group, or instance level. Use when viewing runner status, assigning runners to projects, checking what jobs a runner handled, seeing manager processes, temporarily pausing a runner, or removing a decommissioned runner. Triggers on runner, glab runner, list runners, assign runner, unassign runner, runner jobs, runner managers, pause runner, unpause runner, delete runner, CI runner.
---

# glab runner

Manage GitLab CI/CD runners from the command line.

> **Added in glab v1.87.0**

## Quick Start

```bash
# List runners for current project
glab runner list

# Pause a runner (v1.90.0+: via update)
glab runner update <runner-id> --pause

# Delete a runner
glab runner delete <runner-id>
```

## Common Workflows

### List Runners

```bash
# List all runners for current project
glab runner list

# List for a specific project
glab runner list --repo owner/project

# List all runners (instance-level, admin only)
glab runner list --all

# Output as JSON
glab runner list --output json

# Paginate
glab runner list --page 2 --per-page 50
```

**Sample JSON output parsing:**
```bash
# Find all paused runners
glab runner list --output json | python3 -c "
import sys, json
runners = json.load(sys.stdin)
paused = [r for r in runners if r.get('paused')]
for r in paused:
    print(f"{r['id']}: {r.get('description','(no description)')} — {r.get('status')}")
"
```

### Pause or Resume a Runner (v1.90.0+)

Pausing a runner prevents it from picking up new jobs without removing it.

```bash
# Pause runner 123
glab runner update 123 --pause

# Resume a paused runner
glab runner update 123 --unpause

# Pause in a specific project context
glab runner update 123 --pause -R owner/project
```

**When to pause:**
- Maintenance window (updates, reboots)
- Investigating a failing runner
- Temporarily reducing runner capacity
- Before decommissioning (verify no jobs are running first)

> **Note:** Older docs/examples may mention `glab runner pause`, but in v1.90.0 the supported command surface uses `glab runner update --pause` / `--unpause`.

### Inspect Jobs Processed by a Runner (v1.90.0+)

```bash
# List recent jobs for runner 9
glab runner jobs 9

# Show only running jobs
glab runner jobs 9 --status running

# JSON output for automation
glab runner jobs 9 --output json
```

Useful for checking whether a runner is currently busy before pausing or deleting it.

### Inspect Runner Managers (v1.90.0+)

```bash
# List managers attached to a runner
glab runner managers 9

# JSON output
glab runner managers 9 --output json
```

Use this when you need to understand which runner manager processes/backends are associated with a runner.

### Delete a Runner

```bash
# Delete with confirmation prompt
glab runner delete 123

# Delete without confirmation
glab runner delete 123 --force

# Delete in a specific project context
glab runner delete 123 --repo owner/project
```

**⚠️ Deletion is permanent.** Pause first if unsure.

## Decision Tree: Pause vs Delete

```
Do you need the runner gone permanently?
├─ No → Pause it (recoverable)
└─ Yes → Is it actively running jobs?
          ├─ Yes → Check `glab runner jobs <id>`, then pause first and wait for jobs to finish
          └─ No → Delete with --force
```

## Runner Status Reference

| Status | Meaning |
|---|---|
| `online` | Connected and ready to accept jobs |
| `offline` | Not connected (check runner process) |
| `paused` | Connected but not accepting new jobs |
| `stale` | No contact in the last 3 months |

## Troubleshooting

**"runner: command not found":**
- Requires glab v1.87.0+. Check with `glab version`.

**"Permission denied" on instance-level runners:**
- Instance-level runner management requires GitLab admin privileges.
- Project runners can be managed by project maintainers.

**Runner won't pause or unpause:**
- Verify runner ID with `glab runner list`.
- Check permissions (must be at least Maintainer on the project).
- Use `glab runner update <id> --pause` or `--unpause`.

**Runner stuck "online" after pause:**
- The runner process is still running on the host — it just won't accept new jobs.
- This is expected. To fully stop, SSH into the runner host and stop the process.

**Cannot delete runner:**
- Runner may be shared/group-level (requires higher privileges).
- Check if runner is assigned to multiple projects; removing from one project may require project-level deletion vs instance-level.

### Assign / Unassign Runners to Projects (v1.88.0+)

Assign an existing runner to a project so it can pick up jobs:

```bash
# Assign a runner to the current project
glab runner assign <runner-id>

# Assign to a specific project
glab runner assign <runner-id> --repo owner/project
```

Remove a runner from a project (does not delete the runner):

```bash
# Unassign from current project
glab runner unassign <runner-id>

# Unassign from a specific project
glab runner unassign <runner-id> --repo owner/project
```

**Note:** Assigning/unassigning requires at least Maintainer role on the project. This is different from `glab runner delete` which permanently removes the runner.

## Related Skills

- `glab-runner-controller` — Manage runner controllers and orchestration (admin-only, experimental)
- `glab-ci` — View and manage CI/CD pipelines and jobs
- `glab-job` — Retry, cancel, trace logs for individual jobs

## v1.90.0 Changes

- Added `glab runner jobs <runner-id>` — list jobs processed by a runner
- Added `glab runner managers <runner-id>` — list runner managers
- Added `glab runner update <runner-id> --pause|--unpause` — pause or resume a runner

## v1.88.0 Changes

- Added `glab runner assign <runner-id>` — assign a runner to a project
- Added `glab runner unassign <runner-id>` — unassign a runner from a project

## Command Reference

```
glab runner <command> [--flags]

Commands:
  assign    Assign a runner to a project (v1.88.0+)
  delete    Delete a runner
  jobs      List jobs processed by a runner (v1.90.0+)
  list      Get a list of runners available to the user
  managers  List runner managers (v1.90.0+)
  unassign  Unassign a runner from a project (v1.88.0+)
  update    Update runner settings, including pause/unpause (v1.90.0+)

Flags (list):
  --all          List all runners (instance-level, admin only)
  --output       Format output as: text, json
  --page         Page number
  --per-page     Number of items per page
  --repo         Select a repository
  -h, --help     Show help
```
