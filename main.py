"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
from dummy import *
from gui.popup import Popup
from organizer.organizer import Organizer


if __name__ == '__main__':

    p = Popup()
    org = Organizer(createListOfDummyParticipants(p.output))

    if not org.participantList:
        quit()

    # while True:
    #
    #     time.sleep(.1)
    #
    #     AA, LA = dummyValues(2)
    #
    #     temp_concussbool, temp_status = areTheyConcussed(LA_GENERIC, AA_GENERIC, LA, AA)
    #     org.selected_participant.updateStatus(temp_concussbool, temp_status)
    #
    #     print("LA: %f m/s^2" % LA, "\nAA: %f rad/s" % AA, "STATUS:", temp_status)
    #     print("\n")
    #
    #     if org.selected_participant.concussedBool():
    #         print(org.selected_participant.__str__())
    #         break
