"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
import random
import time
import numpy

from constants import *
from Diagnostic import areTheyConcussed
from Participant import Participant


# from Athlete import Athlete
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LA = 0.0
    AA = 0.0

    dummyName = "Dummy"
    age = "20"
    height = "180"
    weight = "90"
    sex = Sex(0)

    p1 = Participant(dummyName, age, height, weight, sex)

    # print(p1.concussedBool())

    while True:
        time.sleep(.1)

        LA = numpy.random.normal(60.0, 20)
        AA = numpy.random.normal(1800, 1000)
        print("LA: %f m/s^2" % LA, "\nAA: %f rad/s" % AA)
        print("\n")

        if areTheyConcussed(LA_GENERIC, AA_GENERIC, LA, AA):
            p1.concussion()

        # print(p1.concussedBool())
        if p1.concussedBool():
            print(p1.__str__())
            break





