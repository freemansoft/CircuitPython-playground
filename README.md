# CircuitPython-playground

## VS Code settings
1. `ctrl-shift-p` to bring up preferneces
1. Search for `editor.trim`
1. Uncheck `editor: Trim Auto Whitespace` in preferences

## TODO
* Bring the esp32 version of the 5110 program up to date with the Pico version

## 5110 Display
Python code that should works on different devices. Save the programs under the name `code.py` to auto run on save

* `5110_ip_address_demo_esp32c3.py` lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits after joining to a network
* `5110_ip_address_demo_pico.py`    lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits

Behavior described at https://joe.blog.freemansoft.com/2023/01/shrinking-ip-address-to-fit-on-pcd8544.html https://github.com/freemansoft/CircuitPython-playground/blob/main/5110_ip_address_demo.py

## Accelerometer

`lib/adafruit_l3gd20.py` is a cloned copy of the official driver and has been updated to recognize the L3G4200D device identifier.  It is required in /lib for the MCP demo.

## Blinka Setup
Host Python Setup
```bash
# setting up windows environment for Blinka
pip3 install hidapi
pip3 install adafruit-blinka
```

## MCP2221
Thse programs are intended to run from Blinka on a PC (Windows or Mac) using an MCP2221 as a prot expander.

*Mandatory Configuration*
Environment configuration that must be done before running host Python `python3`
* Linux `set BLINKA_MCP2221=1`
* Powershell `$env:BLINKA_MCP2221=1`

Run `python3` on the PC to bring up the REPL and then paste the the rest of the .py file

`mcp2221-usb-enumeration-output.json` contains the output from the USB HID library enumeration for the `MCP2221`.  The file only contains the MCP2221 record. Everything else has been removed

### Adafruit I2C 16x2 LCD
Assumes
* Code is running on a laptop communicating with the MCP2221 breakout board via CircuitPython and Blinka

**Setup**
```bash
# app specific libraries
pip3 install adafruit-circuitpython-charlcd
```
Verify env by running or pasting `blinka_mcp222_env_check.py`
Run or open a python3 REPL and paste the contents of `mcp2221_lcd16x2.py`

### L3GD4200D via hacked adafruit_L3GD20I driver
Assumes
* Code is running on a laptop or desktop communicating with the accelerometer via a MCP2221 breakout board.
* Using an L3G4200D or one of the L3GD20 accelerometer on I2C
* Have installed the correct libraries from above

**Setup**
```bash
# app specific libraries
# pip3 install ?? what library is needed
```

Run or open a python3 REPL and paste the contents of `mcp2221_L3GD4200D.py`

## RP2040 running U2IF - Never got displays to work

**I never got any of the displays to work correclty with the u2if firmware**

These programs are intended to run from Blinka on a PC (Windows or Mac) using a RP2040 Pico as a port expander.  The RP2040 should be running [u2if firmware](https://github.com/execuc/u2if).

Thse programs are intended to run from Blinka on a PC (Windows or Mac)

*Mandatory Configuration*
Environment configuration that must be done before running host Python `python3`
* Linux `set BLINKA_U2IF=1`
* Powershell `$env:BLINKA_U2IF=1`

Run `python3` on the PC to bring up the REPL and then paste the the rest of the .py file

### SPI OLED
Verify the environment by running or pasting `blinka_u2if_env_check.py`

**BROKEN: Does not display correctly** I think it is because of the way the Adafruit redirects the REPL

**Setup**
```bash
# app specific libraries
pip3 install adafruit-blinka-displayio

#pip3 install adafruit-circuitpython-terminalio
pip3 install adafruit-circuitpython-displayio-sh1106
pip3 install adafruit-circuitpython-display-text
```

### Noki1 5110 PCD8544
Verify the environment by running or pasting `blinka_u2if_env_check.py`

**BROKEN: Displays nothing**

See the setup instructions in the pico demo file



