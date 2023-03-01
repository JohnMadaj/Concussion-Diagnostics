import dummy
from ON_PD.Diagnostic import *
from math import sqrt

def three_way_vector_magnitude(datapacket):
    splitpacket = datapacket.split(',')
    x = float(splitpacket[0])
    y = float(splitpacket[1])
    z = float(splitpacket[2])
    return sqrt(x * x + y * y + z * z)

def transmit(LA, concussbool):
    """
    TODO: send to reciever
    :param LA:
    :param concussbool:
    :return:
    """
    pass
    print(LA, concussbool)

def tester():
    LA = three_way_vector_magnitude(str(dummy.dummyValues()) + "," +
                                    str(dummy.dummyValues()) + "," +
                                    str(dummy.dummyValues()))  # TODO: pass measurement from device

    # TODO: (later) generic must replace with participant specific
    concussbool = areTheyConcussed(LA=LA, LAthreshold=80)
    return [LA, concussbool]

if __name__ == '__main__':

    LA = three_way_vector_magnitude("0,0,0") # TODO: pass measurement from device

    # TODO: (later) generic must replace with participant specific
    concussbool = areTheyConcussed(LA=LA, LAthreshold=80)

    transmit(LA, concussbool)