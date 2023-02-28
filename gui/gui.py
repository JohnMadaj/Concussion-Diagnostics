import random
import tkinter.font as font
import tkinter.ttk as ttk
from ttkthemes import ThemedTk, THEMES
import names
from tkinter import *
from PIL import ImageTk, Image
from constants import *
from gui.Device_Manager_Popup import Device_Manager_Popup
from gui.SideMenu import SideMenu
from gui.clock import Clock

from gui.Participant_Panel import ParticipantPanel


class GUI:

    def __init__(self, org):
        self.org = org
        self.org.select_new_participant()
        self.running = False

        self.root = ThemedTk(themebg=True)
        self.root.set_theme('blue')

        self.font3 = font.Font(family="Helvetica", size=40, weight="bold")
        self.random_vals_bool = False

        def create_window():
            self.root.geometry("800x500")
            self.root.title(gui_name)
            self.root.attributes('-fullscreen', True)
            self.root.configure(background=sage)
        create_window()

        def draw_pictures():

            self.image2 = Image.open(top_label_path)
            self.test2 =ImageTk.PhotoImage(self.image2)
            self.label2 = tk.Label(image=self.test2, background=sage)
            self.label2.image = self.image2
            self.label2.pack(padx=120, anchor=NE)

            self.image1 = Image.open(logo_path)
            self.image1.resize((100, 100), Image.ANTIALIAS)
            self.test1 = ImageTk.PhotoImage(self.image1)
            self.label1 = tk.Label(image=self.test1)
            self.label1.image = self.image1
            self.label1.place(x=80, y=15)
        draw_pictures()

        self.sidemenu = SideMenu
        self.p_panel = ParticipantPanel

        def build_widgets():
            self.create_displayframe()
            self.create_menubar()
            self.create_themebox()
            self.create_clock()
            self.refresh()

        build_widgets()

        self.root.mainloop()


    def create_menubar(self):

        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        actionmenu = tk.Menu(menubar, tearoff=0)

        def make_menubar_commands():
            filemenu.add_command(label="Open", font=font2)
            filemenu.add_separator()
            filemenu.add_command(label="Close", font=font2, command=exit)

            # cmd_str = self.start_command()
            # actionmenu.add_command(
            #     label=cmd_str,
            #     command=self.toggle_session
            # )
            actionmenu.add_command(
                label="Toggle Random Input on No Connection (%s)"
                      % self.p_panel.random_vals_bool,
                command=self.toggle_rvb, font=font2)
            actionmenu.add_command(
                label="Device Manager",
                command=self.device_manager, font=font2)

        make_menubar_commands()

        menubar.add_cascade(menu=filemenu, label="File")
        menubar.add_cascade(menu=actionmenu, label="Action")
        menubar.add_command(label="Close", command=self.on_closing)

        self.root.config(menu=menubar)
    def start_command(self):
        if self.running:
            return "End Session"
        else:
            return "Start Session"

    def create_displayframe(self):

        displayframe = tk.Frame(self.root)
        displayframe.columnconfigure(0, weight=1)
        displayframe.columnconfigure(1, weight=2)
        displayframe.columnconfigure(2, weight=3)

        def call_sidemenu():
            self.sidemenu_canvas = tk.Canvas(displayframe)
            self.sidemenu = SideMenu(displayframe, 0, master=self.root, organizer=self.org)
            self.sidemenu.grid(column=0, sticky="news")
            # self.sidemenu.pack(side="left")
            # self.sidemenu = SideMenu(self.sidemenu_canvas, 0, master=self.root, organizer=self.org)
            # t = Label(self.sidemenu_canvas, text="FUCK\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
            # \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
            # \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFUCK")
            # t.pack(side="left")
            self.sidemenu_canvas.grid(column=0, sticky="news")
        call_sidemenu()
        # self.myscrollbar = Scrollbar(displayframe, orient="vertical")
        # self.myscrollbar.grid(column=1, sticky="news", rowspan=8)
        # self.myscrollbar.config(command=self.sidemenu_canvas.yview)

        def call_participant_panel():
            self.p_panel = ParticipantPanel(parent=displayframe, organizer=self.org)
            self.p_panel.grid(row=0, column=2, sticky="new", rowspan=8)
            self.p_panel.config(background="grey")
        call_participant_panel()

        displayframe.pack(pady=0, fill='x', expand=1)

    def refresh_from_device_manager(self):
        self.sidemenu.fill_sidemenu()
        self.p_panel.refresh()

    def refresh(self):
        self.sidemenu.refresh()
        self.p_panel.refresh()

    # def toggle_session(self):
    #     self.running = not self.running
    #     self.p_panel.refresh()
    #     self.create_menubar()

    def on_closing(self):
        print(closing_string)
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

    def create_clock(self):
        Clock(self.root)

    def toggle_rvb(self):
        self.p_panel.random_vals_bool = not self.p_panel.random_vals_bool
        self.create_menubar()


    def device_manager(self):
        Device_Manager_Popup(self.org, self)
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


if __name__ == "__main__":
    GUI()
