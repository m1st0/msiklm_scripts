#! /usr/bin/env python3
#
# Change SteelSeries MSi keyboards directly like windows through a C++ program.

import subprocess
import shlex
from colormap.colors import hsv2rgb
from colormap.colors import rgb2hex
import re
import time

def wave(color_left, color_middle, color_right, seconds):
    command_line = '/usr/local/bin/msiklm %s,%s,%s high normal' % (color_left, color_middle, color_right)
    run_line_array = shlex.split(command_line)
    subprocess.check_call(run_line_array)

def convert_hsv_hue(hue_value):
    rgb_value = hsv2rgb(hue_value, 100, 100, False)
    return rgb_value

def convert_hsv_saturation(saturation_value):
    rgb_value = hsv2rgb(0, saturation_value, 100, False)
    return rgb_value

def convert_rgb(rgb_values):
    html_hex_value = rgb2hex(rgb_values[0], rgb_values[1], rgb_values[2], True)
    formatted_hex_value = html_hex_value.replace('#', '0x')
    return formatted_hex_value

def rainbow():
    wait_time = 0.01
    for hue in range(0, 360):
        color_rgb_left = convert_hsv_hue(hue)
        color_rgb_middle = convert_hsv_hue(max(0, hue - 52))
        color_rgb_right = convert_hsv_hue(max(0, hue - 103))
        color_hex_left = convert_rgb(color_rgb_left)
        color_hex_middle = convert_rgb(color_rgb_middle)
        color_hex_right = convert_rgb(color_rgb_right)
        wave(color_hex_left, color_hex_middle, color_hex_right, wait_time)
    for hue in range(360, -1, -1):
        color_rgb_left = convert_hsv_hue(hue)
        color_rgb_middle = convert_hsv_hue(max(0, hue - 52))
        color_rgb_right = convert_hsv_hue(max(0, hue - 103))
        color_hex_left = convert_rgb(color_rgb_left)
        color_hex_middle = convert_rgb(color_rgb_middle)
        color_hex_right = convert_rgb(color_rgb_right)
        wave(color_hex_left, color_hex_middle, color_hex_right, wait_time)
    for saturation in range(100, -1, -1):
        print(saturation)
        color_rgb_left = convert_hsv_saturation(saturation)
        color_rgb_middle = convert_hsv_saturation(max(0, saturation - 10))
        color_rgb_right = convert_hsv_saturation(max(0, saturation - 20))
        color_hex_left = convert_rgb(color_rgb_left)
        color_hex_middle = convert_rgb(color_rgb_middle)
        color_hex_right = convert_rgb(color_rgb_right)
        print(color_hex_left)
        wave(color_hex_left, color_hex_middle, color_hex_right, wait_time)
    for saturation in range(0, 100):
        print(saturation)
        color_rgb_left = convert_hsv_saturation(saturation)
        color_rgb_middle = convert_hsv_saturation(max(0, saturation - 10))
        color_rgb_right = convert_hsv_saturation(max(0, saturation - 20))
        color_hex_left = convert_rgb(color_rgb_left)
        color_hex_middle = convert_rgb(color_rgb_middle)
        color_hex_right = convert_rgb(color_rgb_right)
        print(color_hex_left)
        wave(color_hex_left, color_hex_middle, color_hex_right, wait_time)

while True:
    rainbow()
