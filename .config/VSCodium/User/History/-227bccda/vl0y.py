import os
from libqtile import widget
from libqtile import qtile
from modules.vars import colors


widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Volume widget
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '婢'
        elif self.volume <= 15:
            self.text = '奄'
        elif self.volume < 50:
            self.text = '奔'
        else:
            self.text = '墳'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '婢'
        elif self.volume <= 15:
            self.text = '奄'
        elif self.volume < 50:
            self.text = '奔'
        else:
            self.text = '墳'
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize=18,
    font='SpaceMono Nerd Font',
    foreground=colors["fg1"],
    background=colors["bg2"],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

# Window name widget
windowname = widget.WindowName(
    foreground=colors["fg2"],
    format="{name}"
)

# Chord widget
chord = widget.Chord(
    chords_colors={'launch': (colors["urgent"], colors["fg1"]),},
    name_transform=lambda name: name.upper(),
)

# Group box widget
groupbox = widget.GroupBox(
    font='SpaceMono Nerd Font',
    disable_drag = True,
    highlight_method='line',
    this_screen_border=colors["fg1"],
    this_current_screen_border=colors["fg1"],
    active=colors["fg1"],
    inactive= colors["inactive"],
    background=colors["bg2"],
    margin_x = 1,
    use_mouse_wheel = False
)

# Tasklist
def txt_remove(text): 
    return ""

tasklist = widget.TaskList(
    background= colors["bg2"],
    color_active = colors["white"],
    color_inactive = colors["inactive"],
    highlight_method="block",
    border= colors["fg1"],
    borderwidth=0,
    icon_size = 20,
    fontsize=18,
    max_title_width = 25,
    title_width_method="uniform",
    parse_text=txt_remove,
    spacing = 5,
    urgent_alert_method="block",
    urgent_border= colors["urgent"],
    theme_path="/usr/share/icons/Papirus-dark",
    theme_mode="preferred",
)

# Current layout widget
layoutcurrent = widget.CurrentLayoutIcon(
    scale=0.75,
    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons/everforest")],
    background =colors["bg2"]
)

# System tray widget
systray = widget.Systray(
    icon_size = 20
)

# Clock widget
clock = widget.Clock(
    format='%m-%d %a %H:%M',
    background= colors["bg2"],
    foreground= colors["fg2"]
)

# Mpris widget
mpris = widget.Mpris2(
    background= colors["bg1"],
    foreground= colors["fg2"],
    stop_pause_text='PAUSED',
    thumbnail = 'xesam:url',
    display_metadata=['xesam:title'],
    width=180,
    scroll=True
)

# Memory widget
memtext = widget.TextBox(
    font = 'SpaceMono Nerd Font',
    foreground = colors["fg1"],
    background = colors["bg2"],
    text = 'RAM:',
    fontsize = 14,
    padding = 0
)

memory = widget.Memory(
        foreground = colors["fg2"],
        background = colors["bg2"],
        #format  =   '{MemUsed:02.0f}{mm}/{MemTotal:.0f}{mm}',
        format = "{MemPercent:.0f}%",
        update_interval = 3,
        fontsize = 14,
        font='SpaceMono Nerd Font',
        measure_mem ='G'
)

# CPU widget
cputext = widget.TextBox(
    font = 'SpaceMono Nerd Font',
    foreground = colors["fg1"],
    background = colors["bg2"],
    text = 'CPU:',
    fontsize = 14,
    padding = 0
)

cpu = widget.CPU(
    foreground = colors["fg2"],
    background = colors["bg2"],
    format="{load_percent}%"
)

# Decor 1 Left
decLeft1 = widget.TextBox(
    font ='Symbols Nerd Font',
    foreground=colors["bg2"],
    text = '',
    fontsize = 28,
    padding = 0
)

# Decor 1 Right
decRight1 = widget.TextBox(
    font ='Symbols Nerd Font',
    foreground=colors["bg2"],
    text = '',
    fontsize = 28,
    padding = 0
)