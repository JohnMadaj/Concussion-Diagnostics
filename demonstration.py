import serial
from gui.participant_panel import *


if __name__ == '__main__':
    app = Main()
    app.geometry("1280x720")
    app.mainloop()

    # while True:
    #     while arduinoData.inWaiting() == 0:
    #         pass
    #     datapacket = arduinoData.readline()
    #     datapacket = str(datapacket, 'utf-8')
    #     splitpacket = datapacket.split(',')
    #
    #     x = float(splitpacket[0])
    #     y = float(splitpacket[1])
    #     z = float(splitpacket[2])
    #
    #     print(x, y, z)