import RPi.GPIO as GPIO

import time
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

wait = random.randint(1,5)
time.sleep(wait)

GPIO.output(26,GPIO.HIGH)
timestart = time.time()

winner = 'NO'
 
while winner == 'No':
    if GPIO.input(20) == True:
        winner = 'player 1'
        
    if GPIO.input(21) == True:
        winner = 'player 2'
        
time_total = time.time() - timestart
time_total = "%.3f" % time_total

print(winner + ' wins!')
print('your reaction time was' + time_total + 'seconds')

GPIO.output(26, GPIO.LOW)
GPIO.cleanup()