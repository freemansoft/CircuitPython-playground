# CircuitPython-playground

Some of these tools run in Circuit Python on the microcontroller.  Others of these tools run in Python on a PC or Mac and communicate with sensors via an intermediary.

## VS Code settings

1. `ctrl-shift-p` to bring up preferneces
1. Search for `editor.trim`
1. Uncheck `editor: Trim Auto Whitespace` in preferences

## TODO

* Bring the esp32 version of the 5110 program up to date with the Pico version

## 5110 Display ( pcd8544_5110_ip_address_demo_....py ) hooked to an esp32c3 or a pico

Python code that should works on different devices. Save the programs under the name `code.py` on the CircuitPython micro controller to auto run on save.

* `5110_ip_address_demo_esp32c3.py` lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits after joining to a network
* `5110_ip_address_demo_pico.py`    lists a machine's address on a 16x2 LCD compressing the ":" characters to ensure it fits

Behavior described at

* [Shrinking an IP address to fit on a pcd8544](https://joe.blog.freemansoft.com/2023/01/shrinking-ip-address-to-fit-on-pcd8544.html)
* [5110 LCD sample python program esp32c3 on Github](https://github.com/freemansoft/CircuitPython-playground/blob/main/pcd8544_5110_ip_address_demo_esp32c3.py)
* [5110 LCD sample python program Pico 2040 on Github](https://github.com/freemansoft/CircuitPython-playground/blob/main/pcd8544_5110_ip_address_demo_pico.py)

## Accelerometer attached to an MCP2221

`lib/adafruit_l3gd20.py` is a cloned copy of the official driver and has been updated to recognize the L3G4200D device identifier.  It is required in /lib for the MCP demo.

## Host Python / Blinka software installation for the MCP2221

Blinka is a set of CircuitPython libraries that lets you run CircuitPython on a laptop or desktop that communicates over a link to a CircuitPython device

Install the adafruit libraries on your host python environment.

```bash
# setting up windows environment for Blinka
pip3 install hidapi
pip3 install adafruit-blinka
```

If its been a while you may wish to update

```bash
# setting up windows environment for Blinka
pip3 install --upgrade hidapi
pip3 install --upgrade adafruit-blinka
```

## MCP2221 port expander

These python programs in `/mcp2221` programs are intended to run using Blinka on a PC (Windows or Mac) using an MCP2221 as a port expander.  The `mcp2221` can't be programmed everything is an HID command.

### Mandatory Configuration

Blinka must be configured to understand the target device. Adafruit Blinka Environment configuration that must be done before running host Python `python3`, before opening the REPL and pasting in the program.

* Linux `set BLINKA_MCP2221=1`
* Powershell `$env:BLINKA_MCP2221=1`

### Running a program

Run `python3` on the PC to bring up the REPL and then paste the the rest of the .py file

`mcp2221-usb-enumeration-output.json` contains the output from the USB HID library enumeration for the `MCP2221`.  The file only contains the MCP2221 record. Everything else has been removed

### Adafruit I2C 16x2 LCD

Assumes

* Code is running on a laptop communicating with the MCP2221 breakout board via CircuitPython and Blinka
* Wirking matches what is expected

#### Setup

We need to add the LCD driver to the python libraries we installed on the host in the previous step

```bash
pip3 install --upgrade hidapi
pip3 install --upgrade adafruit-blinka
# Device specific libraries
pip3 install adafruit-circuitpython-charlcd
```

Verify env by running or pasting `blinka_mcp222_env_check.py`
Run or open a python3 REPL and paste the contents of `mcp2221_lcd16x2.py`

### L3GD4200D via hacked adafruit_L3GD20I driver

This assumes

* Code is running on a laptop or desktop communicating with the accelerometer via a MCP2221 breakout board.
* Using an L3G4200D or one of the L3GD20 accelerometer on I2C
* Have installed the correct libraries from above

#### Setup for the the L3GD4200D

```bash
# app specific libraries
# pip3 install ?? what library is needed
```

Run or open a python3 REPL and paste the contents of `mcp2221_L3GD4200D.py`

## RP2040 running U2IF

These programs are intended to run from Blinka on a PC (Windows or Mac) using a RP2040 Pico as a port expander.  The RP2040 should be running [u2if firmware](https://github.com/execuc/u2if).

### Host software installation to communicate with the RP2040 U2IF

This is the same installation as the MCP2221 instructions above

```bash
# setting up windows environment for Blinka
pip3 install hidapi
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-charlcd
```


### RP2040 U2IF Mandatory Configuration

Environment configuration that must be done before running host Python `python3`

* Linux `set BLINKA_U2IF=1`
* Powershell `$env:BLINKA_U2IF=1`

Run `python3` on the PC to bring up the REPL and then paste the the rest of the .py file

### LCD 16X2 Pullup Resistors

The Pico does not come with the same I2C pin pullup resistors as the Raspberry Pi that my I2C LCD was designed for.  This means we need to add pullup resistors.  I added 1.8K resistors from the SDA/SCL pins to +5V to get the Pi Plate to work

### SPI OLED

Verify the environment by running or pasting `blinka_u2if_env_check.py`

**BROKEN: Does not display correctly** I think it is because of the way the Adafruit redirects the REPL

#### Setup for the OLED

```bash
# app specific libraries
pip3 install adafruit-blinka-displayio

#pip3 install adafruit-circuitpython-terminalio
pip3 install adafruit-circuitpython-displayio-sh1106
pip3 install adafruit-circuitpython-display-text
```

### Noki1 5110 PCD8544

Verify the environment by running or pasting `blinka_u2if_env_check.py`

**Displays nothing** This could be a pullup resistor issue also

See the setup instructions in the pico demo file
