import random

import numpy
import names
from constants import *
from Participants.Participant import Participant


def namegenerator(num):
    nameslist = []
    for i in range(num):
        nameslist.append(names.get_full_name())
    return nameslist

def sexgenerator():
    return random.choice([Sex.MALE, Sex.FEMALE])


def agegenerator():
    return random.randint(18, 28)


def heightgenerator():
    return random.randrange(80, 200)


def weightgenerator():
    return random.randrange(100, 250)


def dummyValues(numvals):
    if numvals == 2:
        return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)
    elif numvals == 1:
        return numpy.random.normal(30.0, 20)
    else:
        return 0


def createListOfDummyParticipants(num):
    tempnameslist = namegenerator(num)
    # participantlist = {}
    participantlist = []
    for name in tempnameslist:
        temp = Participant(name, agegenerator(), heightgenerator(), weightgenerator(), sexgenerator())
        # participantlist[temp.id] = temp
        participantlist.append(temp)
    return participantlist
