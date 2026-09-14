# glab issue help

> Selected help blocks were refreshed from the checksum-verified glab v1.117.0 macOS arm64 release binary. Refreshed renderer output removes terminal padding and trailing whitespace; untouched legacy blocks may retain older padding or inherited-flag wording.

```

  Work with GitLab issues.                                                                                              
         
  USAGE  
         
    glab issue [command] [--flags]                                         
            
  EXAMPLES  
            
    $ glab issue list                                                      
    $ glab issue create --label --confidential                             
    $ glab issue view --web 123                                            
    $ glab issue note -m "closing because !123 was merged" <issue number>  
            
  COMMANDS  
            
    board [command] [--flags]        Work with GitLab issue boards in the given project.
    close [<id> | <url>] [--flags]   Close an issue.
    create [--flags]                 Create an issue.
    delete <id>                      Delete an issue.
    list [--flags]                   List project issues.
    note <issue-id> [--flags]        Comment on an issue in GitLab.
    reopen [<id> | <url>] [--flags]  Reopen a closed issue.
    subscribe <id>                   Subscribe to an issue.
    unsubscribe <id>                 Unsubscribe from an issue.
    update <id> [--flags]            Update issue
    view <id> [--flags]              Display the title, body, and other information about an issue.
         
  FLAGS  
         
    -h --help                        Show help for this command.
    -R --repo                        Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue board

```

  Work with GitLab issue boards in the given project.                                                                   
         
  USAGE  
         
    glab issue board [command] [--flags]  
            
  COMMANDS  
            
    create [--flags]  Create a project issue board.
    view [--flags]    View project issue board.
         
  FLAGS  
         
    -h --help         Show help for this command.
    -R --repo         Select another repository using the OWNER/REPO format or the project ID. Supports group namespaces.
```

## issue board view

```
Opens an interactive view of the project's issue boards in your terminal, where you can browse issues by list.

USAGE
  glab issue board view [--flags]

EXAMPLES
  glab issue board view

FLAGS
  -a --assignee   Filter board issues by assignee username.
  -h --help       Show help for this command.
  -l --labels     Filter board issues by labels. Multiple labels can be comma-separated or specified by repeating the flag.
  -m --milestone  Filter board issues by milestone.
     --paginate   Make additional HTTP requests to retrieve all board issues.
  -R --repo       Select another repository using the OWNER/REPO format or the project ID. Supports group namespaces.
```

## issue close

```

  Close an issue.                                                                                                       
         
  USAGE  
         
    glab issue close [<id> | <url>] [--flags]                          
            
  EXAMPLES  
            
    $ glab issue close 123                                             
    $ glab issue close https://gitlab.com/NAMESPACE/REPO/-/issues/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue create

