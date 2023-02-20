from Participants.Participant import Participant
from gui.gui import GUI


class Organizer:

    def __init__(self, participantList):
        self.participantList = participantList
        self.visualize = True

        if not participantList:
            quit()

        if len(self.participantList):
            self.selected_participant = participantList[0]
        else:
            self.selected_participant = Participant("Empty Slot", 0, 0, 0, 0)
        self.selected_index = 0

        self.gui = GUI(self)

    # @TODO: This function is SLOW because it loops through list
    # @TODO: I am almost positive the answer is that participant list should be a dict
    def get_participant_from_ID(self, id):
        for participant in self.participantList:
            if participant.id == id:
                return participant

    def update_participant_by_ID(self, id, name, age, sex, height, weight):
        for participant in self.participantList:
            if participant.id == id:
                participant.name = name
                participant.age = age
                participant.sex = sex
                participant.height = height
                participant.weight = weight
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