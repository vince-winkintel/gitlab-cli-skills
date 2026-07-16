# glab config help

> Help output captured from `glab config --help`.

```

  Manage key/value strings.                                                                                             
                                                                                                                        
  Current respected settings:                                                                                           
                                                                                                                        
  - branch_prefix: Prefix used by glab stack when naming generated branches. Defaults to $USER, then glab-stack.
  - browser: If unset, uses the default browser. Override with $BROWSER.
  - check_update: Notify about new glab versions. Defaults to true. Override with $GLAB_CHECK_UPDATE.
  - display_hyperlinks: Enable terminal hyperlinks. Defaults to true. Override with $FORCE_HYPERLINKS.
  - duo_cli_auto_download: Automatically download Duo CLI without prompting.
  - duo_cli_auto_run: Automatically run Duo CLI without prompting.
  - editor: If unset, uses the default editor. Override with $EDITOR.
  - git_protocol: Git protocol. Supported values: ssh, https. Defaults to ssh.
  - glab_pager: Pager command, such as less -R.
  - glamour_style: Markdown renderer style: dark, light, notty, or a custom glamour style.
  - host: If unset, defaults to https://gitlab.com.
  - no_prompt: Disable interactive prompts. Defaults to false.
  - notify_skill_updates: Show installed agent-skill update notices. Defaults to true. Override with $GLAB_NOTIFY_SKILL_UPDATES.
  - orbit_local_auto_download: Automatically download Orbit local CLI without prompting.
  - orbit_local_auto_run: Automatically run Orbit local CLI without prompting.
  - remote_alias: Preferred Git remote name when multiple remotes exist.
  - show_whats_new: Show the one-time post-upgrade glab whatsnew banner. Defaults to true. Override with $GLAB_SHOW_WHATS_NEW.
  - telemetry: Send usage data to the GitLab instance. Defaults to true. Override with $GLAB_SEND_TELEMETRY.
  - token: GitLab access token. Defaults to environment variables.
  - visual: Takes precedence over editor. Override with $VISUAL.
                                                                                                                        
         
  USAGE  
         
    glab config [command] [--flags]  
            
  COMMANDS  
            
    edit [--flags]               Opens the glab configuration file.
    get <key> [--flags]          Prints the value of a given configuration key.
    set <key> <value> [--flags]  Updates configuration with the value of a given key.
         
  FLAGS  
         
    -g --global                  Use global config file.
    -h --help                    Show help for this command.
```

## config edit

```

  Opens the glab configuration file.                                                                                    
  The command uses the following order when choosing the editor to use:                                                 
                                                                                                                        
  1. 'glab_editor' field in the configuration file                                                                      
  2. 'VISUAL' environment variable                                                                                      
  3. 'EDITOR' environment variable                                                                                      
                                                                                                                        
         
  USAGE  
         
    glab config edit [--flags]                                        
            
  EXAMPLES  
            
    Open the configuration file with the default editor               
    - glab config edit                                                
                                                                      
    Open the configuration file with vim                              
    - EDITOR=vim glab config edit                                     
                                                                      
    Set vim to be used for all future 'glab config edit' invocations  
    - glab config set editor vim                                      
    - glab config edit                                                
                                                                      
    Open the local configuration file with the default editor         
    - glab config edit -l                                             
         
  FLAGS  
         
    -h --help   Show help for this command.
    -l --local  Open '.git/glab-cli/config.yml' file instead of the global '~/.config/glab-cli/config.yml' file.
```

## config get

```

  Prints the value of a given configuration key.                                                                        
         
  USAGE  
         
    glab config get <key> [--flags]  
            
  EXAMPLES  
            
    $ glab config get editor         
    > vim                            
                                     
    $ glab config get glamour_style  
    > notty                          
         
  FLAGS  
         
    -g --global  Read from global config file (~/.config/glab-cli/config.yml). (default checks 'Environment variables → Local → Global')
    -h --help    Show help for this command.
    --host       Get per-host setting.
```

## config set

```

  Update the configuration by setting a key to a value.                                                                 
  Use 'glab config set --global' to set a global config.                                                                
  Specifying the '--host' flag also saves in the global configuration file.                                             
                                                                                                                        
         
  USAGE  
         
    glab config set <key> <value> [--flags]          
            
  EXAMPLES  
            
    - glab config set editor vim                     
    - glab config set token xxxxx --host gitlab.com  
    - glab config set check_update false --global    
         
  FLAGS  
         
    -g --global  Write to global '~/.config/glab-cli/config.yml' file rather than the repository's '.git/glab-cli/config.yml' file.
    -h --help    Show help for this command.
    --host       Set per-host setting.
```

