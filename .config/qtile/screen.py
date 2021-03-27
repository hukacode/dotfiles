import subprocess
from libqtile.config import Screen
from libqtile import bar
from theme import colors
from widget import primary_widgets, secondary_widgets, status_bar

screens = [Screen(top=status_bar(primary_widgets))]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))
