import random
import tkinter.font as font
import tkinter.ttk as ttk
from ttkthemes import ThemedTk, THEMES
import names
from tkinter import *
from PIL import ImageTk, Image
from constants import *
from gui.Connection_Viewer_Popup import Connection_Viewer_Popup
from gui.Device_Manager_Popup import Device_Manager_Popup
from gui.SideMenu import SideMenu
from gui.clock import Clock

from gui.Participant_Panel import ParticipantPanel


class GUI:

    def __init__(self, org):
        self.org = org

    def startup(self):
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
            filemenu.add_command(label="Open", font=font2, command=self.refresh)
            filemenu.add_separator()
            filemenu.add_command(label="Close", font=font2, command=exit)

            actionmenu.add_command(
                label="Toggle Random Input on No Connection (%s)"
                      % self.p_panel.random_vals_bool,
                command=self.toggle_rvb, font=font2)
            actionmenu.add_command(
                label="Device Manager",
                command=self.device_manager, font=font2)
            actionmenu.add_command(
                label="View Device Connections",
                command=self.connection_viewer, font=font2
            )
            actionmenu.add_command(
                label="Toggle Visualizer (%s)" % self.org.visualize,
                command=self.toggle_visualizer, font=font2
            )

        make_menubar_commands()

        menubar.add_cascade(menu=filemenu, label="File")
        menubar.add_cascade(menu=actionmenu, label="Action")
        menubar.add_command(label="Close", command=self.org.on_closing)

        self.root.config(menu=menubar)

    def create_displayframe(self):

        displayframe = tk.Frame(self.root)
        displayframe.columnconfigure(0, weight=1)
        displayframe.columnconfigure(1, weight=3)

        def call_sidemenu():
            self.sidemenu_canvas = tk.Canvas(displayframe)
            self.sidemenu = SideMenu(displayframe, 0, gui=self, organizer=self.org)
            self.sidemenu.grid(column=0, sticky="news")
            self.sidemenu_canvas.grid(column=0, sticky="news")
        call_sidemenu()


        def call_participant_panel():
            self.p_panel = ParticipantPanel(parent=displayframe, organizer=self.org, gui=self)
            self.p_panel.grid(row=0, column=1, sticky="new", rowspan=8)
            self.p_panel.config(background="grey")
        call_participant_panel()

        displayframe.pack(pady=0, fill='x', expand=1)

    def refresh_from_device_manager(self):
        self.sidemenu.fill_sidemenu()
        self.p_panel.refresh()

    def refresh(self):
        # if self.org.Active_Mode:
        #     self.call_receive_data()
        self.sidemenu.refresh()
        self.p_panel.refresh()

    def call_receive_data(self):
        self.org.receive_data()

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

    def connection_viewer(self):
        Connection_Viewer_Popup(self.org, self)

    def toggle_visualizer(self):
        self.org.visualize = not self.org.visualize
        self.create_menubar()


if __name__ == "__main__":
    GUI()
