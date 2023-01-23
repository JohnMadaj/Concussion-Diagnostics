import serial

arduinoData = serial.Serial("Port_#0001.Hub_#0001", 115200, timeout=1)

while True:
    while (arduinoData.inWaiting()==0):
        pass
    datapacket = arduinoData.readline()
    datapacket = str(datapacket, 'utf-8')
    print(datapacket)
