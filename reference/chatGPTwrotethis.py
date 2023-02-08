import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time


class AnimatedGraph:
    def __init__(self, master, frame, row, column):
        self.master = master
        self.frame = frame
        self.figure = plt.Figure(figsize=(2, 2), dpi=40)
        self.ax = self.figure.add_subplot(111)
        self.x = []
        self.y = []
        self.row = row
        self.column = column
        self.counter = 0
        self.start_time = time.time()

    def animate(self, i):
        self.counter += 1
        self.x.append(time.time() - self.start_time)
        self.x = self.x[:20]
        self.y.append(random.randint(0, 100))

        self.ax.clear()
        self.ax.set_xlabel('Time (seconds)')
        self.ax.set_ylabel('LA')
        self.ax.plot(self.x, self.y[-20:])

    def plot(self):
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=self.row, column=self.column)

        self.ani = animation.FuncAnimation(self.figure, self.animate, interval=50)
        plt.show()


if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.columnconfigure(0)
    frame.columnconfigure(1)
    frame.columnconfigure(2)
    frame.rowconfigure(0)
    frame.rowconfigure(1)
    frame.grid()
    for _ in range(3):
        AnimatedGraph(root, frame, _, 0).plot()
        AnimatedGraph(root, frame, _, 1).plot()


    root.mainloop()
