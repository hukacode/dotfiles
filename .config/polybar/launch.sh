#!/usr/bin/env bash

# kill existing polybar instances
killall -q polybar

# launch polybar
polybar topbar -r >>/tmp/polybar.log 2>&1 & disown