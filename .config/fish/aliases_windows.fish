function timestamp
    python -c 'import time; print(int(time.time()))'
end

alias df 'df -m'
alias j 'jobs'
alias l 'ls'
alias ll 'ls -la'
alias ls 'ls -FG'
alias su 'su -m'

alias g git
alias c clear
alias notes 'rg "TODO|HACK|FIXME|OPTIMIZE"'

alias cd.. 'cd ..'
alias .. 'cd ..'
alias ... 'cd ../..'
alias .... 'cd ../../..'
alias ..... 'cd ../../../..'

alias md 'mkdir -p'
function take
    set -l dir $argv[1]
    mkdir -p $dir; and cd $dir
end
alias cx 'chmod +x'
alias 'c-x' 'chmod -x'

alias h=heroku

function wtf -d "Print which and --version output for the given command"
    for arg in $argv
        echo $arg: (which $arg)
        echo $arg: (sh -c "$arg --version")
    end
end

## cd
alias hrms='cd /mnt/r/source/hrms/'
alias coffee-shop='cd /mnt/r/source/coffee-shop/'
alias blog='cd /mnt/r/source/hugo-blog/'
alias hk='cd /mnt/r/source/hktool/'
alias titama='cd /mnt/r/source/titama/'