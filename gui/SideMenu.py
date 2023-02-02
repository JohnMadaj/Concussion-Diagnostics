from constants import *
from gui.SideMenu_Button import SideMenu_Button


class SideMenu(tk.Frame):
    def __init__(self, parent, controller, master, organizer):
        self.org = organizer  # organizer class
        self.master = master  # the TK window
        self.parent = parent  # the frame being added to
        tk.Frame.__init__(self, parent)

        self.sidemenu_list = []

        self.running = False
        self.fill_sidemenu()

    def fill_sidemenu(self):
        for i, participant in enumerate(self.org.participantList):
            # photo = PhotoImage(file=logo_path)

            self.sidemenu_list.append(SideMenu_Button(self, participant))
            self.sidemenu_list[-1].grid(column=0, sticky="nswe")
