# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
#
# https://learn.adafruit.com/scanning-i2c-addresses/circuitpython
# CircuitPython I2C Device Address Scan
# Based on the above code
#
# MANDATORY
#   Linux export BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# or
#   Linux export BLINKA_U2IF=1
#   Powershell $env:BLINKA_U2IF=1

import time

import board
import busio

# List of potential I2C busses
# You should only scan busses with devices attached or it may scan forever
# Enable scanning only the bus you are using
# My I2C LCD was on bus 0
# My DeskPi PicoMate only has I2C on I2C1
#
# board.I2C() is the default I2C bus and is the same as board.I2C(0)
# The last last two entries represent the same bus
ALL_I2C = (
    "board.I2C()",
    # "board.STEMMA_I2C()",
    # "busio.I2C(board.SCL, board.SDA)",
    # "busio.I2C(board.SCL0, board.SDA0)",
    # "busio.I2C(board.SCL1, board.SDA1)",
    # "busio.I2C(board.GP15, board.GP14)",
)

# Determine which busses are valid
found_i2c = []
for name in ALL_I2C:
    try:
        print("Checking {}...".format(name), end="")
        bus = eval(name)
        bus.unlock()
        found_i2c.append((name, bus))
        print("ADDED.")
    except Exception as e:
        print("SKIPPED:", e)

# Scan of RP2040 sitting in a DeskPi PicoMate should show
# busio.I2C(board.GP15, board.GP14) addresses found: ['0x30', '0x44', '0x53', '0x6a']
#
# - 0x30 - magnamometer - MMC5603NJ
#           pip3 install adafruit-circuitpython-mmc56x3
#           https://learn.adafruit.com/adafruit-mmc5603-triple-axis-magnetometer/python-circuitpython
# - 0x44 - temp and humidity - SHT30-DIS
#          1pip3 install adafruit-circuitpython-sht30d
#           https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout/python-circuitpython
# - 0x53 - optical sensor - LTR-381RGB-01
# - 0x6a - 6 axis IMU - LSM6DS3TR-C
#           pip3 install adafruit-circuitpython-lsm6ds
#           https://learn.adafruit.com/adafruit-lsm6ds3tr-c-6-dof-accel-gyro-imu/python-circuitpython
#
# Scan valid busses
# Can't have any blank lines inside the indentation
# if you want to paste this into the REPL

if len(found_i2c):
    print("-" * 40)
    print("I2C SCAN")
    print("-" * 40)
    while True:
        for bus_info in found_i2c:
            name = bus_info[0]
            bus = bus_info[1]
            print(" Scanning", bus_info[0], bus_info[1])
            while not bus.try_lock():
                print("lock fail")
                pass
            print(
                name,
                "addresses found:",
                [hex(device_address) for device_address in bus.scan()],
            )
            bus.unlock()
        time.sleep(2)
else:
    print("No valid I2C bus found.")
