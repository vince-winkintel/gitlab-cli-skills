# glab incident help

> Affected help output refreshed from the checksum-verified glab v1.117.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed.

```

  Work with GitLab incidents.                                                                                           
         
  USAGE  
         
    glab incident [command] [--flags]  
            
  EXAMPLES  
            
    $ glab incident list               
            
  COMMANDS  
            
    close [<id> | <url>] [--flags]   Close an incident.
    list [--flags]                   List project incidents.
    note <incident-id> [--flags]     Comment on an incident in GitLab.
    reopen [<id> | <url>] [--flags]  Reopen a resolved incident.
    subscribe <id>                   Subscribe to an incident.
    unsubscribe <id>                 Unsubscribe from an incident.
    view <id> [--flags]              Display the title, body, and other information about an incident.
         
  FLAGS  
         
    -h --help                        Show help for this command.
    -R --repo                        Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## incident close

```

  Close an incident.                                                                                                    
         
  USAGE  
         
    glab incident close [<id> | <url>] [--flags]                                   
            
  EXAMPLES  
            
    $ glab incident close 123                                                      
    $ glab incident close https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## incident list

```

  List project incidents.                                                                                               
         
  USAGE  
         
    glab incident list [--flags]                             
            
  EXAMPLES  
            
    $ glab incident list --all                               
    $ glab incident ls --all                                 
    $ glab incident list --assignee=@me                      
    $ glab incident list --milestone release-2.0.0 --opened  
         
  FLAGS  
         
    -A --all            Get all incidents.
    -a --assignee       Filter incident by assignee <username>.
    --author            Filter incident by author <username>.
    -c --closed         Get only closed incidents.
    -C --confidential   Filter by confidential incidents.
    -e --epic           List issues belonging to a given epic (requires --group, no pagination support).
    -g --group          Select a group or subgroup. Ignored if a repo argument is set.
    -h --help           Show help for this command.
    --in                Search in: title, description. (title,description)
    -l --label          Filter incident by label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    -m --milestone      Filter incident by milestone <id>.
    --not-assignee      Filter incident by not being assigned to <username>.
    --not-author        Filter incident by not being by author(s) <username>.
    --not-label         Filter incident by lack of label <name>. Multiple labels can be comma-separated or specified by repeating the flag.
    --order             Order incident by <field>. Order options: created_at, updated_at, priority, due_date, relative_position, label_priority, milestone_due, popularity, weight. (created_at)
    -O --output         Options: 'text' or 'json'. (text)
    -F --output-format  Options: 'details', 'ids', 'urls'. (details)
    -p --page           Page number. (1)
    -P --per-page       Number of items to list per page. (30)
    -R --repo           Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    --search            Search <string> in the fields defined by '--in'.
    -s --sort           Sort direction for --order field: asc or desc. (desc)
```

## incident note

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

    glab incident note <incident-id> [--flags]

  EXAMPLES

    # Comment on incident 123, opening an editor for the message
    glab incident note 123

    # Comment with the message given inline
    glab incident note 123 --message "Looking into this now."

    # Attach a screenshot alongside the message
    glab incident note 123 --message "Here is the repro." --attach ./screenshot.png

    # Attach an image piped from the clipboard
    pngpaste - | glab incident note 123 --attach -

  FLAGS

    --attach      (Experimental) Upload a file and reference it at the end of the comment. Use "-" to read the file from standard input. Repeat the flag to attach multiple files.
    -h --help     Show help for this command.
    -m --message  Message text.
    -R --repo     Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## incident reopen

```

  Reopen a resolved incident.                                                                                           
         
  USAGE  
         
    glab incident reopen [<id> | <url>] [--flags]                                   
            
  EXAMPLES  
            
    $ glab incident reopen 123                                                      
    $ glab incident open 123                                                        
    $ glab incident reopen https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## incident subscribe

```

  Subscribe to an incident.                                                                                             
         
  USAGE  
         
    glab incident subscribe <id> [--flags]                                         
            
  EXAMPLES  
            
    $ glab incident subscribe 123                                                  
    $ glab incident sub 123                                                        
    $ glab incident subscribe https://gitlab.com/OWNER/REPO/-/issues/incident/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## incident unsubscribe

```

  Unsubscribe from an incident.                                                                                         
         
  USAGE  
         
    glab incident unsubscribe <id> [--flags]                                         
            
  EXAMPLES  
            
    $ glab incident unsubscribe 123                                                  
    $ glab incident unsub 123                                                        
    $ glab incident unsubscribe https://gitlab.com/OWNER/REPO/-/issues/incident/123  
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## incident view

```

  Display the title, body, and other information about an incident.                                                     
         
  USAGE  
         
    glab incident view <id> [--flags]                                             
            
  EXAMPLES  
            
    $ glab incident view 123                                                      
    $ glab incident show 123                                                      
    $ glab incident view --web 123                                                
    $ glab incident view --comments 123                                           
    $ glab incident view https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123  
         
  FLAGS  
         
    -c --comments     Show incident comments and activities.
    -h --help         Show help for this command.
    -F --output       Format output as: text, json. (text)
    -p --page         Page number. (1)
    -P --per-page     Number of items to list per page. (20)
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
    -s --system-logs  Show system activities and logs.
    -w --web          Open incident in a browser. Uses the default browser, or the browser specified in the $BROWSER variable.
```

