from statistics import mean

from constants import *


def areTheyConcussed(LAthreshold, AAthreshold, LA, AA):
    """
    :param LAthreshold:
    :param AAthreshold:
    :param LA:
    :param AA:


    :return: Concussion BOOL, Concussion STATUS (color)

    TODO: add sophistication to diagnostic:
    - create degrees of impact severity that reflect on participant overview:
        (concept)
            % of threshold      color       severity
            80                  red         high
            50                  yellow      moderate
            <30%                green       normal
    - WTSC
    - Multiple impact adjustment
    - EEG
    - Cumulative impact over time
    - blood oxygen bias??

    """
    LAratio = LA / LAthreshold
    AAratio = AA / AAthreshold

    currentStatus = mean([LAratio, AAratio])
    if LA > LAthreshold or AA > AAthreshold:
        return True, getStatus(currentStatus)
    return False, getStatus(currentStatus)


def getStatus(ratio):
    if ratio >= red_intensity:
        return Status(2)
    elif ratio >= yellow_intensity:
        return Status(1)
    return Status(0)
