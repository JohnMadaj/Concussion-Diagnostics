from constants import *
from gui.SideMenu_Button import SideMenu_Button


class SideMenu(tk.Frame):
    def __init__(self, parent, controller, master, organizer):
        self.button_accent = tk.PhotoImage(file=r"graphics\button_accent.png")

        self.org = organizer  # organizer class
        self.master = master  # the TK window
        self.parent = parent  # the frame being added to
        tk.Frame.__init__(self, parent)

        self.sidemenu_list = []
        self.columnconfigure(0)

        self.running = False
        self.fill_sidemenu()

    def fill_sidemenu(self):
        for i, participant in enumerate(self.org.participantList):
            # photo = PhotoImage(file=logo_path)

            self.sidemenu_list.append(SideMenu_Button(self, participant, i))
            self.sidemenu_list[-1].grid(columnspan=1, sticky="nswe")

    def refresh(self):
        # self.sidemenu_list[random.randint(0, 9)].config(bg="red")
        for i, participant in enumerate(self.org.participantList):
            self.sidemenu_list[i].config(background=str(participant.status)[7:])
        self.after(TIME_CONSTANT, self.refresh)
