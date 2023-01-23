import serial

import tkinter as tk
from tkinter import ttk

from Diagnostic import areTheyConcussed
from organizer.organizer import Organizer
from dummy import *
from constants import *

LARGE_FONT = ("ariel", 20)


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.grid_columnconfigure(0, weight=1)  # as did this
        self.title("GUI")
        self.attributes('-fullscreen', True)

        closebtn = tk.Button(self, text="Close", command=quit)
        closebtn.grid(row=0, column=0)

        main_container = tk.Frame(self)
        main_container.grid(column=0, row=0, sticky="nsew")
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for fr in (MainPage,):
            frame = fr(main_container, self)
            self.frames[fr] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, pointer):
        frame = self.frames[pointer]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # uncommented these lines
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.Toplabel = tk.Label(self, text="Participant Name:", font=LARGE_FONT)
        self.LAlabel = tk.Label(self, text="LA: 0 m/s^2", font=LARGE_FONT)

        self.Toplabel.grid(row=0)
        self.LAlabel.grid(row=1, padx=10, pady=10)
        #
        # button1 = ttk.Button(self, text="Graphs", command=quit)
        # button1.grid(row=1, sticky='nswe')

        reset_button = ttk.Button(self, text="Reset", command=self.on_reset)
        reset_button.grid(row=2, sticky='nswe')

        button3 = ttk.Button(self, text="Exit", command=quit)
        button3.grid(row=3, sticky='nswe')

#############################################################
# BELOW IS ADDED FOR IN-CLASS DEMONSTRATION################
########################################################

        self.org = Organizer(createListOfDummyParticipants(10))
        if not self.org.participantList:
            quit()
        self.Toplabel.config(text="Participant " + self.org.selected_participant.__str__())

    def on_reset(self):
        # while not self.org.selected_participant.concussed:
        LA = dummyValues()
        self.LAlabel.config(text="LA " + str(LA) + " m/s^2")
        self.after(1000, self.on_reset) # ask the mainloop to call this method again in 1,000 milliseconds



if __name__ == '__main__':

    # org = Organizer(createListOfDummyParticipants(10))
    # if not org.participantList:
    #     quit()
    # print(org.__str__())
    #
    # LA = dummyValues()
    # temp_concussbool, temp_status = areTheyConcussed(LAthreshold=LA_GENERIC, LA=LA)
    # org.selected_participant.updateStatus(temp_concussbool, temp_status)
    #
    # print("LA: %f m/s^2" % LA, "STATUS:", temp_status)
    # print("\n")

    app = Main()
    app.geometry("1280x720")
    app.mainloop()
