"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

Participant - base class
"""
from constants import *


class Participant:
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = Sex(sex)

        self.status = Status.GREEN
        self.concussed = False

        self.LA = []

    def getlastLA(self):
        return self.LA[-1]

    def updateLA(self, val):
        self.LA.append(val)
        if len(self.LA) > input_storage_limit:
            self.LA = self.LA[1:]

    def concussedBool(self):
        return self.concussed

    def updateStatus(self, concussbool, newstatus):
        if not self.concussed:
            self.concussed = concussbool
        self.status = newstatus

    def info(self):
        info = "Info:\n" + str(self.sex)[4:] +\
                      "\nAge: " + str(self.age) +\
                      "\nHeight: " + str(self.height) +\
                      "\nWeight: " + str(self.weight)
        return info

    def __str__(self):
        if self.concussed:
            return "%s is concussed" % self.name
        return "%s is not concussed" % self.name
