from ON_RECIEVER.recieve_data import recieve_data

from gui.gui import GUI
from constants import *


class Organizer:

    def __init__(self, participantList):
        self.participantList = participantList
        self.participantDict = {p.id: p for p in self.participantList}

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
        # assumes dict format {id: [measurement, bool]}
        for device_id, data in recieve_data().items():
            # print(device_id, data)
            self.give_data_by_device_id(int(device_id), data)

    def give_data_by_device_id(self, device_id, data):
        # TODO: Need a fast access/match for device id from participant
        for participant in self.participantList:
            if participant.device_id == device_id:
                participant.updateLA(data[0])
                participant.updateStatus(data[1],
                                         self.getStatus(data[1] / participant.LAThreshold))

    def getStatus(self, ratio):
        if ratio >= red_intensity:
            return Status(2)
        elif ratio >= yellow_intensity:
            return Status(1)
        return Status(0)

    def add_participant(self, participant):
        self.participantList.append(participant)
        self.participantDict[participant.id] = participant


    def get_participant_from_ID(self, id):
        # for participant in self.participantList:
        #     if participant.id == id:
        #         return participant
        try:
            return self.participantDict[id]
        except Exception as e:
            raise e

    def update_participant_by_ID(self, id, name, age, sex, height, weight, device_id):
        # for participant in self.participantList:
        #     if participant.id == id:
        #         participant.name = name
        #         participant.age = age
        #         participant.sex = sex
        #         participant.height = height
        #         participant.weight = weight
        #         participant.device_id = device_id
        #         return
        try:
            self.participantDict[id].name = name
            self.participantDict[id].age = age
            self.participantDict[id].sex = sex
            self.participantDict[id].height = height
            self.participantDict[id].weight = weight
            self.participantDict[id].device_id = device_id
        except Exception as e:
            raise e

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
        for i in self.participantDict.values():
            print(i.concussed, i.LA)
        for i in self.participantList:
            print(i.concussed, i.LA)
        quit()
