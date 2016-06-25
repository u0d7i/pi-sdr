#!/usr/bin/python

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# map gpio numbers to keys
key_circle = 23 # Circle Button GPIO23 - handled by kernel module
key_square = 22 # Square Button GPIO22
key_trigon = 24 # Trigon Button GPIO24
key_x      = 5  # X      Button GPIO5
key_up     = 17 # Up     Button GPIO17
key_down   = 4  # Down   Button GPIO4
key_led    = 27 # Screen Light  GPIO27


# FIXME via loop and single datastructure

GPIO.setmode(GPIO.BCM)
# buttons
GPIO.setup(key_square, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key_trigon, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key_x, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# screen backlit
GPIO.setup(key_led, GPIO.OUT, initial=GPIO.HIGH) # on by default

events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_ENTER, uinput.KEY_ESC)

device = uinput.Device(events)

status_up = False
status_down = False
status_enter = False
status_esc = False
status_led = False

while True:
  # Up
  if (not status_up) and (not GPIO.input(key_up)):        #  button pressed
    status_up = True
    device.emit(uinput.KEY_UP, 1)
    GPIO.output(key_led,GPIO.HIGH) # wake screen light
  if status_up and GPIO.input(key_up):                    # button released
    status_up = False
    device.emit(uinput.KEY_UP, 0)
  # Down
  if (not status_down) and (not GPIO.input(key_down)):    # button pressed
    status_down = True
    device.emit(uinput.KEY_DOWN, 1)
    GPIO.output(key_led,GPIO.HIGH) # wake screen light
  if status_down and GPIO.input(key_down):                # button released
    status_down = False
    device.emit(uinput.KEY_DOWN, 0)
  # Enter
  if (not status_enter) and (not GPIO.input(key_square)): # button pressed
    status_enter = True
    device.emit(uinput.KEY_ENTER, 1)
  if status_enter and GPIO.input(key_square):             # button released
    status_enter = False
    device.emit(uinput.KEY_ENTER, 0)
  # Escape
  if (not status_esc) and (not GPIO.input(key_trigon)):   # button pressed
    status_esc = True
    device.emit(uinput.KEY_ESC, 1)
  if status_esc and GPIO.input(key_trigon):               # button released
    status_esc = False
    device.emit(uinput.KEY_ESC, 0)
  # Screen Light
  if (not status_led) and (not GPIO.input(key_x)):        # button pressed
    status_led = True
    if GPIO.input(key_led):
      GPIO.output(key_led,GPIO.LOW)
    else:
      GPIO.output(key_led,GPIO.HIGH)
  if (status_led) and GPIO.input(key_x):                  # button released
    status_led = False
  time.sleep(.04)
