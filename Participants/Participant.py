"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

Participant - base class
"""
import uuid
from constants import *



class Participant:
    def __init__(self, name, age, height, weight, sex):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = Sex(sex)

        self.status = Status.GREEN
        self.concussed = False

        self.time = []
        self.LA = []
        self.LAThreshold = LA_GENERIC

        self.y = []

    def getlastLA(self):
        return self.LA[-1]

    def get_last_intensity(self):
        return self.LA[-1] / self.LAThreshold

    def graph_helper(self):
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


    def concussedBool(self):
        return self.concussed

    def concussed_State(self):
        if self.concussed:
            return "%s is concussed" % self.name
        return "%s is not concussed" % self.name

    def updateStatus(self, concussbool, newstatus):
        if not self.concussed:
            self.concussed = concussbool
        self.status = newstatus

    def info(self):
        info = "Info:\n" + str(self.sex)[4:] +\
                      "\nAge: " + str(self.age) +\
                      "\nHeight: " + str(self.height) +\
                      "\nWeight: " + str(self.weight) #+\
                      # "\nID: " + str(self.id)
        return info

    def __str__(self):
        return self.name
