abbr --add g            "git"
abbr --add ga           "git add"
abbr --add gaa          "git add --all"
abbr --add gap          "git apply"
abbr --add gapa         "git add --patch"
abbr --add gb           "git branch -vv"
abbr --add gba          "git branch -a -v"
abbr --add gban         "git branch -a -v --no-merged"
abbr --add gbam         "git branch -a -v --merged"
abbr --add gbD          "git branch -D"
abbr --add gbd          "git branch -d"
abbr --add gbl          "git blame -b -w"
abbr --add gbs          "git bisect"
abbr --add gbsb         "git bisect bad"
abbr --add gbsg         "git bisect good"
abbr --add gbsr         "git bisect reset"
abbr --add gbss         "git bisect start"
abbr --add gc           "git commit -v"
abbr --add gc!          "git commit -v --amend"
abbr --add gca          "git commit -v -a"
abbr --add gca!         "git commit -v -a --amend"
abbr --add gcam         "git commit -a -m"
abbr --add gcan!        "git commit -v -a --no-edit --amend"
abbr --add gcav         "git commit -a -v --no-verify"
abbr --add gcav!        "git commit -a -v --no-verify --amend"
abbr --add gcb          "git checkout -b"
abbr --add gcl          "git clone"
abbr --add gclean       "git clean -di"
abbr --add gclean!      "git clean -dfx"
abbr --add gclean!!     "git reset --hard; and git clean -dfx"
abbr --add gcm          "git commit -m"
abbr --add gcn!         "git commit -v --no-edit --amend"
abbr --add gco          "git checkout"
abbr --add gcod         "git checkout develop"
abbr --add gcom         "git checkout main"
abbr --add gcount       "git shortlog --summary --numbered --email"
abbr --add gcountall    "git shortlog --summary --numbered --email --all"
abbr --add gcp          "git cherry-pick"
abbr --add gcpa         "git cherry-pick --abort"
abbr --add gcpc         "git cherry-pick --continue"
abbr --add gcv          "git commit -v --no-verify"
abbr --add gd           "git diff"
abbr --add gdd          "git diff develop"
abbr --add gddo         "git diff origin/develop"
abbr --add gdh          "git diff HEAD"
abbr --add gdca         "git diff --cached"
abbr --add gds          "git diff --stat"
abbr --add gdsc         "git diff --stat --cached"
abbr --add gdw          "git diff --word-diff"
abbr --add gdwc         "git diff --word-diff --cached"
abbr --add gf           "git fetch"
abbr --add gfa          "git fetch --all --prune"
abbr --add gfm          "git fetch origin main --prune; and git merge FETCH_HEAD"
abbr --add gfo          "git fetch origin"
abbr --add gignore      "git update-index --assume-unchanged"
abbr --add glg          "git log --graph --abbrev-commit --decorate --format=format:'%C(blue)%h%C(reset) - %C(green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(yellow)%d%C(reset)' --all"
abbr --add glgg         "git log --graph --max-count=10"
abbr --add glgga        "git log --graph --decorate --all"
abbr --add glo          "git log --oneline --decorate --color"
abbr --add glod         "git log --oneline --decorate --color develop.."
abbr --add glog         "git log --oneline --decorate --color --graph"
abbr --add glom         "git log --oneline --decorate --color main.."
abbr --add gloo         "git log --pretty=format:'%C(yellow)%h %Cred%ad %Cblue%an%Cgreen%d %Creset%s' --date=short"
abbr --add gls          "git log --stat --max-count=10"
abbr --add gm           "git merge"
abbr --add gmd          "git merge develop"
abbr --add gmod         "git merge origin/develop"
abbr --add gmt          "git mergetool --no-prompt"
abbr --add gp           "git pull"
abbr --add gpl          "git pull origin"
abbr --add gpr          "git pull --rebase"
abbr --add gps          "git push"
abbr --add gps!         "git push --force-with-lease"
abbr --add gpso         "git push origin"
abbr --add gpso!        "git push --force-with-lease origin"
abbr --add gpsp!        "git push --force-with-lease"
abbr --add gpsu         "git push --set-upstream"
abbr --add gpsv         "git push --no-verify"
abbr --add gpsv!        "git push --no-verify --force-with-lease"
abbr --add gr           "git remote -vv"
abbr --add gra          "git remote add"
abbr --add grb          "git rebase"
abbr --add grba         "git rebase --abort"
abbr --add grbc         "git rebase --continue"
abbr --add grbd         "git rebase develop"
abbr --add grbod         "git rebase origin/develop"
abbr --add grbdi        "git rebase main --interactive"
abbr --add grbdia       "git rebase main --interactive --autosquash"
abbr --add grbi         "git rebase --interactive"
abbr --add grbm         "git rebase main"
abbr --add grbmi        "git rebase main --interactive"
abbr --add grbmia       "git rebase main --interactive --autosquash"
abbr --add grbs         "git rebase --skip"
abbr --add grev         "git revert"
abbr --add grh          "git reset"
abbr --add grhh         "git reset --hard"
abbr --add grm          "git rm"
abbr --add grmc         "git rm --cached"
abbr --add grmv         "git remote rename"
abbr --add grrm         "git remote remove"
abbr --add grs          "git restore"
abbr --add grset        "git remote set-url"
abbr --add grss         "git restore --source"
abbr --add grup         "git remote update"
abbr --add grv          "git remote -v"
abbr --add gscam        "git commit -S -a -m"
abbr --add gsd          "git svn dcommit"
abbr --add gsh          "git show"
abbr --add gsr          "git svn rebase"
abbr --add gss          "git status -s"
abbr --add gst          "git status"
abbr --add gsta         "git stash"
abbr --add gstu         "git stash --include-untracked"
abbr --add gstd         "git stash drop"
abbr --add gstl         "git stash list"
abbr --add gstp         "git stash pop"
abbr --add gsts         "git stash show --text"
abbr --add gsu          "git submodule update"
abbr --add gsur         "git submodule update --recursive"
abbr --add gsuri        "git submodule update --recursive --init"
abbr --add gsw          "git switch"
abbr --add gswc         "git switch --create"
abbr --add gswd         "git switch develop"
abbr --add gts          "git tag -s"
abbr --add gtv          "git tag | sort -V"
abbr --add gunignore    "git update-index --no-assume-unchanged"
abbr --add gup          "git pull --rebase"
abbr --add gwch         "git whatchanged -p --abbrev-commit --pretty=medium"

