#! /usr/bin/env python3

import subprocess
import shlex
import colormap as colors
import re
import time
import traceback
import random
#from SmoothColors import SmoothColors

class MsiKeyboard:
    'Change SteelSeries MSI keyboards directly like windows through a C++ program.'
    def wave(self, color_left, color_middle, color_right):
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb wave' % (color_left, color_middle, color_right)
        self.command_runner(command_line)

    def normal(self, color_left, color_middle, color_right):
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb normal' % (color_left, color_middle, color_right)
        self.command_runner(command_line)

    def breathe(self, color):
        command_line = '/usr/local/bin/msiklm %s rgb breathe' % (color)
        self.command_runner(command_line)

    def breathe_colors(self, color_left, color_middle, color_right):
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb breathe' % (color_left, color_middle, color_right)
        self.command_runner(command_line)

    def radiate(self, color_in, color_out):
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb breathe' % (color_out, color_in, color_out)
        self.command_runner(command_line)

    def command_runner(self, command_in):
        run_line_array = shlex.split(command_in)
        subprocess.check_call(run_line_array)

    def convert_hsv_hue(self, hue_value):
        rgb_value = colors.hsv2rgb(hue_value, 100, 100, False)
        return rgb_value

    def convert_hsv_saturation(self, saturation_value):
        rgb_value = colors.hsv2rgb(0, saturation_value, 100, False)
        return rgb_value

    def convert_rgb(self, rgb_values):
        html_hex_value = colors.rgb2hex(rgb_values[0], rgb_values[1], rgb_values[2], True)
        formatted_hex_value = html_hex_value.replace('#', '0x')
        return formatted_hex_value

    def rainbow(self):
        for hue in range(361):
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(max(0, hue - 52))
            color_rgb_right = self.convert_hsv_hue(max(0, hue - 103))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal(color_hex_left, color_hex_middle, color_hex_right)
            #self.wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        for hue in reversed(range(360)):
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(max(0, hue - 52))
            color_rgb_right = self.convert_hsv_hue(max(0, hue - 103))
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            self.normal(color_hex_right, color_hex_middle, color_hex_left)
            #self.wave(color_hex_right, color_hex_middle, color_hex_left)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        #for saturation in range(100, -1, -1):
            #color_rgb_left = self.convert_hsv_saturation(saturation)
            #color_rgb_middle = self.convert_hsv_saturation(max(0, saturation - 10))
            #color_rgb_right = self.convert_hsv_saturation(max(0, saturation - 20))
            #color_hex_left = self.convert_rgb(color_rgb_left)
            #color_hex_middle = self.convert_rgb(color_rgb_middle)
            #color_hex_right = self.convert_rgb(color_rgb_right)
            #self.normal_wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        #for saturation in range(0, 100):
            #color_rgb_left = self.convert_hsv_saturation(saturation)
            #color_rgb_middle = self.convert_hsv_saturation(max(0, saturation - 10))
            #color_rgb_right = self.convert_hsv_saturation(max(0, saturation - 20))
            #color_hex_left = self.convert_rgb(color_rgb_left)
            #color_hex_middle = self.convert_rgb(color_rgb_middle)
            #color_hex_right = self.convert_rgb(color_rgb_right)
            #self.normal_wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)

    def random_wave(self):
        hue = random.randint(0, 361)
        hue2 = random.randint(0, 361)
        hue3 = random.randint(0, 361)
        color_rgb_left = self.convert_hsv_hue(hue)
        color_rgb_middle = self.convert_hsv_hue(hue2)
        color_rgb_right = self.convert_hsv_hue(hue3)
        color_hex_left = self.convert_rgb(color_rgb_left)
        color_hex_middle = self.convert_rgb(color_rgb_middle)
        color_hex_right = self.convert_rgb(color_rgb_right)
        try:
            self.wave(color_hex_left, color_hex_middle, color_hex_right)
        except Exception as ex:
            print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))

    def smooth_flow(self):
        wait_time = 0.07
        try:
            #sC = SmoothColors()
            while True:
                #list_of_colors = sC.color_next()
                #self.normal_wave(list_of_colors[0], list_of_colors[1], list_of_colors[2])
                #self.breathe(list_of_colors[0])
                #self.radiate(list_of_colors[0], list_of_colors[1])
                self.rainbow()
                time.sleep(wait_time)
        except Exception as ex:
            print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
