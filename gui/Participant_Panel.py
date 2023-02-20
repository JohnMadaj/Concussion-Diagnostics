import math
import tkinter as tk

from Diagnostic import areTheyConcussed
from dummy import *
from constants import *
from gui.participant_panel_plot import ParticipantPanel_Plot


class ParticipantPanel(tk.Frame):

    def __init__(self, parent, organizer):

        self.org = organizer
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.running = False
        self.random_vals_bool = False

        def build_grid():
            self.columnconfigure(0, weight=2)
            self.columnconfigure(1, weight=1)
            self.columnconfigure(2, weight=1)

            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.rowconfigure(3, weight=1)
            self.rowconfigure(4, weight=1)
            self.rowconfigure(5, weight=4)
        build_grid()


        self.Toplabel = tk.Label(self, text="Participant Name:", font=HEADER_FONT)
        self.StatusLabel = tk.Label(self, text="Status:", font=LARGE_FONT)
        self.LAlabel = tk.Label(self, text="LA: 0 m/s^2", font=LARGE_FONT)
        self.blurb = tk.Label(self, text="info", font=LARGE_FONT)

        self.reset_button = tk.Button(self, font=BUTTON_FONT)
        self.exit_button = tk.Button(self, font=BUTTON_FONT, text="Exit",
                                     command=quit,)
        self.reset_button.grid(row=4, column=0, sticky='nwse')
        self.exit_button.grid(row=4, column=1, sticky='nsew')

        self.Toplabel.grid(row=0, columnspan=2, sticky="news")
        self.StatusLabel.grid(row=1, columnspan=2, sticky="news")
        self.LAlabel.grid(row=2, columnspan=2, sticky="news")
        self.blurb.grid(row=3, column=1, sticky="news")

        self.connect_status_label = tk.Label(self.parent)

        self.plot(3, 0)
        if simulate_on_startup:
            self.on_reset()
        else:
            self.on_stop()

    def on_stop(self):
        self.running = False
        self.reset_button.config(text="Begin",
                                      command=self.on_reset,)

        if not self.org.participantList:
            quit()
        self.Toplabel.config(text=self.org.selected_participant.__str__())

    def plot(self, row, column):
        self.pp_plot = ParticipantPanel_Plot(self.org, self.master, self, row, column)

    def on_reset(self):
        self.running = True
        self.reset_button.config(text="Stop", command=self.on_stop)
        self.refresh()

    def refresh(self):

        self.connect_status_label.place(x=600, y=400)

        cbool, status = 0, 0
        if self.running:
            try:
                cbool, status = self.calculate_input_magnitude()
            except Exception as e:
                cbool, status = self.if_no_input()
            finally:
                self.org.selected_participant.updateStatus(cbool, status)
                self.update_labels()
                if self.org.visualize:
                    self.pp_plot.refresh()

            self.after(TIME_CONSTANT, self.refresh)

    def update_labels(self):
        self.Toplabel.config(
            text="Participant " + self.org.selected_participant.concussed_State())
        self.LAlabel.config(
            text="LA " + str(self.org.selected_participant.getlastLA()) + " m/s^2")

        self.blurb.config(text=self.org.selected_participant.info())

        colorstatus = str(self.org.selected_participant.status)[7:]

        self.StatusLabel.config(text="Status: " + colorstatus,
                                background=colorstatus,
                                foreground="blue",
                                font=LARGE_FONT)

    def calculate_input_magnitude(self):
        self.connect_status_label.config(text="")
        while arduinoData.inWaiting() == 0:
            pass
        datapacket = arduinoData.readline()
        datapacket = str(datapacket, 'utf-8')
        datapacket = three_way_vector_magnitude(datapacket)

        self.org.selected_participant.updateLA(datapacket)
        return areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)

    def if_no_input(self):
        if self.random_vals_bool:
            self.connect_status_label.config(text="NO DEVICE CONNECTED: RANDOM VALUES ASSIGNED")
            self.org.selected_participant.updateLA(dummyValues(1))
        else:
            self.connect_status_label.config(text="NO DEVICE CONNECTED")
            self.org.selected_participant.updateLA(1)
        return areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)


def three_way_vector_magnitude(datapacket):
        splitpacket = datapacket.split(',')

        x = float(splitpacket[0])
        y = float(splitpacket[1])
        z = float(splitpacket[2])

        return math.sqrt(x * x + y * y + z * z)


if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("1280x720")
    app.mainloop()
