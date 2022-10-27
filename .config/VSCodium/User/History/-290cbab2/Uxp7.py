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
                mpris,
                groupbox,   
                layoutcurrent,
                widget.Spacer(length=720),
                systray,
                volume,
                clock,
                widget.Sep(padding=3, linewidth=0, background='#2B3339'),                                             
            ],
            24,  # height in px
            background='#2B3339'  # background color
        ),
        wallpaper="/home/qtiletester/.config/qtile/Wallpaper/No_mans_sky_wallp_01.png",
        wallpaper_mode='fill', 
    ),
]
