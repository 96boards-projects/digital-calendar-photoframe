#################################################################
# Title: wall-calendar.sh
# Author: Sahaj Sarup
# Copyright (c) 2018 Linaro Limited
#################################################################

#!/bin/bash

xset -dpms
xset s off
xset s noblank

unclutter &
chromium 'https://calendar.google.com/calendar/embed?src=en.indian%23holiday%40group.v.calendar.google.com&ctz=Asia%2FCalcutta' --window-size=800,480 --start-fullscreen --fast --kiosk --incognito --noerrdialogs --disable-translate --no-first-run --disable-infobars --no-sandbox
