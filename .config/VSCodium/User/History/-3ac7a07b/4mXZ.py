from libqtile.lazy import lazy
from libqtile.config import Key
import os
from modules.vars import *

keys = [
    # Switch window focus
    Key([mod], "Left", lazy.layout.left(), 
        desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), 
        desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), 
        desc="Move focus to down"),
    Key([mod], "Up", lazy.layout.up(), 
        desc="Move focus to up"),
    
    # Move window position
    Key([mod, ctrl], "Left", lazy.layout.shuffle_left(),
        desc="Move the window to the left"),
    Key([mod, ctrl], "Right", lazy.layout.shuffle_right(),
        desc="Move the window to the right"),
    Key([mod, ctrl], "Down", lazy.layout.shuffle_down(),
        desc="Move the window down"),
    Key([mod, ctrl], "Up", lazy.layout.shuffle_up(), 
        desc="Move the window up"),

    # Grow/shrink window.
    Key([mod, alt], "Up", lazy.layout.grow(), 
        desc="Grow the focused window"),
    Key([mod, alt], "Down", lazy.layout.shrink(), 
        desc="Shrink the focused window"),

    # Toggle between different layouts or flip
    Key([mod], "Tab", lazy.next_layout(), 
        desc="Toggle between layouts"),
    Key([mod, shft], "f", lazy.window.toggle_floating(), 
        desc="Toggle floating mode"),
    Key([mod, shft], "t", lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen mode"),
    Key([mod], "g", lazy.layout.flip(), 
        desc="Flip layout"),

    # Qtile restart, logout, kill window
    Key([mod, alt], "r", lazy.restart(), 
        desc="Restart Qtile"),
    Key([ctrl, alt], "Delete", lazy.spawn(home + pwmenu), 
        desc="Shutdown Qtile"),
    Key([mod], "q", lazy.window.kill(), 
        desc="Kill focused window"),

    # Multimedia Keys
    Key([], "XF86AudioRaiseVolume",lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volup.sh")), 
        desc="Increase Volume"),
    Key([], "XF86AudioLowerVolume",lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/voldown.sh")), 
        desc="Decrease Volume"),
    Key([], "XF86AudioMute",lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volmute.sh")), 
        desc="Mute Volume"),
    Key([], "XF86AudioPlay",lazy.spawn("playerctl play-pause"), 
        desc="Start/Pause media"),
    Key([mod], "XF86AudioPlay",lazy.spawn("playerctl stop"), 
        desc="Stop media"),
    Key([], "XF86AudioNext",lazy.spawn("playerctl next"), 
        desc="Next media"),
    Key([], "XF86AudioPrev",lazy.spawn("playerctl previous"), 
        desc="Previous media"),

    # Screenshot
    Key([], "Print", lazy.spawn("flameshot screen"), 
        desc="Take a screenshot"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), 
        desc="Select an area for taking screenshot"),

    # Spawner
    Key([mod], "r", lazy.spawn(home + rofi), 
        desc="spawn rofi"),
    Key([mod, shft], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), 
        desc="Launch browser"),
    Key([mod], "m", lazy.spawn(filemanager), 
        desc="Launch file manager"),

]
