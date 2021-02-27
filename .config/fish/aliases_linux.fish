## cd
alias hrms='cd /run/media/huka/workspace/huka-project/hrms/'
alias coffee-shop='cd /run/media/huka/workspace/huka-project/coffee-shop/'
alias blog='cd /run/media/huka/workspace/huka-gohugo/hugo-blog/'
alias titama='cd /run/media/huka/workspace/huka-project/titama/'

function timestamp
    python -c 'import time; print(int(time.time()))'
end

function setcountdown    
    sleep $argv[1] && notify-send $argv[2]
end

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
alias j 'jobs'
alias su 'su -m'

# app
alias h=heroku
alias g git
alias cl clear
alias notes 'rg "TODO|HACK|FIXME|OPTIMIZE"'

## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'

# get error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# navigation
alias ..='cd ..' 
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# make dir
alias md 'mkdir -p'

function take
    set -l dir $argv[1]
    mkdir -p $dir; and cd $dir
end

# chmod
alias cx 'chmod +x'
alias 'c-x' 'chmod -x'

# pacman and yay
alias pacsyu='sudo pacman -Syyu'                # update only standard pkgs
alias yaysua="yay -Sua --noconfirm"             # update only AUR pkgs
alias yaysyu="yay -Syu --noconfirm"             # update standard pkgs and AUR pkgs
alias unlock="sudo rm /var/lib/pacman/db.lck"   # remove pacman lock
alias cleanup='sudo pacman -Rns (pacman -Qtdq)' # remove orphaned packages
alias install='sudo pacman -S'                  
alias uninstall='sudo pacman -Rns'              

# get fastest mirrors
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

# Changing "ls" to "exa"
alias ls='exa -al --color=always --group-directories-first' # my preferred listing
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | egrep "^\."'

# alias l 'ls'
# alias ll 'ls -la'
# alias ls 'ls -FG'

# Colorize grep output (good for log files)
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

function wtf -d "Print which and --version output for the given command"
    for arg in $argv
        echo $arg: (which $arg)
        echo $arg: (sh -c "$arg --version")
    end
end

