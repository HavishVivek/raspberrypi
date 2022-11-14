from gpiozero import Servo, Button
from time import sleep

servo = Servo(17)
bnt = Button(13)

while True:
    servo.min()
    sleep(2)
    bnt.wait_for_press()
    servo.max()
    sleep(2)
    bnt.wait_for_press()
    print(servo)
    