abbr --add gcommend     "git commit --amend --no-edit"
abbr --add contributors "git shortlog --summary --numbered"
abbr --add gln          "git log --graph -n 20 --pretty=format:'%C(yellow)%h%C(cyan)%d%Creset %s %C(green)- %an, %cr%Creset' --name-status"
abbr --add gls          "git log --stat --abbrev-commit -n 1" # display previous log
abbr --add gwhatadded   "git log --diff-filter=A"
abbr --add gwhatis      "git show -s --pretty='tformat:%h (%s, %ad)' --date=short"
abbr --add gwhoami      "git config user.email"
abbr --add gwip         "git for-each-ref --sort='authordate:iso8601' --format='%(color:green)%(authordate:relative)%09%(color:reset)%(refname:short)' refs/heads"

# git flow abbreviations
abbr --add gfb          "git flow bugfix"
abbr --add gff          "git flow feature"
abbr --add gfr          "git flow release"
abbr --add gfh          "git flow hotfix"
abbr --add gfs          "git flow support"
abbr --add gfbs         "git flow bugfix start"
abbr --add gffs         "git flow feature start"
abbr --add gfrs         "git flow release start"
abbr --add gfhs         "git flow hotfix start"
abbr --add gfss         "git flow support start"
abbr --add gfbt         "git flow bugfix track"
abbr --add gfft         "git flow feature track"
abbr --add gfrt         "git flow release track"
abbr --add gfht         "git flow hotfix track"
abbr --add gfst         "git flow support track"
abbr --add gfp          "git flow publish"

