import time

from servo import SERVO_CONTROL
import accel

accel.init()
SERVO_CONTROL.x.set(0)

STEP = 0.01
POS_PERIOD = 5
POSITIONS = [135, 45, 90]

ticks = 0
desired_angle_index = 0
desired_angle = POSITIONS[desired_angle_index]

while True:
    if ticks > POS_PERIOD / STEP:
        desired_angle_index = desired_angle_index + 1
        if desired_angle_index >= len(POSITIONS):
            desired_angle_index = 0
        desired_angle = POSITIONS[desired_angle_index]
        ticks = 0

    angle = accel.read_angle()
    diff = - desired_angle + angle
    print("angle: {}, diff: {}".format(angle, diff))
    SERVO_CONTROL.x.set(diff)
    time.sleep(STEP)
    ticks = ticks + 1
