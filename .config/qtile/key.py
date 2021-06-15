import subprocess
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from constant import powermenu_cmd, launcher_cmd, terminal_app, screenshot_area_cmd, \
    screenshot_full_cmd, screenshot_windows_cmd, translate_cmd, mute_cmd, lower_cmd, \
    raise_cmd, next_cmd, previous_cmd, brightnessDown_cmd, brightnessUp_cmd, \
    screenshot_menu_cmd, switchapp_cmd, rofimoji_cmd, web_app, editor_app, music_app
from group import groups

mod = "mod4" # windows key

keys = [
    # Kill window, restart and exit Qtile
    Key([mod], "c", lazy.window.kill()),
    Key([mod], "x", lazy.spawn("lock")),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key(["mod1", "control"], "Delete", lazy.spawn(powermenu_cmd)),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift", "control"], "q", lazy.shutdown()),
    # Key([mod], "grave", lazy.group['scratch'].dropdown_toggle('term')),
    Key([mod], "Tab", lazy.spawn(switchapp_cmd)),

    # Application Hotkeys
    Key([mod], "Return",
        lazy.spawn(terminal_app),
        desc='Launches My Terminal'
        ),
    Key([mod], "r",
        lazy.spawn(launcher_cmd),
        desc='Run Launcher'
    ),
    Key([mod], 'period', lazy.spawn(rofimoji_cmd)),
    Key([], 'Print', lazy.spawn(screenshot_area_cmd)),
    Key([mod], 'Print', lazy.spawn(screenshot_menu_cmd)),
    Key(['control'], 'Print', lazy.spawn(screenshot_full_cmd)),
    Key(['mod1'], 'Print', lazy.spawn(screenshot_windows_cmd)),

    KeyChord([mod], "o", [
        Key([], "w", lazy.spawn(web_app)),
        Key([], "e", lazy.spawn(editor_app)),
        Key([], "m", lazy.spawn(music_app)),
    ]),

    KeyChord([mod], "t", [
        Key([], "e",
            lazy.spawn(translate_cmd),
            desc='Translate English'
        ),
    ]),

    ### Switch focus of monitors
    # Key([mod, "control"], "period",
    #     lazy.next_screen(),
    #     desc='Move focus to next monitor'
    #     ),
    # Key([mod, "control"], "comma",
    #     lazy.prev_screen(),
    #     desc='Move focus to prev monitor'
    #     ),

    ### Switch focus to specific monitor
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),

    # Layout Management
    Key([mod], "n", lazy.next_layout()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(["mod1"], "f", lazy.window.toggle_floating()),
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod], "h",
        lazy.layout.left(),
        desc='Move focus left in current stack pane'
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc='Move focus right in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc='Move windows left in current stack'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc='Move windows right in current stack'
        ),
    # Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    # Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    # Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j",
        lazy.layout.shrink(), # Shrink window (MonadTall), decrease number in master pane (Tile)
        lazy.layout.decrease_nmaster(),
        lazy.layout.grow_down()
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow(), # Expand window (MonadTall), increase number in master pane (Tile)
        lazy.layout.increase_nmaster(),
        lazy.layout.grow_up()
        ),
    Key([mod, "control"], "h",
        lazy.layout.shrink(), # Expand window (MonadTall), increase number in master pane (Tile)
        lazy.layout.increase_nmaster(),
        lazy.layout.grow_left()
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow(), # Shrink window (MonadTall), decrease number in master pane (Tile)
        lazy.layout.decrease_nmaster(),
        lazy.layout.grow_right()
        ),
    Key([mod, "mod1"], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),

    ### Stack controls
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),

    Key(["mod1"], "Tab",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key(["mod1", "shift"], "Tab",
        lazy.layout.previous(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn(mute_cmd)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(lower_cmd)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(raise_cmd)),
    Key([], "XF86AudioPrev", lazy.spawn(previous_cmd)),
    Key([], "XF86AudioNext", lazy.spawn(next_cmd)),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(brightnessUp_cmd)),
    Key([], "XF86MonBrightnessDown", lazy.spawn(brightnessDown_cmd)),
    ]

for i in groups:
    keys.extend([
        # Workspace navigation
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Switch group
        # Key([mod], "Tab", lazy.screen.next_group()),
        # Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "control"], "Left", lazy.screen.prev_group()),
        Key([mod, "control"], "Right", lazy.screen.next_group()),
        Key([mod, "control"], i.name, lazy.window.togroup(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        if hasattr(k, 'desc'):
            key_help += "{:<30} {}".format(mods, k.desc + "\n")
        else:
            key_help += "{:<30}".format(mods)

    return key_help

# keys.extend(
#     [
#         KeyChord([mod], "o", [
#             Key(
#                 "k",
#                 lazy.spawn(
#                     "sh -c 'echo \""
#                     + show_keys()
#                     + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p "?"\''
#                 ),
#                 desc="Print keyboard bindings",
#             ),
#         ]),
#     ]
# )
keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p "?"\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)