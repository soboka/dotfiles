#!/bin/bash

volume="$(pamixer --get-volume)"

#Check volume level
if [ "$volume" = "0" ]; then
    dunstify "Volume MUTED"
else
    dunstify $volume
fi