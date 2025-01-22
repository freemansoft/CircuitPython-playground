# Piod RP2040 running the custom U2IF firmware

These programs run on a Mac or PC and remotely control an RP2040 running the U2IF firmware.

These will probably work correctly with the Adafruit MCP2221A or FTD232 breakout boards with different env variables

## MCP2221 note

The MCP2221 can act as an extension of the PC or Mac.  The MCP2221 breakout board doesn't support on device software.

## Connections for I2C

Pico I2C pins require pullups for PiHat LCD.  I used 1.8K resistors

Pico U2IF pinout. The Pico U2IF has 2 I2C ports

Blinka environment variablesvalues

| Shell      | MCP2221 Env Command | U2IF Env Command     |
| ---------- | ------------------- | -------------------- |
| Linux      | `set MCP2221=1`     | `set BLINKA_U2IF=1`  |
| Powershell | `$env:MCP2221=1`    | `$env:BLINKA_U2IF=1` |

I2C pins with U2IF

| function                | Pico Functon | Pico Pin |
| ----------------------- | ------------ | -------- |
| SDA0 - I2C port 0 data  | GP4 Pico     | pin 6    |
| SCL0 - I2C port 0 clock | GP5 Pico     | pin 7    |
| SDA1 - I2C port 1 data  | GP14 Pico    | pin 19   |
| SCL1 - I2C port 1 clock | GP15 Pico    | pin 20   |
