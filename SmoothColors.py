#! /usr/bin/env python3

from collections import deque

class SmoothColors:
    'Provide proper changes to color values in succession.'
    x = 0
    colors = deque(['0xff0000', '0xff00ff', '0x0000ff', '0x00ffff', '0x00ff00', '0xffff00'])
    #color_number = len(colors)

    def color_next(self):
        color_hex_value = SmoothColors.colors.popleft()
        SmoothColors.colors.append(color_hex_value)
        return [SmoothColors.colors[0], SmoothColors.colors[1], SmoothColors.colors[2]]
