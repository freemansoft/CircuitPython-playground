# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# Simple board and env check
# Extracted from other programs

import os

# verify should = 1
try:
    os.environ["BLINKA_U2IF"]
    print("BLINKA_MCP2221 set correctly.  Well Done!")
except KeyError:
    print("**** ABORT! BLINKA_U2IF not set")
    exit

import board
import busio
import board
import hid

# a bunch of sanity checks
# describe the board
# dir(board)
# prints the api for the board
# help(board)

# Should really verify device
# This actually returns a list object
print(hid.enumerate())
device = hid.device()
# Open the device.  No error means we can talk to it
# the IDs for the Adafruit msp2221
# device.open(0x04D8, 0x00DD)
# the  IDs for the Pico with u2if firmware
device.open(0xCAFE, 0x4005)
# Simple check to verify BLINKA environment and other stuff

import os
import hid

# verify should = 1
try:
    os.environ["BLINKA_U2IF"]
    print("BLINKA_MCP2221 set correctly.  Well Done!")
except KeyError:
    print("**** ABORT! BLINKA_U2IF not set")
    exit
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
# device.open(0x04D8, 0x00DD)
# the  IDs for the Pico with u2if firmware
device.open(0xCAFE, 0x4005)
print("We found the device if there was no error")
