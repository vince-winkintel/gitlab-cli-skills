---
name: glab-mcp
description: Migrate integrations that still invoke the removed glab mcp command. Use for legacy glab mcp serve configuration and historical reference; current integrations should use the GitLab MCP Server.
---

# Removed glab MCP integration

Check `glab version` against the [migration compatibility boundary](references/compatibility.md) to distinguish a legacy integration from one already broken by removal. Current glab does not provide `glab mcp` or `glab mcp serve`. Do not invoke them or configure a new integration around them. Use the [GitLab MCP Server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) for a supported integration, with separate authorization for configuration, authentication, and external actions.

This installation identity remains for migration routing. The [legacy skill](references/legacy-skill.md) and [older help captures](references/commands.md) are historical evidence only; their command examples and behavior are not current instructions. Preserve existing integration configuration until its migration or removal is explicitly authorized.
