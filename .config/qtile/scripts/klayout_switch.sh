#!/bin/sh

if setxkbmap -print|grep -q us; then
  setxkbmap -layout hu -variant "102_qwerty_dot_dead"
else
  setxkbmap -layout us -variant "altgr-intl"
fi
