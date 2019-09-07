import time

from servo import SERVO_CONTROL
import accel

accel.init()
SERVO_CONTROL.x.set(0)

desired_angle = 90

while True:
    angle = accel.read_angle()
    diff = desired_angle - angle
    SERVO_CONTROL.x.set(diff)
    time.sleep(0.05)
