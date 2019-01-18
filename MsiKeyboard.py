#! /usr/bin/env python3

import subprocess
import shlex
import colormap as colors
import re
import time
import traceback
import random
#from SmoothColors import SmoothColors
from colormath.color_objects import *
from colormath.color_conversions import convert_color
import pandas
import numpy

class MsiKeyboard:
    # Change SteelSeries MSI keyboards directly like windows through a C++ program.

    def wave(self, color_left, color_middle, color_right):
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb wave' % (color_left, color_middle, color_right)
        self.command_runner(command_line)

    def travel(self, color_previous, color_left):
        # Issues remain as when it runs through the method it resets to the next color instead of flowing to it.

        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb normal' % (color_previous, color_previous, color_previous)
        self.command_runner(command_line)
        time.sleep(0.05)
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb normal' % (color_left, color_previous, color_previous)
        self.command_runner(command_line)
        time.sleep(0.05)
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb normal' % (color_left, color_left, color_previous)
        self.command_runner(command_line)
        time.sleep(0.05)
        command_line = '/usr/local/bin/msiklm %s,%s,%s rgb normal' % (color_left, color_left, color_left)
        self.command_runner(command_line)
        time.sleep(0.05)


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

    def convert_rgb(self, rgb_value):
        html_hex_value = colors.rgb2hex(rgb_value[0], rgb_value[1], rgb_value[2], False)
        formatted_hex_value = html_hex_value.replace('#', '0x')
        return formatted_hex_value

    def rainbow(self):
        for hue in range(361):
            color_rgb_previous = self.convert_hsv_hue(max(0, hue - 1))
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(max(0, hue - 52))
            color_rgb_right = self.convert_hsv_hue(max(0, hue - 103))
            color_hex_previous = self.convert_rgb(color_rgb_previous)
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            #self.travel(color_hex_previous, color_hex_left)
            self.wave(color_hex_left, color_hex_middle, color_hex_right)
            #self.breathe(color_hex_left)
            #self.radiate(color_hex_middle, color_hex_left)
        for hue in range(361, 0):
            # improve the following check
            color_rgb_previous = self.convert_hsv_hue(min(360, hue + 1))
            color_rgb_left = self.convert_hsv_hue(hue)
            color_rgb_middle = self.convert_hsv_hue(hue)
            color_rgb_right = self.convert_hsv_hue(hue)
            color_hex_previous = self.convert_rgb(color_rgb_previous)
            color_hex_left = self.convert_rgb(color_rgb_left)
            color_hex_middle = self.convert_rgb(color_rgb_middle)
            color_hex_right = self.convert_rgb(color_rgb_right)
            #self.travel(color_hex_previous, color_hex_left)
            self.wave(color_hex_left, color_hex_middle, color_hex_right)
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

    # https://github.com/michalmonday/RGB_rainbowLoop/blob/master/RGB_rainbowLoop.py
    def rainbow2(self):
        for i in range(360):
            hue = i
            saturation = 1
            value = 1
            C = value * saturation
            X = C * (1 - abs((hue//60)%2 - 1))
            m = value - C
            sectionList = [
                [C, X, 0],
                [X, C, 0],
                [0, C, X],
                [0, X, C],
                [X, 0, C],
                [C, 0, X],
                ]
            section = sectionList[hue//60]
            rgb = [
                (section[0]+m)*255,
                (section[1]+m)*255,
                (section[2]+m)*255,
                ]

            #next_color = ''.join(map(str, rgb))
            #print(self.convert_rgb(rgb))
            color_hex = self.convert_rgb(rgb)
            self.normal(color_hex, color_hex, color_hex)

    # Added some work from
    # https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/color-advice/kindlmann/kindlmann.ipynb
    # to transverse a colormap with the use of DataFrame structures to color
    # the keyboard
    def safe_color(self, color):
        '''Given a color from the colormath.color_objects package,
        returns whether it is in the RGB color gamut and far enough
        away from the gamut border to be considered 'safe.' Colors
        right on the edge of displayable colors sometimes do not
        display quite right and also sometimes leave the color
        gamut when interpolated.'''
        rgb_color = convert_color(color, sRGBColor)
        rgb_vector = rgb_color.get_value_tuple()
        clamp_dist = 0.05*(numpy.max(rgb_vector) - numpy.min(rgb_vector))
        return ((rgb_color.rgb_r >= clamp_dist) and (rgb_color.rgb_r <= 1-clamp_dist) and
                (rgb_color.rgb_g >= clamp_dist) and (rgb_color.rgb_g <= 1-clamp_dist) and
                (rgb_color.rgb_b >= clamp_dist) and (rgb_color.rgb_b <= 1-clamp_dist))

    def scale_hue(self, hue, scalar):
        '''Given a hue value (in degrees) and a scalar value between
        0 and 1, create a color to have a luminance proportional to
        the scalar with the given hue. Returns an sRGBColor value.'''
        #Special cases
        if scalar <= 0:
            return sRGBColor(0, 0, 0)
        if scalar >= 1:
            return sRGBColor(1, 1, 1)

        hsv_original = HSVColor(hue, 1.0, 1.0)
        rgb_original = convert_color(hsv_original, sRGBColor)
        lab_original = convert_color(rgb_original, LabColor)
        l_target = 100.0*scalar
        a_original = lab_original.lab_a
        b_original = lab_original.lab_b

        high_scale = 1.0
        low_scale = 0.0
        for i in range(0, 12):
            mid_scale = (high_scale-low_scale)/2 + low_scale
            if self.safe_color(LabColor(l_target, mid_scale*a_original, mid_scale*b_original)):
                low_scale = mid_scale
            else:
                high_scale = mid_scale

        return convert_color(LabColor(l_target, low_scale*a_original, low_scale*b_original), sRGBColor)

    def build_kindlmann_colors(self):
        table = pandas.DataFrame()
        start_hue = 300.0
        end_hue = 0.0
        hue_array = numpy.linspace(start_hue, end_hue, 1024)
        table['hue'] = hue_array
        table['scalar'] = numpy.linspace(0.0, 1.0, table['hue'].size)
        # Use the scale_hue function on each row to get the color we
        # should use at each point.
        color_array = table.apply(lambda row: self.scale_hue(row['hue'], row['scalar']), axis=1)
        table['sRGBColor'] = color_array
        table['RGB'] = color_array.apply(lambda rgb: rgb.get_upscaled_value_tuple())
        table['sRGB'] = color_array.apply(lambda rgb: rgb.get_value_tuple())
        return table

    def unzip_rgb_triple(self, dataframe, column='RGB'):
        '''Given a dataframe and the name of a column holding an RGB triplet,
        this function creates new separate columns for the R, G, and B values
        with the same name as the original with '_r', '_g', and '_b' appended.'''
        # Creates a data frame with separate columns for the triples in the given column
        unzipped_rgb = pandas.DataFrame(dataframe[column].values.tolist(), columns=['r', 'g', 'b'])
        # Add the columns to the original data frame
        dataframe[column + '_r'] = unzipped_rgb['r']
        dataframe[column + '_g'] = unzipped_rgb['g']
        dataframe[column + '_b'] = unzipped_rgb['b']

    def rainbow3(self):
        colors_table = self.build_kindlmann_colors()
        self.unzip_rgb_triple(colors_table, 'RGB')
        for i in range (1024):
            rgb_value = [colors_table['RGB_r'][i], colors_table['RGB_g'][i], colors_table['RGB_b'][i]]
            #print(rgb_value)
            #print(self.convert_rgb(rgb_value))
            color_hex_left = self.convert_rgb(rgb_value)
            color_hex_middle = self.convert_rgb(rgb_value)
            color_hex_right = self.convert_rgb(rgb_value)
            #self.travel(color_hex_previous, color_hex_left)
            self.normal(color_hex_left, color_hex_middle, color_hex_right)

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
        wait_time = 1
        try:
            #sC = SmoothColors()
            while True:
                #list_of_colors = sC.color_next()
                #self.normal_wave(list_of_colors[0], list_of_colors[1], list_of_colors[2])
                #self.breathe(list_of_colors[0])
                #self.radiate(list_of_colors[0], list_of_colors[1])
                self.rainbow3()
                time.sleep(wait_time)
        except Exception as ex:
            print(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
