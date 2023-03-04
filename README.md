# CircuitPython-playground

## 5110 Display
Python code that should work on many different devices.

* `5110_ip_address_demo_esp32c3.py` lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits after joining to a network
* `5110_ip_address_demo_pico.py`    lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits

Behavior described at https://joe.blog.freemansoft.com/2023/01/shrinking-ip-address-to-fit-on-pcd8544.html https://github.com/freemansoft/CircuitPython-playground/blob/main/5110_ip_address_demo.py

## Accelerometer

`adafruit_l3gd20.py` is a cloned copy of the official driver and has been updated to recognize the L3G4200D device identifier.  It is required in /lib for the MCP demo.

## Blinka Setup
Host Python Setup
```bash
# setting up windows environment for Blinka
pip3 install hidapi
pip3 install adafruit-blinka
```

## MCP2221
Thse programs are intended to run from Blinka on a PC (Windows or Mac) using an MCP2221 as a prot expander

*Mandatory* environment configuration that must be done before running host Python
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

## RP2040 running U2IF
These programs are intended to run from Blinka on a PC (Windows or Mac) using a Pico with u2if firmware as a port expander

Thse programs are intended to run from Blinka on a PC (Windows or Mac)

*Mandatory* environment configuration that must be done before running host Python
* Linux `set BLINKA_U2IF=1`
* Powershell `$env:BLINKA_U2IF=1`

Run `python3` on the PC to bring up the REPL and then paste the the rest of the .py file

### SPI OLED
**THIS IS BROKEN and DOES NOT DISPLAY CORRECTLY**

### Setup
```bash
# app specific libraries
pip3 install adafruit-blinka-displayio

#pip3 install adafruit-circuitpython-terminalio
pip3 install adafruit-circuitpython-displayio-sh1106
pip3 install adafruit-circuitpython-display-text
```




