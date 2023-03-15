from dummy import dummyDataPacket
from gui.gui import GUI
from constants import *


class Organizer:

    def __init__(self, participantList):
        self.gui = GUI(self)
        self.participantList = participantList
        self.participantDict = {p.id: p
                                for p in self.participantList}
        self.device_id_connections = {p.id: p.device_id
                                      for p in self.participantList}

        self.visualize = True
        self.Active_Mode = False

        if len(self.participantList):
            self.selected_participant = participantList[0]
        else:
            self.selected_participant = None
        self.selected_index = 0

    def toggle_mode(self):
        self.gui.root.destroy()
        self.Active_Mode = not self.Active_Mode

    def create_gui(self):
        # self.gui = GUI(self)
        self.gui.startup()

    def receive_data(self):
        # TODO: however the data is transmitted from receiver to organizer
        # assumes n lines of id: la: bool_digit\n
        try:
            while arduinoData.inWaiting() == 0:
                pass
            datapacket = str(arduinoData.readline(), 'utf-8')
            # datapacket = "2: 20.32: 1"
            # datapacket = dummyDataPacket()

            def process_data(datapacket):
                datapacket = datapacket.split('\n')
                for message in datapacket:
                    print(message)
                    message = message.split(': ')
                    device_id = int(message[0])
                    concussbool = not not int(message[2])
                    data = [float(message[1]), concussbool]
                    self.give_data_by_device_id(int(device_id), data)
                # print("\n")
            process_data(datapacket)
        except Exception as e:
            print("organizer/receive_data error:", e)

    def give_data_by_device_id(self, device_id, data):
        # # TODO: Need a fast access/match for device id from participant
        for participant in self.participantList:
            if participant.device_id == device_id:
                participant.updateLA(data[0])
                participant.updateStatus(data[1], self.getStatus(data[0] / participant.LAThreshold))
        # if device_id not in self.device_id_connections.values():
        #     return
        # for id in self.device_id_connections:
        #     if self.device_id_connections[id] == device_id:
        #         p_id = id
        # print(p_id)
        # th = self.participantDict[p_id].LAThreshold
        # self.participantDict[p_id].updateLA(data[0])
        # self.participantDict[p_id].updateStatus(data[1], self.getStatus(data[1] / th))

    def getStatus(self, ratio):
        if ratio >= red_intensity:
            return Status(2)
        elif ratio >= yellow_intensity:
            return Status(1)
        return Status(0)

    def add_participant(self, participant):
        if participant.device_id in self.device_id_connections and participant.device_id !=0:
            return False
        self.participantList.append(participant)
        self.participantDict[participant.id] = participant
        self.device_id_connections[participant.id] = participant.device_id
        return True


    def get_participant_from_ID(self, id):
        try:
            return self.participantDict[id]
        except Exception as e:
            raise e

    def update_participant_by_ID(self, id, name, age, sex, height, weight, device_id):
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
        ####
        self.gui.root.destroy()
        while True:
            self.receive_data()

        print(closing_string)
        quit()

    def error_popup(self, error_msg):
        root = tk.Tk()
        root.wm_attributes("-topmost", 2)
        root.withdraw()
        messagebox.showerror("Error: ", error_msg)