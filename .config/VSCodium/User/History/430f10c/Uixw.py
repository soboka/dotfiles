from libqtile import layout
from libqtile.config import Match
from modules.vars import colors

basic_theme = {
    "margin":8, 
    "border_width":2,
    "border_focus": colors["fg1"],
    "border_normal": colors["inactive"]
}

layouts = [
    layout.MonadTall(
        **basic_theme
    ),
    layout.MonadThreeCol(
        **basic_theme,
        new_client_position='bottom'
        ),
    layout.Max(),
    layout.Stack(
        **basic_theme,
        num_stacks=1
    ),
    # layout.Columns(border_focus_stack= colors["urgent"]),
    # layout.Bsp(margin=8, border_focus= colors["fg1"],
    #                 border_normal= colors["inactive"]),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    auto_float_types=[
        "notification",
        "toolbar",
        "splash",
        "dialog",
    ],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_type="utility"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(wm_class='pavucontrol'),
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(title='Qalculate!'),
        Match(title='Krita - Edit Text'),
        Match(title='ksnip'),  # Krita Text Editor
        Match(wm_class="Steam"),
    ],
    border_focus= colors["fg1"],
    border_width=3,
)
