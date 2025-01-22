# Derived from the adafruit_motor section of
# The linux code runs fine for the Pico U2IF because it is blinka code
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/pwm-outputs-servos
#
# Other links
# https://learn.adafruit.com/adafruit-io-basics-servo/python-code
#
# MANDATORY
#   Linux set BLINKA_MCP2221=1
#   Powershell $env:BLINKA_MCP2221=1
# or
#   Linux set BLINKA_U2IF=1
#   Powershell $env:BLINKA_U2IF=1
#
# Requires
#  pip3 install adafruit_circuitpython_motor
#
# Original copyright
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board
import pwmio
from adafruit_motor import servo

dir(o=board)

# create a PWMOut object on Pin D5.
pwm = pwmio.PWMOut(board.GP14, duty_cycle=2**15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP15, duty_cycle=2**15, frequency=50)

# Create a servo object.
servo1 = servo.Servo(pwm)
servo2 = servo.Servo(pwm2)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo1.angle = angle
        servo2.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        servo1.angle = angle
        servo2.angle = angle
        time.sleep(0.05)
