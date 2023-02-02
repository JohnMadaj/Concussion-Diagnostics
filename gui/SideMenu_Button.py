import tkinter.tix

from constants import *


class SideMenu_Button(tk.Button):
    def __init__(self, parent, participant):
        self.participant = participant
        tk.Button.__init__(self, parent, text=participant.name,
                           # font=self.font4,
                           foreground="white",
                           # image=self.button_accent,
                           compound=tk.CENTER,
                           background=str(participant.status)[7:],
                           activebackground='#4444ff',
                           # command=self.on_sidemenu_button_press))
                           command=self.on_press)
    def on_press(self):
        print(self.participant.name)
