from ON_PD.transmit_data import tester


#
# with serial.Serial() as ser:
#     ser.baudrate = 115200
#     ser.port = 'COM1'
#     ser.open()
#     ser.write(b'hello')



def recieve_data():
    """
    :param id: Participant ID
    :return: Hashmap, key=ID, value=[measurement float, concussion bool]
    """
    data = {}
    # TODO: FOR ALL INCOMING DATA BY DEVICE ID
    try:
        # while arduinoData.inWaiting() == 0:
        #     pass
        # datapacket = str(arduinoData.readline(), 'utf-8')
        # TODO: recieve from PD
        datapacket = tester()
        datapacket = [float(datapacket[0]), bool(datapacket[1])]
        data[1] = datapacket #TODO: HARDCODED, KEY NEEDS TO BE DEVICE ID
        data[2] = [float(10), bool(False)]

    except Exception as e:
        pass
    return data

if __name__ == '__main__':
    print(recieve_data())
