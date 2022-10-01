. ~/.config/fish/aliases.fish
. ~/.config/fish/abbreviations.fish

# cat ~/.cache/wal/sequences &

function fish_right_prompt
#intentionally left blank
end

set fish_greeting
fish_config theme choose Nord

# set -x CLUTTER_BACKEND wayland
# set -x GDK_BACKEND wayland
set -x COMPOSE_DOCKER_CLI_BUILD 1
set -x DOCKER_BUILDKIT 1
set -gx EDITOR 'code --wait'
set -x LANG en_US.UTF-8
set -x LC_ALL en_US.UTF-8
set -x RIPGREP_CONFIG_PATH ~/.config/ripgrep/config
set -x GOPATH ~/go
set -gx GPG_TTY (tty)

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
test -d /home/linuxbrew/.linuxbrew/bin       ; and set PATH /home/linuxbrew/.linuxbrew/bin/ $PATH
test -d /opt/homebrew/bin                    ; and set PATH /opt/homebrew/bin $PATH

set JBOSS_HOME /opt/homebrew/opt/wildfly-as/libexec
# set PATH $JBOSS_HOME/bin $PATH

test -e /usr/local/bin/jump                  ; and status --is-interactive; and source (jump shell fish | psub)
test -e /usr/bin/jump                        ; and status --is-interactive; and source (jump shell fish | psub)
test -e /opt/homebrew/bin/jump               ; and status --is-interactive; and source (jump shell fish | psub)
test -e /usr/sbin/starship                   ; and starship init fish | source
test -e /usr/local/bin/starship              ; and starship init fish | source
test -e /opt/homebrew/bin/starship           ; and starship init fish | source
test -e /usr/bin/direnv                      ; and direnv hook fish | source
test -e /usr/local/bin/navi                  ; and navi widget fish | source
test -e /opt/shell-color-scripts/colorscripts ; and colorscript random

# Emulates vim's cursor shape behavior
# Set the normal and visual mode cursors to a block
set fish_cursor_default block blink
# Set the insert mode cursor to a line
set fish_cursor_insert line blink
# Set the replace mode cursor to an underscore
set fish_cursor_replace_one underscore blink
# The following variable can be used to configure cursor shape in
# visual mode, but due to fish_cursor_default, is redundant here
set fish_cursor_visual block blink

