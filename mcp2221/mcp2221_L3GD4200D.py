# WARNING
#   This relies on the hacked adafruit L3GD20 library included in this project.
#   The only change is an additional valid hardware id for the older L3GD4200
#   Note that you get the local if you import and not the one that doesn't work for the L3GD4200
#
# setting up windows environment
# pip3 install hdapi
# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-l3gd20
# The adafruit library is overwritten by the local file with the same name
#
# MANDATORY
#   Linux set BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# python3 to bring up the REPL and then paste the the rest of the file
#
# https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/python-circuitpython#
#
# Assumes SDA and SCL are the only things hooked up

import os
import board
import hid
import adafruit_l3gd20
import time

# verify should = 1
try:
    os.environ["BLINKA_MCP2221"]
    print("BLINKA_MCP2221 set correctly.  Well Done!")
except ValueError:
    print("**** ABORT! BLINKA_MCP2221 not set")
    exit
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
device.open(0x04D8, 0x00DD)

# Modify this if you have a different sized Character LCD
# Initialise I2C bus.
i2c = board.I2C()
# i2c.scan()
start_connect = time.perf_counter()
# L3G4200D dies hear with bad chip id
# L3G4200D id=0xd3 L3GD20 id=0xd4 L3GD20H id=0xd7
# Parallax L3G4200D board is at address 105 0x69
gyro = adafruit_l3gd20.L3GD20_I2C(i2c, address=105)
end_connect = time.perf_counter()
print("conect time: " + str(end_connect - start_connect))


run_count = 500
print("starting run [", run_count, "]... ")
pre_run = time.perf_counter()
for run_num in range(run_count):
    tosser = gyro.gyro

post_run = time.perf_counter()
print("take " + str(run_count) + " readings " + str(post_run - pre_run) + " secs")
# can be commented out
print("Snapshot of Angular Velocity (rad/s): {}".format(gyro.gyro))

print("ending run [", run_count, "]... ")

print("Exit repl to terminate")

while True:
    print("Angular Velocity (rad/s): {}".format(gyro.gyro))
    time.sleep(1)
