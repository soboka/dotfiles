#!/bin/bash

volume="$(pamixer --get-volume)"

#Check volume level
if [ "$volume" = "0" ]; then
    notify-send "Volume MUTED"
else
    notify-send $volume
fi