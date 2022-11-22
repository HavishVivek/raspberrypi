import time,RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.OUT)



try:
    while True:
       if GPIO.input(22) == False and GPIO.input(13) == False:
           GPIO.output(26, GPIO.HIGH)
       elif GPIO.input(22) == False or GPIO.input(13) == False:
           GPIO.output(26, GPIO.HIGH)
           time.sleep(0.2)
           GPIO.output(26, GPIO.LOW)
           time.sleep(0.2)
       else:
          GPIO.output(26, GPIO.LOW)
       time.sleep(0.05)    


except KeyboardInterrupt:
    GPIO.cleanup()
