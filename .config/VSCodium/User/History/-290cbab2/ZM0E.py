from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background='#2B3339'),
                widget.Prompt(),
                tasklist,
                chord,
                widget.Spacer(length=300),
                groupbox,   
                layoutcurrent,
                widget.Spacer(length=720),
                systray,
                notifier,
                volume,
                clock,
                widget.Sep(padding=3, linewidth=0, background='#2B3339'),                                             
            ],
            24,  # height in px
            background='#2B3339'  # background color
        ), ),
]
