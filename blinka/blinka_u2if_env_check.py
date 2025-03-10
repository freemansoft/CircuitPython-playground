# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Simple board and env check hard coded to open an RP2040 Pico U2IF
#
# Setting up windows environment
# pip3 install hdapi
# pip3 install adafruit-blinka

# MANDATORY
#   Linux export BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# or
#   Linux export BLINKA_U2IF=1
#   Powershell $env:BLINKA_U2IF=1
#
# python3 to bring up the REPL and then paste the the rest of the file

import os

# verify "BLINKA_U2IF" set. Should = 1
try:
    os.environ["BLINKA_U2IF"]
    print("BLINKA_U2IF set correctly.  Well Done!")
except KeyError:
    print("**** ABORT! BLINKA_U2IF not set")
    exit
except ValueError:
    print("**** ABORT! BLINKA_U2IF not set")
    exit

import board
import hid

# a bunch of sanity checks
# PICO RP2040
# dir(board) returns the following
# [
#   'ADC0', 'ADC1',
#   'GP0',
#   'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19',
#   'GP2', 'GP20', 'GP21', 'GP22', 'GP26', 'GP27', 'GP28',
#   'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9',
#   'I2C',
#   'MISO', 'MISO0', 'MISO1', 'MOSI', 'MOSI0', 'MOSI1', 'SCK', 'SCK0', 'SCK1',
#   'SCL', 'SCL0', 'SCL1', 'SCLK', 'SCLK0', 'SCLK1', 'SDA', 'SDA0', 'SDA1',
#   'SPI',
#   '__blinka__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__repo__', '__spec__', '__version__',
#   'ap_board', 'board_id', 'detector', 'pin', 'sys'
#    ]
#
# KB2040
# [
#   'A0', 'A1', 'A2', 'A3',
#   'BUTTON',
#   'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
#   'I2C',
#   'MISO', 'MOSI',
#   'NEOPIXEL',
#   'RX',
#   'SCL', 'SCLK', 'SDA',
#   'SPI',
#   'TX',
#   '__blinka__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__repo__', '__spec__', '__version__',
#   'ap_board', 'board_id', 'detector', 'pin', 'sys'
#   ]
#
dir(o=board)
# prints the api for the board
help(board)

# Should really verify device
# This actually returns a list object
print(hid.enumerate())
device = hid.device()
# Open the device.  No error means we can talk to it
# the IDs for the Adafruit msp2221
# device.open(0x04D8, 0x00DD)
# the  IDs for the Pico with u2if firmware
device.open(0xCAFE, 0x4005)
print("We found the device if there was no error")
