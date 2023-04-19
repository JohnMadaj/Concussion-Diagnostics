"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

Participant - base class
"""
import uuid
from constants import *



class Participant:
    def __init__(self, name=0, age=0, height=0, weight=0, sex=0, device_id=0):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = Sex(sex)

        self.device_id = int(device_id)

        self.status = Status.GREEN
        self.concussed = False

        self.battery = None
        if self.device_id > 0:
            self.battery = 0

        self.time = []
        self.LA = []
        self.LAThreshold = LA_GENERIC

        self.LA_PEAK = 0

        self.y = []

    def populate(self, name, age, height, weight, device_id, sex=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        # self.sex = Sex(sex)
        self.device_id = int(device_id)

    def getlastLA(self):
        if not self.LA:
            return 0
        return self.LA[-1]

    def updatepeak(self):
        self.LA_PEAK = max(self.LA)


    def get_last_intensity(self):
        return self.LA[-1] / self.LAThreshold

    def graph_helper(self):
        if not self.LA:
            return 0
        if self.LA[-1] / self.LAThreshold > yellow_intensity:
            self.y.append(self.LA[-1])
        else:
            self.y.append(0)
        if len(self.y) > input_storage_limit:
            self.y = self.y[1:]
        return self.y

    def updateLA(self, val):
        self.LA.append(round(val, 4))
        self.time.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        if len(self.LA) > input_storage_limit:
            self.LA = self.LA[1:]
        if len(self.time) > input_storage_limit:
            self.time = self.time[1:]

    def updateBattery(self, battery):
        self.battery = battery


    def concussedBool(self):
        return self.concussed

    def concussed_State(self):
        if self.concussed:
            return "%s is concussed" % self.name
        return "%s is not concussed" % self.name

    def updateStatus(self, concussbool, newstatus):
        if not self.concussed:
            # if concussbool != self.concussed:
            #     beep()
            self.concussed = concussbool
        self.status = newstatus

    def info(self):
        info = "Info:\n" + str(self.sex)[4:] + \
               "\nAge: " + str(self.age) + \
               "\nHeight: " + str(self.height) + " cm" + \
               "\nWeight: " + str(self.weight) + " kg" + \
               "\nDevice ID: " + str(self.device_id)

        if self.battery:
            info+="\nBattery: %d %%" % self.battery
        else:
            info+="\nNot Connected"
        return info

    def __str__(self):
        return self.name
