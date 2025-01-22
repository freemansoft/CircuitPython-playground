# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Simple board and env check hard coded to open an RP2040 Pico U2IF
#
# Setting up windows environment
# pip3 install hdapi
# pip3 install adafruit-blinka
#
# MANDATORY
#   Linux set BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# or
#   Linux set BLINKA_U2IF=1
#   Powershell $env:BLINKA_U2IF=1
#
# python3 to bring up the REPL and then paste the the rest of the file
#
# https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/python-circuitpython#
#
# Assumes SDA and SCL are the only things hooked up


import os

# verify should = 1
try:
    os.environ["BLINKA_MCP2221"]
    print("BLINKA_MCP2221 set correctly.  Well Done!")
except KeyError:
    print("**** ABORT! BLINKA_MCP2221 not set")
    exit
except ValueError:
    print("**** ABORT! BLINKA_MCP2221 not set")
    exit

import board
import hid

# a bunch of sanity checks
# describe the board
dir(board)
# prints the api for the board
help(board)

# Should really verify device
# This actually returns a list object
print(hid.enumerate())
device = hid.device()
# Open the device.  No error means we can talk to it
# the IDs for the Adafruit msp2221
device.open(0x04D8, 0x00DD)
# the  IDs for the Pico with u2if firmware
# device.open(0xCAFE, 0x4005)
print("We found the device if there was no error")
