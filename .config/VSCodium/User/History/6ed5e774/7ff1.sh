#!/bin/bash

mute="$(pamixer --get-mute)"
volume="$(pamixer --get-volume)"

#Check volume level

if [ "$mute" = "false"]; then
    notify-send "Volume MUTED"
else
    notify-send "Volume " + $volume
fi

pamixer -t