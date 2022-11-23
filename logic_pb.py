import time,RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)

led = False
old_switch = False

try:
    while True:
        new_switch = GPIO.input(13)
        if new_switch == False and old_switch == False:
            led = not led
            time.sleep(0.2)
        GPIO.output(26, led)
        
        time.sleep(0.05)


except KeyboardInterrupt:
    GPIO.cleanup()