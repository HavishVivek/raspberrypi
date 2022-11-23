from RPi import GPIO
from gpiozero import MotionSensor, LED

from keypad import inputs, output


def libary():
    from gpiozero import LED,MotionSensor
    import RPi.GPIO as GPIO
    from time import sleep


libary()
 
def PinVariables():
     led = LED(26)
     pir = MotionSensor(4)
     inputs = [12,25,24,23]
     output = [16,20,21]
     
PinVariables()


def setup():
    GPIO.setup(inputs,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(output,GPIO.OUT)


setup()    


def keypad():
    r1 = ['1', '2', '3']
    r2 = ['4', '5', '6']
    r3 = ['7', '8', '9']
    r4 = ['*', '0', '#']


keypad()
