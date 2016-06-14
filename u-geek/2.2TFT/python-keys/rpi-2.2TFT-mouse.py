""" rpi-2.2TFT-mouse.py by ukonline2000 2015.12.08
GPIO mouse driver for Raspberry Pi 2.2TFT for use with 5 Buttons
requires uinput kernel module (sudo modprobe uinput)
requires python-uinput (git clone https://github.com/tuomasjjrasanen/python-uinput)
requires python RPi.GPIO (from http://pypi.python.org/pypi/RPi.GPIO/)
Steps:

1.Install the python lib
$sudo apt-get update
$sudo apt-get install libudev-dev
$sudo apt-get install python-pip
$sudo pip install rpi.gpio
$sudo pip install python-uinput

2. Perform the command
$sudo modprobe uinput

3. Perform the demo python program
$sudo python rpi-2.2TFT-mouse.py
"""

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Up, Down, left, right, BTN_LEFT, BTN_RIGHT
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #X Button for GPIO5
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Trigon Button for GPIO24
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Square Button for GPIO22
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Circle Button for GPIO23
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #L Button for GPIO17
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #R Button for GPIO4											

events = (uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT, uinput.BTN_RIGHT)

device = uinput.Device(events)

# Bools to keep track of movement
BTN_LEFT = False
BTN_RIGHT = False
up = False
down = False
left = False
right = False


while True:
        i=10

	# mouse Y up
        if (not up) and (not GPIO.input(23)):
                while (not up and (not GPIO.input(23))):                      
                        device.emit(uinput.REL_Y, -i)
                        i+=5
                        time.sleep(.2)
                up = True
        if up and GPIO.input(23):
                up = False
                device.emit(uinput.REL_Y, 0)

	# mouse Y down
        if (not down) and (not GPIO.input(22)):
                while (not down and (not GPIO.input(22))):
                        device.emit(uinput.REL_Y, i)
                        i+=5
                        time.sleep(.2)
                down = True
        if down and GPIO.input(22):
                down = False
                device.emit(uinput.REL_Y, 0)

	# mouse X left
        if (not left) and (not GPIO.input(24)):
                while (not left and (not GPIO.input(24))):
                        device.emit(uinput.REL_X, -i)
                        i+=5
                        time.sleep(.2)
                left = True
        if left and GPIO.input(24):
                left = False
                device.emit(uinput.REL_X, 0)

	# mouse X right
        if (not right) and (not GPIO.input(5)):
                while (not right and (not GPIO.input(5))):
                        device.emit(uinput.REL_X, i)
                        i+=5
                        time.sleep(.2)
                right = True
        if right and GPIO.input(5):
                right = False
                device.emit(uinput.REL_X, 0)
	# mouse BTN

        if (not BTN_LEFT) and (not GPIO.input(17)):  # mouse BTN_LEFT pressed
                BTN_LEFT = True
                device.emit(uinput.BTN_LEFT, 1)
        if BTN_LEFT and GPIO.input(17):              # mouse BTN_LEFT released
                BTN_LEFT = False
                device.emit(uinput.BTN_LEFT, 0)
        if (not BTN_RIGHT) and (not GPIO.input(4)):  # mouse BTN_LEFT pressed
                BTN_RIGHT = True
                device.emit(uinput.BTN_RIGHT, 1)
        if BTN_RIGHT and GPIO.input(4):              # mouse BTN_LEFT released
                BTN_RIGHT = False
                device.emit(uinput.BTN_RIGHT, 0)

        time.sleep(.02)  # Poll every 20ms (otherwise CPU load gets too high)