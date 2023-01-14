# CircuitPython-playground

## 5110 Display
* 5110_ip_address_demo.py
* https://joe.blog.freemansoft.com/2023/01/shrinking-ip-address-to-fit-on-pcd8544.html https://github.com/freemansoft/CircuitPython-playground/blob/main/5110_ip_address_demo.py

## MCP2221 Adafruit I2C 16x2 LCD
Assumes running on a laptop communicating with the MCP2221 breakout board via CircuitPython and Blinka

The enumeration json file shows the output from the USB HID library enumeration.  The file only contains the MCP2221 record. Everything else has been removed

## MCP2221 and L3GD4200D via hacked adafruit_L3GD20I driver
Assumes 
* Code is running on a laptop or desktop communicating with the accelerometer via a MCP2221 breakout board.
* Using an L3G4200D or one of the L3GD20 accelerometer on I2C
* Have installed the correct libraries from above

## Local library file
`adafruit_l3gd20.py` is a cloned copy of the official driver and has been to support the L3G4200D
