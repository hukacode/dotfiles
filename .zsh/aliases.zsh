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
