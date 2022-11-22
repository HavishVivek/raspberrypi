import RPi.GPIO as GPIO
import time

BUTTON_PIN = 13
slide = 22
led = 26
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(slide, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

print("1")

button_count = 0

try:
    print("2")
    while True:
        print("2.1")
        if GPIO.input(BUTTON_PIN) == False:
            print("3")
            button_count += 1
            print("button  count is ")
            print(button_count)
            
            if GPIO.input(slide) == False:
                GPIO.output(led, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led, GPIO.LOW)
            
except KeyboardInterrupt:    
    GPIO.cleanup() 