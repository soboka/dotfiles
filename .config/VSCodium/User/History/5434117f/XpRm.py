from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.hooks import *
import os
from modules.screens import screens
from modules.scratchpad import *

main = None  # WARNING: this is deprecated and will be removed soon

dgroups_key_binder = None
dgroups_app_rules = []  # type: List

follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

widget_defaults = dict(
        font='Cascadia Code',
        fontsize=13,
        padding=3
)

wmname = "Qtile"
