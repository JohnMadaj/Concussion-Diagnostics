from Participants.Participant import Participant
from gui.gui import GUI


class Organizer:

    def __init__(self, participantList):
        self.participantList = participantList
        if len(self.participantList):
            self.selected_participant = participantList[0]
        else:
            self.selected_participant = Participant("Empty Slot", 0, 0, 0, 0)
        self.selected_index = 0

        # experimental code###
        self.gui = GUI(self)

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
        self.gui.p_panel.update_labels()

    def get_selected_index(self):
        return self.selected_index

    def __str__(self):
        prstr = ""
        for part in self.participantList:
            prstr = prstr + part.__str__() + "\n"
        return prstr