import math
import tkinter as tk

from Diagnostic import areTheyConcussed
from organizer.organizer import Organizer
from dummy import *
from constants import *

# class Main(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.grid_rowconfigure(0, weight=1)  # this needed to be added
#         self.grid_columnconfigure(0, weight=1)  # as did this
#         self.title("GUI")
#         self.attributes('-fullscreen', True)
#         # self.configure(background=bg)
#
#         main_container = tk.Frame(self)
#         main_container.grid(column=0, row=0, sticky="nsew")
#         main_container.grid_rowconfigure(0, weight=1)
#         main_container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for fr in (MainPage,):
#             frame = fr(main_container, self)
#             self.frames[fr] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.show_frame(MainPage)
#
#     def show_frame(self, pointer):
#         frame = self.frames[pointer]
#         frame.tkraise()


class ParticipantPanel(tk.Frame):

    def __init__(self, parent, controller, organizer):

        # self.org = Organizer(createListOfDummyParticipants(10))
        self.org = organizer
        tk.Frame.__init__(self, parent)
        self.running = False

        def build_grid():
            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=1)

            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.rowconfigure(3, weight=1)
            self.rowconfigure(4, weight=1)
        build_grid()

        self.Toplabel = tk.Label(self, text="Participant Name:", font=HEADER_FONT)
        self.StatusLabel = tk.Label(self, text="Status:", font=LARGE_FONT)
        self.LAlabel = tk.Label(self, text="LA: 0 m/s^2", font=LARGE_FONT)

        self.Toplabel.grid(row=0, columnspan=2, sticky="news")
        self.StatusLabel.grid(row=1, columnspan=2, sticky="news")
        self.LAlabel.grid(row=2, columnspan=2, sticky="news")

        self.plot()
        self.on_stop()

    def on_stop(self):
        self.running = False
        self.reset_button = tk.Button(self,
                                      text="Reset with New Participant",
                                      command=self.on_reset,
                                      font=BUTTON_FONT)

        self.exit_button = tk.Button(self,
                                     text="Exit",
                                     command=quit,
                                     font=BUTTON_FONT)

        self.reset_button.grid(row=4,
                               column=0,
                               sticky='nwse')

        self.exit_button.grid(row=4,
                              column=1,
                              sticky='nsew')

        if not self.org.participantList:
            quit()
        self.Toplabel.config(text="Participant ")

    def plot(self):
        fig = Figure(figsize=(5, 5),
                     dpi=100)
        fig.set_animated(True)

        y = self.org.selected_participant.LA

        # adding the subplot
        plot1 = fig.add_subplot(111)
        plot1.set_xlim(right=20)
        plot1.set_ylim(top=100)

        # plotting the graph
        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig,
                                   master=self)
        canvas.draw()

        canvas.get_tk_widget().grid(row=3,
                                    columnspan=2,
                                    sticky="news")

    def on_reset(self):
        self.running = True
        self.org.select_new_participant()
        self.reset_button.config(text="Stop", command=self.on_stop)
        self.refresh()

    def refresh(self):
        cbool, status = 0, 0
        if self.running:
            try:
                cbool, status = self.calculate_input_magnitude()
            except Exception as e:
                cbool, status = self.if_no_input()
            finally:
                self.org.selected_participant.updateStatus(cbool, status)
                self.update_labels()
                self.plot()
            self.after(TIME_CONSTANT, self.refresh)

    def update_labels(self):
        self.Toplabel.config(
            text="Participant " + self.org.selected_participant.__str__())
        self.LAlabel.config(
            text="LA " + str(self.org.selected_participant.getlastLA()) + " m/s^2")

        colorstatus = str(self.org.selected_participant.status)[7:]

        self.StatusLabel.config(text="Status: " + colorstatus,
                                background=colorstatus,
                                foreground="blue",
                                font=LARGE_FONT)

    def calculate_input_magnitude(self):
        while arduinoData.inWaiting() == 0:
            pass
        datapacket = arduinoData.readline()
        datapacket = str(datapacket, 'utf-8')
        splitpacket = datapacket.split(',')

        x = float(splitpacket[0])
        y = float(splitpacket[1])
        z = float(splitpacket[2])

        self.org.selected_participant.updateLA(
            math.sqrt(x * x + y * y + z * z))
        return areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)

    def if_no_input(self):
        self.org.selected_participant.updateLA(dummyValues(1))
        # self.org.selected_participant.updateLA(10)
        print("didnt work my guy my bro my homie")
        return areTheyConcussed(LA=self.org.selected_participant.getlastLA(), LAthreshold=LA_GENERIC)
        # status = e


if __name__ == '__main__':
    app = Main()
    app.geometry("1280x720")
    app.mainloop()
