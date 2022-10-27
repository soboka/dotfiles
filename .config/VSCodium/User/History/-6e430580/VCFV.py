from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.command import lazy
from modules.keys import keys, mod
from modules.vars import terminal
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
        )
))

keys.extend([
    Key([mod, "shift"], "Return", lazy.group["scratchgroup"].dropdown_toggle("term")),
])