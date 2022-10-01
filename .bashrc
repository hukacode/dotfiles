# System default
# --------------------------------------------------------------------

[ -z ${PLATFORM+x} ] && export PLATFORM=$(uname -s)
[ -f /etc/bashrc ] && . /etc/bashrc

[ -f "${BASH_SOURCE[0]}" ] && BASE=$(dirname "$(readlink "${BASH_SOURCE[0]}")") ||
  BASE=$(dirname "$(readlink ~/.bashrc)")

# Options
# --------------------------------------------------------------------

### Append to the history file
shopt -s histappend

### Check the window size after each command ($LINES, $COLUMNS)
shopt -s checkwinsize

### Better-looking less for binary files
[ -x /usr/bin/lesspipe    ] && eval "$(SHELL=/bin/sh lesspipe)"

### Bash completion
[ -f /etc/bash_completion ] && . /etc/bash_completion


# Environment variables
# --------------------------------------------------------------------

### man bash
export HISTCONTROL=ignoreboth:erasedups
export HISTSIZE=
export HISTFILESIZE=
export HISTTIMEFORMAT="%Y/%m/%d %H:%M:%S:   "
[ -z "$TMPDIR" ] && TMPDIR=/tmp

### Global
export GOPATH=~/gosrc
export EDITOR=vim
mkdir -p $GOPATH
export PATH=~/bin:$PATH
if [ "$PLATFORM" = Linux ]; then
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.:/usr/local/lib
fi
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

### OS X
export COPYFILE_DISABLE=true
export BASH_SILENCE_DEPRECATION_WARNING=1

# Aliases
# --------------------------------------------------------------------

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias cd.='cd ..'
alias cd..='cd ..'
alias l='ls -alF'
alias ll='ls -l'
alias vi=$EDITOR
alias vim=$EDITOR
alias which='type -p'
alias k5='kill -9 %%'

alias d='docker'
alias dl='docker ps -lq' # display id of latest created container
alias dim='docker images'
alias dpsa='dps -a'
alias drma='docker rm (docker ps -aq)' # delete all stopped containers
alias drml='docker rm (docker ps -lq)' # delete last container
alias dsa='docker stop (docker ps -aq)' # stop all containers
alias dsl='docker stop (docker ps -lq)' # stop last container
alias drmdi='docker rmi (docker images -qf dangling=true)' # delete dangling images
alias digrep='docker-images' # grep through images
alias dgrep='docker-grep' # grep through containers
alias drmg='docker rm (docker-grep'
alias dpid="docker inspect --format \'{{.State.Pid}}\' (docker ps -lq)"
alias dcl='docker rm (docker ps -aq); docker rmi (docker images -qf dangling=true)' # clean
alias de='docker exec'

alias dc='docker-compose'
alias dcu='docker-compose up -d'
alias dcs='docker-compose stop'
alias dcd='docker-compose down'

# Prompt
#----------------------------------------------------------------------

RED="\[\033[0;31m\]"
BROWN="\[\033[0;33m\]"
GREY="\[\033[0;97m\]"
GREEN="\[\033[0;32m\]"
BLUE="\[\033[0;34m\]"
PS_CLEAR="\[\033[0m\]"
SCREEN_ESC="\[\033k\033\134\]"

COLOR1="${BLUE}"
COLOR2="${BLUE}"
P="\$"

prompt_simple() {
    unset PROMPT_COMMAND
    PS1="\W\$(parse_git_branch) → "
    PS2="> "
}

prompt_compact() {
    unset PROMPT_COMMAND
    PS1="${COLOR1}${P}${PS_CLEAR} "
    PS2="> "
}

prompt_color() {
    local remote=""
    if grep docker /proc/1/cgroup -qa >/dev/null 2>&1; then
        remote="🐶 "
    fi

    PS1="${GREEN}${remote}\W\$(parse_git_branch) → ${GREY}"
    PS2="\[[33;1m\]continue \[[0m[1m\]> "
}

parse_git_branch() {
    [ -d .git ] || return 1
    git symbolic-ref HEAD 2> /dev/null | sed 's#\(.*\)\/\([^\/]*\)$# \2#'
}
