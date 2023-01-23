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
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        self.org = Organizer(createListOfDummyParticipants(10))

        self.Toplabel = tk.Label(self, text="Participant Name:", font=LARGE_FONT)
        self.StatusLabel = tk.Label(self, text="Status:", font=LARGE_FONT)
        self.LAlabel = tk.Label(self, text="LA: 0 m/s^2", font=LARGE_FONT)

        self.Toplabel.grid(row=0, columnspan=2)
        self.StatusLabel.grid(row=1, columnspan=2)
        self.LAlabel.grid(row=2, columnspan=2, padx=10, pady=10)
        self.plot()
        #
        # button1 = ttk.Button(self, text="Graphs", command=quit)
        # button1.grid(row=1, sticky='nswe')

        reset_button = ttk.Button(self, text="Reset with New Participant", command=self.on_reset)
        button3 = ttk.Button(self, text="Exit", command=quit)

        reset_button.grid(row=4, column=0, sticky='nwse')
        button3.grid(row=4, column=1, sticky='nsew')

#############################################################
# BELOW IS ADDED FOR IN-CLASS DEMONSTRATION################
########################################################

        if not self.org.participantList:
            quit()
        self.Toplabel.config(text="Participant " + self.org.selected_participant.__str__())

    def plot(self):
        fig = Figure(figsize=(5, 5),
                     dpi=100)
        y = self.org.selected_participant.LA

        # adding the subplot
        plot1 = fig.add_subplot(111)
        # plotting the graph
        plot1.plot(y)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=3, columnspan=2, sticky="news")

    def on_reset(self):
        self.org.select_new_participant()
        self.refresh()

    def refresh(self):
        self.org.selected_participant.updateLA(dummyValues(1))
        cbool, status = areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)
        self.org.selected_participant.updateStatus(cbool, status)

        self.update_labels()
        self.plot()

        self.after(1000, self.refresh) # ask the mainloop to call this method again in 1,000 milliseconds

    def update_labels(self):
        self.Toplabel.config(text="Participant " + self.org.selected_participant.__str__())
        self.LAlabel.config(text="LA " + str(self.org.selected_participant.getlastLA()) + " m/s^2")
        self.StatusLabel.config(text="Status: " + str(self.org.selected_participant.status))




if __name__ == '__main__':

    app = Main()
    app.geometry("1280x720")
    app.mainloop()
