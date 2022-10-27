from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from modules.vars import wlpaper, home, colors
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background='#2B3339'),
                widget.Prompt(),
                decLeft1,
                tasklist,
                decRight1,
                chord,
                widget.Spacer(length=300),
                mpris,
                widget.Spacer(length=100),
                decLeft1,
                groupbox,
                layoutcurrent,
                decRight1,
                decLeft1,
                memtext,
                memory,
                decRight1,
                widget.Spacer(length=430),
                systray,
                decLeft1,
                volume,
                decRight1,
                decLeft1,
                clock,
                decRight1,
                widget.Sep(padding=3, linewidth=0, background='#2B3339'),                                             
            ],
            24,  # height in px
            background= colors["bg1"]  # background color
        ),
        wallpaper= home + wlpaper,
        wallpaper_mode='fill', 
    ),
]
