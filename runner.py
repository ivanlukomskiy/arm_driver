import time

from servo import SERVO_CONTROL
import accel

accel.init()
SERVO_CONTROL.x.set(0)

while True:
    print('sleeping')
    accel.read_angle()
    time.sleep(1)
