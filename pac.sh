# !/usr/bin/bash
pmset -g log | grep -e "PowerButton" -e "Start" | tail -1| awk {'print $1 " Start time: " $2 " "'} 
