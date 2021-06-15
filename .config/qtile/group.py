from libqtile.config import Group, Match
from libqtile.command import lazy

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["", "", "", "", "", "", "", "", "", ""]
# group_labels = ["DIR", "CMD", "WEB", "DEV", "DOC", "VID", "MED", "GIT", "MSG", "ETC"]
group_layouts = ["max", "monadtall", "max", "monadtall", "max", "max", "max", "max", "max", "max"]
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
