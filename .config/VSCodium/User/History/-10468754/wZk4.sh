#!/bin/bash

volume="$(pamixer --get-volume)"
killall dunst

#Check volume level
if [ "$volume" = "0" ]; then
    notify-send "Volume MUTED"
else
    notify-send $volume
fi