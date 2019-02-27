#################################################################
# Title: wall.py
# Author: Sahaj Sarup
# Copyright (c) 2018 Linaro Limited
#################################################################

from evdev import InputDevice, categorize, ecodes
import evdev
import time
import subprocess as sub

timeout = 5
touchdev = 'WaveShare WaveShare Touchscreen'

def touch(dev):
    start = 0
    for event in dev.read_loop():
            if str(evdev.categorize(event))[-1] == 'p':
                print("Hello")
                sub.call('sudo pkill fbi', shell=True)
                time.sleep(10)
                sub.call('fbi -d /dev/fb0 -T 1 -a ./images/* -t ' + timeout + ' -u', shell=True)

if __name__=="__main__":
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    sub.call('startx ./wall-calendar.sh &', shell=True)
    time.sleep(10)
    sub.call('fbi -d /dev/fb0 -T 1 -a ./images/* -t ' + timeout + ' -u', shell=True)
    for device in devices:
        print(device.path, device.name, device.phys)
        if(device.name == touchdev):
            dev = InputDevice(device.path)
    touch(dev)
