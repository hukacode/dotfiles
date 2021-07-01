from libqtile import layout
from libqtile.config import Match
from theme import colors
from custom.bsp import Bsp as CustomBsp

layout_conf = {
    "border_focus": colors["blue"][0],
    "border_width": 0,
    "margin": 0
}

layouts = [
    layout.MonadTall(**layout_conf, ratio=0.5),
    layout.Max(),
    # layout.Floating(**layout_conf),
    # CustomBsp(**layout_conf, fair=False),
    # layout.Tile(shift_windows=True, **layout_conf),
    # layout.Stack(stacks=2, **layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Columns(**layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.VerticalTile(**layout_conf),
    # layout.Matrix(**layout_conf),
    # layout.Zoomy(**layout_conf),
    # layout.TreeTab(
    #      font = font,
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND"],
    #      section_fontsize = 11,
    #      bg_color = "141414",
    #      active_bg = "90C435",
    #      active_fg = "000000",
    #      inactive_bg = "384323",
    #      inactive_fg = "a0a0a0",
    #      padding_y = 5,
    #      section_top = 10,
    #      panel_width = 320
    #      )
]

# Run the utility of `xprop` to see the wm class and name of an X client.
floating_layout = layout.Floating(
    float_rules=[
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(func=lambda c: c.has_fixed_size()),
        Match(wm_class='org.gnome.clocks'),
        Match(wm_class='pavucontrol'),
        Match(wm_class='Arandr')
    ],
    border_focus=colors["purple"][0]
)