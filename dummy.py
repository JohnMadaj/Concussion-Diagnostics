import random

import numpy
import names
from constants import *
from Participants.Participant import Participant


def namegenerator(num=0):
    if num:
        nameslist = []
        for i in range(num):
            nameslist.append(names.get_full_name())
        return nameslist
    return names.get_full_name()

def sexgenerator():
    return random.choice([Sex.MALE, Sex.FEMALE])


def agegenerator():
    return random.randint(18, 28)


def heightgenerator():
    return random.randrange(80, 200)


def weightgenerator():
    return random.randrange(50, 110)


def dummyValues(numvals=1):
    if numvals == 2:
        return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)
    elif numvals == 1:
        return numpy.random.normal(30.0, 20)
    else:
        return 0

def randomDummy():
    return Participant(namegenerator(), agegenerator(), heightgenerator(), weightgenerator(), sexgenerator())

def createListOfDummyParticipants(num):
    tempnameslist = namegenerator(num)
    # participantlist = {}
    participantlist = []
    for name in tempnameslist:
        temp = Participant(name, agegenerator(), heightgenerator(), weightgenerator(), sexgenerator())
        # participantlist[temp.id] = temp
        participantlist.append(temp)
    return participantlist

def dummyDataPacket(): #d_id: LA.4f: bool(binary)
    rec_str = ""
    for i in range(4):
        m = dummyValues()
        b = 0
        if m > 80:
            b = 1
        rec_str += "%s: %f: %d: %d\n" % (str(i+1), m, b, 50)
    return rec_str[:-1]

