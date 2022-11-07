"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

"""
from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Sport(Enum):
    FOOTBALL = 0
    ICE_HOCKEY = 1

class Age(Enum):
    YOUTH = 12
    HS = 17
    COLLEGE = 23
    @classmethod
    def getAgeRange(cls):
        if 


# metrics - linear acceleration (g), angular acceleration (m/s^2)


LA_YOUTH_ICE_HOCKEY = 31.80
LA_COLLEGE_ICE_HOCKEY = 44.07

AA_YOUTH_ICE_HOCKEY = 2911.00
AA_COLLEGE_ICE_HOCKEY = 3807.67

LA_YOUTH_FOOTBALL = 57.37
LA_HS_FOOTBALL = 90.76
LA_COLLEGE_FOOTBALL = 94.71

AA_YOUTH_FOOTBALL = 3359.50
AA_HS_FOOTBALL = 6174.22
AA_COLLEGE_FOOTBALL = 4596.79
