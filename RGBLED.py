from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, gree=10, blue=11)

led.red = 1
sleep(1)
led.red - 0.5
sleep(1)

led.color = (0, 1, 0) # full color
sleep(1)
led.color = (1,0,1) # magenta
sleep(1)
led.color = (1,1,0) # yellow
sleep(1)
led.color = (0,1,1) # cyan
sleep(1)
led.color = (1,1,1) # whilte
sleep