import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #setup for board instead of BCM

servoPin = 12 # set servo pin

GPIO.setup(servoPin, GPIO.OUT) # make servo pin output

# start PWM on servoPin at 50 Hz
pwm = GPIO.PWM(servoPin, 50)

# start PWM and set servo at duty cycle of (7)
pwm.start(7.5)

for i in range(0, 20):
        # ask user for input
	desiredPosition=input("Where do you want servo 0 - 180?: ")
	
        # set duty cycle
        DC = 1.0 / 18.0 * (desiredPosition) + 2
	
	# keep setting suty cycle
	pwm.ChangeDutyCycle(DC)


# stop PWM
pwm.stop()

# cleanup GPIO
GPIO.cleanup()


