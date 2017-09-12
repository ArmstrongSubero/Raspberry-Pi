from time import sleep  # time library for sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# assign button pins
button1 = 16
button2 = 18

# setup buttons as input
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

while(1):
    # if button1 pressed let user know
    if GPIO.input(button1) == 0:
	print "Button 1 was pressed"
        sleep(0.1)
	
    if GPIO.input(button2) == 0:
	print "Button 2 was pressed"

