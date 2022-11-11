# importing various libraries

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib import animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import datetime as dt

from constants import *

# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.start_button = QPushButton('Begin Diagnostic')

        # adding action to the button
        self.start_button.clicked.connect(self.animate)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.start_button)

        # setting layout to the main window
        self.setLayout(layout)




