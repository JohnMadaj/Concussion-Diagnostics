
from constants import *
from gui.participant_panel_plot import ParticipantPanel_Plot


class ParticipantPanel(tk.Frame):

    def __init__(self, parent, organizer, gui):

        self.gui = gui
        self.org = organizer
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.random_vals_bool = False
        self.colorstatus = "green"

        def build_grid():
            self.columnconfigure(0, weight=2)
            self.columnconfigure(1, weight=1)

            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.rowconfigure(3, weight=1)
            self.rowconfigure(4, weight=1)
            self.rowconfigure(5, weight=4)

        build_grid()

        self.Toplabel = tk.Label(self, text="Participant Name:", font=HEADER_FONT)
        self.StatusLabel = tk.Label(self, text="Status:", font=LARGE_FONT)
        self.LAlabel = tk.Label(self, text="G Force", font=LARGE_FONT)
        self.PeakLabel = tk.Label(self, text="Peak", font=LARGE_FONT)
        self.blurb = tk.Label(self, text="info", font=LARGE_FONT)
        self.blurb.config(text=self.org.selected_participant.info())


        boldlabelfont = font.Font(family="Helvetica", size=20, weight="bold")
        self.LabelOne = tk.Label(self, text="LA", font=boldlabelfont)
        self.LabelTwo = tk.Label(self, text="Peak", font=boldlabelfont)




        self.reset_button = tk.Button(self, font=BUTTON_FONT)
        self.exit_button = tk.Button(self, font=BUTTON_FONT, text="Exit",
                                     command=self.org.on_closing, )



        def grid_setup():
            self.reset_button.grid(row=5, column=0, sticky='nwse')
            self.exit_button.grid(row=5, column=1, sticky='nsew')

            self.Toplabel.grid(row=0, columnspan=2, sticky="news")
            self.StatusLabel.grid(row=1, columnspan=2, sticky="news")
            self.LAlabel.grid(row=3, column=0, sticky="news")
            self.PeakLabel.grid(row=3, column=1, sticky="news")
            self.blurb.grid(row=4, column=1, sticky="news")

            self.LabelOne.grid(row=2, column=0, sticky="news")
            self.LabelTwo.grid(row=2, column=1, sticky="news")


        grid_setup()

        self.connect_status_label = tk.Label(self.parent)

        self.plot(4, 0)
        if simulate_on_startup:
            self.on_reset()
        else:
            self.on_stop()

    def on_stop(self):
        self.org.Active_Mode = False
        self.reset_button.config(text="Begin (Active Mode)",
                                 command=self.on_reset, )

        if not self.org.participantList:
            quit()
        self.Toplabel.config(text=self.org.selected_participant.__str__())

    def plot(self, row, column):
        self.pp_plot = ParticipantPanel_Plot(self.org, self.master, self, row, column)

    def on_reset(self):
        if self.org.selected_participant != None:
            self.org.Active_Mode = True
            self.reset_button.config(text="Stop (Setup Mode)", command=self.on_stop)
            self.refresh()

    def refresh(self):
        self.connect_status_label.place(x=600, y=400)
        if self.org.Active_Mode:
            # self.pass_input_to_Participant()
            self.gui.call_receive_data()
        self.update_labels()
        if self.org.Active_Mode:
            if self.org.visualize and self.org.temp_visualize:
                self.pp_plot.refresh()
            self.after(TIME_CONSTANT, self.refresh)

    def update_labels(self):
        self.Toplabel.config(
            text=" " + self.org.selected_participant.concussed_State())
        self.LAlabel.config(
            text=" " + str(self.org.selected_participant.getlastLA()) + " g")
        self.PeakLabel.config(
            text="Peak: " + str(self.org.selected_participant.LA_PEAK) + " g")

        self.blurb.config(text=self.org.selected_participant.info())

        self.colorstatus = str(self.org.selected_participant.status)[7:]

        self.StatusLabel.config(text="Status: " + self.colorstatus,
                                background=self.colorstatus,
                                foreground="white",
                                font=LARGE_FONT)

    # def pass_input_to_Participant(self):
    #     def calculate_input_magnitude():
    #         """
    #         TODO: reciever-based calculation function, needs to move, id specific
    #         :return:
    #         """
    #         self.connect_status_label.config(text="")
    #         datapacket = port_comm.recieve_data(self.org.selected_participant.id)
    #         self.org.selected_participant.updateLA(datapacket)
    #         cbool, status = areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)
    #         self.org.selected_participant.updateStatus(cbool, status)
    #         # doesnt have a return right now but it will need one when it moves
    #     # if self.parent.running:
    #         """
    #         TODO: Below is device input code, needs to go to receiver, id specific
    #         """
    #     try:
    #         calculate_input_magnitude()
    #     except Exception as e:
    #         self.if_no_input()


    # def if_no_input(self):
    #     """
    #     TODO: simulation function, will be reduced
    #     :return:
    #     """
    #     if self.random_vals_bool:
    #         self.connect_status_label.config(text="NO DEVICE CONNECTED: RANDOM VALUES ASSIGNED")
    #         self.org.selected_participant.updateLA(dummyValues(1))
    #     else:
    #         self.connect_status_label.config(text="NO DEVICE CONNECTED")
    #         self.org.selected_participant.updateLA(1)
    #     cbool, status = areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)
    #     self.org.selected_participant.updateStatus(cbool, status)


if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1280x720")
    app.mainloop()
