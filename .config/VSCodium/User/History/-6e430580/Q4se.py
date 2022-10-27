from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.command import lazy
from modules.keys import keys, mod
from modules.vars import terminal

groups.append(ScratchPad('Scratchpad',[
    DropDown(
        "term", 
        terminal, 
        height=0.6, 
        width=0.6, 
        opacity=1,
        x=0.2,
        y=0.2
    ),
    DropDown(
        "processinfo", 
        terminal + "-e htop", 
        height=0.7, 
        width=0.7, 
        opacity=1,
        x=0.15,
        y=0.15
    ),
    DropDown(
        "torrent", 
        "deluge", 
        height=0.7, 
        width=0.7, 
        opacity=1,
        x=0.15,
        y=0.15
    ),
    DropDown(
        "music", 
        "audacious", 
        height=0.7, 
        width=0.7, 
        opacity=1,
        x=0.15,
        y=0.15
    ),
]))

keys.extend([
    Key([mod, 'shift'], "Return", lazy.group['Scratchpad'].dropdown_toggle('term')),
    Key([mod, 'shift'], "i", lazy.group['Scratchpad'].dropdown_toggle('processinfo')),
    Key([mod, 'shift'], "o", lazy.group['Scratchpad'].dropdown_toggle('torrent')),
    Key([mod, 'shift'], "l", lazy.group['Scratchpad'].dropdown_toggle('music')),
])