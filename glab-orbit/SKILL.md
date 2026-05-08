---
name: glab-orbit
description: Query the GitLab Knowledge Graph (Orbit) from the CLI. Use when discovering Orbit availability, inspecting schema/tools, running graph queries, or checking graph indexing status. Triggers on orbit, knowledge graph, graph query, orbit schema, orbit remote query, orbit tools.
---

# glab orbit

Access the GitLab Knowledge Graph (product name: **Orbit**) from `glab`.

In v1.94.0, the user-facing surface is the new experimental `glab orbit` command family, focused on **remote** Knowledge Graph access.

## ⚠️ Experimental Feature

Upstream marks Orbit as **EXPERIMENTAL**:
- command shape may change
- the API is gated behind the `knowledge_graph` feature flag
- access is user-scoped, not project-scoped
- `glab orbit local` is mentioned as coming soon, but v1.94.0 is effectively about `glab orbit remote`

See: https://docs.gitlab.com/policy/development_stages_support/

## Quick start

```bash
# First: confirm the service is available for your user
glab orbit remote status

# Discover the graph model
glab orbit remote schema
glab orbit remote tools

# Inspect specific node types
glab orbit remote schema User Project MergeRequest
```

## Recommended workflow: discover first, query second

The upstream docs strongly point to a discovery-first flow:

1. `glab orbit remote status` — verify Orbit is enabled and reachable
2. `glab orbit remote schema` — inspect the ontology (entities, edges, properties)
3. `glab orbit remote tools` — inspect the authoritative JSON Schema for the query DSL
4. `glab orbit remote query ...` — run actual graph queries once you know the schema

That order matters because `schema` and `tools` are the source of truth for what the graph exposes and what request bodies are valid.

## Common workflows

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
# Show the MCP tool manifest / DSL schema
glab orbit remote tools
```

`tools` returns the authoritative JSON Schema for the query DSL in the `query_graph` tool manifest. Use this when generating or validating query bodies programmatically.

### 4) Run a remote query

`glab orbit remote query` reads a full Orbit query envelope from a file or stdin:

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
glab orbit remote query --format raw ./query.json
```

Notes:
- Default output is `llm`, which is compact and agent-friendly.
- Use `--format raw` when you want structured JSON for further processing.
- The query body shape is defined by `glab orbit remote tools`, not by guesswork.

### 5) Check indexing progress

```bash
# By full path
glab orbit remote graph-status --full-path gitlab-org/gitlab

# By numeric IDs
glab orbit remote graph-status --project-id 278964
glab orbit remote graph-status --namespace-id 9970

# Compact output for agents
glab orbit remote graph-status --full-path gitlab-org/gitlab --format llm
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
- Fetch the current DSL schema with `glab orbit remote tools`.
- Fetch the ontology with `glab orbit remote schema`.
- Prefer `--format raw` when debugging exact response structure.

**Need local/offline graph commands:**
- The v1.94.0 docs only document `glab orbit remote`.
- `glab orbit local` is mentioned as coming soon, not as current guidance.

## Related skills

- `glab-api` — fall back to direct REST API calls when you need lower-level GitLab access
- `glab-auth` — verify login state before Orbit calls
- `glab-mcp` — separate MCP server tooling for AI integrations

## Command reference

```text
glab orbit remote status [flags]
  --hostname    Target GitLab host

glab orbit remote schema [node...] [flags]
  --hostname    Target GitLab host

glab orbit remote tools [flags]
  --hostname    Target GitLab host

glab orbit remote query [file|-] [flags]
  --format      llm|raw (default: llm)
  --hostname    Target GitLab host

glab orbit remote graph-status [flags]
  --format        raw|llm (default: raw)
  --full-path     Project/group full path
  --hostname      Target GitLab host
  --namespace-id  Group ID
  --project-id    Project ID
```
