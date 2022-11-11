import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib import animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import datetime as dt

from constants import *


class Figure:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        self.LA = 0

    def setLA(self, LA):
        self.LA = LA






