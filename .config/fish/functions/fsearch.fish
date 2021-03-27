function fsearch -d "Fuzzy search w/grep"
    rg --line-buffered --color=never -r "" * | fzf
end
