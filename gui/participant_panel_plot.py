from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


class ParticipantPanel_Plot:
    def __init__(self, master):
        fig = Figure(figsize=(5, 5),
                     dpi=100)
        fig.set_animated(True)

        y = master.org.selected_participant.LA

        # adding the subplot
        plot1 = fig.add_subplot(111)
        plot1.set_xlim(right=20)
        plot1.set_ylim(top=100)

        # plotting the graph
        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig,
                                   master=master)
        canvas.draw()

        canvas.get_tk_widget().grid(row=3,
                                    columnspan=2,
                                    sticky="news")