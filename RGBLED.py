from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, gree=10, blue=11)

led.red = 1
sleep(1)
led.red - 0.5
sleep(1)