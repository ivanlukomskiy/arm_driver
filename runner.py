import time

from servo import SERVO_CONTROL
import accel

accel.init()
SERVO_CONTROL.x.set(0)

while True:
    print('sleeping')
    time.sleep(1)
