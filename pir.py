from gpiozero import LED
from gpiozero import MotionSensor

led = LED(26)
pir = MotionSensor(4)
led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    led.on()
    pir.wait_for_no_motion()
    led.off()
    print("Motion Stopped")
    