---
name: glab-duo
description: Interact with GitLab Duo AI assistant for code suggestions and chat. Use when accessing AI-powered code assistance, getting code suggestions, or chatting with GitLab Duo. Triggers on Duo, AI assistant, code suggestions, AI chat.
---

# glab duo

## Overview

```

  Work with GitLab Duo, our AI-native assistant for the command line.                                                   
                                                                                                                        
  GitLab Duo for the CLI integrates AI capabilities directly into your terminal                                         
  workflow. It helps you retrieve forgotten Git commands and offers guidance on                                         
  Git operations. You can accomplish specific tasks without switching contexts.                                         
                                                                                                                        
         
  USAGE  
         
    glab duo <command> prompt [command] [--flags]  
            
  COMMANDS  
            
    ask <prompt> [--flags]  Generate Git commands from natural language.
         
  FLAGS  
         
    -h --help               Show help for this command.
```

## Quick start

```bash
glab duo --help
```

## v1.87.0 Changes

### Binary download management
As of v1.87.0, `glab duo` includes a CLI binary download management command for installing and updating the GitLab Duo AI binary.

```bash
# Download/update the Duo CLI binary
glab duo update

# Check current Duo binary version
glab duo --version
```

**When to use:** Run `glab duo update` after upgrading glab to ensure the Duo AI binary matches your CLI version. If `glab duo ask` stops working after a glab upgrade, this is usually the fix.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