```

  Opens an editor to draft the issue unless you pass a title and
  description. Use `--web` to create the issue in your browser, or
  `--template` to start from an issue template.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. An attachment satisfies the description requirement, so `--title` with
  `--attach` completes without prompting.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.

  The `--recover` flag is an experiment: it might be unstable or
  removed at any time, and is not ready for production use. For more
  information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab issue create [--flags]

  EXAMPLES

    glab issue create
    glab issue new
    glab issue create -m release-2.0.0 -t "we need this feature" --label important
    glab issue new -t "Fix CVE-YYYY-XXXX" -l security --linked-mr 123
    glab issue create -m release-1.0.1 -t "security fix" --label security --web --recover
    glab issue create -t "Bug Report" --template bug
    glab issue create -t "Feature Request" --template feature_proposal.md --yes

    # Read the description from a file
    glab issue create -t "we need this feature" --description-file description.md

    # Read the description from standard input
    cat description.md | glab issue create -t "we need this feature" --description-file -

    # Attach a screenshot to the description
    glab issue create -t "Login button misaligned" -d "See below." --attach ./screenshot.png

  FLAGS

    -a --assignee       Assign issue to people by their `usernames`. Multiple usernames can be comma-separated or specified by repeating the flag.
    --attach            (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -c --confidential   Set an issue to be confidential.
    -d --description    Issue description. Set to "-" to open an editor.
    --description-file  Read the issue description from a file. Use "-" to read from standard input.
    --due-date          A date in 'YYYY-MM-DD' format.
    --epic              Id of the epic to add the issue to.
    -h --help           Show help for this command.
    -l --label          Add label by name. Multiple labels can be comma-separated or specified by repeating the flag.
    --link-type         Type for the issue link. (relates_to)
    --linked-issues     The IIDs of issues that this issue links to. Multiple IIDs can be comma-separated or specified by repeating the flag.
    --linked-mr         The IID of a merge request in which to resolve all issues.
    -m --milestone      The global ID or title of a milestone to assign.
    --no-editor         Don't open editor to enter a description. If set to true, uses prompt.
    --recover           Save the options to a file if the issue fails to be created. If the file exists, the options will be loaded from the recovery file. (EXPERIMENTAL)
    -R --repo           Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --template          Name of a template in '.gitlab/issue_templates/' to pre-populate the description. The '.md' extension is optional. Templates are loaded from the local repository only.
    -e --time-estimate  Set time estimate for the issue.
    -s --time-spent     Set time spent for the issue.
    -t --title          Issue title.
    --web               Continue issue creation with web interface.
    -w --weight         Issue weight. Valid values are greater than or equal to 0.
    -y --yes            Don't prompt for confirmation to submit the issue.

```

## issue delete

```

  Delete an issue.                                                                                                      
         
  USAGE  
         
    glab issue delete <id> [--flags]                                    
            
  EXAMPLES  
            
    $ glab issue delete 123                                             
    $ glab issue del 123                                                
    $ glab issue delete https://gitlab.com/profclems/glab/-/issues/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue list

```

  List project issues.                                                                                                  
         
  USAGE  
         
    glab issue list [--flags]                             
            
  EXAMPLES  
            
    $ glab issue list --all                               
    $ glab issue ls --all                                 
    $ glab issue list --assignee=@me                      
    $ glab issue list --milestone release-2.0.0 --opened  
         
  FLAGS  
         
    -A --all            Get all issues.
    -a --assignee       Filter issue by assignee <username>.
    --author            Filter issue by author <username>.
    -c --closed         Get only closed issues.
    -C --confidential   Filter by confidential issues.
    -e --epic           List issues belonging to a given epic (requires --group, no pagination support).
    -g --group          Select a group or subgroup. Ignored if a repo argument is set.
    -h --help           Show help for this command.
    --in                Search in: title, description. (title,description)
    -t --issue-type     Filter issue by its type. Options: issue, incident, test_case.
    -i --iteration      Filter issue by iteration <id>.
    -l --label          Filter issue by label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    -m --milestone      Filter issue by milestone <id>.
    --not-assignee      Filter issue by not being assigned to <username>.
    --not-author        Filter issue by not being by author(s) <username>.
    --not-label         Filter issue by lack of label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    --order             Order issue by <field>. Order options: created_at, updated_at, priority, due_date, relative_position, label_priority, milestone_due, popularity, weight. (created_at)
    -O --output         Options: 'text' or 'json'. (text)
    -F --output-format  Options: 'details', 'ids', 'urls'. (details)
    -p --page           Page number. (1)
    -P --per-page       Number of items to list per page. (30)
    -R --repo           Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    --search            Search <string> in the fields defined by '--in'.
    -s --sort           Sort direction for --order field: asc or desc. (desc)
```

## issue note

```

  Opens an editor for the comment if you don't use `--message`.

  `--attach` uploads a file and references it at the end of the comment. Repeat the flag for more than one file, or pass
  `-` to read the file from standard input. An attachment is content on its own, so a comment with only `--attach` skips
  the editor.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab issue note <issue-id> [--flags]

  EXAMPLES

    # Comment on issue 123, opening an editor for the message
    glab issue note 123

    # Comment with the message given inline
    glab issue note 123 --message "Looking into this now."

    # Attach a screenshot alongside the message
    glab issue note 123 --message "Here is the repro." --attach ./screenshot.png

    # Attach an image piped from the clipboard
    pngpaste - | glab issue note 123 --attach -

  FLAGS

    --attach      (Experimental) Upload a file and reference it at the end of the comment. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -h --help     Show help for this command.
    -m --message  Message text.
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## issue reopen

