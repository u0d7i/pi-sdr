""" rpi-2.2TFT-jstk.py by ukonline2000 2015.12.08
GPIO Joystick driver for Raspberry Pi 2.2TFT for use with 5 Buttons
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
$sudo python rpi-2.2TFT-jstk.py


"""

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Up, Down, left, right, fire
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Trigon Button for GPIO24
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #X Button for GPIO5
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Circle Button for GPIO23
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Square Button for GPIO22
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #R Button for GPIO4
												  #L Button for GPIO17

events = (uinput.BTN_JOYSTICK, uinput.ABS_X + (0, 255, 0, 0), uinput.ABS_Y + (0, 255, 0, 0))

device = uinput.Device(events)

# Bools to keep track of movement
fire = False
up = False
down = False
left = False
right = False

# Center joystick
# syn=False to emit an "atomic" (128, 128) event.
device.emit(uinput.ABS_X, 128, syn=False)
device.emit(uinput.ABS_Y, 128)

while True:
  if (not fire) and (not GPIO.input(4)):  # Fire button pressed
    fire = True
    device.emit(uinput.BTN_JOYSTICK, 1)
  if fire and GPIO.input(4):              # Fire button released
    fire = False
    device.emit(uinput.BTN_JOYSTICK, 0) 
  if (not up) and (not GPIO.input(24)):   # Up button pressed
    up = True
    device.emit(uinput.ABS_Y, 0)          # Zero Y
  if up and GPIO.input(24):               # Up button released
    up = False
    device.emit(uinput.ABS_Y, 128)        # Center Y
  if (not down) and (not GPIO.input(5)): # Down button pressed
    down = True
    device.emit(uinput.ABS_Y, 255)        # Max Y
  if down and GPIO.input(5):             # Down button released
    down = False
    device.emit(uinput.ABS_Y, 128)        # Center Y
  if (not left) and (not GPIO.input(23)): # Left button pressed
    left = True
    device.emit(uinput.ABS_X, 0)          # Zero X
  if left and GPIO.input(23):             # Left button released
    left = False
    device.emit(uinput.ABS_X, 128)        # Center X
  if (not right) and (not GPIO.input(22)):# Right button pressed
    right = True
    device.emit(uinput.ABS_X, 255)        # Max X
  if right and GPIO.input(22):            # Right button released
    right = False
    device.emit(uinput.ABS_X, 128)        # Center X
  time.sleep(.02)  # Poll every 20ms (otherwise CPU load gets too high)
