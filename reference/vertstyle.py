from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as ttkboot
from ttkbootstrap.constants import *
from ttkthemes.themed_tk import ThemedTk

app = ThemedTk()

# create the vertical tab alignment
app.style.configure('long.TNotebook', tabposition='wn')

# manually assign the new style to the notebook
nb = ttk.Notebook(app, style='long.TNotebook')

nb.pack(fill=BOTH, expand=YES)

for x in range(5):
    tabname = f'Tab {x}'
    nb.add(child=ttkboot.Notebook(width=300, height=300), text=tabname)

app.mainloop()