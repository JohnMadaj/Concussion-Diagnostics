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
import tkinter as tk
from tkinter import messagebox
from threading import Thread
#from playsound import playsound
import pygame

import datetime as dt
from matplotlib import animation
import names

from local_resources import *

# pygame.mixer.init()# initialise the pygame



global COMPORT
COMPORT = "COM12"

# import serial
# import serial.tools.list_ports
#
# def find_esp32_port():
#     for port in serial.tools.list_ports.comports():
#         if "/dev/ttyUSB" in port.name or "COM" in port.name:
#             if "Adafruit ESP32 Huzzah32 Feather" in port.description:
#                 return serial.Serial(port=port.device, baudrate=115200)
#     raise IOError("ESP32 not found on any serial port")


try:
    arduinoData = serial.Serial(COMPORT, 115200, timeout=1)
except Exception as e:
    print(e)

# TODO: simulate_on_startup causes gui to hang indefinitely, refresh loop
simulate_on_startup = False

# def beep():
#     pygame.mixer.music.load(r"graphics/beep-beep-6151.mp3")
#     pygame.mixer.music.play(loops=0)

TIME_CONSTANT = 15  # ms
# TIME_CONSTANT = 500

AA_UNIT = "rad/s^2"
LA_UNIT = "m/s^2"
input_storage_limit = 20


class Status(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2


yellow_intensity = 0.5
red_intensity = 0.8


def status_bg_from_status(stat):
    if stat == Status.RED:
        return red_menu_status_path
    elif stat == Status.YELLOW:
        return yellow_menu_status_path
    elif stat == Status.GREEN:
        return green_menu_status_path


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

if __name__ == '__main__':
    beep()