abbr --add vup          "vagrant up"
abbr --add vsh          "vagrant ssh"

# docker
abbr --add d            "docker"
abbr --add dl           "docker ps -lq" # display id of latest created container
abbr --add dim          "docker images"
abbr --add dpsa         "dps -a"
abbr --add drma         "docker rm (docker ps -aq)" # delete all stopped containers
abbr --add drml         "docker rm (docker ps -lq)" # delete last container
abbr --add dsa          "docker stop (docker ps -aq)" # stop all containers
abbr --add dsl          "docker stop (docker ps -lq)" # stop last container
abbr --add drmdi        "docker rmi (docker images -qf dangling=true)" # delete dangling images
abbr --add digrep       "docker-images" # grep through images
abbr --add dgrep        "docker-grep" # grep through containers
abbr --add drmg         "docker rm (docker-grep"
abbr --add dpid         "docker inspect --format \'{{.State.Pid}}\' (docker ps -lq)"
abbr --add dcl          "docker rm (docker ps -aq); docker rmi (docker images -qf dangling=true)" # clean
abbr --add de           "docker exec"

abbr --add dc           "docker-compose"
abbr --add dcu          "docker-compose up -d"
abbr --add dcs          "docker-compose stop"
abbr --add dcd          "docker-compose down"

abbr --add dm           "docker-machine"

# kubernetes
abbr --add k            "kubectl"
abbr --add kg           "kubectl get"
abbr --add kd           "kubectl describe"
abbr --add ke           "kubectl exec"
abbr --add kc           "kubectl config"
abbr --add kcu          "kubectl config use-context"
abbr --add kcc          "kubectl config use-context"
abbr --add kcf          "kubectl create -f"
abbr --add kaf          "kubectl apply -f"
abbr --add kp           "kubectl port-forward"
abbr --add kls          "kubectl logs -f --since 1s"
abbr --add ks           "kubectl_context_switch_peco"
abbr --add ka           "kubectl_attach_pod"
abbr --add kn           "kubectl -n kube-system"

# app
abbr --add y            "yarn"
abbr --add ld           "lazydocker"
abbr --add q            "quarkus"
abbr --add qd           "quarkus dev"
abbr --add qe           "quarkus ext"
abbr --add c            "code"
abbr --add wt           "curl wttr.in/DaNang"
abbr --add rp           "rsync -rltp --partial --info=progress2"


# fish
abbr --add efc          "vim ~/.config/fish/config.fish"
abbr --add eff          "vim ~/.config/fish/functions"
abbr --add fc           "source ~/.config/fish/config.fish"
abbr --add sf           "source ~/.config/fish/config.fish"

# system
abbr --add chmox        "chmod +x"
abbr --add s            "sudo"
abbr --add se           "sudo -E"
abbr --add sudoe        "sudo -E"

# youtube-dl
abbr --add yta-aac      "youtube-dl --extract-audio --audio-format aac "
abbr --add yta-best     "youtube-dl --extract-audio --audio-format best "
abbr --add yta-flac     "youtube-dl --extract-audio --audio-format flac "
abbr --add yta-m4a      "youtube-dl --extract-audio --audio-format m4a "
abbr --add yta-mp3      "youtube-dl --extract-audio --audio-format mp3 "
abbr --add yta-opus     "youtube-dl --extract-audio --audio-format opus "
abbr --add yta-vorbis   "youtube-dl --extract-audio --audio-format vorbis "
abbr --add yta-wav      "youtube-dl --extract-audio --audio-format wav "
abbr --add ytv-best     "youtube-dl -f bestvideo+bestaudio "
