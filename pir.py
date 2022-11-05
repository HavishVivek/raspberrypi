from gpiozero import LED
from gpiozero import MotionSensor

led = LED(17)
pir = MotionSensor(26)
led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    led.on()
    pir.wait_for_no_motion()
    led.off()
    print("Motion Stopped")