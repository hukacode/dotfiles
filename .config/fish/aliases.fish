# create and jump to dir
function take
    set -l dir $argv[1]
    mkdir -p $dir; and cd $dir
end

function wtf -d "Print which and --version output for the given command"
    for arg in $argv
        echo $arg: (which $arg)
        echo $arg: (sh -c "$arg --version")
    end
end

function timestamp ; python -c 'import time; print(int(time.time()))' ; end
function setcountdown ; sleep $argv[1] && notify-send $argv[2] ; end
function digga    ; command dig +nocmd $argv[1] any +multiline +noall +answer; end
function httpdump ; sudo tcpdump -i en1 -n -s 0 -w - | grep -a -o -E "Host\: .*|GET \/.*" ; end
function ip       ; curl -s http://checkip.dyndns.com/ | sed 's/[^0-9\.]//g' ; end
function localip  ; ipconfig getifaddr en0 ; end
function lookbusy ; cat /dev/urandom | hexdump -C | grep --color "ca fe" ; end

# bat
if test -x "/home/linuxbrew/.linuxbrew/bin/bat"; or test -x "/usr/bin/bat"; or test -x "/opt/homebrew/bin/bat"
  alias cat='bat -pp --theme="Nord"'
end

if test -x "/usr/bin/nvim"; or test -x "/opt/homebrew/bin/nvim"; or test -x "/usr/local/bin/nvim"  
  alias vim='nvim'
end

# Changing "ls" to "exa"
if test -x "/home/linuxbrew/.linuxbrew/bin/exa"; or test -x "/usr/bin/exa"; or test -x "/opt/homebrew/bin/exa"
  alias ls='exa -al --color=always --group-directories-first --icons' # my preferred listing
  alias la='exa -a --color=always --group-directories-first --icons'  # all files and dirs
  alias ll='exa -l --color=always --group-directories-first --icons'  # long format
  alias lt='exa -aT --color=always --group-directories-first --icons' # tree listing
  alias l.='exa -a | egrep "^\."'
end
alias l 'ls'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
# alias j 'jobs'
alias su 'su -m'
alias vimdiff='nvim -d'

# app

# utilities
alias cl clear
alias cls clear
alias notes 'rg "TODO|HACK|FIXME|OPTIMIZE"'
alias md 'mkdir -p'
alias cx 'chmod +x'
alias 'c-x' 'chmod -x'

## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'

# get error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# pacman and yay
alias pacsyu='sudo pacman -Syyu'                # update only standard pkgs
alias yaysua="yay -Sua --noconfirm"             # update only AUR pkgs
alias yaysyu="yay -Syu --noconfirm"             # update standard pkgs and AUR pkgs
alias unlock="sudo rm /var/lib/pacman/db.lck"   # remove pacman lock
alias cleanup='sudo pacman -Rns (pacman -Qtdq)' # remove orphaned packages
alias pin='sudo pacman -S'
alias pun='sudo pacman -Rns'
alias yin='yay -S'
alias yun='yay -Rns'

# get fastest mirrors
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Systemd
alias sstatus "sudo systemctl status"
alias sstart "sudo systemctl start"
alias srestart "sudo systemctl restart"
alias sstop "sudo systemctl stop"
alias senable "sudo systemctl enable"
alias sdisable "sudo systemctl disable"

# Archives
alias ltar "tar -ztvf"
alias untar "tar -zxvf"
alias ctar "tar -cvzf"
