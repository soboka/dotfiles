#!/bin/sh

if setxkbmap -print|grep -q us; then
  setxkbmap -layout hu -variant "102_qwerty_dot_dead"
  notify-send "kLayout: HU" -t 1000
else
  setxkbmap -layout us -variant "altgr-intl"
  notify-send "kLayout: EN" -t 1000
fi
