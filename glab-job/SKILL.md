---
name: glab-job
description: Work with individual CI/CD jobs including view, retry, cancel, trace logs, and download artifacts. Use when debugging job failures, viewing job logs, retrying jobs, or managing job execution. Triggers on job, CI job, job logs, retry job, job artifacts.
---

# glab job

Work with individual CI/CD jobs.

## Quick start

```bash
# View job details
glab job view <job-id>

# Download job artifacts
glab job artifact main build-job

# Retry a failed job
glab ci retry <job-id>

# View job logs
glab ci trace <job-id>
```

## Decision: Pipeline vs Job Commands?

```
What level are you working at?
├─ Entire pipeline (all jobs)
│  └─ Use glab-ci commands:
│     ├─ glab ci status     (pipeline status)
│     ├─ glab ci view       (all jobs in pipeline)
│     ├─ glab ci run        (trigger new pipeline)
│     └─ glab ci cancel     (cancel entire pipeline)
│
└─ Individual job
   └─ Use glab-job or glab ci job commands:
      ├─ glab ci trace <job-id>    (job logs)
      ├─ glab ci retry <job-id>    (retry one job)
      ├─ glab job view <job-id>    (job details)
      └─ glab job artifact <ref> <job> (job artifacts)
```

**Use `glab ci` (pipeline-level) when:**
- Checking overall build status
- Viewing all jobs in a pipeline
- Triggering new pipeline runs
- Validating `.gitlab-ci.yml`

**Use `glab job` (job-level) when:**
- Debugging a specific failed job
- Downloading artifacts from a specific job
- Retrying individual jobs (not entire pipeline)
- Viewing detailed job information

## Common workflows

### Debugging a failed job

1. **Find the failed job:**
   ```bash
   glab ci view  # Shows all jobs, highlights failures
   ```

2. **View job logs:**
   ```bash
   glab ci trace <job-id>
   ```

3. **Retry the job:**
   ```bash
   glab ci retry <job-id>
   ```

### Working with artifacts

**Download artifacts from specific job:**
```bash
glab job artifact main build-job
```

**Download artifacts from latest successful run:**
```bash
glab job artifact main build-job --artifact-type job
```

### Job monitoring

**Watch job logs in real-time:**
```bash
glab ci trace <job-id>  # Follows logs until completion
```

**Check specific job status:**
```bash
glab job view <job-id>
```

## Related Skills

**Pipeline operations:**
- See `glab-ci` for pipeline-level commands
- Use `glab ci view` to see all jobs in a pipeline
- Script: `scripts/ci-debug.sh` for automated failure diagnosis

**CI/CD configuration:**
- See `glab-variable` for managing job variables
- See `glab-schedule` for scheduled job runs

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `artifact` - Download job artifacts
- `view` - View job details
- Most job operations use `glab ci <command> <job-id>`:
  - `glab ci trace <job-id>` - View logs
  - `glab ci retry <job-id>` - Retry job
  - `glab ci cancel <job-id>` - Cancel job
