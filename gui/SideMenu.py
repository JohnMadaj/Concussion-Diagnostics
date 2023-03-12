from constants import *
from gui.SideMenu_Button import SideMenu_Button


class SideMenu(tk.Frame):
    def __init__(self, parent, controller, gui, organizer):
        self.button_accent = tk.PhotoImage(file=button_accent_path)

        self.org = organizer  # organizer class
        self.gui = gui # the GUI class
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
    # def rebuild(self):
    #     for i, participant in enumerate(self.org.participantList):


    def make_button(self, index, participant):
        self.sidemenu_list[index] = SideMenu_Button(self, participant, index, gui=self.gui)
        self.sidemenu_list[index].grid(columnspan=1, sticky="nswe")

    def fill_sidemenu(self):
        self.sidemenu_list = {}
        for i, participant in enumerate(self.org.participantList):
            self.make_button(i, participant)

    # def manage_buttons(self):
    #     # if len(self.sidemenu_list) != len(self.org.participantList):
    #     #     self.rebuild()
    #     # for i, participant in enumerate(self.org.participantList):
    #     #     self.sidemenu_list[i] = participant
    #     for i, button in enumerate(self.org.participantList):
    #         button.grid_forget()
    #         button.destroy()
    #     self.fill_sidemenu()


    def refresh(self):
        # self.fill_sidemenu()
        for i, button in self.sidemenu_list.items():
            # print(str(button.participant.status))
            if button.participant.concussed:
                self.sidemenu_list[i].config(background="red")
            else:
                s = str(button.participant.status)[7:]
                self.sidemenu_list[i].config(background=s)

        self.after(TIME_CONSTANT, self.refresh)

