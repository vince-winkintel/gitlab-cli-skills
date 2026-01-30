```
  ____ ___ _____ _        _    ____     ____ _     ___   ____  _  ___ _     _     ____
 / ___|_ _|_   _| |      / \  | __ )   / ___| |   |_ _| / ___|| |/ _ \ |   | |   / ___|
| |  _ | |  | | | |     / _ \ |  _ \  | |   | |    | |  \___ \| | | | |   | |   \___ \
| |_| || |  | | | |___ / ___ \| |_) | | |___| |___ | |   ___) | | |_| |___| |___ ___) |
 \____|___| |_| |_____/_/   \_\____/   \____|_____|___| |____/|_|\___/_____|_____|____/
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
