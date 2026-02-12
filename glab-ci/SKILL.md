---
name: glab-ci
description: Work with GitLab CI/CD pipelines, jobs, and artifacts. Use when checking pipeline status, viewing job logs, debugging CI failures, triggering manual jobs, downloading artifacts, validating .gitlab-ci.yml, or managing pipeline runs. Triggers on pipeline, CI/CD, job, build, deployment, artifact, pipeline status, failed build, CI logs.
---

# glab ci

Work with GitLab CI/CD pipelines, jobs, and artifacts.

## Quick start

```bash
# View current pipeline status
glab ci status

# View detailed pipeline info
glab ci view

# Watch job logs in real-time
glab ci trace <job-id>

# Download artifacts
glab ci artifact main build-job

# Validate CI config
glab ci lint
```

## Common workflows

### Debugging pipeline failures

1. **Check pipeline status:**
   ```bash
   glab ci status
   ```

2. **View failed jobs:**
   ```bash
   glab ci view --web  # Opens in browser for visual review
   ```

3. **Get logs for failed job:**
   ```bash
   # Find job ID from ci view output
   glab ci trace 12345678
   ```

4. **Retry failed job:**
   ```bash
   glab ci retry 12345678
   ```

**Automated debugging:**

For quick failure diagnosis, use the debug script:
```bash
scripts/ci-debug.sh 987654
```

This automatically: finds all failed jobs → shows logs → suggests next steps.

### Working with manual jobs

1. **View pipeline with manual jobs:**
   ```bash
   glab ci view
   ```

2. **Trigger manual job:**
   ```bash
   glab ci trigger <job-id>
   ```

### Artifact management

**Download build artifacts:**
```bash
glab ci artifact main build-job
```

**Download from specific pipeline:**
```bash
glab ci artifact main build-job --pipeline-id 987654
```

### CI configuration

**Validate before pushing:**
```bash
glab ci lint
```

**Validate specific file:**
```bash
glab ci lint --path .gitlab-ci-custom.yml
```

### Pipeline operations

**List recent pipelines:**
```bash
glab ci list --per-page 20
```

**Run new pipeline:**
```bash
glab ci run
```

**Run with variables:**
```bash
glab ci run --variables KEY1=value1 --variables KEY2=value2
```

**Cancel running pipeline:**
```bash
glab ci cancel <pipeline-id>
```

**Delete old pipeline:**
```bash
glab ci delete <pipeline-id>
```

## Troubleshooting

**Pipeline stuck/pending:**
- Check runner availability: View pipeline in web UI
- Check job logs: `glab ci trace <job-id>`
- Cancel and retry: `glab ci cancel <id>` then `glab ci run`

**Job failures:**
- View logs: `glab ci trace <job-id>`
- Check artifact uploads: Verify paths in job output
- Validate config: `glab ci lint`

## Related Skills

**Job-specific operations:**
- See `glab-job` for individual job commands (list, view, retry, cancel)
- Use `glab-ci` for pipeline-level, `glab-job` for job-level

**Pipeline triggers and schedules:**
- See `glab-schedule` for scheduled pipeline automation
- See `glab-variable` for managing CI/CD variables

**MR integration:**
- See `glab-mr` for merge operations
- Use `glab mr merge --when-pipeline-succeeds` for CI-gated merges

**Automation:**
- Script: `scripts/ci-debug.sh` for quick failure diagnosis

## Command reference

For complete command documentation and all flags, see [references/commands.md](references/commands.md).

**Available commands:**
- `status` - View pipeline status for current branch
- `view` - View detailed pipeline info
- `list` - List recent pipelines
- `trace` - View job logs (real-time or completed)
- `run` - Create/run new pipeline
- `retry` - Retry failed job
- `cancel` - Cancel running pipeline/job
- `delete` - Delete pipeline
- `trigger` - Trigger manual job
- `artifact` - Download job artifacts
- `lint` - Validate .gitlab-ci.yml
- `config` - Work with CI/CD configuration
- `get` - Get JSON of pipeline
- `run-trig` - Run pipeline trigger
