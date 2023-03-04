# Libraries needed that must be copied to /lib
#     adafruit_pcd8533.mpy
#     adafruit_framebuf.mpy
# Fonts that must be copied to the root or the same directory as the script
#     font5x8.bin must be acquired from from https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/main/examples/font5x8.bin
#
# test program without the network portion
import adafruit_pcd8544

import board
import busio
import digitalio
import time

print("Hello World!")

# 5x8 - font
# 6x10 - pad one on the side and two on the bottom
# 5 lines of text is 50 pixels or 48 vertical pixels because we don't need to pad the last row
char_width = 6
char_height = 10
#  TODO do font size math to make this work on other displays
def display_ip_compressed(display, our_address, y_position):
    """
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
# Pico Pins - SPI0
# GP20 -              = RESET
# GP19 - SPI0 TX MOSI = D IN
# GP18 - SPI0 SCK     = CLK
# GP17 - SPI0 CSn     = CE
# GP16 - SPI0 RX      = DC

DISPLAY_RESET = board.GP20  # pin26
DISPLAY_DC = board.GP16  # pin 21
DISPLAY_CS = board.GP17  # pin 22
SCK = board.GP18  # pin 24
MOSI = board.GP19  # pin 25


#################################################################

# Show we're up using status light on LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = 0
for i in range(1, 4):
    led.value = not led.value
    time.sleep(0.1)
    led.value = not led.value
    time.sleep(0.1)

# LCD setup
spi = busio.SPI(SCK, MOSI=MOSI)
dc = digitalio.DigitalInOut(DISPLAY_DC)  # data/command
cs = digitalio.DigitalInOut(DISPLAY_CS)  # Chip select
reset = digitalio.DigitalInOut(DISPLAY_RESET)  # reset
display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
display.contrast = 60
display.fill(0)

# compress the width needed by putting a blank space instead of "."
display.text("IP Address", 0, char_height * 0, 1)
our_address = "192.168.100.101"
print("IP Address: %s" % our_address)
display_ip_compressed(display, our_address, char_height * 1)
display.text(str(our_address), 0, char_height * 2, 1)
display.show()
