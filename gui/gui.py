import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from panel import Panel
from PIL import Image, ImageTk



class GUI:

    def __init__(self):
        self.num = 1
        self.root = tk.Tk()

        font1 = ("Arial", 18)
        font2 = ("Times New Roman", 12)
        font3 = font.Font(family="Helvetica", size=32, weight="bold")

        self.root.geometry("800x500")
        self.root.title("GUI")
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='light gray')

        self.closebtn = tk.Button(self.root, text="Close", font=font2, command=self.on_closing)
        # # passing show_message as function hence no parenthesis
        self.closebtn.pack(padx=10, pady=10, side=tk.TOP, anchor=tk.NE)

        self.root.toplabel = tk.Label(text="Concussion Diagnostics Software", font=font3)
        self.root.toplabel.pack(padx=10, pady=10)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", font=font2)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", font=font2, command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="This button doesnt do anything")

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=2)

        sidemenu = []
        for i in range(20):
            sidemenu.append(tk.Button(buttonframe, text="sidebutton", font=1))
            sidemenu[-1].grid(row=i, sticky="nswe")

        # self.panel = Panel(buttonframe)
        # self.panel.root.grid(row=0, column=1, sticky="news")

        # btn2 = tk.Button(buttonframe, text="dos", font=font1)
        # btn2.grid(row=0, column=1, sticky="we")  # we = west, east (acronym)
        #
        # btn5 = tk.Button(buttonframe, text="more", font=font1)
        # btn5.grid(row=1, column=1, sticky="we")  # we = west, east (acronym)

        buttonframe.pack(pady=50, fill='x')

        self.root.mainloop()


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
    gui = GUI()
