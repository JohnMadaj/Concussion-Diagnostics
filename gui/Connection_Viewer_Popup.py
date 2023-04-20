from constants import *


class Connection_Viewer_Popup:
    def __init__(self, org, parent=0):
        self.org = org
        self.parent = parent
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Connections")
        self.root.wm_attributes("-topmost", 2)
        self.table = TableFrame(self.root, self.org)
        self.table.pack()


class TableFrame(tk.Frame):
    def __init__(self, master, org):
        super().__init__(master)
        self.num_rows = len(org.participantList)

        # Create the labels for the first row of the table
        participant_label = tk.Label(self, text="Participant", font=font2)
        device_id_label = tk.Label(self, text="Device ID", font=font2)
        device_status_label = tk.Label(self, text="Device Status", font=font2)

        # Add the labels to the grid
        participant_label.grid(row=0, column=0)
        device_id_label.grid(row=0, column=1)
        device_status_label.grid(row=0, column=2)

        # Add the input fields for the remaining rows of the table
        current_row = 1
        for p_id in org.participantDict.keys():
            d_id = org.device_id_connections[p_id]
            if d_id == 0:
                d_id = "(No Device)"
                status = "NA"
            else:
                # print("battery: ", str(org.participantDict[p_id].battery))
                status = str(org.participantDict[p_id].battery) + "%"

            tk.Label(self, text=org.participantDict[p_id].name).grid(row=current_row, column=0)
            tk.Label(self, text=d_id).grid(row=current_row, column=1)
            tk.Label(self, text=status).grid(row=current_row, column=2)
            current_row += 1
