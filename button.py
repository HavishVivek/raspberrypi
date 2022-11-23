import RPi.GPIO as GPIO
import time

BUTTON_PIN = 13
slide = 22
led = 26
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(slide, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)


button_count = 0

try:
    #print("2")
    while True:
        if GPIO.input(13) == False:
            #print("3")
            button_count += 1
            print("button  count is")
            print(button_count)
            
            if GPIO.input(slide) == False:
                GPIO.output(26, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led, GPIO.LOW)
            
except KeyboardInterrupt:    
    GPIO.cleanup() 