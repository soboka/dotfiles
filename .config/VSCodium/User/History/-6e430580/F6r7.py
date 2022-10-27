from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.command import lazy
from modules.keys import keys, mod
from modules.vars import terminal, pinfo, tclient, muclient
from modules.groups import groups

groups.append(ScratchPad(
    "scratchgroup",
    [
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
            terminal + " -e " + pinfo, 
            height=0.7, 
            width=0.7, 
            opacity=1,
            x=0.15,
            y=0.15
        ),
        DropDown(
            "torrent", 
            tclient,
            Match= (wm_class="deluge"),
            height=0.7, 
            width=0.7, 
            opacity=1,
            x=0.15,
            y=0.15
        ),
        DropDown(
            "music", 
            muclient, 
            height=0.7, 
            width=0.7, 
            opacity=1,
            x=0.15,
            y=0.15
        ),
    ]
))

keys.extend([
    Key([mod, "shift"], "Return", lazy.group["scratchgroup"].dropdown_toggle("term")),
    Key([mod, "shift"], "i", lazy.group["scratchgroup"].dropdown_toggle("processinfo")),
    Key([mod, "shift"], "o", lazy.group["scratchgroup"].dropdown_toggle("torrent")),
    Key([mod, "shift"], "l", lazy.group["scratchgroup"].dropdown_toggle("music")),
])