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

#variable to ask user how many times to blink
blink_num = input("How many times do you want to blink? ")

for i in range (0, blink_num):
	
	# set LED pin high
	GPIO.output(redLed, True)

	# sleep for 1 second
	time.sleep(1)

	# set pin low
	GPIO.output(redLed, False)

	time.sleep(1)

# leave program clean
GPIO.cleanup()
