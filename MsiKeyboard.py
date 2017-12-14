#! /usr/bin/env python3

import subprocess
import shlex
from colormap.colors import hsv2rgb
from colormap.colors import rgb2hex
import re
import time
from SmoothColors import SmoothColors

class MsiKeyboard:
    'Change SteelSeries MSI keyboards directly like windows through a C++ program.'
    def wave(self, color_left, color_middle, color_right):
        command_line = 'sudo /usr/local/bin/msiklm %s,%s,%s high wave' % (color_left, color_middle, color_right)
        run_line_array = shlex.split(command_line)
        subprocess.check_call(run_line_array)

    def normal_wave(self, color_left, color_middle, color_right):
        command_line = 'sudo /usr/local/bin/msiklm %s,%s,%s high normal' % (color_left, color_middle, color_right)
        run_line_array = shlex.split(command_line)
        subprocess.check_call(run_line_array)

    def breathe(self, color):
        command_line = 'sudo /usr/local/bin/msiklm %s high normal' % (color)
        run_line_array = shlex.split(command_line)
        subprocess.check_call(run_line_array)

    def radiate(self, color_in, color_out):
        command_line = 'sudo /usr/local/bin/msiklm %s,%s,%s high normal' % (color_out, color_in, color_out)
        run_line_array = shlex.split(command_line)
        subprocess.check_call(run_line_array)

    def convert_hsv_hue(self, hue_value):
        rgb_value = hsv2rgb(hue_value, 100, 100, False)
        return rgb_value

    def convert_hsv_saturation(self, saturation_value):
        rgb_value = hsv2rgb(0, saturation_value, 100, False)
        return rgb_value

    def convert_rgb(self, rgb_values):
        html_hex_value = rgb2hex(rgb_values[0], rgb_values[1], rgb_values[2], True)
        formatted_hex_value = html_hex_value.replace('#', '0x')
        return formatted_hex_value

    def rainbow(self):
        for hue in range(0, 360):
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(max(0, hue - 52))
            color_rgb_right = self.convert_hsv_hue(max(0, hue - 103))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal_wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        for hue in range(360, -1, -1):
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(max(0, hue - 52))
            color_rgb_right = self.convert_hsv_hue(max(0, hue - 103))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal_wave(color_hex_right, color_hex_middle, color_hex_left)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        for saturation in range(100, -1, -1):
            color_rgb_left = self.convert_hsv_saturation(saturation)
            color_rgb_middle = self.convert_hsv_saturation(max(0, saturation - 10))
            color_rgb_right = self.convert_hsv_saturation(max(0, saturation - 20))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal_wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        for saturation in range(0, 100):
            color_rgb_left = self.convert_hsv_saturation(saturation)
            color_rgb_middle = self.convert_hsv_saturation(max(0, saturation - 10))
            color_rgb_right = self.convert_hsv_saturation(max(0, saturation - 20))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal_wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)

    def smooth_flow(self):
        wait_time = 0.07
        try:
            sC = SmoothColors()
            while True:
                #list_of_colors = sC.color_next()
                #self.normal_wave(list_of_colors[0], list_of_colors[1], list_of_colors[2])
                #self.breathe(list_of_colors[0])
                #self.radiate(list_of_colors[0], list_of_colors[1])
                self.rainbow()
                time.sleep(wait_time)
        except:
            print('Bye')
