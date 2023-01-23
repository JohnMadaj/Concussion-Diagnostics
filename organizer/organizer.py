from Participants.Participant import Participant


class Organizer:

    def __init__(self, participantList):
        self.participantList = participantList
        if len(self.participantList):
            self.selected_participant = participantList[0]
        else:
            self.selected_participant = 0

    def select_new_participant(self, index):
        self.selected_participant = self.participantList[index]

    def get_selected_index(self):
        return self.participantList[self.selected_participant]

    def __str__(self):
        prstr = ""
        for part in self.participantList:
            prstr = prstr + part.__str__() + "\n"
        return prstr
