import tkinter.tix

from constants import *


class SideMenu_Button(tk.Button):
    def __init__(self, parent, participant, index, gui):
        self.font4 = font.Font(family="Arial", size=18,weight="bold")
        self.index = index
        self.parent = parent
        self.participant = participant
        self.gui = gui
        tk.Button.__init__(self, parent, text=participant.name,
                           font=self.font4,
                           foreground="white",
                           image=self.parent.button_accent,
                           compound=tk.CENTER,
                           background=str(participant.status)[7:],
                           activebackground='#4444ff',
                           command=self.on_press)
    def on_press(self):
        self.parent.org.select_new_participant(self.index)
        if not self.parent.org.Active_Mode:
            self.gui.refresh()
        # print(self.participant.name)
