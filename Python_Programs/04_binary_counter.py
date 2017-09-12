# import library for delay
import time

# import library for GPIO
import RPi.GPIO as GPIO

# use board mode instead of BCM mode
GPIO.setmode(GPIO.BOARD)

# variable for LED
led1  = 22
led2  = 15
led3  = 16
led4  = 18

x = 10

# make LED pins output
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

for i in range (0, x):
        
	binNum = bin(i) + "0000"
	
	onevar = int(binNum[5])
	twovar = int(binNum[4])
	threevar = int(binNum[3])
        fourvar = int(binNum[2])

        if (onevar != None):
		GPIO.output(led1, onevar)

        if (twovar != None):
        	GPIO.output(led2, twovar)
        
	if (threevar != None):
		GPIO.output(led3, threevar)
        
	if (fourvar != None):
		GPIO.output(led4, fourvar)
        
        print i 
	print binNum

	# sleep for 1 second
	time.sleep(1)	

# leave program clean
GPIO.cleanup()
