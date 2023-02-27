"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
from dummy import *
from gui.gui import GUI
from gui.popup import Popup
from organizer.organizer import Organizer
from gui.Device_Manager_Popup import Device_Manager_Popup


if __name__ == '__main__':

    org = Organizer([])
    p = Device_Manager_Popup(org, startupbool=True)
    # org.create_gui()

