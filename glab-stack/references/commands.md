# glab stack help

> The `stack`, `stack delete`, and `stack reorder` blocks were captured from the checksum-verified glab v1.120.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed; untouched legacy blocks retain their older renderer formatting. The v1.120.0 release archive SHA-256 is `8769650c49bb5d5ac52156d46e448e87f5570a868fe4e7bfcbd8cc66693c7afb`.

```text

  Stacked diffs are a way of creating small changes that build upon each other to ultimately deliver a feature. This
  kind of workflow can be used to accelerate development time by continuing to build upon your changes, while earlier
  changes in the stack are reviewed and updated based on feedback.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack <command> [command] [--flags]

  EXAMPLES

    glab stack create cool-new-feature
    glab stack sync

  COMMANDS

    amend [--flags]                   Save more changes to a stacked diff. (EXPERIMENTAL)
    create                            Create a new stacked diff. (EXPERIMENTAL)
    delete [<stack-name>] [--flags]   Delete a stack. (EXPERIMENTAL)
    first                             Moves to the first diff in the stack. (EXPERIMENTAL)
    infer <revision-range> [--flags]  Add layers to a stack based on a range of commits. (EXPERIMENTAL)
    last                              Moves to the last diff in the stack. (EXPERIMENTAL)
    list                              Lists all entries in the stack. (EXPERIMENTAL)
    move                              Moves to any selected entry in the stack. (EXPERIMENTAL)
    next                              Moves to the next diff in the stack. (EXPERIMENTAL)
    prev                              Moves to the previous diff in the stack. (EXPERIMENTAL)
    reorder [--flags]                 Reorder a stack of diffs. (EXPERIMENTAL)
    save [--flags]                    Save your progress within a stacked diff. (EXPERIMENTAL)
    switch [stack-name]               Switch between stacks. (EXPERIMENTAL)
    sync [--flags]                    Sync and submit progress on a stacked diff. (EXPERIMENTAL)

  FLAGS

    -h --help                         Show help for this command.
    -R --repo                         Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack amend

```

  Add more changes to an existing stacked diff.                                                                         
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack amend [--flags]                          
            
  EXAMPLES  
            
    # Amend diff with currently staged changes
    $ glab stack amend -m "Fix a function"
    # Add specified file to staged changes and amend diff
    $ glab stack amend newfile -m "forgot to add this"
    # Add all tracked files to staged changes and amend diff
    $ glab stack amend -a -m "fixed a function in exisiting file"
    # Add all tracked and untracked files to staged changes and amend diff
    $ glab stack amend . -m "refactored file into new files"
    # Reword the commit message without adding any files
    $ glab stack amend --reword -m "updated commit message"
         
  FLAGS  
         
    -a --all          Automatically stage modified and deleted tracked files.
    -d --description  A description of the change
    -h --help         Show help for this command.
    -m --message      Alias for the description flag
       --no-verify    Bypass the pre-commit and commit-msg hooks of git-commit(1).
       --reword       Only update the commit message without staging any files.
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack create

```

  Create a new stacked diff. Adds metadata to your `./.git/stacked` directory.                                          
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack create [--flags]           
            
  EXAMPLES  
            
    $ glab stack create cool-new-feature  
    $ glab stack new cool-new-feature     
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack delete

```text

  Delete a stacked diff.

  Removes the stack's local metadata from the `.git/stacked` directory.
  Use this command to clean up stacks for merged or abandoned merge requests.
  Branches, commits, and merge requests are not affected.

  When stack-name is omitted, choose from the list of all stacks.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack delete [<stack-name>] [--flags]

  EXAMPLES

    # Interactively pick from the list of available stacks
    glab stack delete

    # Delete a specific stack by name
    glab stack delete <stack-name>

    # Delete a specific stack without the confirmation prompt
    glab stack delete <stack-name> -y

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -y --yes   Skip the confirmation prompt.

```

## stack first

```

  Moves to the first diff in the stack, and checks out that branch.                                                     
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack first [--flags]  
            
  EXAMPLES  
            
    $ glab stack first          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack infer

