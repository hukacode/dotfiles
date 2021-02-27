import os, subprocess, json

from libqtile.command import lazy
from libqtile import bar, widget, qtile
from constant import launcher_cmd, powermenu_cmd, font, icon_path, weather_cmd, cpu_cmd, memory_cmd, volume_cmd, calendar_cmd
from theme import colors

colorText = "#ffffff"

icon = lambda fg=colors[0], bg=colors[1], fontsize=22, text="?", mouse_callbacks={}: widget.TextBox(
    background=bg,
    foreground=fg,
    font=font,
    fontsize=fontsize,
    text=text,
    padding=5,
    mouse_callbacks = mouse_callbacks,
)

powerline_left = lambda fg=colors[0], bg=colors[1]: widget.TextBox(
    background=bg,
    foreground=fg,
    font=font,
    fontsize=21,
    text="",
    padding= -1
)

powerline_right = lambda fg=colors[0], bg=colors[1]: widget.TextBox(
    background=bg,
    foreground=fg,
    font=font,
    fontsize=21,
    text="",
    padding= -1
)

workspaces = lambda: [
    widget.Image(
        background=colors[0],foreground=colors[0],
        filename = icon_path,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(launcher_cmd)}
        ),
    powerline_left(bg=colors[1], fg=colors[0]),

    widget.GroupBox(
        font=font,
        fontsize=12,
        disable_drag=True,
        padding=3,
        rounded=False,
        highlight_method="line",
        urgent_alert_method="block",
        urgent_border=colors[6],
        active=colorText,
        inactive=colors[7],
        this_current_screen_border=colors[7],
        this_screen_border=colors[3],
        other_current_screen_border=colors[0],
        other_screen_border=colors[0],
        foreground=colors[7],
        background=colors[1]),
    powerline_left(bg=colors[0], fg=colors[1]),

    widget.TaskList(
        background=colors[0],
        border=colors[0],
        borderwidth=2,
        highlight_method="block",
        # icon_size=20,
        margin_y=3,
        margin_x=3,
        padding_x=3,
        padding_y=3,
        spacing=0,
        # max_title_width=24,
        markup_floating="",
        markup_focused="",
        markup_maximized="",
        markup_minimized="",
        markup_normal="",),
    widget.Spacer(length=bar.STRETCH,background=colors[0],foreground=colors[0]),
]
primary_widgets = [
    *workspaces(),
    powerline_right(bg=colors[0], fg=colors[8]),
    widget.Systray(icon_size=18, background=colors[8], foreground=colorText),

    powerline_right(bg=colors[8], fg=colors[7]),
    icon(text="摒", bg=colors[7], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(weather_cmd)}),
    # widget.OpenWeather(background=colors[7], foreground=colorText, app_key='e45a0f07f0c675b273ef8636663941db', cityid='1583992', 
    #     format='{main_temp}°{units_temperature}', metric=True, update_interval=600,
    #     mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(weather_cmd)}),
    
    # powerline_right(bg=colors[7], fg=colors[6]),
    icon(text="", bg=colors[7], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(memory_cmd)}),
    # widget.Memory(background=colors[6], foreground=colorText, format='{MemUsed}M'),
    
    # powerline_right(bg=colors[6], fg=colors[5]),
    icon(text="", bg=colors[7], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(cpu_cmd)}),
    # widget.CPU(background=colors[5], foreground=colorText, format='{load_percent}%',
    #     mouse_callbacks={'Button1': cpu_cmd}),
    #widget.CPUGraph(type='linefill', fill_color=colors[7], border_color=colors[0], graph_color=colors[0], foreground=colors[0], background=colors[5], padding=5, mouse_callbacks={'Button1': htop}),    

    # icon(text="", bg=colors[5], fg=colorText,
    #     mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(storage_cmd)}),
    # widget.DF(format='{p} ({uf}{m}|{r:.0f}%)', measure='G', Partition='/', update_interval=60, foreground=colors[0], background=colors[3], padding=5, visible_on_warn=False,mouse_callbacks={'Button1':lambda qtile: qtile.cmd_spawn(term + '-e ranger')}, warn_color="ff0000"),

    powerline_right(bg=colors[7], fg=colors[3]),
    icon(text="", bg=colors[3], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(volume_cmd)}),
    widget.PulseVolume(background=colors[3], foreground=colorText, volume_app="pavucontrol"),

    powerline_right(bg=colors[3], fg=colors[1]),
    icon(text="", bg=colors[1], fg=colorText),
    widget.Pomodoro(
        background=colors[1],
        foreground=colorText,
        color_active=colorText,
        color_break=colors[5],
        color_inactive=colorText,
        length_pomodori=50,
        length_short_break= 5,
        length_long_break=15,
        num_pomodori=3,
        prefix_break='Break',
        prefix_inactive='Start',
        prefix_long_break='Long Break',
        prefix_paused='' ),

    powerline_right(bg=colors[1], fg=colors[2]),
    icon(text="", bg=colors[2], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)}),
    widget.Clock(
        background=colors[2],
        foreground=colorText,
        format="%a %d %b | %H:%M ",
        update_interval=1,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)}),

    powerline_right(bg=colors[2], fg=colors[6]),
    widget.CurrentLayoutIcon(background=colors[6], foreground=colors[0], scale=0.65),
    icon(text="襤", bg=colors[6], fg=colorText,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(powermenu_cmd)}),
]

secondary_widgets = [
    *workspaces(),
]