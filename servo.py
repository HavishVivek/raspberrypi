from gpiozero import LED
from time import sleep

red = LED(26)

red.on()
sleep(1)
red.off()
sleep(1)