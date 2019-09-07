import math

from smbus2 import SMBus
import time
import bitstring

BUS = 1
ADDRESS = 0x18  # I2C address of the accelerometer
CTRL_REG_1 = 0x20  # Basic settings register of LIS331DLH
# CTRL_REG_1_CONF = 0b00111001  # 1kHz refresh time; enable only X axis measurements
CTRL_REG_1_CONF = 0b01000001  # 0.5Hz


# Init accelerometer settings
def init():
    with SMBus(1) as bus:
        bus.write_byte_data(0x18, 0x20, 0b00111111)


def read_angle():
    with SMBus(1) as bus:
        # todo 1: read registers as blocks of data to make it faster
        # todo 2: use locks to avoid concurrency issues
        # todo 3: check is_ready register
        # todo 4: use more precise values (second component)
        # b1 = bus.read_byte_data(0x18, 0x27, 3)  # status register
        x = bus.read_byte_data(0x18, 0x29)
        y = bus.read_byte_data(0x18, 0x2B)

        x_val = float(bitstring.Bits(uint=x, length=8).unpack('int')[0])
        y_val = float(bitstring.Bits(uint=y, length=8).unpack('int')[0])
        angle = math.degrees(math.atan2(-y_val, x_val))
        # print("({}, {}) -> === {}".format(x_val, y_val, angle))
        return angle
