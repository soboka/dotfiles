from libqtile import hook
import subprocess
import os

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scrpits/autostart.sh")
    subprocess.call([home])
