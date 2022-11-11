"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
import random
import time
import numpy

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from constants import *
from Diagnostic import areTheyConcussed
from Participant import Participant
from window import *
from Figure import Figure


def runLoop(LA):
    def animate(i, xs, ys):
        # Add x and y to lists
        fig1.xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        # fig2.xs = fig1.xs
        # fig1.ys.append(LA)
        fig1.ys.append(np.random.normal(60, 20))
        # fig2.ys.append(np.random.normal(1800, 1000))

        # Limit x and y lists to 20 items
        fig1.xs = fig1.xs[-20:]
        fig1.ys = fig1.ys[-20:]

        # Draw x and y lists
        fig1.ax.clear()
        fig1.ax.plot(fig1.xs, fig1.ys)

        # fig2.ax.clear()
        # fig2.ax.plot(fig2.xs, fig2.ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('LA')
        plt.ylabel(LA_UNIT)

    ani = animation.FuncAnimation(fig1.fig, animate, fargs=(fig1.xs, fig1.ys), interval=20)
    ani2 = animation.FuncAnimation(fig2.fig, animate, fargs=(fig2.xs, fig2.ys), interval=20)

    plt.show()


def dummyValues():
    return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)


if __name__ == '__main__':

    # # creating apyqt5 application
    # app = QApplication(sys.argv)
    #
    # # creating a window object
    # main = Window()
    #
    # # showing the window
    # main.show()
    #
    # # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    #
    # app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #         QWidget {
    #             font-size: 30px;
    #         }
    #     ''')
    #
    # myApp = MyApp()
    # myApp.show()
    #
    # try:
    #     sys.exit(app.exec_())
    # except SystemExit:
    #     print('Closing Window...')

    fig1 = Figure()
    fig2 = Figure()

    runLoop(1)

    dummyName = "Dummy"
    age = "20"
    height = "180"
    weight = "90"
    sex = Sex(0)

    p1 = Participant(dummyName, age, height, weight, sex)

    while True:
        time.sleep(.1)

        AA, LA = dummyValues()



        print("LA: %f m/s^2" % LA, "\nAA: %f rad/s" % AA)
        print("\n")

        if areTheyConcussed(LA_GENERIC, AA_GENERIC, LA, AA):
            p1.concussion()

        # print(p1.concussedBool())
        if p1.concussedBool():
            print(p1.__str__())
            break

    # # loop
    # sys.exit(app.exec_())




