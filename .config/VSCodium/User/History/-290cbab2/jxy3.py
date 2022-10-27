from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from modules.vars import wlpaper, home, colors
import os

screens = [
    Screen(
        top=bar.Bar(
            [   tasklist,
                decRight1,
                chord,
                widget.Spacer(length=300),
                mpris,
                widget.Spacer(length=100),
                decLeft1,
                cputext,
                cpu,
                widget.Spacer(length=25, background= colors["bg2"]),
                #decRight1,
                #decLeft1,
                groupbox,
                layoutcurrent,
                #decRight1,
                #decLeft1,
                widget.Spacer(length=25, background= colors["bg2"]),
                memtext,
                memory,
                decRight1,
                widget.Spacer(length=524),
                systray,
                decLeft1,
                volume,
                decRight1,
                decLeft1,
                clock                                           
            ],
            24,  # height in px
            background= colors["bg1"]  # background color
        ),
        wallpaper= home + wlpaper,
        wallpaper_mode='fill', 
    ),
]
