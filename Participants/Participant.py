"""
Capstone 2022-23: Concussion Detector - Christopher Castle, John Madaj, Josh Uvodich, Justin Murphy

Participant - base class
"""
import constants

from tkinter import *



master = Tk()
master.geometry("300x150")
master.title("Participants Information")
#command prompt needs to execute a loop to add info to user interface
button = Button(master, text="Add", bd = '5', command = master.destroy)

button.grid(row=5, column=1)


Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
Label(master, text='Sex').grid(row=2)
Label(master, text='Age').grid(row=3)
Label(master, text='Weight').grid(row=4)

e1 = Entry(master).grid(row=0, column=1)
e2 = Entry(master).grid(row=1, column=1)
e3 = Entry(master).grid(row=2, column=1)
e4 = Entry(master).grid(row=3, column=1)
e5 = Entry(master).grid(row=4, column=1)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)
#e5.grid(row=4, column=1)
mainloop()




class Participant:
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex

        self.concussed = False

    def concussedBool(self):
        return self.concussed

    def concussion(self):
        self.concussed = True

    def __str__(self):
        if self.concussed:
            return "%s is concussed" % self.name
        return "%s is not concussed" % self.name
