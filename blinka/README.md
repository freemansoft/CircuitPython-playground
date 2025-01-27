# Blinka on a PC

These programs run on a Mac or PC and remotely control peripheral sensors, motors and displays using the following as breakout boards.

* RP2040 running the U2IF firmware.
* Adafruit MCP2221A breakout
* Adafrut FTD232 breakout boards

Board selection is via environment variables

## MCP2221 note

The MCP2221 can act as an extension of the PC or Mac.  The MCP2221 breakout board doesn't support on device software.

## I2C Connection Notes

Pico I2C pins require pullups for PiHat LCD. Most of the breakout boards come with resistors installed. The Raspberry Pi comes with resistors for its I2C pins.  This means that boards designed to sit directly on the Raspberry Pi may not have resisotrs and this require them when used with something like the Pico. I used 1.8K resistors

Rasperry Pi Pico U2IF pinout. The Pico U2IF has 2 I2C ports

## Blinka environment variablesvalues

| Shell      | MCP2221 Env Configuration | U2IF Env Configuration |
| ---------- | ------------------------- | ---------------------- |
| Linux      | `set MCP2221=1`           | `export BLINKA_U2IF=1` |
| Powershell | `$env:MCP2221=1`          | `$env:BLINKA_U2IF=1`   |

## Assigned Pico RP2040  I2C pins with U2IF

| function                | Pico Functon | Pico Pin |
| ----------------------- | ------------ | -------- |
| SDA0 - I2C port 0 data  | GP4 Pico     | pin 6    |
| SCL0 - I2C port 0 clock | GP5 Pico     | pin 7    |
| SDA1 - I2C port 1 data  | GP14 Pico    | pin 19   |
| SCL1 - I2C port 1 clock | GP15 Pico    | pin 20   |

## Jupyter Notebook

Install with `python3 -m pip install jupyter`
Install ipympl with `python3 -m pip install ipympl`
Launch with `jupyter lab`