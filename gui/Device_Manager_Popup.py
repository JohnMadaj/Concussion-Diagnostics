from constants import *


class Device_Manager_Popup():
    def __init__(self, org):
        self.org = org
        self.root = tk.Tk()
        self.root.geometry("200x100")
        self.root.title("Device Manager")
        self.root.wm_attributes("-topmost", 2)

        # Kills graph on manager startup to save performance
        self.org.visualize = False

        # Create Tkinter StringVar to store selected participant
        self.selected_participant = tk.StringVar()

        # Set default value for selected participant
        self.selected_participant.set(self.org.selected_participant)

        self.label = tk.Label(self.root, text="Select Participant to Configure")
        self.label.pack()
        # Create dropdown menu
        dropdown = tk.OptionMenu(self.root, self.selected_participant, *self.org.participantList)
        dropdown.pack()

        # Function to handle selection from dropdown menu
        def on_select(participant):
            EditConfigurationsPopup(self.root, participant)

        # Bind on_select function to selected_participant variable
        self.selected_participant.trace("w", lambda name, index, mode,
                                        sv=self.selected_participant: on_select(sv.get()))

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.org.visualize = True
        self.root.destroy()


class EditConfigurationsPopup:
    def __init__(self, parent, participant, device_properties=0):
        self.parent = parent
        self.participant = participant
        self.device_properties = str(device_properties)
        self.popup = tk.Toplevel(parent)
        self.popup.geometry("300x300")
        self.popup.title(participant)
        self.popup.wm_attributes("-topmost", 1)


        # Create labels and entries for participant info
        tk.Label(self.popup, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.popup)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, "name")

        tk.Label(self.popup, text="Sex:").grid(row=1, column=0)
        self.sex_entry = tk.Entry(self.popup)
        self.sex_entry.grid(row=1, column=1)
        self.sex_entry.insert(0, "sex")

        tk.Label(self.popup, text="Age:").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.popup)
        self.age_entry.grid(row=2, column=1)
        self.age_entry.insert(0, "age")

        tk.Label(self.popup, text="Height:").grid(row=3, column=0)
        self.height_entry = tk.Entry(self.popup)
        self.height_entry.grid(row=3, column=1)
        self.height_entry.insert(0, "height")

        tk.Label(self.popup, text="Weight:").grid(row=4, column=0)
        self.weight_entry = tk.Entry(self.popup)
        self.weight_entry.grid(row=4, column=1)
        self.weight_entry.insert(0, "weight")

        self.divider = tk.Label(self.popup, text="")
        self.divider.grid(row=5, column=1)

        # Create labels and entries for device properties
        tk.Label(self.popup, text="\nPort Number:").grid(row=5, column=0)
        self.port_entry = tk.Entry(self.popup)
        self.port_entry.grid(row=6, column=1)
        self.port_entry.insert(0, "device_properties")

        # Create buttons for save and cancel
        save_button = tk.Button(self.popup, text="Save", command=self.save)
        save_button.grid(row=7, column=0)

        cancel_button = tk.Button(self.popup, text="Cancel", command=self.cancel)
        cancel_button.grid(row=7, column=1)

    def save(self):
        """
        TODO: this function needs to update the organizer participant in question with
        all updated values
        :return:
        """
        # # Update participant info with values from entries
        # self.participant["name"] = self.name_entry.get()
        # self.participant["sex"] = self.sex_entry.get()
        # self.participant["age"] = self.age_entry.get()
        # self.participant["height"] = self.height_entry.get()
        # self.participant["weight"] = self.weight_entry.get()
        #
        # # Update device properties with value from entry
        # self.device_properties["port"] = self.port_entry.get()

        # Close popup
        self.popup.destroy()

    def cancel(self):
        # Close popup
        self.popup.destroy()