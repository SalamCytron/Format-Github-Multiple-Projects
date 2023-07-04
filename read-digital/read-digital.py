"""
DESCRIPTION:
This example code used for Maker Pi Pico to display OLED.
This demo code is written in CircuitPython and it serves as an easy quality check when you first receive the board.

CONNECTIONS:
Maker Pi Pico : OLED Display
GP0           -  SDA	              
GP1           -  SCL	

AUTHOR   : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io

REFERENCE:
Code adapted from 2023 Liz Clark for Adafruit Industries:
https://learn.adafruit.com/pico-w-http-server-with-circuitpython/code-the-pico-w-http-server

MORE INFO:
https://cytron.io/p-robo-pico-simplifying-robotics-with-raspberry-pi-pico
https://circuitpython.org/board/raspberry_pi_pico
"""

import board
from analogio import AnalogIn
import busio as io
import adafruit_ssd1306

# define analog input pin 
analog_in = AnalogIn(board.GP27)

# helper function to calculate voltage from analog readings
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# initialize OLED
# I2C: SCL = GP1, SDA = GP0
# OLED: 128x64 pixels
i2c = io.I2C(board.GP1, board.GP0)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# program loop
while True:
	# clear all pixels
    oled.fill(0)
	
	# display analog value
	# text(string, x, y, color, *, font_name="font5x8.bin", size=1)
    oled.text('Analog value = ', 0, 0, 1)
    oled.text(str(analog_in.value), 90, 0, 1)
	
	# display voltage
    oled.text('Voltage = ', 0, 12, 1)
    oled.text(str(get_voltage(analog_in)), 60, 12, 1)
	
    # draw a rectangle based on analog value
	# fill_rect(x, y, width, height, color)
    oled.fill_rect(0, 30, (analog_in.value >> 9), 10, 1)

	# show on OLED
    oled.show()
