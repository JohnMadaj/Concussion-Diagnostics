
from gui.gui import GUI
from constants import *


class Organizer:

    def __init__(self, participantList):
        self.participantList = participantList
        self.visualize = True

        if len(self.participantList):
            self.selected_participant = participantList[0]
        else:
            self.selected_participant = None
        self.selected_index = 0

    def create_gui(self):
        self.gui = GUI(self)

    def recieve_data(self):
        # TODO: however the data is transmitted from receiver to organizer
        # assumes id: la: bool_digit
        try:
            # while arduinoData.inWaiting() == 0:
            #     pass
            # datapacket = str(arduinoData.readline(), 'utf-8')
            datapacket = "2: 20.32: 1"
            datapacket = datapacket.split(': ')
            device_id = int(datapacket[0])
            concussbool = not not int(datapacket[2])
            data = [float(datapacket[1]), concussbool]
            print(data)
            self.give_data_by_device_id(int(device_id), data)
        except Exception as e:
            print(e)

    def give_data_by_device_id(self, device_id, data):
        for participant in self.participantList:
            if participant.device_id == device_id:
                participant.updateLA(data[0])
                participant.updateStatus(data[1],
                                         self.getStatus(data[1]/participant.LAThreshold))

    def getStatus(self, ratio):
        if ratio >= red_intensity:
            return Status(2)
        elif ratio >= yellow_intensity:
            return Status(1)
        return Status(0)


    # @TODO: This function is SLOW because it loops through list
    # @TODO: I am almost positive the answer is that participant list should be a dict
    def get_participant_from_ID(self, id):
        for participant in self.participantList:
            if participant.id == id:
                return participant

    def update_participant_by_ID(self, id, name, age, sex, height, weight, device_id):
        for participant in self.participantList:
            if participant.id == id:
                participant.name = name
                participant.age = age
                participant.sex = sex
                participant.height = height
                participant.weight = weight
                participant.device_id = device_id
                return


    def select_new_participant(self, index=None):
        if index is not None:
            self.selected_participant = self.participantList[index]
            self.selected_index = index

        elif self.selected_index == (len(self.participantList) - 1):
            self.selected_participant = self.participantList[0]
            self.selected_index = 0
        else:
            self.selected_index += 1
            self.selected_participant = self.participantList[self.selected_index]
        # try:
        #     # self.gui.p_panel.update_labels()
        #     pass
        # except Exception as e:
        #     print(e)

    def get_selected_index(self):
        return self.selected_index

    def __str__(self):
        prstr = ""
        for part in self.participantList:
            prstr = prstr + part.__str__() + "\n"
        return prstr

    def on_closing(self):
        print(closing_string)
        quit()