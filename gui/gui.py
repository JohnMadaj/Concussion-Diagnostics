import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from panel import Panel
from PIL import Image, ImageTk


class GUI:

    def __init__(self, numrows):
        self.num = 1
        self.root = tk.Tk()

        self.font1 = ("Arial", 18)
        self.font2 = ("Times New Roman", 12)
        self.font3 = font.Font(family="Helvetica", size=32, weight="bold")

        self.root.geometry("800x500")
        self.root.title("GUI")
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='light gray')

        self.closebtn = tk.Button(self.root, text="Close", font=self.font2, command=self.on_closing)
        # # passing show_message as function hence no parenthesis
        self.closebtn.pack(padx=10, pady=10, side=tk.TOP, anchor=tk.NE)

        self.root.toplabel = tk.Label(text="Concussion Diagnostics Software", font=self.font3)
        self.root.toplabel.pack(padx=10, pady=10)

        self.create_menubar()
        self.create_frame(numrows)

        self.root.mainloop()

    def create_menubar(self):

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", font=self.font2)
        filemenu.add_separator()
        filemenu.add_command(label="Close", font=self.font2, command=exit)

        actionmenu = tk.Menu(menubar, tearoff=0)
        actionmenu.add_command(label="This button doesnt do anything")

        menubar.add_cascade(menu=filemenu, label="File")
        menubar.add_cascade(menu=actionmenu, label="Action")

        self.root.config(menu=menubar)

        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_frame(self, numrows):

        buttonframe = tk.Frame(self.root)

        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=3)

        sidemenu = []
        for i in range(numrows):
            sidemenu.append(tk.Button(buttonframe, text="sidebutton", font=self.font1))
            sidemenu[-1].grid(row=i, sticky="nswe")

        submenu = tk.Frame(buttonframe)
        submenu.grid(row=0, column=1, sticky="news", rowspan=numrows)
        submenu.config(background="pink")

        for i in range(3):
            submenu.columnconfigure(i, weight=1)

        submenu.rowconfigure(1, weight=1)
        tk.Label(submenu, text='Top left').grid(row=0, column=0, sticky='w')
        tk.Label(submenu, text='Top center').grid(row=0, column=1)
        tk.Label(submenu, text='Top right').grid(row=0, column=2, sticky='e')
        tk.Label(submenu, text='center').grid(row=1, column=1)
        tk.Label(submenu, text='Bottom left').grid(row=2, column=0, sticky='w')
        tk.Label(submenu, text='Bottom center').grid(row=2, column=1)
        tk.Label(submenu, text='Bottom right').grid(row=2, column=2, sticky='e')
        buttonframe.pack(pady=50, fill='x')

    # def show_message(self):
    #     if self.check_var.get():
    #         messagebox.showinfo(title="Message", message="hitler had some good points")
    #         print(self.num)
    #         self.num +=1
    #     else:
    #         print(self.textbox.get('1.0', tk.END))
    #
    # def shortcut(self, event):
    #     print(event)
    #     if event.keysym == "Control_L":
    #         print("You hit CTRL L")
    #         self.show_message()
    #     if event.keysym == "q":
    #         self.on_closing()
    #
    def on_closing(self):
        # if messagebox.askyesno(title="Are u sure?", message="???? are you?"):
        print("Goodbye, come again!")
        self.root.destroy()

    #
    # def openfun(self):
    #     messagebox.showinfo(title="Open", message="You fucking idiot theres nothing to open this isnt a real program")


if __name__ == "__main__":
    gui = GUI(10)
