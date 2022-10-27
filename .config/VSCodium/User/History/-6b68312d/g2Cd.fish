### EXPORT ###
set TERM "xterm-256color" 
set fish_greeting 
set EDITOR vim
set VISUAL vim

### SET MANPAGER ###

# "vim" as manpager
set -x MANPAGER '/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

### ALIAS ###

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'

# Colorize grep output
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# get error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# Flatpak
alias flup="flatpak update"
alias fl="flatpak"
alias flis="flatpak install"

# Clear
alias c='clear'

# confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Replace LS with EXA
alias ls='exa --icons'
alias lS='exa --oneline --icons'
alias la='exa -a --icons'
alias lA='exa -a --oneline --icons'
alias ll='exa --long --header --icons'
alias lt='exa --tree --icons'
alias llt='exa --long --header --tree --icons'
alias llta='exa --long --header --tree -a --icons'

# adding flags
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-opus="youtube-dl --extract-audio --audio-format opus "
alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv-best="youtube-dl -f bestvideo+bestaudio "
alias ytap-m4a="youtube-dl -i --format bestaudio --embed-thumbnail --extract-audio --audio-format m4a --yes-playlist "
