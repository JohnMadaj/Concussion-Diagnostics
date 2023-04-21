from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import tkinter as tk
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
from constants import *

import dummy

y = []


class ParticipantPanel_Plot_old:
    def __init__(self, org, master, frame, row, column):
        self.org = org
        # self.master = master
        self.frame = frame
        self.row = row
        self.column = column
        fig = Figure(figsize=(5, 5),
                     dpi=5)
        # fig.set_animated(True)

        self.y = []

        # adding the subplot
        self.plot1 = fig.add_subplot(111)
        self.plot1.set_xlim(right=20)
        self.plot1.set_ylim(top=100)

        # plotting the graph
        self.plot1.plot(y, linewidth=3)
        self.canvas = FigureCanvasTkAgg(fig,
                                        master=self.frame)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=row,
                                         columnspan=1,
                                         sticky="news")

    # def updateY(self):

    def refresh(self):
        self.plot1.clear()
        # self.y.append(self.org.selected_participant.graph_helper())

        self.y = self.org.selected_participant.graph_helper()

        self.plot1.plot(self.y, linewidth=8)
        # self.plot1.set_xlim(right=20)
        # self.plot1.set_ylim(top=100)
        self.canvas.draw()

        # self.canvas.get_tk_widget().grid(row=self.row,
        #                             column=self.column,
        #                             sticky="news")

        # self.frame.after(TIME_CONSTANT, self.update())


class ParticipantPanel_Plot:
    def __init__(self, org, master, frame, row, column):
        self.org = org
        self.frame = frame
        self.row = row
        self.column = column

        self.y = []
        self.canvas = tk.Canvas(master=self.frame, width=300, height=100, bg='white')
        self.canvas.grid(row=row, sticky="news")
        self.bar = self.canvas.create_rectangle(600,  # x0
                                                200,  # y0
                                                660,  # x1
                                                200,  # y1
                                                fill="blue")
        self.refresh()

    def refresh(self):
        acceleration = self.org.selected_participant.graph_helper()
        if type(acceleration) == list:
            acceleration = acceleration[-1]
        self.canvas.coords(self.bar, 600,
                           200 - acceleration,
                           660,
                           200)


if __name__ == "__main__":
    t = tk.Tk()
    t.geometry("800x500")
    t.resizable(width=True, height=True)
    frame = tk.Frame(t)
    frame.rowconfigure(0)
    p = ParticipantPanel_Plot(frame, 0)
    frame.grid()
    tk.mainloop()
