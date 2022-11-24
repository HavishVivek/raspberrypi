import time,random,RPi.GPIO as GPIO




def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)


setup()


def loop():
    
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26,GPIO.LOW)
    
    pwm_19 = GPIO.PWM(19,300)
    pwm_19.start(50)
    time.sleep(0.5)
    pwm_19.stop()


loop()

GPIO.cleanup()
    

