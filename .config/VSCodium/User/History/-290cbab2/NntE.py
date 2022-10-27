from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from modules.vars import wlpaper
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background='#2B3339'),
                widget.Prompt(),
                tasklist,
                chord,
                widget.Spacer(length=300),
                mpris,
                widget.Spacer(length=100),
                decLeft1,
                groupbox,
                layoutcurrent,
                decRight1,
                widget.Spacer(length=720),
                systray,
                volume,
                clock,
                widget.Sep(padding=3, linewidth=0, background='#2B3339'),                                             
            ],
            24,  # height in px
            background='#2B3339'  # background color
        ),
        wallpaper= wlpaper,
        wallpaper_mode='fill', 
    ),
]
