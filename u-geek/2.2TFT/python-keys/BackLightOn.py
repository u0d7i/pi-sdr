import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT) 


while True:
  GPIO.output(27,GPIO.HIGH)
  time.sleep(.04)
