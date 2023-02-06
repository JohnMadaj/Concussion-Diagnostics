from constants import *
from gui.SideMenu_Button import SideMenu_Button


class SideMenu(tk.Frame):
    def __init__(self, parent, controller, master, organizer):
        self.button_accent = tk.PhotoImage(file=button_accent_path)

        self.org = organizer  # organizer class
        self.master = master  # the TK window
        self.parent = parent  # the frame being added to
        self.controller = controller

        tk.Frame.__init__(self, parent)


        self.sidemenu_list = {}
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.running = False
        self.fill_sidemenu()
        # self.create_scrollbar()

        self.v = tk.Scrollbar(self)
        self.v.grid(column=1,rowspan=10)
        # self.yscrollcommand = self.v.set
        # self.v.config(command=self.yview)

    def fill_sidemenu(self):
        for i, participant in enumerate(self.org.participantList):
            # photo = PhotoImage(file=logo_path)

            # self.sidemenu_list.append()
            self.sidemenu_list[i] = SideMenu_Button(self, participant, i)
            self.sidemenu_list[i].grid(columnspan=1, sticky="nswe")

    def refresh(self):
        for i, button in self.sidemenu_list.items():
            # print(str(button.participant.status))
            s = str(button.participant.status)[7:]
            self.sidemenu_list[i].config(background=s)

            if s == "RED":
                move_button = self.sidemenu_list[i]
                self.sidemenu_list[i] = self.sidemenu_list[1]
                self.sidemenu_list[1] = move_button

        self.after(TIME_CONSTANT, self.refresh)

    # def create_scrollbar(self):
    #     v = tk.Scrollbar(self)
    #     v.config(command=self.yview)

