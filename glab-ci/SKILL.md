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

## Pipeline Configuration

### Getting started with .gitlab-ci.yml

**Use ready-made templates:**

See [templates/](templates/) for production-ready pipeline configurations:
- `nodejs-basic.yml` - Simple Node.js CI/CD
- `nodejs-multistage.yml` - Multi-environment deployments
- `docker-build.yml` - Container builds and deployments

**Validate templates before using:**
```bash
glab ci lint --path templates/nodejs-basic.yml
```

**Best practices guide:**

For detailed configuration guidance, see [references/pipeline-best-practices.md](references/pipeline-best-practices.md):
- Caching strategies
- Multi-stage pipeline patterns
- Coverage reporting integration
- Security scanning
- Performance optimization
- Environment-specific configurations

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

### Runtime Issues

**Pipeline stuck/pending:**
- Check runner availability: View pipeline in web UI
- Check job logs: `glab ci trace <job-id>`
- Cancel and retry: `glab ci cancel <id>` then `glab ci run`

**Job failures:**
- View logs: `glab ci trace <job-id>`
- Check artifact uploads: Verify paths in job output
- Validate config: `glab ci lint`

### Configuration Issues

**Cache not working:**
```bash
# Verify cache key matches lockfile
cache:
  key:
    files:
      - package-lock.json  # Must match actual file name

# Check cache paths are created by jobs
cache:
  paths:
    - node_modules/  # Verify this directory exists after install
```

**Jobs running in wrong order:**
```bash
# Add explicit dependencies with 'needs'
build:
  needs: [lint, test]  # Waits for both to complete
  script:
    - npm run build
```

**Slow builds:**
1. Check cache configuration (see [pipeline-best-practices.md](references/pipeline-best-practices.md#caching-strategies))
2. Parallelize independent jobs:
   ```yaml
   lint:eslint:
     script: npm run lint:eslint
   lint:prettier:
     script: npm run lint:prettier
   ```
3. Use smaller Docker images (`node:20-alpine` vs `node:20`)
4. Optimize artifact sizes (exclude unnecessary files)

**Artifacts not available in later stages:**
```yaml
build:
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour  # Extend if later jobs run after expiry

deploy:
  needs:
    - job: build
      artifacts: true  # Explicitly download artifacts
```

**Coverage not showing in MR:**
```yaml
test:
  script:
    - npm test -- --coverage
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'  # Regex must match output
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

### Performance Optimization Workflow

**1. Identify slow pipelines:**
```bash
glab ci list --per-page 20
```

**2. Analyze job duration:**
```bash
glab ci view --web  # Visual timeline shows bottlenecks
```

**3. Common optimizations:**
- **Parallelize:** Run independent jobs simultaneously
- **Cache aggressively:** Cache dependencies, build outputs
- **Fail fast:** Run quick checks (lint) before slow ones (build)
- **Optimize Docker layers:** Use multi-stage builds, smaller base images
- **Reduce artifact size:** Exclude source maps, test files

**4. Validate improvements:**
```bash
# Compare pipeline duration before/after
glab ci list --per-page 5
```

**See also:** [pipeline-best-practices.md](references/pipeline-best-practices.md#performance-optimization) for detailed optimization strategies.

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

**Configuration Resources:**
- [templates/](templates/) - Ready-to-use pipeline templates
- [pipeline-best-practices.md](references/pipeline-best-practices.md) - Comprehensive configuration guide
- [commands.md](references/commands.md) - Complete command reference

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
