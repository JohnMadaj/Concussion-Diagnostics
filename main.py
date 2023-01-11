"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""

import numpy as np
from Diagnostic import areTheyConcussed
from Participants.Participant import Participant
from constants import *
from Figure import Figure
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import animation


def dummyValues():
    return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)


if __name__ == '__main__':

    fig1 = Figure()

    dummyName = "Dummy"
    age = "20"
    height = "180"
    weight = "90"
    sex = Sex(0)

    p1 = Participant(dummyName, age, height, weight, sex)

    while True:
        time.sleep(.1)

        AA, LA = dummyValues()
        fig1.runLoop(LA)

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




