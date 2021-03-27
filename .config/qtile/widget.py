import os, subprocess, json

from libqtile.command import lazy
from libqtile import bar, widget, qtile
from constant import launcher_cmd, powermenu_cmd, font, icon_path, weather_cmd, cpu_cmd, \
    memory_cmd, volume_cmd, calendar_cmd
from theme import colors
from custom.pomodoro import Pomodoro as CustomPomodoro
from custom.windowname import WindowName as CustomWindowName

powerline_left = lambda : widget.TextBox(    
    foreground=colors["background"],
    background=colors["black"],
    font=font,
    fontsize=21,
    text="",
    padding= -1
)

powerline_right = lambda : widget.TextBox(    
    foreground=colors["background"],
    background=colors["black"],
    font=font,
    fontsize=21,
    text="",
    padding= -1
)

separate = lambda : widget.Sep(
    linewidth=0,
    foreground=colors["foreground"],
    padding=10,
    size_percent=50,
)

widget_defaults = dict(
    font=font, fontsize=13, padding=3, background=colors["black"]
)
group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors["cyan"],
    "inactive": colors["brightBlack"],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors["foreground"],
    "block_highlight_text_color": colors["foreground"],
    "highlight_method": "block",
    "this_current_screen_border": colors["blue"],
    "this_screen_border": colors["purple"],
    "other_current_screen_border": colors["brightBlack"],
    "other_screen_border": colors["brightBlack"],
    "foreground": colors["foreground"],
    "background": colors["background"],
    "urgent_border": colors["brightRed"],
}

workspaces = lambda: [
    widget.Image(
        background=colors["black"],foreground=colors["black"],
        filename = icon_path,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(launcher_cmd)}
    ),

    separate(),

    powerline_left(),
    widget.GroupBox(
        font="Font Awesome 5 Free Solid",
        visible_groups=["1","2"],
        **group_box_settings,
    ),
    widget.GroupBox(
        font="Font Awesome 5 Brands",
        visible_groups=["3"],
        **group_box_settings,
    ),
    widget.GroupBox(
        font="Font Awesome 5 Free Solid",
        visible_groups=["4", "5", "6", "7"],
        **group_box_settings,
    ),
    widget.GroupBox(
        font="Font Awesome 5 Brands",
        visible_groups=["8"],
        **group_box_settings,
    ),
    widget.GroupBox(
        font="Font Awesome 5 Free Solid",
        visible_groups=["9", "0"],
        **group_box_settings,
    ),
    powerline_right(),

    separate(),

    powerline_left(),
    widget.CurrentLayoutIcon(
        foreground=colors["foreground"],
        background=colors["background"],
        scale=0.65
    ),
    powerline_right(),

    # widget.TaskList(
    #     background=colors["black"],
    #     border=colors["black"],
    #     borderwidth=2,
    #     highlight_method="block",
    #     # icon_size=20,
    #     margin_y=3,
    #     margin_x=3,
    #     padding_x=3,
    #     padding_y=3,
    #     spacing=0,
    #     # max_title_width=24,
    #     markup_floating="",
    #     markup_focused="",
    #     markup_maximized="",
    #     markup_minimized="",
    #     markup_normal="",
    # ),
    separate(),

    widget.TextBox(
        text=" ",
        foreground=colors["blue"],
        background=colors["black"],
        font="Font Awesome 5 Free Solid",
    ),
    CustomWindowName(
        foreground=colors["blue"],
        background=colors["black"],
        width=bar.CALCULATED,
        empty_group_string="Desktop",
        max_chars=55,
        mouse_callbacks = {"Button3": lambda: qtile.cmd_spawn(killwindow_cmd)},
    ),
    widget.Spacer(),
]
primary_widgets = [
    *workspaces(),
    powerline_left(),
    widget.Systray(
        icon_size=18, 
        background=colors["background"],
        padding=10,
    ),
    powerline_right(),
    
    separate(),

    powerline_left(),
    CustomPomodoro(
        background=colors["background"],
        fontsize=24,
        color_active=colors["red"],
        color_break=colors["cyan"],
        color_inactive=colors["brightPurple"],
        timer_visible=False,
        prefix_active="",
        prefix_break="",
        prefix_inactive="",
        prefix_long_break="",
        prefix_paused="",
    ),
    powerline_right(),

    separate(),

    powerline_left(),
    widget.TextBox(
        text=" ",
        foreground=colors["cyan"],
        background=colors["background"],
        font="Font Awesome 5 Free Solid",
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(volume_cmd)}
    ),
    widget.PulseVolume(
        foreground=colors["cyan"],
        background=colors["background"],
        limit_max_volume="True",
        volume_app="pavucontrol"
    ),
    powerline_right(),

    separate(),
    
    powerline_left(),
    widget.TextBox(
        text=" ",
        font="Font Awesome 5 Free Solid",
        foreground=colors["green"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)},
    ),
    widget.Clock(
        format="%b %d %a",
        foreground=colors["green"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)},
    ),
    powerline_right(),

    separate(),

    powerline_left(),
    widget.TextBox(
        text=" ",
        font="Font Awesome 5 Free Solid",
        foreground=colors["brightYellow"],
        background=colors["background"],
    ),
    widget.Clock(
        format="%I:%M %p",
        foreground=colors["brightYellow"],
        background=colors["background"],
    ),
    powerline_right(),

    widget.TextBox(
        text="⏻",
        foreground=colors["cyan"],
        font="Font Awesome 5 Free Solid",
        fontsize=19,
        padding=18,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(powermenu_cmd)},
    ),
]

secondary_widgets = [
    *workspaces(),
]

status_bar = lambda widgets: bar.Bar(widgets, 24)