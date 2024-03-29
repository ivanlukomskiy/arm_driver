import time

from servo import SERVO_CONTROL
from simple_pid import PID
import accel

accel.init()
SERVO_CONTROL.x.set(0)

STEP = 0.001
POS_PERIOD = 5
LOG_TICKS = 500
POSITIONS = [0, 45, -45]

ticks = 0
desired_angle_index = 0
desired_angle = POSITIONS[desired_angle_index]

pid = PID(2, 0.2, 0, setpoint=0)


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
    diff = desired_angle - angle
    SERVO_CONTROL.x.set(desired_angle)
    time.sleep(STEP)

    # pid.setpoint = desired_angle
    # control = -pid(angle)
    # if control > 100:
    #     control = 100
    # if control < -100:
    #     control = -100
    # # print("control: {}, angle: {}, desired_angle: {}".format(control, angle, desired_angle))
    #
    if ticks % LOG_TICKS == 0:
        print("angle: {}, diff: {}, desired: {}".format(angle, diff, desired_angle))
    #
    # SERVO_CONTROL.x.set(control * 0.3)
    # time.sleep(STEP)
    # ticks = ticks + 1
