# GitLab CI Pipeline Best Practices

This reference provides best practices for writing effective `.gitlab-ci.yml` configurations that are fast, reliable, and maintainable.

## Table of Contents

- [Caching Strategies](#caching-strategies)
- [Multi-Stage Pipeline Patterns](#multi-stage-pipeline-patterns)
- [Coverage Reporting Integration](#coverage-reporting-integration)
- [Security Scanning](#security-scanning)
- [Common Pipeline Patterns](#common-pipeline-patterns)
- [Performance Optimization](#performance-optimization)
- [Environment-Specific Configurations](#environment-specific-configurations)

---

## Caching Strategies

Effective caching dramatically reduces build times by reusing dependencies and build artifacts across pipeline runs.

### Node.js Caching (node_modules)

**Best Practice: Cache based on lockfile hash**

```yaml
cache:
  key:
    files:
      - package-lock.json  # or yarn.lock, pnpm-lock.yaml
  paths:
    - node_modules/
    - .npm/  # npm cache directory
```

**Why it works:**
- Cache key updates only when dependencies change
- Avoids expensive `npm install` on every run
- `.npm/` caching speeds up `npm ci` even on cache miss

### Per-Job Caching

```yaml
variables:
  NPM_CONFIG_CACHE: "$CI_PROJECT_DIR/.npm"

cache:
  key: "$CI_COMMIT_REF_SLUG"
  paths:
    - node_modules/
    - .npm/
    - .next/cache/  # Next.js build cache

build:
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - .next/  # Build output for reuse in deploy stage
    policy: push  # Only write to cache
```

### Cache Policies

- `pull` - Download cache, don't update it (default for most jobs)
- `push` - Upload cache, don't download it (good for install/build jobs)
- `pull-push` - Both download and upload (default when not specified)

**Example:**

```yaml
install:
  cache:
    policy: pull-push  # Update cache with fresh dependencies
  script:
    - npm ci

test:
  cache:
    policy: pull  # Only read cache, don't update
  script:
    - npm test
```

### Cache Invalidation

**Force cache refresh:**
```yaml
cache:
  key: "$CI_COMMIT_REF_SLUG-v2"  # Increment version to bust cache
```

**Branch-specific caching:**
```yaml
cache:
  key: "$CI_COMMIT_REF_SLUG"  # Different cache per branch
```

**Fallback cache keys:**
```yaml
cache:
  key:
    files:
      - package-lock.json
  fallback_keys:
    - "$CI_COMMIT_REF_SLUG"  # Use branch cache if lockfile cache miss
    - default                # Use default cache as last resort
```

---

## Multi-Stage Pipeline Patterns

Structure pipelines with clear stages for better parallelization and failure isolation.

### Standard Stages

```yaml
stages:
  - install      # Install dependencies once
  - lint         # Fast quality checks (fail early)
  - test         # Run test suites
  - build        # Create production artifacts
  - deploy       # Deploy to environments
```

### Dependencies Between Jobs

**Sequential execution:**

```yaml
build:
  stage: build
  needs: [lint, test]  # Wait for both to complete
  script:
    - npm run build
```

**Parallel execution:**

```yaml
lint:
  stage: lint
  script:
    - npm run lint

test:unit:
  stage: test
  script:
    - npm run test:unit

test:integration:
  stage: test
  script:
    - npm run test:integration
```

Both test jobs run in parallel since they don't depend on each other.

### Artifact Sharing Between Stages

```yaml
install:
  stage: install
  script:
    - npm ci
  artifacts:
    paths:
      - node_modules/
    expire_in: 1 hour  # Clean up after pipeline completes

build:
  stage: build
  needs:
    - job: install
      artifacts: true  # Download artifacts from install job
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
      - .next/
    expire_in: 1 week
```

### Branch-Based Workflow

```yaml
deploy:staging:
  stage: deploy
  script:
    - deploy-to-staging.sh
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

deploy:production:
  stage: deploy
  script:
    - deploy-to-production.sh
  environment:
    name: production
    url: https://example.com
  only:
    - main
  when: manual  # Require manual approval
```

**Rules-based alternative (more flexible):**

```yaml
deploy:staging:
  stage: deploy
  script:
    - deploy-to-staging.sh
  environment:
    name: staging
  rules:
    - if: '$CI_COMMIT_BRANCH == "develop"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: manual

deploy:production:
  stage: deploy
  script:
    - deploy-to-production.sh
  environment:
    name: production
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
```

---

## Coverage Reporting Integration

Display test coverage directly in GitLab merge requests.

### Jest Coverage (Node.js)

```yaml
test:
  stage: test
  script:
    - npm test -- --coverage --coverageReporters=text --coverageReporters=lcov
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'  # Extract coverage percentage
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
    paths:
      - coverage/
    expire_in: 30 days
```

**What this does:**
- `coverage: '/regex/'` - Extracts coverage percentage for badge display
- `coverage_report` - Enables MR diff coverage annotations
- `cobertura` format - GitLab's preferred coverage format

### Vitest Coverage

```yaml
test:
  stage: test
  script:
    - npm test -- --coverage --reporter=verbose
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

### Coverage Thresholds

**Fail pipeline if coverage drops:**

```yaml
test:
  script:
    - npm test -- --coverage --coverageThreshold='{"global":{"lines":80}}'
  allow_failure: false
```

### Coverage Badges

GitLab automatically generates coverage badges from the extracted percentage:

```markdown
![coverage](https://gitlab.com/your-group/your-project/badges/main/coverage.svg)
```

---

## Security Scanning

Integrate security scanning into your pipeline to catch vulnerabilities early.

### Dependency Scanning (npm audit)

```yaml
security:audit:
  stage: test
  script:
    - npm audit --audit-level=moderate
  allow_failure: true  # Don't block pipeline, but flag issues
```

**Stricter enforcement:**

```yaml
security:audit:
  script:
    - npm audit --audit-level=high --production
  allow_failure: false  # Block pipeline on high/critical vulnerabilities
```

### SAST (Static Application Security Testing)

**Using GitLab's built-in SAST:**

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml

variables:
  SAST_EXCLUDED_PATHS: "spec,test,tests,tmp,node_modules"
```

### License Compliance

```yaml
license:check:
  stage: test
  script:
    - npx license-checker --onlyAllow "MIT;Apache-2.0;BSD-3-Clause;ISC"
  allow_failure: true
```

### Secret Detection

**Prevent secrets from being committed:**

```yaml
include:
  - template: Security/Secret-Detection.gitlab-ci.yml
```

### Docker Image Scanning

```yaml
container:scan:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker pull $CI_REGISTRY_IMAGE:latest
    - docker run --rm aquasec/trivy image $CI_REGISTRY_IMAGE:latest
```

---

## Common Pipeline Patterns

### Matrix Builds (Multiple Node Versions)

```yaml
test:
  stage: test
  parallel:
    matrix:
      - NODE_VERSION: ["16", "18", "20"]
  image: node:${NODE_VERSION}
  script:
    - npm ci
    - npm test
```

### Conditional Jobs

**Run only on merge requests:**

```yaml
lint:mr-only:
  stage: lint
  script:
    - npm run lint
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

**Run only on main branch:**

```yaml
deploy:
  stage: deploy
  script:
    - deploy.sh
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
```

**Run on tags:**

```yaml
release:
  stage: deploy
  script:
    - create-release.sh
  rules:
    - if: '$CI_COMMIT_TAG'
```

### Manual Jobs with Auto-deploy Option

```yaml
deploy:production:
  stage: deploy
  script:
    - deploy.sh
  when: manual
  allow_failure: false  # Pipeline waits for manual trigger
  environment:
    name: production
    on_stop: stop:production  # Enable environment cleanup

stop:production:
  stage: deploy
  script:
    - cleanup.sh
  when: manual
  environment:
    name: production
    action: stop
```

### Retry Failed Jobs Automatically

```yaml
test:flaky:
  script:
    - npm run test:integration
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure
```

### Timeout Configuration

```yaml
build:
  script:
    - npm run build
  timeout: 30m  # Override default 1h timeout
```

---

## Performance Optimization

### Fail Fast Strategy

Run quick checks before expensive ones:

```yaml
stages:
  - lint       # ~30 seconds
  - test       # ~2 minutes
  - build      # ~5 minutes
  - deploy     # ~3 minutes

lint:
  stage: lint
  script:
    - npm run lint
  allow_failure: false  # Stop pipeline immediately if fails

test:
  stage: test
  needs: [lint]  # Only run if lint passes
  script:
    - npm test
```

### Parallelize Independent Jobs

```yaml
lint:eslint:
  stage: lint
  script:
    - npm run lint:eslint

lint:prettier:
  stage: lint
  script:
    - npm run lint:prettier

lint:types:
  stage: lint
  script:
    - npm run check-types
```

All three lint jobs run simultaneously.

### Use Smaller Docker Images

```yaml
# ❌ Slow - full image download every time
image: node:20

# ✅ Fast - smaller alpine image
image: node:20-alpine

# ✅ Even faster - cache locally built image
image: $CI_REGISTRY_IMAGE/node-build:latest
```

### Optimize Artifact Size

```yaml
build:
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
    exclude:
      - dist/**/*.map  # Exclude source maps
      - dist/**/*.test.js
    expire_in: 1 day  # Auto-cleanup
```

### Pipeline Efficiency Metrics

**Check pipeline duration:**
```bash
glab ci list --per-page 10
```

**Identify slow jobs:**
```bash
glab ci view --web  # Visual timeline of jobs
```

**Optimize based on:**
- Jobs taking longest → parallelize or optimize
- Jobs failing most → add retries or fix flakiness
- Cache hit rate → adjust cache keys

---

## Environment-Specific Configurations

### Environment Variables

**Pipeline-level:**

```yaml
variables:
  NODE_ENV: "production"
  API_BASE_URL: "https://api.example.com"
```

**Job-level:**

```yaml
deploy:staging:
  variables:
    API_BASE_URL: "https://staging-api.example.com"
  script:
    - deploy.sh
```

**Protected environments:**

Store secrets in GitLab CI/CD variables (Settings → CI/CD → Variables):
- Mark as "Protected" - only available on protected branches
- Mark as "Masked" - hidden in job logs

```yaml
deploy:production:
  script:
    - deploy.sh
  environment:
    name: production
  variables:
    DATABASE_URL: $PRODUCTION_DB_URL  # Protected variable
```

### Dynamic Environments

**Review apps:**

```yaml
review:
  stage: deploy
  script:
    - deploy-review-app.sh
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    url: https://$CI_COMMIT_REF_SLUG.review.example.com
    on_stop: stop:review
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'

stop:review:
  stage: deploy
  script:
    - cleanup-review-app.sh
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    action: stop
  when: manual
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

### Environment Protection

```yaml
deploy:production:
  environment:
    name: production
    deployment_tier: production  # Visible in deployment boards
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual  # Require approval
```

**Set in GitLab UI (Settings → CI/CD → Environments):**
- Protected - only deployable by maintainers
- Deployment approvals - require manual approval before deploy

---

## Validation & Testing

Before pushing your pipeline config:

```bash
# Validate syntax
glab ci lint

# Validate specific file
glab ci lint --path .gitlab-ci-custom.yml

# Dry run (simulate without executing)
glab ci run --dry-run
```

---

## Further Reading

- [GitLab CI/CD YAML Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)
- [GitLab CI/CD Best Practices](https://docs.gitlab.com/ee/ci/pipelines/pipeline_efficiency.html)

**Related glab-cli-skills:**
- [glab-ci](../SKILL.md) - CLI commands for pipeline management
- [glab-job](../../glab-job/SKILL.md) - Job-specific operations
- [glab-variable](../../glab-variable/SKILL.md) - Managing CI/CD variables
- [glab-schedule](../../glab-schedule/SKILL.md) - Scheduled pipelines