```

  Add layers to a stack based on a range of commits.
  This will append layers to an existing stack, or create a new one if needed.

  This feature is experimental. It might be broken or removed without any prior notice.
  Read more about what experimental features mean at
  https://docs.gitlab.com/policy/development_stages_support/

  Use experimental features at your own risk.

  USAGE

    glab stack infer <revision-range> [--flags]

  EXAMPLES

    # Commit range syntax is similar to "git rev-list".
    # The start of the range must be a branch name (not a relative ref like HEAD~5).

    ## Infer stack from commits between main and current branch
    $ glab stack infer main..HEAD

    ## Infer stack from commits on a feature branch since it diverged from develop
    $ glab stack infer develop..HEAD

    ## Create a new stack with a specific name
    $ glab stack infer --name feature-stack main..HEAD

  FLAGS

    -h --help      Show help for this command.
    -n --name      Name for the new stack (used when creating a stack)
    -R --repo      Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack last

```

  Moves to the last diff in the stack, and checks out that branch.                                                      
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack last [--flags]  
            
  EXAMPLES  
            
    $ glab stack last          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack list

```

  Lists all entries in the stack. To select a different revision, use a command like 'stack move'.                      
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack list [--flags]  
            
  EXAMPLES  
            
    $ glab stack list          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack move

```

  Shows a menu with a fuzzy finder to select a stack.                                                                   
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack move [--flags]  
            
  EXAMPLES  
            
    $ glab stack move          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack next

```

  Moves to the next diff in the stack, and checks out that branch.                                                      
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack next [--flags]  
            
  EXAMPLES  
            
    $ glab stack next          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack prev

```

  Moves to the previous diff in the stack, and checks out that branch.                                                  
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack prev [--flags]  
            
  EXAMPLES  
            
    $ glab stack prev          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack reorder

```text

  Change the order of diffs in the current stack.

  You choose the new order in your editor. After you save and close the file, each branch is then rebased onto its new
  parent so the local Git history matches the new order, and each diff is retargeted onto the branch before it to
  reflect the new order. Nothing is pushed. GitLab shows the old commits until you run `glab stack sync` to force-push
  the rebased branches.

  If a rebase hits a conflict, resolve it, finish the rebase with `git rebase --continue` and then run `glab stack
  reorder --continue`. Alternatively, run `glab stack reorder --abort` to restore the original branch order.
  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab stack reorder [--flags]

  EXAMPLES

    # Reorder the stack by choosing a new branch order in your editor
    glab stack reorder

    # Continue a reorder after resolving a conflict
    glab stack reorder --continue

    # Abort a reorder and restore the original branch order
    glab stack reorder --abort

  FLAGS

    --abort     Abort a reorder and restore original branch state.
    --continue  Continue a reorder after resolving conflicts.
    -h --help   Show help for this command.
    -R --repo   Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## stack save

```

  Save your current progress with a diff on the stack.                                                                  
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack save [--flags]                  
            
  EXAMPLES  
            
    $ glab stack save added_file               
    $ glab stack save . -m "added a function"  
    $ glab stack save -m "added a function"    
         
  FLAGS  
         
    -d --description  Description of the change.
    -h --help         Show help for this command.
    -m --message      Alias for the description flag.
       --no-verify    Bypass the pre-commit and commit-msg hooks of git-commit(1).
    -R --repo         Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack switch

```

  Switch between stacks to work on another stack created with "glab stack create".                                      
  When stack-name is omitted, choose from the list of all stacks.                                                       
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack switch [stack-name] [--flags]  
            
  EXAMPLES  
            
    $ glab stack switch                       
    $ glab stack switch <stack-name>          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

## stack sync

```

  Sync and submit progress on a stacked diff. This command runs these steps:                                            
                                                                                                                        
  1. Optional. If working in a fork, select whether to push to the fork,                                                
     or the upstream repository.                                                                                        
  1. Pushes any amended changes to their merge requests.                                                                
  1. Rebases any changes that happened previously in the stack.                                                         
  1. Removes any branches that were already merged, or with a closed merge request.                                     
                                                                                                                        
  This feature is experimental. It might be broken or removed without any prior notice.                                 
  Read more about what experimental features mean at                                                                    
  https://docs.gitlab.com/policy/development_stages_support/                                                            
                                                                                                                        
  Use experimental features at your own risk.                                                                           
                                                                                                                        
         
  USAGE  
         
    glab stack sync [--flags]  
            
  EXAMPLES  
            
    $ glab stack sync          
         
  FLAGS  
         
    -h --help  Show help for this command.
    -R --repo  Select another repository. Can use either `OWNER/REPO` or `GROUP/NAMESPACE/REPO` format. Also accepts full URL or Git URL.
```

