import numpy as np
import matplotlib.pyplot as plt
from constants import *


class Figure:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.LA = 0

        # Add x and y to lists
        self.xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        # fig2.xs = self.fig.xs
        # self.fig.ys.append(LA)
        self.ys.append(np.random.normal(60, 20))
        # fig2.ys.append(np.random.normal(1800, 1000))

        # Limit x and y lists to 20 items
        self.xs = self.xs[-20:]
        self.ys = self.ys[-20:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        # fig2.ax.clear()
        # fig2.ax.plot(fig2.xs, fig2.ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('LA')
        plt.ylabel(LA_UNIT)

        self.runLoop()

    def setLA(self, LA):
        self.LA = LA

    def runLoop(self):
        def animate(i, xs, ys):
            # Add x and y to lists
            self.xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
            # fig2.xs = self.xs
            # self.ys.append(LA)
            self.ys.append(np.random.normal(60, 20))
            # fig2.ys.append(np.random.normal(1800, 1000))

            # Limit x and y lists to 20 items
            self.xs = self.xs[-20:]
            self.ys = self.ys[-20:]

            # Draw x and y lists
            self.ax.clear()
            self.ax.plot(self.xs, self.ys)

            # fig2.ax.clear()
            # fig2.ax.plot(fig2.xs, fig2.ys)

            # Format plot
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('LA')
            plt.ylabel(LA_UNIT)

        ani = animation.FuncAnimation(self.fig, animate, fargs=(self.xs, self.ys), interval=20)

        plt.show()

if __name__ == "__main__":
    Figure()




