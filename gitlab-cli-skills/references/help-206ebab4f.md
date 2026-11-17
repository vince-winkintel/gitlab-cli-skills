# Captured gitlab-cli-skills help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab (root)

<!-- help-capture: 206ebab4f:52a5f911ec69 -->

```text

  GLab is an open source GitLab CLI tool that brings GitLab to your command line.

  USAGE

    glab <command> <subcommand> [command] [--flags]

  COMMANDS

    alias [command] [--flags]                         Create, list, and delete aliases.
    api <endpoint> [--flags]                          Make an authenticated request to the GitLab API.
    artifact-registry <command> [command]             Authenticate with GitLab Artifact Registry. (EXPERIMENTAL)
    attestation <command> [command] [--flags]         Manage software attestations. (EXPERIMENTAL)
    auth <command> [command]                          Manage authentication for glab.
    changelog <command> [command] [--flags]           Generate changelogs from your project's commit history.
    check-update                                      Check for the latest glab version.
    ci <command> [command] [--flags]                  Work with GitLab CI/CD pipelines and jobs.
    cluster <command> [command] [--flags]             Manage GitLab Agents for Kubernetes and their clusters.
    completion [--flags]                              Generate shell completion scripts.
    config [command] [--flags]                        Manage glab settings.
    container-registry <command> [command] [--flags]  Work with GitLab container registries.
    dependency-firewall <command> [command]           Configure and monitor GitLab Dependency Firewall for local package managers. (BETA)
    deploy-key <command> [command] [--flags]          Manage deploy keys.
    deploy-token <command> [command] [--flags]        Manage deploy tokens.
    duo [command]                                     Work with GitLab Duo.
    gpg-key <command> [command] [--flags]             Manage GPG keys registered with your GitLab account.
    help [command]                                    Help about any command
    incident [command] [--flags]                      Work with GitLab incidents.
    issue [command] [--flags]                         Work with GitLab issues.
    iteration <command> [command] [--flags]           Retrieve iteration information.
    job <command> [command] [--flags]                 Work with GitLab CI/CD jobs.
    label <command> [command] [--flags]               Manage project and group labels.
    milestone <command> [command] [--flags]           Manage group or project milestones.
    minder <command> [command]                        Manage AI governance. (EXPERIMENTAL)
    mr <command> [command] [--flags]                  Create, view, and manage merge requests.
    opentofu <command> [command] [--flags]            Work with the OpenTofu or Terraform integration.
    orbit [command] [<command>] [--flags]             Query the GitLab Orbit context graph. (EXPERIMENTAL)
    packages <command> [command] [--flags]            Manage packages in the GitLab package registry.
    release <command> [command] [--flags]             Manage GitLab releases.
    repo <command> [command] [--flags]                Work with GitLab repositories and projects.
    runner <command> [command] [--flags]              Manage GitLab CI/CD runners.
    runner-controller <command> [command] [--flags]   Manage runner controllers. (EXPERIMENTAL)
    schedule <command> [command] [--flags]            Work with GitLab CI/CD schedules.
    search <command> [command] [--flags]              Search for code and resources in a GitLab project. (BETA)
    securefile <command> [command] [--flags]          Manage secure files for a project.
    security <command> [command] [--flags]            Manage GitLab security scan profiles for a project. (EXPERIMENTAL)
    service-account <command> [command] [--flags]     Manage service accounts.
    skills <command> [command]                        Manage glab agent skills. (EXPERIMENTAL)
    snippet <command> [command] [--flags]             Create snippets.
    ssh-key <command> [command] [--flags]             Manage SSH keys registered with your GitLab account.
    stack <command> [command] [--flags]               Create, manage, and work with stacked diffs. (EXPERIMENTAL)
    timelog <command> [command] [--flags]             Report on time logged on issues and merge requests.
    todo <command> [command] [--flags]                Manage your to-do list.
    token [command] [--flags]                         Manage personal, project, or group tokens.
    user <command> [command] [--flags]                Interact with a GitLab user account.
    variable [command] [--flags]                      Manage variables for a GitLab project or group.
    version                                           Show version information for glab.
    whatsnew [version] [--flags]                      Show release notes for new versions of glab.
    work-items <command> [command] [--flags]          Manage work items. (EXPERIMENTAL)

  FLAGS

    -h --help                                         Show help for this command.
    -v --version                                      Show glab version information.

```

