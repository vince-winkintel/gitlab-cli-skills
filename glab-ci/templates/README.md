# GitLab CI Pipeline Templates

Ready-to-use `.gitlab-ci.yml` templates for common workflows.

## Available Templates

### 1. nodejs-basic.yml

**Use for:** Simple Node.js projects with basic CI/CD needs

**Includes:**
- Dependency installation with caching
- Linting
- Testing with coverage reports
- Build step
- Manual production deployment

**Best for:**
- Small to medium Node.js applications
- Projects with straightforward deployment
- Getting started with GitLab CI

---

### 2. nodejs-multistage.yml

**Use for:** Node.js projects with multiple environments

**Includes:**
- Separate unit and integration test jobs
- Automatic staging deployment (on `develop` branch)
- Manual production deployment (on `main` branch)
- Review apps for merge requests
- Environment cleanup jobs

**Best for:**
- Production applications with staging environments
- Teams using GitFlow or similar branching strategies
- Projects requiring review apps for MR testing

---

### 3. docker-build.yml

**Use for:** Containerized applications with Docker

**Includes:**
- Docker image build and push to GitLab Container Registry
- Container testing (run tests inside image)
- Security scanning with Trivy
- Multi-tag strategy (SHA, latest, release tags)
- Kubernetes deployment examples
- Registry cleanup jobs

**Best for:**
- Microservices and containerized apps
- Kubernetes deployments
- Projects requiring image security scanning
- Docker-first development workflows

---

## Usage

### Quick Start

1. **Copy the appropriate template:**
   ```bash
   cp glab-ci/templates/nodejs-basic.yml .gitlab-ci.yml
   ```

2. **Customize for your project:**
   - Update deployment commands
   - Set environment URLs
   - Configure variables (if needed)

3. **Validate before pushing:**
   ```bash
   glab ci lint
   ```

4. **Commit and push:**
   ```bash
   git add .gitlab-ci.yml
   git commit -m "Add GitLab CI pipeline"
   git push
   ```

### Validation

Always validate your pipeline configuration before committing:

```bash
# Validate .gitlab-ci.yml in current directory
glab ci lint

# Validate a template before copying
glab ci lint --path glab-ci/templates/nodejs-multistage.yml
```

### Customization Tips

**Adjust Node.js version:**
```yaml
image: node:18-alpine  # Change to 16, 18, 20, etc.
```

**Change package manager:**
```yaml
# For yarn
- yarn install --frozen-lockfile

# For pnpm
- pnpm install --frozen-lockfile
```

**Update cache key for different lockfiles:**
```yaml
cache:
  key:
    files:
      - yarn.lock      # or pnpm-lock.yaml
```

**Configure deployment:**
```yaml
deploy:
  script:
    - npm run deploy           # Generic
    - vercel --prod            # Vercel
    - netlify deploy --prod    # Netlify
    - aws s3 sync dist/ s3://bucket  # AWS S3
```

### Environment Variables

Set required variables in GitLab:
**Settings → CI/CD → Variables**

**Common variables to configure:**
- `VERCEL_TOKEN` - For Vercel deployments
- `NETLIFY_AUTH_TOKEN` - For Netlify deployments
- `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` - For AWS
- `KUBE_CONTEXT` - For Kubernetes deployments
- `DOCKER_AUTH_CONFIG` - For private Docker registries

**Protection:**
- ✅ Mark as **Protected** for production secrets (only available on protected branches)
- ✅ Mark as **Masked** to hide in job logs

---

## Template Comparison

| Feature | nodejs-basic | nodejs-multistage | docker-build |
|---------|--------------|-------------------|--------------|
| **Complexity** | Simple | Medium | Advanced |
| **Stages** | 5 | 5 + review apps | 4 |
| **Environments** | Production only | Staging + Production | Staging + Production |
| **Testing** | Single test job | Unit + Integration | Container testing |
| **Deployment** | Manual | Auto staging, Manual prod | Auto staging, Manual prod |
| **Docker** | No | No | Yes |
| **Security Scan** | No | No | Yes (Trivy) |
| **Review Apps** | No | Yes | No |
| **Best For** | Simple apps | Multi-env apps | Containerized apps |

---

## Advanced Patterns

### Monorepo Support

Add path filters to run jobs only when specific directories change:

```yaml
test:frontend:
  script:
    - npm run test
  rules:
    - changes:
        - frontend/**/*
        - package.json

test:backend:
  script:
    - npm run test
  rules:
    - changes:
        - backend/**/*
        - package.json
```

### Matrix Builds (Multiple Node Versions)

Test across multiple Node.js versions:

```yaml
test:
  parallel:
    matrix:
      - NODE_VERSION: ["16", "18", "20"]
  image: node:${NODE_VERSION}-alpine
  script:
    - npm ci
    - npm test
```

### Scheduled Pipelines

Run nightly builds or cleanup jobs:

**Settings → CI/CD → Schedules**

Then add a rule:

```yaml
cleanup:
  script:
    - cleanup-old-artifacts.sh
  rules:
    - if: '$CI_PIPELINE_SOURCE == "schedule"'
```

---

## Troubleshooting

### Pipeline validation fails

```bash
# Check syntax errors
glab ci lint

# Common issues:
# - Indentation (YAML is whitespace-sensitive)
# - Missing required fields (script, stage)
# - Invalid stage names
```

### Cache not working

```bash
# Verify cache key matches your lockfile
cache:
  key:
    files:
      - package-lock.json  # Must match actual file

# Check cache paths exist
cache:
  paths:
    - node_modules/  # Verify this directory is created
```

### Jobs fail with "npm: command not found"

```bash
# Ensure correct base image
image: node:20-alpine  # Must be a Node.js image
```

### Artifacts not available in later jobs

```yaml
build:
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour  # Extend if jobs run longer

deploy:
  needs:
    - job: build
      artifacts: true  # Explicitly download artifacts
```

---

## Related Skills

- **[glab-ci](../SKILL.md)** - CLI commands for pipeline management
- **[pipeline-best-practices.md](../references/pipeline-best-practices.md)** - Detailed configuration best practices
- **[glab-variable](../../glab-variable/SKILL.md)** - Managing CI/CD variables
- **[glab-schedule](../../glab-schedule/SKILL.md)** - Scheduled pipeline runs

---

## Further Resources

- [GitLab CI/CD YAML Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)
- [GitLab Pipeline Efficiency](https://docs.gitlab.com/ee/ci/pipelines/pipeline_efficiency.html)

---

**Need help?** Run `glab ci lint` to validate your config, or check the [pipeline-best-practices.md](../references/pipeline-best-practices.md) guide for detailed explanations.
