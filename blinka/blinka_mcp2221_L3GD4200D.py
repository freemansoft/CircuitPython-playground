# SPDX-FileCopyrightText: 2022 Joe Freeman joe@freemansoft.com
#
# SPDX-License-Identifier: MIT
#
# WARNING
#   This relies on the adafruit L3GD20 library hacked to include this chip ID
#   The only change is an additional valid hardware id for the older L3GD4200
#   You get the local if you import and not the one that doesn't work for the L3GD4200
#
# setting up windows environment
# pip3 install hdapi
# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-l3gd20
# The adafruit library is overwritten by the local file with the same name
#
# MANDATORY
#   Linux export BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# or
#   Linux export BLINKA_U2IF=1
#   Powershell $env:BLINKA_U2IF=1
#
# $env:BLINKA_U2IF=1
# python3 to bring up the REPL and then paste the the rest of the file
#
# https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/python-circuitpython#
#
# Assumes SDA and SCL are the only things hooked up

import time

import board

# Use the library version hacked to support this chip id
import lib.adafruit_l3gd20_hacked as adafruit_l3gd20

# Modify this if you have a different sized Character LCD
# Initialise I2C bus.
i2c = board.I2C()
# i2c.scan()
start_connect = time.perf_counter()
# L3G4200D dies here with bad chip id so we force address
# L3G4200D id=0xd3
# L3GD20   id=0xd4
# L3GD20H  id=0xd7
# L3G4200D (Parallax board) is at address 0x69 105 in decimal
gyro = adafruit_l3gd20.L3GD20_I2C(i2c, address=105)
end_connect = time.perf_counter()
print("connect time: " + str(end_connect - start_connect))

# warm up(?)
run_count = 500
print("starting run [", run_count, "]... ")
pre_run = time.perf_counter()
for run_num in range(run_count):
    tosser = gyro.gyro

post_run = time.perf_counter()
print(
    "take " + str(run_count) + " readings " + str(post_run - pre_run) + " secs"
)
# can be commented out
print(f"Snapshot of Angular Velocity (rad/s): {gyro.gyro_raw} - {gyro.gyro}")

print("ending run [", run_count, "]... ")

print("Exit repl to terminate")

while True:
    print(f"Angular Velocity (rad/s): {gyro.gyro_raw} - {gyro.gyro}")
    time.sleep(1)
