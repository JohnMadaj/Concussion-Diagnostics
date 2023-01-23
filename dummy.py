import numpy
import names
import constants
from Participants.Participant import Participant


def namegenerator(num):
    nameslist = []
    for i in range(num):
        nameslist.append(names.get_full_name())
    return nameslist
def dummyValues():
    # return numpy.random.normal(1800, 1000), numpy.random.normal(60.0, 20)
    return numpy.random.normal(20.0, 20)

def createListOfDummyParticipants(num):
    tempnameslist = namegenerator(num)
    participantlist = []
    for name in tempnameslist:
        participantlist.append(Participant(name, 20, 180, 90, constants.Sex.MALE))
    return participantlist