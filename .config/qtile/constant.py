from os import path

icon_path = path.join(path.expanduser('~'), "icon/huka.png")
theme_path = path.join(path.expanduser('~'), ".cache/wal/colors.json")
# theme_path = path.join(path.expanduser('~'), ".config/qtile/material.json")

terminal_app = "alacritty"
font = "JetBrainsMono Nerd Font Mono"
icon_font = "Font Awesome 5 Free"

weather_cmd = terminal_app + " --hold -e curl wttr.in/DaNang"
cpu_cmd = terminal_app + " -e gtop"
memory_cmd = terminal_app + " -e htop"
volume_cmd = "pavucontrol"
calendar_cmd = terminal_app + " -e calcurse"
screenshot_area_cmd = "flameshot gui"
screenshot_full_cmd = "flameshot full -c"
screenshot_windows_cmd = "flameshot screen -r -c"
screenshot_menu_cmd = path.join(path.expanduser('~'), "script/flameshotmenu")
next_cmd = "playerctl next"
previous_cmd = "playerctl previous"
mute_cmd = "playerctl play-pause && pulsemixer --unmute"
lower_cmd = "pulsemixer --change-volume -5 --unmute"
raise_cmd = "pulsemixer --change-volume 5 --unmute"
brightnessUp_cmd = "brightnessctl set +10%"
brightnessDown_cmd = "brightnessctl set 10%-"
translate_cmd = path.join(path.expanduser('~'), "script/wordlookup")
launcher_cmd = path.join(path.expanduser('~'), "script/launcher")
powermenu_cmd = path.join(path.expanduser('~'), "script/powermenu")
autostart_cmd = path.join(path.expanduser('~'), "script/autostart")
alwaystart_cmd = path.join(path.expanduser('~'), "script/alwaystart")
# mute_cmd = "amixer -q set Master toggle"
# lower_cmd = "amixer -q set Master 5%-"
# raise_cmd = "amixer -q set Master 5%+"

#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
#  
# ◤ ◢
