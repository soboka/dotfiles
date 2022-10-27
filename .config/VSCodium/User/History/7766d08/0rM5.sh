#!/bin/bash

# https://github.com/Z-8Bit/Qtile
# You can call this script like this:
# $ ./volume.sh up
# $ ./volume.sh down

DIR="$HOME/.config/dunst"


function send_notification {
  mute="$(pamixer --get-mute)"
  volume=$(pamixer --get-volume)
  bar=$(seq -s "━" 0 $(($volume / 5)) | sed 's/[0-9]//g')
  if [ '$(pamixer --get-mute)' = "true" ]; then
    icon_name="$DIR/icons/volume-muted.svg"
    bar=""
    dunstify " Volume " "$volume" -i $icon_name -r 5555 -u normal
  else
    if [  "$volume" -lt "10" ]; then
      icon_name="$DIR/icons/volume-low.svg"
    #dunstify " Volume " "$volume" -i $icon_name -r 5555 -u normal
    else
      if [ "$volume" -lt "30" ]; then
        icon_name="$DIR/icons/volume-low.svg"
      else
        if [ "$volume" -lt "70" ]; then
          icon_name="$DIR/icons/volume-medium.svg"
        else
          icon_name="$DIR/icons/volume-high.svg"
        fi
      fi
    fi
  fi
  # Send the notification
  dunstify -u normal -r "9993" -h int:value:"$volume" -i $icon_name "Volume: ${volume}%" -t 920
  #dunstify "Volume: $volume" "$bar" -i $icon_name -r 5555 -u normal
}

case $1 in
  up)
    pamixer -u
    #pamixer -i 5 --allow-boost
    pamixer -i 5
    send_notification
    ;;
  down)
    pamixer -u
    #pamixer -d 5 --allow-boost
    pamixer -d 5
    send_notification
    ;;
  mute)
    # Toggle mute
    pamixer -t
    send_notification
    fi
    ;;
esac