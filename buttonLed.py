import time,RPi.GPIO as GPIO

button = 26
led = 13

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)
    
setup()
try:
    while True:
            if GPIO.input(button) == GPIO.LOW:
                print("test 1")
                GPIO.output(led,GPIO.HIGH)
            elif GPIO.input(button) == GPIO.HIGH:
                print("test 2")
                GPIO.output(led,GPIO.LOW)
                
                
except KeyboardInterrupt:
    GPIO.cleanup()
                
                
                
    