import os
import re
import socket
import subprocess
import json
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy

mod = "mod4" # windows key
icon_path = path.join(path.expanduser('~'), ".config/qtile/theme/logo-huka_32x32.png")
theme_path = path.join(path.expanduser('~'), ".config/qtile/theme/nord.json")

terminal = "alacritty"

font = "CaskaydiaCove Nerd Font"
icon_font = "Font Awesome 6 Free"

keys = [
    Key([mod], "c", lazy.window.kill()),
    Key([mod], "x", lazy.spawn("lock")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key(["mod1", "control"], "Delete", lazy.spawn("~/_bin/powermenu")),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift", "control"], "q", lazy.shutdown()),
    # Key([mod], "grave", lazy.group["scratch"].dropdown_toggle("term")),
    Key([mod], "Tab", lazy.spawn("~/_bin/switchapp")),
    Key([mod, "control"], "Left", lazy.screen.prev_group()),
    Key([mod, "control"], "Right", lazy.screen.next_group()),

    # Application Hotkeys
    Key([mod], "Return", lazy.spawn(terminal), desc="Launches My Terminal"),
    Key([mod], "r", lazy.spawn("~/_bin/launcher"), desc="Run Launcher"),
    Key([mod], "e", lazy.spawn("Thunar"), desc="Run File explorer"),
    Key([mod], "period", lazy.spawn("rofimoji -a type"), desc="Emoji"),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "Print", lazy.spawn("~/_bin/flameshotmenu")),
    Key(["control"], "Print", lazy.spawn("flameshot full -c")),
    Key(["mod1"], "Print", lazy.spawn("flameshot screen -r -c")),
    Key([mod, "control"], "v", lazy.spawn("~/_bin/save2inbox")),
    Key([mod], "v", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'")),

    KeyChord([mod], "o", [
        Key([], "w", lazy.spawn("google-chrome-stable")),
        Key([], "e", lazy.spawn("code")),
        Key([], "m", lazy.spawn("clementine")),
    ]),

    KeyChord([mod], "t", [
        Key([], "e", lazy.spawn("~/_bin/wordlookup"), desc="Translate English"),
    ]),

    ### Switch focus of monitors
    # Key([mod, "control"], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    # Key([mod, "control"], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),

    ### Switch focus to specific monitor
    # Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    # Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),

    # Layout Management
    Key([mod], "n", lazy.next_layout()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(["mod1"], "f", lazy.window.toggle_floating()),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus left in current stack pane"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right in current stack pane"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move windows down in current stack"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move windows up in current stack"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move windows left in current stack"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move windows right in current stack"),
    # Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    # Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    # Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow(), lazy.layout.increase_nmaster(), lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.shrink(), lazy.layout.increase_nmaster(), lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow(), lazy.layout.decrease_nmaster(),lazy.layout.grow_right()),
    Key([mod, "mod1"], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    # Key([mod], "i", lazy.layout.grow()),
    # Key([mod], "m", lazy.layout.shrink()),
    # Key([mod], "o", lazy.layout.maximize()),

    ### Stack controls
    Key([mod, "shift"], "space", lazy.layout.rotate(), lazy.layout.flip(), desc="Switch which side main pane occupies (XmonadTall)"),
    Key(["mod1"], "Tab", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
    Key(["mod1", "shift"], "Tab", lazy.layout.previous(), desc="Switch window focus to other pane(s) of stack"),
    Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("mpc toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -10 --unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume 10 --unmute")),
    Key([], "XF86AudioPrev", lazy.spawn("mpc previous")),
    Key([], "XF86AudioNext", lazy.spawn("mpc next")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
  ]

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["", "", "", "", "", "", "", "", "", ""]
# group_labels = ["DIR", "CMD", "WEB", "DEV", "DOC", "VID", "MED", "GIT", "MSG", "ETC"]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]
group_matches = [
                    [
                        Match(wm_class='doublecmd')
                    ],
                    [
                        Match(wm_class='Alacritty')
                    ],
                    [
                        Match(wm_class='google-chrome-stable'),
                        Match(wm_class="firefox")
                    ],
                    [
                        Match(wm_class='Code'),
                        Match(wm_class='wpspdf')
                    ],
                    [
                        Match(wm_class='calibre'),
                        Match(wm_class="libreoffice")
                    ],
                    [
                        Match(wm_class='vlc')
                    ],
                    [
                        Match(wm_class='Clementine'),
                    ],
                    [
                        Match(wm_class='SmartGit')
                    ],
                    [
                        Match(wm_class="slack"),
                        Match(wm_class="lightcord"),
                        Match(wm_class="polari"),
                        Match(wm_class='Skype'),
                        Match(wm_class="zoom"),
                        Match(wm_class="Telegram"),
                    ],
                    [
                        Match(wm_class="connman-gtk"),
                    ],
                ]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches=group_matches[i]
        ))

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

def load_theme():
  with open(theme_path) as f:
    return json.load(f)

if __name__ == "theme":
    colors = load_theme()

layout_conf = {
  "border_normal": "1D2330",
  "border_focus": colors["blue"][0],
  "border_width": 0,
  "margin": 0
}

layouts = [
    layout.MonadTall(**layout_conf, ratio=0.5),
    layout.MonadWide(**layout_conf, ratio=0.5),
    layout.Max()
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

separate = lambda : widget.Sep(
  linewidth=0,
  foreground=colors["background"],
  background=colors["background"],
  padding=10,
  size_percent=50,
)

group_box_settings = {
  "active": colors["foreground"],
  "inactive": colors["brightPurple"],
  "this_current_screen_border": colors["brightPurple"],
  "borderwidth": 4,
  "padding": 5,
  "disable_drag": True,
  "rounded": True,
  "highlight_color": colors["foreground"],
  "block_highlight_text_color": colors["foreground"],
  "highlight_method": "block",
  "this_screen_border": colors["purple"],
  "other_current_screen_border": colors["brightBlack"],
  "other_screen_border": colors["brightBlack"],
  "foreground": colors["purple"],
  "background": colors["background"],
  "urgent_border": colors["brightRed"],
}

workspaces = lambda: [
  widget.Image(
      background=colors["background"],foreground=colors["background"],
      filename = icon_path,
      mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(launcher_cmd)}
  ),
  separate(),

  widget.TextBox(
      text=" ",
      foreground=colors["blue"],
      background=colors["background"],
      font="Font Awesome 5 Free Solid",
      mouse_callbacks = {"Button2": lambda: qtile.cmd_spawn(killwindow_cmd)},
  ),
  CustomWindowName(
      foreground=colors["foreground"],
      background=colors["background"],
      width=bar.CALCULATED,
      empty_group_string="Desktop",
      max_chars=80,
      mouse_callbacks = {"Button2": lambda: qtile.cmd_spawn(killwindow_cmd)},
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
      foreground=colors["green"],
      background=colors["background"],
      mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(calendar_cmd)},
  ),
  separate(),
  widget.TextBox(
      text=" ",
      font="Font Awesome 5 Free Solid",
      foreground=colors["yellow"],
      background=colors["background"],
      mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(clock_cmd)},
  ),
  widget.Clock(
      format="%I:%M %p",
      foreground=colors["yellow"],
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

status_widgets = lambda: [
  # widget.Spacer(background=colors["background"]),
  # separate(),
  widget.TextBox(
      text="",
      foreground=colors["yellow"],
      background=colors["background"],
      font="Font Awesome 5 Free Solid"
  ),
  widget.CPUGraph(
      border_color=colors["yellow"],
      graph_color=colors["yellow"],
      background=colors["background"],
      border_width=1,
      line_width=1,
      type="line",
      width=100
  ),
  separate(),
  widget.TextBox(
      text="",
      foreground=colors["green"],
      background=colors["background"],
      font="Font Awesome 5 Free Solid"
  ),
  widget.MemoryGraph(
      border_color=colors["green"],
      graph_color=colors["green"],
      background=colors["background"],
      border_width=1,
      line_width=1,
      type="line",
      width=100
  ),
  separate(),
  widget.TextBox(
      text="",
      foreground=colors["cyan"],
      background=colors["background"],
      font="Font Awesome 5 Free Solid"
  ),
  widget.NetGraph(
      border_color=colors["cyan"],
      graph_color=colors["cyan"],
      background=colors["background"],
      border_width=1,
      line_width=1,
      type="line",
      width=100
  ),
  widget.Spacer(background=colors["background"]),
  separate(),
  CustomPomodoro(
      background=colors["background"],
      fontsize=20,
      color_active=colors["red"],
      color_break=colors["cyan"],
      color_inactive=colors["yellow"],
      timer_visible=False,
      prefix_active="",
      prefix_break="",
      prefix_inactive="",
      prefix_long_break="",
      prefix_paused="",
  ),
  widget.Systray(
      icon_size=18,
      background=colors["background"],
      padding=10,
  ),
]

bottom_widgets = [
  *status_widgets(),
]

status_bar = lambda widgets: bar.Bar(widgets, 24)
bottom_bar = lambda widgets: bar.Bar(widgets, 24)

screens = [Screen(top=status_bar(primary_widgets), bottom=status_bar(bottom_widgets))]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))

floating_types = ["notification", "toolbar", "splash", "dialog", "utility", "menu", "dropdown_menu", "popup_menu", "tooltip", "dock"]

@hook.subscribe.startup
def start():
    subprocess.call(["~/_bin/alwaystart"])

@hook.subscribe.client_new
def modify_window(client):
    transient = client.window.get_wm_transient_for()
    if client.window.get_wm_type() in floating_types or transient:
        client.floating = True
    else:
        for group in groups:  # follow on auto-move
            match = next((m for m in group.matches if m.compare(client)), None)
            if match:
                targetgroup = client.qtile.groups_map[
                    group.name
                ]  # there can be multiple instances of a group
                targetgroup.cmd_toscreen(toggle=False)
                break

follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"