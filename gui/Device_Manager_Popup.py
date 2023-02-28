import dummy
from Participants.Participant import Participant
from constants import *


class Device_Manager_Popup():
    def __init__(self, org, parent=0, startupbool=False):
        self.org = org
        self.parent = parent
        self.root = tk.Tk()
        self.root.geometry(popup_size)
        self.root.title("Device Manager")
        self.root.wm_attributes("-topmost", 2)

        self.startupbool = startupbool

        # Kills graph on manager startup to save performance
        self.org.visualize = False

        # Create Tkinter StringVar to store selected participant
        self.selected_participant_string = tk.StringVar()

        # Set default value for selected participant
        self.selected_participant_string.set(self.org.selected_participant)

        self.label = tk.Label(self.root, text="Select Participant to Configure")
        self.label.pack()

        # Create dropdown menu
        if self.org.participantList:
            dropdown = tk.OptionMenu(self.root, self.selected_participant_string, *self.org.participantList,
                                     command=lambda obj: on_select(obj))
            dropdown.pack()

        # Function to handle selection from dropdown menu
        def on_select(participant):
            EditConfigurationsPopup(self.root, self.org, participant)


        def on_add():
            EditConfigurationsPopup_AddParticipant(parent=self.root, organizer=self.org)

        self.add_button = tk.Button(self.root, text="Add Participant", command=on_add)
        self.add_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if self.parent:
            self.parent.refresh_from_device_manager()
        self.org.visualize = True
        self.root.destroy()
        if self.startupbool:
            self.org.create_gui()


class EditConfigurationsPopup:
    def __init__(self, parent, organizer, participant, device_properties=0):
        self.parent = parent
        self.org = organizer
        self.participant = participant
        self.device_properties = str(device_properties)
        self.popup = tk.Toplevel(parent)
        self.popup.geometry(popup_size)
        self.popup.title(self.participant.name)
        self.popup.wm_attributes("-topmost", 1)

        # Create labels and entries for participant info
        # .insert => creates filled-in default values

        tk.Label(self.popup, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.popup)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, self.participant.name)

        tk.Label(self.popup, text="Age:").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.popup)
        self.age_entry.grid(row=2, column=1)
        self.age_entry.insert(0, self.participant.age)

        tk.Label(self.popup, text="Sex:").grid(row=1, column=0)
        self.sex_entry = tk.Entry(self.popup)
        self.sex_entry.grid(row=1, column=1)
        self.sex_entry.insert(0, self.participant.sex)

        tk.Label(self.popup, text="Height:").grid(row=3, column=0)
        self.height_entry = tk.Entry(self.popup)
        self.height_entry.grid(row=3, column=1)
        self.height_entry.insert(0, self.participant.height)

        tk.Label(self.popup, text="Weight:").grid(row=4, column=0)
        self.weight_entry = tk.Entry(self.popup)
        self.weight_entry.grid(row=4, column=1)
        self.weight_entry.insert(0, self.participant.weight)

        self.divider = tk.Label(self.popup, text="")
        self.divider.grid(row=5, column=1)

        # Create labels and entries for device properties
        tk.Label(self.popup, text="\nDevice ID:").grid(row=5, column=0)
        self.port_entry = tk.Entry(self.popup)
        self.port_entry.grid(row=6, column=1)
        self.port_entry.insert(0, self.participant.device_id)

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

        # TODO: need a check for saving device ID to make sure that device ID isnt being used

        self.org.update_participant_by_ID(self.participant.id, self.name_entry.get(),
                                          self.age_entry.get(),
                                          self.sex_entry.get(),
                                          self.height_entry.get(),
                                          self.weight_entry.get(),
                                          self.port_entry.get())

        #
        # # Update device properties with value from entry
        # self.device_properties["port"] = self.port_entry.get()

        # Close popup
        self.popup.destroy()


    def cancel(self):
        # Close popup
        self.popup.destroy()

class EditConfigurationsPopup_AddParticipant:
    def __init__(self, parent, organizer, device_properties=0):
        self.org = organizer
        self.participant = Participant()
        self.device_properties = str(device_properties)
        self.popup = tk.Toplevel(parent)
        self.popup.geometry(popup_size)
        self.popup.title("Add Participant")
        self.popup.wm_attributes("-topmost", 1)

        # Create labels and entries for participant info
        # .insert => creates filled-in default values

        tk.Label(self.popup, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.popup)
        self.name_entry.grid(row=0, column=1)
        # self.name_entry.insert(0, self.participant.name)

        tk.Label(self.popup, text="Age:").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.popup)
        self.age_entry.grid(row=2, column=1)
        # self.age_entry.insert(0, self.participant.age)

        # tk.Label(self.popup, text="Sex:").grid(row=1, column=0)
        # self.sex_entry = tk.Entry(self.popup)
        # self.sex_entry.grid(row=1, column=1)
        # # self.sex_entry.insert(0, self.participant.sex)

        tk.Label(self.popup, text="Height:").grid(row=3, column=0)
        self.height_entry = tk.Entry(self.popup)
        self.height_entry.grid(row=3, column=1)
        # self.height_entry.insert(0, self.participant.height)

        tk.Label(self.popup, text="Weight:").grid(row=4, column=0)
        self.weight_entry = tk.Entry(self.popup)
        self.weight_entry.grid(row=4, column=1)
        # self.weight_entry.insert(0, self.participant.weight)

        self.divider = tk.Label(self.popup, text="")
        self.divider.grid(row=5, column=1)

        # Create labels and entries for device properties
        tk.Label(self.popup, text="\nDevice ID:").grid(row=5, column=0)
        self.port_entry = tk.Entry(self.popup)
        self.port_entry.grid(row=6, column=1)
        # self.port_entry.insert(0, "device_properties")

        # Create buttons for save and cancel
        save_button = tk.Button(self.popup, text="Save", command=self.save)
        save_button.grid(row=7, column=0)

        random_button = tk.Button(self.popup, text="Random", command=self.save_random)
        random_button.grid(row=7, column=1)

        cancel_button = tk.Button(self.popup, text="Cancel", command=self.cancel)
        cancel_button.grid(row=7, column=2)

    def save(self):
        """
        TODO: this function needs to update the organizer participant in question with
        all updated values
        :return:
        """
        self.participant.populate(
            name= self.name_entry.get(),
            age= self.age_entry.get(),
            # sex= self.sex_entry.get(),
            height= self.height_entry.get(),
            weight= self.weight_entry.get(),
            device_id= self.port_entry.get()
        )

        self.org.participantList.append(self.participant)

        #
        # # Update device properties with value from entry
        # self.device_properties["port"] = self.port_entry.get()

        # Close popup
        self.popup.destroy()

    def save_random(self):
        self.org.participantList.append(dummy.randomDummy())
        self.popup.destroy()

    def cancel(self):
        # Close popup
        self.popup.destroy()
