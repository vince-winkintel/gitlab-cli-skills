# MCP migration compatibility boundary

Check the installed executable with `glab version` before assessing an existing `glab mcp serve` integration; do not start the legacy server as a discovery probe.

- **glab v1.131.0 removes `glab mcp`, including `glab mcp serve`.** Existing configuration invoking either command breaks on that upgrade; migration must be approved and completed before upgrading a dependent integration.
- **glab v1.130.0 still registers the deprecated experimental command.** A deployment on that release is a legacy integration to migrate, not evidence that the command is supported in current glab. Earlier releases that included MCP may also still run it; this is not a claim that every older release provided it or that the legacy server remains secure or compatible.

For an integration already on the removal side of the boundary, stop invoking the missing command and obtain approval to migrate its configuration and authentication to the [GitLab MCP Server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/). For an integration still on the legacy side, preserve its configuration until an approved migration or removal; do not silently downgrade or pin an obsolete executable to restore service. Current CLI flags, schemas and behavior must not be assumed to apply to a legacy server. No retirement deadline or safe legacy-runtime guarantee is established here.

Immutable evidence:

- [Removal release](https://gitlab.com/gitlab-org/cli/-/releases/v1.131.0) and [removal commit](https://gitlab.com/gitlab-org/cli/-/commit/88f05f96).
- [Current root command registration](https://gitlab.com/gitlab-org/cli/-/blob/206ebab4fc3fa590b720d2885ac890c195c46650/internal/commands/root.go), with no MCP command.
- [Legacy root registration](https://gitlab.com/gitlab-org/cli/-/blob/9b430a11f95ec78d87f19be071d1c381d8803630/internal/commands/root.go) and [deprecated MCP implementation](https://gitlab.com/gitlab-org/cli/-/blob/9b430a11f95ec78d87f19be071d1c381d8803630/internal/commands/mcp/mcp.go).

The [legacy guidance](legacy-skill.md) and [historical help](commands.md) preserve evidence, not instructions for new integrations.
