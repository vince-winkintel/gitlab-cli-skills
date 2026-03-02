---
name: glab-runner
description: Manage GitLab CI/CD runners — list, pause, and delete runners at project, group, or instance level. Use when viewing runner status, temporarily pausing a runner, or removing a decommissioned runner. Triggers on runner, glab runner, list runners, pause runner, delete runner, CI runner.
---

# glab runner

Manage GitLab CI/CD runners from the command line.

> **Added in glab v1.87.0**

## Quick Start

```bash
# List runners for current project
glab runner list

# Pause a runner
glab runner pause <runner-id>

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
    print(f\"{r['id']}: {r.get('description','(no description)')} — {r.get('status')}\")
"
```

### Pause a Runner

Pausing a runner prevents it from picking up new jobs without removing it.

```bash
# Pause runner 123
glab runner pause 123

# Pause in a specific project context
glab runner pause 123 --repo owner/project
```

**When to pause:**
- Maintenance window (updates, reboots)
- Investigating a failing runner
- Temporarily reducing runner capacity
- Before decommissioning (verify no jobs are running first)

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
          ├─ Yes → Pause first, wait for jobs to finish, then delete
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

**Runner won't pause:**
- Verify runner ID with `glab runner list`.
- Check permissions (must be at least Maintainer on the project).

**Runner stuck "online" after pause:**
- The runner process is still running on the host — it just won't accept new jobs.
- This is expected. To fully stop, SSH into the runner host and stop the process.

**Cannot delete runner:**
- Runner may be shared/group-level (requires higher privileges).
- Check if runner is assigned to multiple projects; removing from one project may require project-level deletion vs instance-level.

## Related Skills

- `glab-runner-controller` — Manage runner controllers and orchestration (admin-only, experimental)
- `glab-ci` — View and manage CI/CD pipelines and jobs
- `glab-job` — Retry, cancel, trace logs for individual jobs

## Command Reference

```
glab runner <command> [--flags]

Commands:
  list    Get a list of runners available to the user
  pause   Pause a runner
  delete  Delete a runner

Flags (list):
  --all          List all runners (instance-level, admin only)
  --output       Format output as: text, json
  --page         Page number
  --per-page     Number of items per page
  --repo         Select a repository
  -h, --help     Show help

Flags (pause / delete):
  --force        Skip confirmation prompt (delete only)
  --repo         Select a repository
  -h, --help     Show help
```
