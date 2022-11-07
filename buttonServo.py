import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11,70)

servo1.ChangeDutyCycle(0)

servo1.start(0)
print(" Wating for 2 seconds")
time.sleep(2)

print("Rotatong 180 degrees in 10 steps")

duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.3)
    duty = duty + 1
    print(duty)


time.sleep(2)

print("Turing back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(2)
print(duty)
print("Turning back to 0 degress")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

print(duty)

servo1.stop()
GPIO.cleanup()

print("program over")



