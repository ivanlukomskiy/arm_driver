import time

from servo import SERVO_CONTROL
from simple_pid import PID
import accel

accel.init()
SERVO_CONTROL.x.set(0)

STEP = 0.01
POS_PERIOD = 5
POSITIONS = [-45, 45, 0]

ticks = 0
desired_angle_index = 0
desired_angle = POSITIONS[desired_angle_index]

pid = PID(1, 0.1, 0.05, setpoint=1)


def transform(angle):
    if angle > 0:
        return angle - 90
    else:
        return angle + 270


while True:
    if ticks > POS_PERIOD / STEP:
        desired_angle_index = desired_angle_index + 1
        if desired_angle_index >= len(POSITIONS):
            desired_angle_index = 0
        desired_angle = POSITIONS[desired_angle_index]
        ticks = 0

    angle = transform(accel.read_angle())
    diff = - desired_angle + angle

    pid.setpoint = desired_angle
    control = pid(angle)
    print("control: {}, angle: {}, desired_angle: {}".format(control, angle, desired_angle))

    print("angle: {}, diff: {}".format(angle, diff))
    SERVO_CONTROL.x.set(-control * 0.2)
    time.sleep(STEP)
    ticks = ticks + 1
