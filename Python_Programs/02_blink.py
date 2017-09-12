# import library for delay
import time

# import library for GPIO
import RPi.GPIO as GPIO

# use board mode instead of BCM mode
GPIO.setmode(GPIO.BOARD)

# variable for LED
redLed = 22

# make LED pin an output pin
GPIO.setup(redLed, GPIO.OUT)

# set LED pin high
GPIO.output(redLed, True)

# sleep for 1 second
time.sleep(1)

# set pin low
GPIO.output(redLed, False)

time.sleep(1)

# set LED pin high
GPIO.output(redLed, True)

# sleep for 1 second
time.sleep(1)

# set pin low
GPIO.output(redLed, False)

time.sleep(1)

# leave program clean
GPIO.cleanup()
