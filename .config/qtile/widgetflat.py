import os, subprocess, json

from libqtile.command import lazy
from libqtile import bar, widget, qtile
from constant import launcher_cmd, powermenu_cmd, font, icon_path, weather_cmd, cpu_cmd, \
    memory_cmd, volume_cmd, calendar_cmd, killwindow_cmd, clock_cmd
from theme import colors
from custom.pomodoro import Pomodoro as CustomPomodoro

separate = lambda : widget.Sep(
    linewidth=0,
    foreground=colors["background"],
    background=colors["background"],
    padding=10,
    size_percent=50,
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
        background=colors["background"],foreground=colors["background"],
        filename = icon_path,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(launcher_cmd)}
    ),
    widget.Systray(
        icon_size=18,
        background=colors["background"],
        padding=10,
    ),
    widget.Spacer(background=colors["background"]),
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
    widget.Spacer(background=colors["background"]),
]
primary_widgets = [
    *workspaces(),
    separate(),
    CustomPomodoro(
        background=colors["background"],
        fontsize=18,
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
    separate(),
    widget.TextBox(
        text=" ",
        foreground=colors["brightYellow"],
        background=colors["background"],
        font="Font Awesome 5 Free Solid",
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(volume_cmd)}
    ),
    widget.PulseVolume(
        foreground=colors["foreground"],
        background=colors["background"],
        limit_max_volume="True",
        volume_app="pavucontrol"
    ),
    separate(),
    widget.TextBox(
        text=" ",
        font="Font Awesome 5 Free Solid",
        foreground=colors["green"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)},
    ),
    widget.Clock(
        format="%b %d (%a)",
        foreground=colors["foreground"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)},
    ),
    separate(),
    widget.TextBox(
        text=" ",
        font="Font Awesome 5 Free Solid",
        foreground=colors["foreground"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(clock_cmd)},
    ),
    widget.Clock(
        format="%I:%M %p",
        foreground=colors["foreground"],
        background=colors["background"],
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(clock_cmd)},
    ),
    widget.TextBox(
        text="",
        foreground=colors["red"],
        background=colors["background"],
        font="Font Awesome 5 Free Solid",
        padding=18,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(powermenu_cmd)},
    ),
]

secondary_widgets = [
    *workspaces(),
]

status_bar = lambda widgets: bar.Bar(widgets, 24)