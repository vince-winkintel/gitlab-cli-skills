---
name: glab-orbit
description: Run the managed Orbit CLI for GitLab Knowledge Graph workflows through glab. Use when discovering Orbit availability, running remote or local Orbit commands, installing or updating the managed orbit-cli binary, or troubleshooting Orbit pass-through authentication. Triggers on orbit, knowledge graph, graph query, orbit remote query, orbit-cli, glab orbit, orbit binary.
---

# glab orbit

Run the managed Orbit CLI for the GitLab Knowledge Graph (product name: **Orbit**) through `glab`.

`glab orbit` routes through the managed `orbit-cli` binary. `glab` downloads, verifies, and updates that binary on first use, then forwards commands and flags verbatim. `glab orbit remote <command>` injects the resolved GitLab credential; other Orbit commands run the managed binary without extra auth environment.

## ⚠️ Experimental Feature

Upstream marks Orbit as **EXPERIMENTAL**:
- most command shape now belongs to the managed `orbit-cli` binary and may change independently
- the API is gated behind the `knowledge_graph` feature flag
- access is user-scoped, not project-scoped
- `glab orbit --install` and `glab orbit --update` install or refresh the managed binary without running it

See: https://docs.gitlab.com/policy/development_stages_support/

## Quick start

```bash
# First: confirm the service is available for your user; glab injects auth for remote commands
glab orbit remote status

# Guided onboarding through the Orbit binary
glab orbit setup claude

# Discover the graph model through orbit-cli
glab orbit remote schema
glab orbit remote dsl
glab orbit remote tools

# Install or update the managed binary without running a command
glab orbit --install
glab orbit --update
```

## Recommended workflow: discover first, query second

Use the Orbit binary's discovery-first flow:

1. `glab orbit setup claude` or `glab orbit remote status` — verify Orbit is enabled and reachable
2. `glab orbit remote schema` — inspect the ontology (entities, edges, properties)
3. `glab orbit remote dsl` — inspect the authoritative JSON Schema for the query DSL
4. `glab orbit remote tools` — inspect the MCP tool manifest when integrating with agents/tools
5. `glab orbit remote query ...` — run actual graph queries once you know the schema

That order matters because `schema` and `dsl` are the source of truth for what the graph exposes and what request bodies are valid; `tools` is still useful for MCP/agent integration metadata.

## Common workflows

### 0) Managed binary setup

```bash
# Install the managed binary without running it
glab orbit --install

# Check for and install updates to the managed binary
glab orbit --update

# Skip wrapper confirmation prompts in non-interactive environments
glab orbit --install --yes
```

Use `orbit_local_auto_download=true` and `orbit_local_auto_run=true` in glab config, or the matching `ORBIT_LOCAL_AUTO_DOWNLOAD=true` and `ORBIT_LOCAL_AUTO_RUN=true` environment variables, when a non-interactive environment must allow the managed binary to download and run.

### 1) Check service health

```bash
# Check the default GitLab host for the current repo/user
glab orbit remote status

# Target a specific GitLab host explicitly
glab orbit remote status --hostname gitlab.com
```

Use this first when you're not sure whether Orbit is even enabled for your account or GitLab instance.

### 2) Inspect the ontology

```bash
# High-level schema overview
glab orbit remote schema

# Expand selected nodes with full detail
glab orbit remote schema User Project MergeRequest
```

Use `schema` to learn what entities exist and which relationships can be traversed.

### 3) Inspect the query DSL schema

```bash
# Show the full query DSL JSON Schema
glab orbit remote dsl
```

`dsl` returns the authoritative JSON Schema for the query DSL. Use this when generating or validating query bodies programmatically.

### 4) Inspect the MCP tool manifest

```bash
# Show the MCP tool manifest
glab orbit remote tools
```

`tools` returns the MCP tool manifest. Use this when integrating Orbit with tool-aware agents or when you need the tool wrapper metadata rather than the bare query DSL schema.

### 5) Run a remote query

`glab orbit remote query` is forwarded to the managed Orbit binary and reads a full Orbit query envelope from a file or stdin:

```json
{
  "query": { "query_type": "..." },
  "response_format": "llm"
}
```

```bash
# Query from a file
glab orbit remote query ./query.json

# Query from stdin
cat ./query.json | glab orbit remote query -

# Force structured JSON for jq pipelines
glab orbit remote query --response-format raw ./query.json
```

Notes:
- Default output is `llm`, which is compact and agent-friendly.
- Use `--response-format raw` when you want structured JSON for further processing.
- Prefer the current Orbit binary's `--response-format` spelling when available; avoid deprecated compatibility aliases in durable automation.
- The query body shape is defined by `glab orbit remote dsl`, not by guesswork.

### 6) Check indexing progress

```bash
# By full path
glab orbit remote graph-status --full-path gitlab-org/gitlab

# By numeric IDs
glab orbit remote graph-status --project-id 278964
glab orbit remote graph-status --namespace-id 9970

# Compact output for agents
glab orbit remote graph-status --full-path gitlab-org/gitlab --response-format llm
```

Use `graph-status` when a query looks incomplete and you need to confirm whether the relevant project/group has been indexed yet.

## Troubleshooting

**Orbit returns 404 / unavailable:**
- Orbit endpoints are typically behind the `knowledge_graph` feature flag.
- Upstream documents exit code `2` for endpoint unavailable.
- Start with `glab orbit remote status` to verify availability before building queries.

**Unauthorized / forbidden:**
- Orbit access is user-scoped.
- Re-check `glab auth status` and confirm the current account has access to a Knowledge Graph-enabled namespace.
- Upstream documents exit code `3` for unauthenticated and `4` for forbidden.

**Rate limited:**
- Upstream documents exit code `5` for HTTP 429 responses.
- Slow down query bursts and prefer fewer, broader discovery calls.

**Query body keeps failing validation:**
- Fetch the current DSL schema with `glab orbit remote dsl`.
- Fetch the ontology with `glab orbit remote schema`.
- Prefer `--response-format raw` when debugging exact response structure.

**Need local/offline graph commands:**
- Use `glab orbit --install` to install the managed binary, then run local Orbit commands through `glab orbit local ...`.
- Keep remote discovery (`status`, `schema`, `dsl`, `tools`) in the workflow so generated local queries still match the server-side graph model.

**Orbit binary fails before command execution:**
- Reinstall with `glab orbit --update`.
- On Windows ARM64, upstream reports x86_64 binary execution failures as an Orbit CLI execution error.

## Related skills

- `glab-api` — fall back to direct REST API calls when you need lower-level GitLab access
- `glab-auth` — verify login state before Orbit calls
- `glab-mcp` — separate MCP server tooling for AI integrations

## Command reference

```text
glab orbit [<command>] [flags]
  --install  Install the Orbit binary without running it
  --update   Check for and install updates to the binary
  --yes      Skip confirmation prompts

Known forwarded workflows include:
  glab orbit setup claude
  glab orbit remote status
  glab orbit remote query ./query.json
  glab orbit remote graph-status --full-path gitlab-org/gitlab
  glab orbit local index
  glab orbit local sql "SELECT 1"
  glab orbit version
```
