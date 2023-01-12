# setting up windows environment
# pip3 install hdapi
# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-charlcd
#
# MANDATORY
#   Linux set BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# python3 to bring up the REPL and then paste the the rest of the file
#
# https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/python-usage
# https://github.com/adafruit/Adafruit_CircuitPython_CharLCD
# https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi.pdf
# https://docs.circuitpython.org/projects/charlcd/en/latest/api.html
# https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout
#
# starting on the end near the edge of the board
# Pin 02 exterior line - 5v corner   outside edge
# Pin 04 exterior line - skip        outside edge
# Pin 06 exterior line - GND 3rd pin outside edge
# Pin 01 interior line corner - skip
# Pin 03 interior line SDA
# Pin 05 interior line SLC
import os
import board
import hid
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import time

# verify should = 1
try:
    os.environ["BLINKA_MCP2221"]
    print("BLINKA_MCP2221 set correctly.  Well Done!")
except ValueError:
    print("**** ABORT! BLINKA_MCP2221 not set")
    exit
# describe the board
# dir(board)
# prints the api for the board
# help(board)

# Should really verify device
# This actually returns a list object
print(hid.enumerate())
device = hid.device()
device.open(0x04D8, 0x00DD)

start_connect = time.perf_counter()
# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2
# Initialise I2C bus.
i2c = board.I2C()
start_connect = time.perf_counter()
# Point the driver at the bus / device
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
end_connect = time.perf_counter()
print("conect time: " + str(end_connect - start_connect))

# I have the RGB backlit Adafruit device
lcd.clear()
# Set LCD color to red
lcd.color = [100, 0, 0]
# Print two line message
start_hello = time.perf_counter()
lcd.message = "Hello\nCircuitPython"
end_hello = time.perf_counter()
print("draw hello time: " + str(end_hello - start_hello))
# make cursor blink
lcd.blink = True
lcd.clear()
lcd.blink = False
lcd.message = "Goodbye"
lcd.cursor_position(8, 1)
lcd.message = "over here"
lcd.home()
lcd.clear()
lcd.color = [0, 0, 0]

print("this is how you read the buttons")
# down_button, right_button, up_button, left_button, select_button
print(lcd.down_button)
