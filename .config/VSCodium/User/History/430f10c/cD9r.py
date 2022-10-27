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
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
