#!/bin/sh

# set wallpaper
#feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png

picom --experimental-backends & disown 

# start polkit agent from GNOME
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown

# start screenshot application
flameshot & disown

# Networkmanager applet
nm-applet & disown