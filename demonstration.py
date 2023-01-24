import serial
from gui.participant_panel import *

# arduinoData = serial.Serial("COM4", 115200, timeout=1)


if __name__ == '__main__':

    # while True:
    #     while (arduinoData.inWaiting() == 0):
    #         pass
    #     datapacket = arduinoData.readline()
    #     datapacket = str(datapacket, 'utf-8')
    #     print(datapacket)

    app = Main()
    app.geometry("1280x720")
    app.mainloop()

