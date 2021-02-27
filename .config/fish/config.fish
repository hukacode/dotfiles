. ~/.config/fish/aliases_linux.fish
. ~/.config/fish/abbreviations.fish
set PATH $PATH ~/script/
set PATH $PATH ~/.local/bin/
set PATH $PATH ~/go/bin
set fish_greeting
set -gx EDITOR 'code --wait'
starship init fish | source # last line
