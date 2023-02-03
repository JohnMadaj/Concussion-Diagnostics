from constants import *
from time import strftime

class Clock():

    def __init__(self, parent):
        # tk.Label.__init__(parent, font=('calibri', 40, 'bold'),
        self.root = tk.Label(parent, font=('calibri', 16, 'bold'),
                       background='purple',
                       foreground='white')

        self.root.place(x=1230, y=15)
        self.time()

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.root.config(text=string)
        self.root.after(1000, self.time)

