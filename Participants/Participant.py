"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

Participant - base class
"""
import constants

class Participant:
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex

        self.status = constants.Status.GREEN
        self.concussed = False

    def concussedBool(self):
        return self.concussed

    def updateStatus(self, concussbool, newstatus):
        self.concussed = concussbool
        self.status = newstatus

    def __str__(self):
        if self.concussed:
            return "%s is concussed" % self.name
        return "%s is not concussed" % self.name
