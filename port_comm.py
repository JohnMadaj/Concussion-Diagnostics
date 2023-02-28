import math

import serial
from constants import *
#
# with serial.Serial() as ser:
#     ser.baudrate = 115200
#     ser.port = 'COM1'
#     ser.open()
#     ser.write(b'hello')


def recieve_data(id):
    try:
        while arduinoData.inWaiting() == 0:
            pass
        datapacket = str(arduinoData.readline(), 'utf-8')
        datapacket = three_way_vector_magnitude(datapacket)
        return datapacket
    except Exception as e:
        pass


def three_way_vector_magnitude(datapacket):
    splitpacket = datapacket.split(',')

    x = float(splitpacket[0])
    y = float(splitpacket[1])
    z = float(splitpacket[2])

    return math.sqrt(x * x + y * y + z * z)
