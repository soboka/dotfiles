import os
from theme.colors import colors

# Home
home = os.path.expanduser("~")

# Keys
mod = "mod4"
alt = "mod1"
ctrl = "Control"
shft = "Shift"

# Applications
apps = {
    terminal = "xfce4-terminal",
    browser = "firefox",
    filemanager = "thunar",
    pinfo = "btop",
    tclient = "deluge",
}

# Menu
rofi  = "/.config/rofi/launchers/type-4/launcher.sh"
pwmenu = "/.config/rofi/powermenu/type-1/powermenu.sh"

# Wallpaper
wlpaper = "/.config/qtile/theme/No_mans_sky_wallp_01.png"

# Colors
colors = colors["everforest"]
