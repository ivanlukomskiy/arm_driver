import time

from servo import SERVO_CONTROL
import accel

accel.init()
SERVO_CONTROL.x.set(0)

desired_angle = 90

SERVO_CONTROL.x.set(10)
time.sleep(0.3)
SERVO_CONTROL.x.set(0)


while True:
    print(accel.read_angle())
    time.sleep(1)
