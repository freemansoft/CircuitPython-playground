# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
"""
Libraries needed that must be copied to /lib
    adafruit_pcd8544.mpy
    adafruit_framebuf.mpy
Fonts that must be copied to the root or the same directory as the script
    font5x8.bin must be acquired from from https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/main/examples/font5x8.bin
See below for pin assignments
"""
import adafruit_pcd8544

import board
import busio
import digitalio
import time
import wifi
import ipaddress

print("Hello World!")

#  TODO do font size math to make this work on other displays
def display_ip_compressed(
    display, our_address, y_position, char_width=6, char_height=10
):
    """
    5x8 - font
    6x10 - pad one on the side and two on the bottom
    5 lines of text is 50 pixels or 48 vertical pixels because we don't need to pad the last row
    writes out an IP address replacing 6 pixels wide '.' character with 4p pixels wide 2x2 square
    Nokia display is 84x48 = 14 characters wide = 84 pixels
    An IP address can be 3*4+3 = 15 characters
    Each character is 6 (5+1) wide.  3 characters are 18 plus a dot is 24 wide
    Each character is 10 (8+2) tall
    """
    display.text("              ", 0, y_position, 1)  # erase the line
    display.rect(
        (char_width * 3) + (4 * 0) + 1, y_position + (char_height - 5), 2, 2, 1
    )
    display.rect(
        (char_width * 6) + (4 * 1) + 1, y_position + (char_height - 5), 2, 2, 1
    )
    display.rect(
        (char_width * 9) + (4 * 2) + 1, y_position + (char_height - 5), 2, 2, 1
    )

    if our_address:
        our_octets = str(our_address).split(".")
        display.text(our_octets[0], (char_width * 0) + (4 * 0), y_position, 1)
        display.text(our_octets[1], (char_width * 3) + (4 * 1), y_position, 1)
        display.text(our_octets[2], (char_width * 6) + (4 * 2), y_position, 1)
        display.text(our_octets[3], (char_width * 9) + (4 * 3), y_position, 1)

    display.show()


#################################################################
# ESP32-C3
# D0 is LED
# D1 not used
# D2 not used
# D3 not used
# D4 not used
# D5 = CE
# D6 = DC
# D8 = SCK = CLK
# D9 = RST
# D10 = MOSI = D In
#################################################################

# Show we're up using status light on D0
led = digitalio.DigitalInOut(board.D0)
led.direction = digitalio.Direction.OUTPUT
led.value = 0
for i in range(1, 4):
    led.value = not led.value
    time.sleep(0.1)
    led.value = not led.value
    time.sleep(0.1)

print("Available WiFi networks:")
for network in wifi.radio.start_scanning_networks():
    print(
        "\t%s\t\tRSSI: %d\tChannel: %d"
        % (str(network.ssid, "utf-8"), network.rssi, network.channel)
    )
wifi.radio.stop_scanning_networks()

# LCD setup
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)  # data/command
cs = digitalio.DigitalInOut(board.D5)  # Chip select
reset = digitalio.DigitalInOut(board.D9)  # reset
display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
display.contrast = 60
display.fill(0)

# compress the width needed by putting a blank space instead of "."
display.text("IP Address", 0, char_height * 0, 1)
# can be too wide for screen
our_address = wifi.radio.ipv4_address
print("IP Address: %s" % our_address)
display_ip_compressed(display, our_address, char_height * 1)
display.show()

ipv4 = ipaddress.ip_address("8.8.4.4")

while True:
    time.sleep(30)
    print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4) * 1000))
