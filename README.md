```
   ____ _ _   _          _        ____ _     ___   ____  _    _ _ _     
  / ___(_) |_| |    __ _| |__    / ___| |   |_ _| / ___|| | _(_) | |___ 
 | |  _| | __| |   / _` | '_ \  | |   | |    | |  \___ \| |/ / | | / __|
 | |_| | | |_| |__| (_| | |_) | | |___| |___ | |   ___) |   <| | | \__ \
  \____|_|\__|_____\__,_|_.__/   \____|_____|___| |____/|_|\_\_|_|_|___/
                                                                        
```

# GitLab CLI Skills

A collection of skills for AI coding agents following the Agent Skills format. These skills enable AI agents to use the GitLab CLI (`glab`) effectively.

## Available Skills

### [`glab-auth`](./glab-auth)
Manage GitLab CLI authentication (login/logout/status, docker helper, DPoP token).

## Installation

```bash
npx skills add vince-winkintel/gitlab-cli-skills
```

## Usage

Skills are automatically activated when relevant tasks are detected. Example prompts:

- "Log into GitLab CLI"
- "Check glab auth status"
- "Configure GitLab Docker auth"

## Prerequisites

- GitLab CLI installed (`glab`)
- GitLab access token or browser auth

## License

MIT
