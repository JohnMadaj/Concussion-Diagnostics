"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
import constants
# import numpy as np
from Diagnostic import areTheyConcussed
from Participants.Participant import Participant
from constants import *
# from Figure import Figure
# import matplotlib.pyplot as plt
# import datetime as dt
# from matplotlib import animation

import names
from gui.gui import GUI
from organizer.organizer import Organizer


def dummyValues():
    return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)


def namegenerator(num):
    nameslist = []
    for i in range(num):
        nameslist.append(names.get_full_name())
    return nameslist


def createListOfDummyParticipants(num):
    tempnameslist = namegenerator(num)
    participantlist = []
    for name in tempnameslist:
        participantlist.append(Participant(name, 20, 180, 90, constants.Sex.MALE))
    return participantlist


if __name__ == '__main__':

    org = Organizer(createListOfDummyParticipants(5))

    gui = GUI()
    # gui.create_menubar()
    # gui.create_frame(namegenerator(5))
    # gui.create_themebox()
    # gui.root.mainloop()
    print(org.__str__())

    # dummyName = "Dummy"
    # age = "20"
    # height = "180"
    # weight = "90"
    # sex = Sex(0)
    # p1 = Participant(dummyName, age, height, weight, sex)

    while True:

        time.sleep(.1)

        AA, LA = dummyValues()

        temp_concussbool, temp_status = areTheyConcussed(LA_GENERIC, AA_GENERIC, LA, AA)
        org.selected_participant.updateStatus(temp_concussbool, temp_status)

        print("LA: %f m/s^2" % LA, "\nAA: %f rad/s" % AA, "STATUS:", temp_status)
        print("\n")

        if org.selected_participant.concussedBool():
            print(org.selected_participant.__str__())
            break
