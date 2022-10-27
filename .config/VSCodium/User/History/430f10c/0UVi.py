from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.MonadTall(margin=8, 
                     border_focus='#A7C080',
                     border_normal='#939A8F'),
    layout.MonadThreeCol(margin=8, 
                         border_focus='#A7C080',
                         border_normal='#939A8F',
                         new_client_position='bottom'),
    layout.Max(),
    # layout.Columns(border_focus_stack='#E69875'),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(margin=8, border_focus='#A7C080',
    #                 border_normal='#939A8F'),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
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
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='qalculate-gtk'),
    Match(title='Krita - Edit Text'),
    Match(title='ksnip'),  # Krita Text Editor
])
