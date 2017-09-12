import RPi.GPIO as GPIO  # import GPIO library

GPIO.setmode(GPIO.BOARD) #set pin to use board pinout instead of BCM

# set LED to PWM  output pin
LED = 12

# setup PWM pin as output pin
GPIO.setup(LED, GPIO.OUT)

# create PWM object and give params of output pin at frequency
my_pwm=GPIO.PWM(LED, 100)

# start PWM at 0% duty cycle
my_pwm.start(0)

while(1):
        # ask user for duty cycle
	bright = input("Enter LED brightness (1- 6): ")
	my_pwm.ChangeDutyCycle(2**bright)

# stop PWM
my_pwm.stop()

# cleanup GPIO
GPIO.cleanup()

