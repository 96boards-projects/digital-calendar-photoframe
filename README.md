# Digital Calendar and Photoframe

# Table of Contents

- [1) Hardware](#1-hardware)
   - [1.1) Hardware Requirements](#11-hardware-requirements)
   - [1.2) Hardware Setup](#12-hardware-setup)
- [2) Software](#2-software)
   - [2.1) Install Dependencies](#21-install-dependencies)
   - [2.2) Code Customization Options](#22-code-customization-options)
   - [2.3) Running the Digital Calendar and Photo frame](#23-running-the-digital-calendar-and-photo-frame)

# 1) Hardware

## 1.1) Hardware Requirements

- [Any 96Boards CE](https://www.96boards.org/products/ce/)
- [HDMI + USB Touchscreen](https://www.arrow.com/en/products/96boards-display-7/linksprite-technologies-inc)

## 1.2) Hardware Setup

- Make sure the touchscreen is connected to 96Boards CE using HDMI cable and USB.

# 2) Software

**This guide assumes that [Debian OS is running on a Dragonboard410c](https://www.96boards.org/documentation/consumer/dragonboard410c/downloads/debian.md.html). How ever the instructions hold true for other 96Boards CE Boards running Debian.**

> This project is compatible with other Linux based OS, but they might have to be tweaked accordingly.

Make sure your CE Board is connected to a WiFi network.

## 2.1) Install Dependencies

**Install File Browser**
- Download File Browser
```Shell
$ wget https://github.com/filebrowser/filebrowser/releases/download/v1.10.0/linux-arm64-filebrowser.tar.gz
```
- Extract to /usr/bin/
```Shell
$ tar -xzf linux-arm64-filebrowser.tar.gz -C /usr/bin/
```

**Package Dependencies**
```Shell
$ sudo apt install python-evdev python-subprocess unclutter chromium xserver-xorg-video-all xserver-xorg-input-all xserver-xorg-core xinit x11-xserver-utils evtest
```

## 2.2) Code Customization Options

- **Custom Calendar:**
  - You can use a customized Google Calendar, follow [these steps](https://support.google.com/calendar/answer/37083?hl=en) to get a customized calendar link.
  - Once you get a sharable link, replace the existing link in the ```wall-calendar.sh``` file.

- **Calendar Resolution:**
  - Calendar resolution can be modified by adjusting the ```--window-size``` flag in ```wall-calendar.sh``` file.

- **Image Timeout:**
  - Slideshow image timeout can be set by adjusting the timeout variable in ```wall.py``` file.

- **Touchscreen Device Name:**
  - Get the touchscreen device name by running ```$ evtest```.
  - Copy the full device name and replace the existing value of ```touchdev``` variable in ```wall.py```.

## 2.3) Running the Digital Calendar and Photo frame

1. **Start the File Browser**
```
$ cd images
$ filebrowser -p 9090 &
$ cd ..
```
2. **Add Images**
  - On another computer/smartphone connected to the same WiFi network, open a web browser and navigate to ```<ip address of the board>:9090``` and start uploading images.
3. **Finally Run:**
```
$ python wall.py
```
or, to run in the background
```
$ python wall.py &
```
You should now see the calendar open up on you display, shorty followed by the images that keep changing. Once you touch the screen the images should disappear revealing the Calendar. The images will re-appear after a timeout of 10 seconds. 
