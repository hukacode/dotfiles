from libqtile import layout
from theme import colors

layout_conf = {
    "border_focus": colors[1],
    "border_width": 2,
    "margin": 4
}

layouts = [
    layout.MonadTall(**layout_conf, ratio=0.7),
    layout.Max(),
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
    #      ),
    # layout.Floating(**layout_conf)
]

# Run the utility of `xprop` to see the wm class and name of an X client.
floating_layout = layout.Floating(
    # float_rules=[
    #     {"role": "EventDialog"},
    #     {"role": "Msgcompose"},
    #     {"role": "Preferences"},
    #     {"role": "pop-up"},
    #     {"role": "prefwindow"},
    #     {"role": "task_dialog"},
    #     {"wname": "Module"},
    #     {"wname": "Terminator Preferences"},
    #     {"wname": "Search Dialog"},
    #     {"wname": "Goto"},
    #     {"wname": "IDLE Preferences"},
    #     {"wname": "Sozi"},
    #     {"wname": "Create new database"},
    #     {"wname": "Preferences"},
    #     {"wname": "File Transfer"},
    #     {"wname": "confirm"},
    #     {"wmclass": "Dukto"},
    #     {"wmclass": "SmartGit"},
    #     {"wmclass": "Guake"},
    #     {"wmclass": "Tilda"},
    #     {"wmclass": "yakuake"},
    #     {"wmclass": "Xfce4-appfinder"},
    #     {"wmclass": "GoldenDict"},
    #     {"wmclass": "Synapse"},
    #     {"wmclass": "Pamac-updater"},
    #     {"wmclass": "TelegramDesktop"},
    #     {"wmclass": "Galculator"},
    #     {"wmclass": "notify"},
    #     {"wmclass": "Lxappearance"},
    #     {"wmclass": "Nitrogen"},
    #     {"wmclass": "Oblogout"},
    #     {"wmclass": "Pavucontrol"},
    #     {"wmclass": "VirtualBox"},
    #     {"wmclass": "Skype"},
    #     {"wmclass": "Steam"},
    #     {"wmclass": "nvidia-settings"},
    #     {"wmclass": "Eog"},
    #     {"wmclass": "Rhythmbox"},
    #     {"wmclass": "obs"},
    #     {"wmclass": "Gufw.py"},
    #     {"wmclass": "Catfish"},
    #     {"wmclass": "libreoffice-calc"},
    #     {"wmclass": "LibreOffice 3.4"},
    #     {"wmclass": "Mlconfig"},
    #     {"wmclass": "Termite"},
    #     {"wmclass": "confirm"},
    #     {"wmclass": "dialog"},
    #     {"wmclass": "download"},
    #     {"wmclass": "error"},
    #     {"wmclass": "file_progress"},
    #     {"wmclass": "notification"},
    #     {"wmclass": "splash"},
    #     {"wmclass": "toolbar"},
    #     {"wmclass": "Arandr"},
    #     {"wname": "Open File"},
    #     {"wmclass": "confirmreset"},  # gitk
    #     {"wmclass": "makebranch"},  # gitk
    #     {"wmclass": "maketag"},  # gitk
    #     {"wname": "branchdialog"},  # gitk
    #     {"wname": "pinentry"},  # GPG key password entry
    #     {"wmclass": "ssh-askpass"},  # ssh-askpass

    # ],
    border_focus=colors[4]
)