from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.command import lazy
from modules.keys import keys, mod
from modules.vars import terminal


groups = []

group_names =   ["1", "2", "3", "4", "5", "6",]

group_labels =  ["", "", "", "ﭮ", "", "",]

group_layouts = [
    #1
    "monadtall",
    #2
    "monadtall", 
    #3
    "monadtall", 
    #4
    "monadtall",
    #5
    "monadtall",
    #6
    "monadtall", 
]

group_matches = [
    #1
    [
        Match(wm_class="vivaldi-stable"),
        Match(wm_class="firefox")
    ],
    #2
    [
        Match(wm_class='vscodium'),
        Match(wm_class='thunar'),
    ],
    #3
    [
        Match(wm_class='lutris'),
    ],
    #4
    [
        Match(wm_class='discord'),
    ],
    #5
    [
        Match(wm_class='thunderbird'),
    ],
    #6
    [
#        Match(wm_class='deluge'),
    ]
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches=group_matches[i]
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "l", lazy.screen.next_group(skip_empty=True),
            desc="Switch to next group"),

        Key([mod], "k", lazy.screen.prev_group(skip_empty=True),
            desc="Switch to previous group"),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])