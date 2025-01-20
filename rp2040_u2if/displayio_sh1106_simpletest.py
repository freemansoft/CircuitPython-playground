# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# Requires from the library bundle when running on the board
#   /lib/adafruit_displayio_sh1106.py
#   /lib/adafruit_display_text/*
# when running on a PC with Blinka
#   pip3 install adafruit-blinka
#   pip3 install adafruit_displayio_sh1106
#   pip3 install adafruit_display_text
#

import adafruit_displayio_sh1106
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label

print("starting")

displayio.release_displays()

# UART 1
OLED_RESET = board.GP20  # pin26
OLED_DC = board.GP16  # pin 21
OLED_CS = board.GP17  # pin 22
SCK = board.GP18  # pin 24
MOSI = board.GP19  # pin 25


spi = busio.SPI(SCK, MOSI)
display_bus = displayio.FourWire(
    spi,
    command=OLED_DC,
    chip_select=OLED_CS,
    reset=OLED_RESET,
    baudrate=1000000,
)

WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_sh1106.SH1106(
    display_bus, width=WIDTH, height=HEIGHT
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(
    color_bitmap, pixel_shader=color_palette, x=0, y=0
)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1
)
splash.append(text_area)
print("display done")


# while True:
#     pass
