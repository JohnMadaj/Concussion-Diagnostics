import tkinter
import tkinter as tk
from tkinter import ttk


class Screen(tk.Frame):
    def __init__(self, ADC, parent, controller):
        tk.Frame.__init__(self, parent)
        self.ADC = ADC
        lbl = ttk.Label(self, text = "Test Display", background = "grey")
        lbl.grid(column = 7, row = 8)
        self.lblTestDisplay = ttk.Label(self, foreground = "lime", background = "black")
        self.lblTestDisplay.grid(column = 7, row = 9, sticky = "ew")

        self.adc_update() # start the adc loop

    def adc_update(self):
        displayText = self.ADC.ReadValues() #this method returns a list of values
        for i in range(len(displayText)):
            displayText[i] = round(displayText[i], 2)
        self.lblTestDisplay.config(text = str(displayText)) # update the display
        self.after(1000, self.adc_update) # ask the mainloop to call this method aga

if __name__ == "__main__":
    Screen(tk)