```

  Reopen a closed issue.                                                                                                
         
  USAGE  
         
    glab issue reopen [<id> | <url>] [--flags]                          
            
  EXAMPLES  
            
    $ glab issue reopen 123                                             
    $ glab issue open 123                                               
    $ glab issue reopen https://gitlab.com/NAMESPACE/REPO/-/issues/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue subscribe

```

  Subscribe to an issue.                                                                                                
         
  USAGE  
         
    glab issue subscribe <id> [--flags]                                
            
  EXAMPLES  
            
    $ glab issue subscribe 123                                         
    $ glab issue sub 123                                               
    $ glab issue subscribe https://gitlab.com/OWNER/REPO/-/issues/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue unsubscribe

```

  Unsubscribe from an issue.                                                                                            
         
  USAGE  
         
    glab issue unsubscribe <id> [--flags]                                
            
  EXAMPLES  
            
    $ glab issue unsubscribe 123                                         
    $ glab issue unsub 123                                               
    $ glab issue unsubscribe https://gitlab.com/OWNER/REPO/-/issues/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## issue update

```

  Change an issue's labels, assignees, milestone, title, or
  description. Use `--label` and `--unlabel` to add or remove
  labels.

  `--attach` uploads a file and references it at the end of the description. Repeat the flag for more than one file, or
  pass `-` to read the file from standard input. Without `--description` the references are added to the description the
  issue already has, instead of replacing it.

  The `--attach` flag is an experiment. It might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab issue update <id> [--flags]

  EXAMPLES

    glab issue update 42 --label ui,ux
    glab issue update 42 --unlabel working

    # Read the description from a file
    glab issue update 42 --description-file description.md

    # Read the description from standard input
    cat description.md | glab issue update 42 --description-file -

    # Add a screenshot to the existing description
    glab issue update 42 --attach ./screenshot.png

  FLAGS

    -a --assignee        Assign users by username. Prefix with '!' or '-' to remove from existing assignees, or '+' to add new. Otherwise, replace existing assignees with these users. Multiple usernames can be comma-separated or specified by repeating the flag.
    --attach             (Experimental) Upload a file and reference it at the end of the description. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -c --confidential    Make issue confidential.
    -d --description     Issue description. Set to "-" to open an editor.
    --description-file   Read the issue description from a file. Use "-" to read from standard input.
    --due-date           A date in 'YYYY-MM-DD' format.
    -h --help            Show help for this command.
    -l --label           Add labels.
    --lock-discussion    Lock discussion on issue.
    -m --milestone       Title of the milestone to assign Set to "" or 0 to unassign.
    -p --public          Make issue public.
    -R --repo            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title           Title of issue.
    --unassign           Unassign all users.
    -u --unlabel         Remove labels.
    --unlock-discussion  Unlock discussion on issue.
    -w --weight          Set weight of the issue.

```

## issue view

```

  Display the title, body, and other information about an issue.                                                        
         
  USAGE  
         
    glab issue view <id> [--flags]                                    
            
  EXAMPLES  
            
    $ glab issue view 123                                             
    $ glab issue show 123                                             
    $ glab issue view --web 123                                       
    $ glab issue view --comments 123                                  
    $ glab issue view https://gitlab.com/NAMESPACE/REPO/-/issues/123  
         
  FLAGS  
         
    -c --comments     Show issue comments and activities.
    -h --help         Show help for this command.
    -F --output       Format output as: text, json. (text)
    -p --page         Page number. (1)
    -P --per-page     Number of items to list per page. (20)
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -s --system-logs  Show system activities and logs.
    -w --web          Open issue in a browser. Uses the default browser, or the browser specified in the $BROWSER variable.
```
