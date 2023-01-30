# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='GeeksforGeeks', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"yellow_menu_status.png")

displayframe = Frame(root)
displayframe.columnconfigure(0, weight=1)
displayframe.columnconfigure(1, weight=3)

def fill_sidemenu():
    for i in range(10):
        # Button(displayframe, text="me", image=photo, command=quit).pack()
        Button(displayframe, text="me", image=photo, command=quit).grid(column=i, row=i, sticky="nswe")
fill_sidemenu()
displayframe.pack()

# here, image option is used to
# set image on button

mainloop()

