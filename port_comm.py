import serial

with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = 'COM1'
    ser.open()
    ser.write(b'hello')

