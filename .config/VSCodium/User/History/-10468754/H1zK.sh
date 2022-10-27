#!/bin/bash

volume="$(pamixer --get-volume)"

#Check volume level
if [ "$volume" = "0" ]; then
    dunstify -h string:x-dunst-stack-tag:volume "Volume: MUTED"
else
    dunstify -h string:x-dunst-stack-tag:volume "Volume: $volume" 
fi