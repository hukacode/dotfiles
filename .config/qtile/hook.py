import os, subprocess
from libqtile import hook
from constant import autostart_cmd, alwaystart_cmd

@hook.subscribe.startup_once
def start_once():
    subprocess.call([autostart_cmd])

@hook.subscribe.startup
def start():
    subprocess.call([alwaystart_cmd])

@hook.subscribe.screen_change
def restart_on_randr():
    #qtile.cmd_spawn('urxvt -e xrandr --output HDMI1 --auto --right-of eDP1')
	qtile.cmd_restart()

@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog", "utility", "menu", "dropdown_menu", "popup_menu", "tooltip", "dock"]
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True