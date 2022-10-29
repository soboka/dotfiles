#!/bin/sh

sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf install alacritty btop deluge-gtk deadbeef deadbeef-plugins deadbeef-mpris2-plugin discord dunst ffmpegthumbnailer fish flameshot krita mediainfo mpv neofetch neovim pcmanfm picom rofi
