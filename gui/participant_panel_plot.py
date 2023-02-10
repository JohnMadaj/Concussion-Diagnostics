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

class ParticipantPanel_Plot:
    def __init__(self, org, master, frame, row, column):
        self.org = org
        # self.master = master
        self.frame = frame
        self.row = row
        self.column = column
        fig = Figure(figsize=(5, 5),
                     dpi=100)
        # fig.set_animated(True)

        self.y = []

        # adding the subplot
        self.plot1 = fig.add_subplot(111)
        self.plot1.set_xlim(right=20)
        self.plot1.set_ylim(top=100)

        # plotting the graph
        self.plot1.plot(y)
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

        self.plot1.plot(self.y)
        self.plot1.set_xlim(right=20)
        self.plot1.set_ylim(top=100)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=self.row,
                                    column=self.column,
                                    sticky="news")
        # self.frame.after(TIME_CONSTANT, self.update())

# class AnimatedGraph:

#
# class ParticipantPanel_Plot:
#     def __init__(self, org, master, frame, row, column):
#         self.org = org
#         self.master = master
#         self.frame = frame
#         self.figure = plt.Figure(figsize=(5, 5), dpi=100)
#         self.ax = self.figure.add_subplot(111)
#         self.x = []
#         self.y = []
#         self.row = row
#         self.column = column
#         self.counter = 0
#         self.start_time = time.time()
#         canvas = FigureCanvasTkAgg(self.figure, self.frame)
#         canvas.draw()
#         canvas.get_tk_widget().grid(row=self.row, column=self.column)
#
#     def animate(self, i):
#         # self.counter += 1
#         # self.x.append(time.time() - self.start_time)
#         # self.x = self.x[:20]
#         # self.y.append(random.randint(0, 100))
#         # self.x = self.org.selected_participant.time
#         self.x = [i for i in range(20)]
#         self.y = self.org.selected_participant.LA
#
#         self.ax.clear()
#         self.ax.set_xlabel('Time (seconds)')
#         self.ax.set_ylabel('LA')
#         self.ax.plot(self.x, self.y)
#
#     def plot(self):
#         canvas = FigureCanvasTkAgg(self.figure, self.frame)
#         canvas.draw()
#         canvas.get_tk_widget().grid(row=self.row, column=self.column)
#
#         self.ani = animation.FuncAnimation(self.figure, self.animate, interval=50)
#         plt.show()


if __name__ == "__main__":
    t = tk.Tk()
    t.geometry("800x500")
    t.resizable(width=True, height=True)
    frame = tk.Frame(t)
    frame.rowconfigure(0)
    p = ParticipantPanel_Plot(frame, 0)
    frame.grid()
    tk.mainloop()