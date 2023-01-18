import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from ttkthemes import ThemedTk, THEMES
import names
from tkinter import *


def namegenerator(num):
    nameslist = []
    for i in range(num):
        nameslist.append(names.get_full_name())
    return nameslist


class GUI:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Concussion Diagnostics")

        label = tk.Label(self.root, text="Number of Participants")
        label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=1)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=50, anchor="center")

        button = tk.Button(self.root, text="Run", command=self.run)
        button.pack(padx=10, pady=10, anchor="s")

        self.root.mainloop()



    def userinfo(self):

        master = Tk()
        master.geometry("300x150")
        master.title("Participants Information")
        # command prompt needs to execute a loop to add info to user interface
        button = Button(master, text="Add", bd='5', command=master.destroy)

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
        master.mainloop()

    def shortcut(self, event):
        if event.keysym == "Return":
            self.run()

    def run(self):
        box = int(self.textbox.get('1.0', tk.END))
        if int(box) > 0:
            self.root.destroy()
            self.userinfo()
            self.mainwindow(box)


    def mainwindow(self, numrows):
        self.num = 1
        # self.root = tk.Tk()
        self.root = ThemedTk(themebg = True)
        self.root.set_theme('blue')
        self.font1 = ("Arial", 18)
        self.font2 = ("Times New Roman", 12)
        self.font3 = font.Font(family="Helvetica", size=40, weight="bold")

        self.root.geometry("800x500")
        self.root.title("GUI")
        self.root.attributes('-fullscreen', True)
        # self.root.configure(background='light gray')

        self.closebtn = tk.Button(self.root, text="Close", font=self.font2, command=self.on_closing)
        # # passing show_message as function hence no parenthesis
        self.closebtn.pack(padx=10, pady=10, side=tk.TOP, anchor=tk.NE)

        self.root.toplabel = tk.Label(text="Concussion Diagnostics Software", font=self.font3)
        self.root.toplabel.config(background="light gray")
        self.root.toplabel.pack(padx=10, pady=10)

        nameslist = namegenerator(numrows)

        self.create_menubar()
        self.create_frame(nameslist)
        self.create_themebox()

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


    def create_frame(self, nameslist):

        buttonframe = tk.Frame(self.root)

        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=3)



        sidemenu = []
        for i, name in enumerate(nameslist):
            #display = tk.Label(submenu, text='Top left').grid(row=0, column=0, sticky='w')
            #need a command output below for button
            sidemenu.append(tk.Button(buttonframe, text=name, font=self.font1, bg = '#ffffff', activebackground = '#4444ff'))

            #sidemenu[-1].configure(bg="red")
            sidemenu[-1].grid(row=i, sticky="nswe")

        submenu = tk.Frame(buttonframe)
        submenu.grid(row=0, column=1, sticky="news", rowspan=16)
        submenu.config(background="grey")

        for i in range(3):
            submenu.columnconfigure(i, weight=1)

#######################################################################

#        lst = [(1, 'Raj', 'Mumbai', 19),
##               (2, 'Aaryan', 'Pune', 18),
#               (3, 'Vaishnavi', 'Mumbai', 20),
#               (4, 'Rachna', 'Mumbai', 21),
##               (5, 'Shubham', 'Delhi', 21)]
#        total_rows = len(lst)
#        total_columns = len(lst[0])
#
 #       for i in range(total_rows):
#            for j in range(total_columns):
 #               e = Entry(tk(), width=20, fg='blue',
  #                             font=('Arial', 16, 'bold'))
   #             submenu.append(
    #                tk.Button(buttonframe, text=e, font=self.font1, bg='#ffffff', activebackground='#4444ff'))
     #           e.grid(row=i, column=j)
      #          e.insert(0, lst[i][j])

        # find total number of rows and
        # columns in list


        # create root window



        submenu.rowconfigure(1, weight=1)
        tk.Label(submenu, text='Top left').grid(row=0, column=0, sticky='w')
        tk.Label(submenu, text='Top center').grid(row=0, column=1)
        tk.Label(submenu, text='Participant name',font=self.font1).grid(row=0, column=2, sticky='e')
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


    def on_closing(self):
        # if messagebox.askyesno(title="Are u sure?", message="???? are you?"):
        print("Goodbye, come again!")
        self.root.destroy()

    def create_themebox(self):
        tc = ttk.Combobox(self.root, values=THEMES)
        tc.pack(anchor="sw", side=tk.LEFT)
        tc.set("Change theme")
        tc.bind("<<ComboboxSelected>>", lambda e: change_theme(tc.get()))

        def change_theme(theme, e=None):
            try:
                self.root.set_theme(theme)
            except:
                pass


if __name__ == "__main__":

    GUI()

