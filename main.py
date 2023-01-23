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

from dummy import *
from gui.gui import GUI
from gui.popup import Popup
from organizer.organizer import Organizer








if __name__ == '__main__':

    p = Popup()
    org = Organizer(createListOfDummyParticipants(p.output))

    if not org.participantList:
        quit()
    gui = GUI(org.participantList)
    print(org.__str__())

    while True:

        time.sleep(.1)

        AA, LA = dummyValues(2)

        temp_concussbool, temp_status = areTheyConcussed(LA_GENERIC, AA_GENERIC, LA, AA)
        org.selected_participant.updateStatus(temp_concussbool, temp_status)

        print("LA: %f m/s^2" % LA, "\nAA: %f rad/s" % AA, "STATUS:", temp_status)
        print("\n")

        if org.selected_participant.concussedBool():
            print(org.selected_participant.__str__())
            break
