. ~/.config/fish/aliases.fish
. ~/.config/fish/abbreviations.fish

set fish_greeting

# set -x CLUTTER_BACKEND wayland
# set -x GDK_BACKEND wayland
set -x COMPOSE_DOCKER_CLI_BUILD 1
set -x DOCKER_BUILDKIT 1
set -gx EDITOR 'code --wait'
set -gx FZF_DEFAULT_OPTS '--height=50% --min-height=15 --reverse'
set -x FZF_CTRL_T_COMMAND $FZF_DEFAULT_COMMAND
set -x FZF_DEFAULT_COMMAND 'git ls-tree -r --name-only HEAD 2> /dev/null; or fd --type f --hidden --follow --exclude .git 2> /dev/null'
set -x FZF_LEGACY_KEYBINDINGS 0
set -x FZF_COMPLETE 1
set -x FZF_REVERSE_ISEARCH_OPTS '--preview-window=up:10 --preview="echo {}" --height 100%'
set -x LANG en_US.UTF-8
set -x LC_ALL en_US.UTF-8
set -x RIPGREP_CONFIG_PATH ~/.config/ripgrep/config
set -x GOPATH ~/go

# Paths
test -d /usr/local/share/npm/bin             ; and set PATH /usr/local/share/npm/bin $PATH
test -d /usr/local/heroku/bin                ; and set PATH /usr/local/heroku/bin $PATH
test -d /usr/local/go/bin                    ; and set PATH /usr/local/go/bin $PATH
test -d /usr/local/sbin                      ; and set PATH /usr/local/sbin $PATH
test -d /usr/local/bin                       ; and set PATH /usr/local/bin $PATH
test -d ~/_bin                               ; and set PATH ~/_bin $PATH
# test -d ~/.cabal/bin                         ; and set PATH ~/.cabal/bin $PATH
# test -d ~/.cargo/bin                         ; and set PATH ~/.cargo/bin $PATH
test -d ~/.local/bin                         ; and set PATH ~/.local/bin $PATH
test -d $GOPATH/bin                          ; and set PATH $GOPATH/bin $PATH
test -d ~/script                             ; and set PATH ~/script $PATH

status --is-interactive; and source (jump shell fish | psub)
# cat ~/.cache/wal/sequences &

starship init fish | source # must be last line
