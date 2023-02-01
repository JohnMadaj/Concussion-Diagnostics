"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
import os
from tkinter import font

import serial
from enum import Enum
import random
import time
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import datetime as dt
from matplotlib import animation
import names

# you'll probably want to edit the two below
COMPORT = "COM5"

# logo_path = r"C:\Users\Jack\Documents\Capstone\Concussion-Diagnostics\graphics\logo_small.png"
logo_path = r"graphics\logo_small.png"
# logo_path = os.path.dirname(os.path.abspath("logo_small.png"))

try:
    arduinoData = serial.Serial(COMPORT, 115200, timeout=1)
except Exception as e:
    print(e)

LARGE_FONT = ("Helvetica", 20)
HEADER_FONT = ("Helvetica", 36)
BUTTON_FONT = ("Helvetica", 16, "bold")

font1 = ("Arial", 18)
font2 = ("Times New Roman", 12)

bg = "#bccbe8"
sage = '#9EAA55'

TIME_CONSTANT = 80  # ms

AA_UNIT = "rad/s^2"
LA_UNIT = "m/s^2"
input_storage_limit = 20


class Status(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2


def status_bg_from_status(stat):
    if stat == Status.RED:
        return "graphics/red_menu_status.png"
    elif stat == Status.YELLOW:
        return "graphics/yellow_menu_status.png"
    elif stat == Status.GREEN:
        return r"C:\Users\Jack\Documents\Capstone\Concussion-Diagnostics\graphics\green_menu_status.png"


yellow_intensity = 0.5
red_intensity = 0.8


class Sex(Enum):
    MALE = 0
    FEMALE = 1


class Sport(Enum):
    FOOTBALL = 0
    ICE_HOCKEY = 1


class Age(Enum):
    YOUTH = 12
    HS = 17
    COLLEGE = 23
    # @classmethod
    # def getAgeRange(cls):


# metrics - linear acceleration (g), angular acceleration (m/s^2)
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5384819/


LA_GENERIC = 80.0  # 100
AA_GENERIC = 3000.0

LA_YOUTH_ICE_HOCKEY = 31.80
LA_COLLEGE_ICE_HOCKEY = 44.07

AA_YOUTH_ICE_HOCKEY = 2911.00
AA_COLLEGE_ICE_HOCKEY = 3807.67

LA_YOUTH_FOOTBALL = 57.37
LA_HS_FOOTBALL = 90.76
LA_COLLEGE_FOOTBALL = 94.71

AA_YOUTH_FOOTBALL = 3359.50
AA_HS_FOOTBALL = 6174.22
AA_COLLEGE_FOOTBALL = 4596.79
