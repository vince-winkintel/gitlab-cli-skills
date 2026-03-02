---
name: glab-mcp
description: Work with Model Context Protocol (MCP) server for AI assistant integration. Exposes GitLab features as tools for AI assistants (like Claude Code) to interact with projects, issues, merge requests, and pipelines. Use when integrating AI assistants with GitLab or working with MCP servers. Triggers on MCP, Model Context Protocol, AI assistant integration, glab mcp serve.
---

# glab mcp

## Overview

```

  Manage Model Context Protocol server features for GitLab integration.                                                 
                                                                                                                        
  The MCP server exposes GitLab features as tools for use by                                                            
  AI assistants (like Claude Code) to interact with GitLab projects, issues,                                            
  merge requests, pipelines, and other resources.                                                                       
                                                                                                                        
  This feature is an experiment and is not ready for production use.                                                    
  It might be unstable or removed at any time.                                                                          
  For more information, see                                                                                             
  https://docs.gitlab.com/policy/development_stages_support/.                                                           
                                                                                                                        
         
  USAGE  
         
    glab mcp <command> [command] [--flags]  
            
  EXAMPLES  
            
    $ glab mcp serve                        
            
  COMMANDS  
            
    serve      Start a MCP server with stdio transport. (EXPERIMENTAL)
         
  FLAGS  
         
    -h --help  Show help for this command.
```

## Quick start

```bash
glab mcp --help
```

## v1.86.0 Changes

### Auto-enabled JSON output
As of v1.86.0, `glab mcp serve` automatically enables JSON output format when running — no manual flag needed. This improves parsing reliability for AI assistants consuming the MCP server's tool responses.

### Unannotated commands excluded
Commands that lack MCP annotations are no longer registered as MCP tools. This means only explicitly supported commands are exposed to AI assistants, reducing noise and improving reliability. If a GitLab operation you expect isn't available as an MCP tool, it may lack MCP annotations in the current release.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
