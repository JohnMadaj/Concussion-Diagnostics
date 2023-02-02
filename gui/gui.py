import random
import tkinter.font as font
import tkinter.ttk as ttk
from ttkthemes import ThemedTk, THEMES
import names
from tkinter import *
from PIL import ImageTk, Image
from constants import *
from gui.SideMenu import SideMenu

from gui.participant_panel import ParticipantPanel


class GUI:

    def __init__(self, org):
        self.org = org

        self.root = ThemedTk(themebg=True)
        self.root.set_theme('blue')

        # self.green_status_bg = PhotoImage(file=status_bg_from_status(Status.GREEN))
        # self.yellow_status_bg = PhotoImage(file=status_bg_from_status(Status.YELLOW))
        # self.red_status_bg = PhotoImage(file=status_bg_from_status(Status.RED))

        self.button_accent = PhotoImage(file=r"graphics\button_accent.png")

        self.font3 = font.Font(family="Helvetica", size=40, weight="bold")
        self.font4 = font.Font(family="Arial", size=18,weight="bold")

        def create_window():
            self.root.geometry("800x500")
            self.root.title("GUI")
            self.root.attributes('-fullscreen', True)
            self.root.configure(background=sage)
        create_window()

        self.close_btn = tk.Button(self.root, text="Close", font=font2, command=self.on_closing)
        self.top_label = tk.Label(self.root, text="Concussion Diagnostics Software", font=self.font3)

        def pack_basics():
            self.close_btn.pack(padx=10, pady=10, side=tk.TOP, anchor=tk.NE)
            self.top_label.config(background=sage)
            self.top_label.pack(padx=120, pady=20, anchor=NE)
        pack_basics()

        # draw logo - cannot be separated into method
        self.image1 = Image.open(logo_path)
        self.image1.resize((100, 100), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(self.image1)
        label1 = tk.Label(image=test)
        label1.image = self.image1
        label1.place(x=100, y=15)


        self.running = True
        self.create_menubar()
        self.create_displayframe()
        self.create_themebox()
        self.root.mainloop()


    def create_menubar(self):

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        actionmenu = tk.Menu(menubar, tearoff=0)

        def make_menubar_commands():
            filemenu.add_command(label="Open", font=font2)
            filemenu.add_separator()
            filemenu.add_command(label="Close", font=font2, command=exit)

            actionmenu.add_command(label="This button doesnt do anything")
        make_menubar_commands()

        menubar.add_cascade(menu=filemenu, label="File")
        menubar.add_cascade(menu=actionmenu, label="Action")

        self.root.config(menu=menubar)

    def create_displayframe(self):

        displayframe = tk.Frame(self.root)
        displayframe.columnconfigure(0, weight=1)
        displayframe.columnconfigure(1, weight=3)

        def call_sidemenu():
            self.sidemenu = SideMenu(displayframe, 0, master=self.root, organizer=self.org)
            self.sidemenu.grid(column=0, sticky="news")
        call_sidemenu()

        def call_participant_panel():
            p_panel = ParticipantPanel(displayframe, 0, master=self.root, organizer=self.org)
            p_panel.grid(row=0, column=1, sticky="news", rowspan=16)
            p_panel.config(background="grey")
        call_participant_panel()

        displayframe.pack(pady=0, fill='x', expand=1)


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
        #                tk.Button(displayframe, text=e, font=font1, bg='#ffffff', activebackground='#4444ff'))
        #           e.grid(row=i, column=j)
        #          e.insert(0, lst[i][j])

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

    def get_bg_from_status(self, status):
        if status == Status.GREEN:
            return self.green_status_bg
        elif status == Status.YELLOW:
            return self.yellow_status_bg
        elif status == Status.RED:
            return self.red_status_bg



if __name__ == "__main__":
    GUI()
