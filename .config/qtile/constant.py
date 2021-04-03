from os import path

icon_path = path.join(path.expanduser('~'), ".config/qtile/logo/logo-huka_32x32.png")
# theme_path = path.join(path.expanduser('~'), ".cache/wal/colors.json")
theme_path = path.join(path.expanduser('~'), ".config/qtile/dracula.json")

terminal_app = "alacritty"
web_app = "google-chrome-stable"
editor_app = "code"
music_app = "clementine"

font = "CaskaydiaCove Nerd Font"
icon_font = "Font Awesome 5 Free"

weather_cmd = terminal_app + " --hold -e curl wttr.in/DaNang"
cpu_cmd = terminal_app + " -e gotop"
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
lower_cmd = "pulsemixer --change-volume -10 --unmute"
raise_cmd = "pulsemixer --change-volume 10 --unmute"
killwindow_cmd = "xdotool getwindowfocus windowkill"
brightnessUp_cmd = "brightnessctl set +10%"
brightnessDown_cmd = "brightnessctl set 10%-"
translate_cmd = path.join(path.expanduser('~'), "script/wordlookup")
launcher_cmd = path.join(path.expanduser('~'), "script/launcher")
powermenu_cmd = path.join(path.expanduser('~'), "script/powermenu")
autostart_cmd = path.join(path.expanduser('~'), "script/autostart")
alwaystart_cmd = path.join(path.expanduser('~'), "script/alwaystart")
switchapp_cmd = path.join(path.expanduser('~'), "script/switchapp")
rofimoji_cmd = "rofimoji -a type"

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
