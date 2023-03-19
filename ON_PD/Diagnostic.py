from constants import *


def areTheyConcussed(LAthreshold=0, AAthreshold=0, LA=0, AA=0):
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
    ### CODE FOR LINEAR ACCELERATION TO G FORCE
    # def linear_accel_to_g_force(LA):
    #     # Define gravitational constant
    #     g = 9.80665  # meters per second squared
    #
    #     # Convert linear acceleration to g-force
    #     g_force = LA / g
    #
    #     return g_force

    if LAthreshold and LA:
        LAratio = LA / LAthreshold
    else:
        LAratio = 0
    if AAthreshold and AA:
        AAratio = AA / AAthreshold
    else:
        AAratio = 0

    currentStatus = 0
    concussbool = False

    # if LAratio and AAratio:
    #     concussbool = False
    #     currentStatus = max([LAratio, AAratio])
    #
    #     if LA > LAthreshold or AA > AAthreshold:
    #         # return True, getStatus(currentStatus)
    #         concussbool = True
    #     # return False, getStatus(currentStatus)

    # elif LAratio:
        concussbool = False
        currentStatus = LAratio
        if LA > LAthreshold:
            # return True, getStatus(currentStatus)
            concussbool = True
        # return False, getStatus(currentStatus)

    return concussbool



