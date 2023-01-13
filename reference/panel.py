import tkinter as tk
from PIL import Image, ImageTk


class Panel:

    def __init__(self, frame):

        self.root = tk.Canvas(frame, width=600, height=400)
        self.root.pack()

        self.root.config(bg="tan")

        # self.root.toplabel = tk.Label(text="Panel Canvas")
        # self.root.toplabel.place(anchor=tk.CENTER, rely=0, relx=0)
        #
        # self.root.btn = tk.Button(self.root, text="button")
        # self.root.btn.pack()

        # img = Image.open("diagram.png")
        # # img=img.resize((200,200))
        # self.root.create_image(10, 10, image=ImageTk.PhotoImage(img))

        # rectangle: x1, y1: top left
        #            x2, y2: bottom right
        self.root.create_rectangle(50, 100, 550, 300, fill="light blue")

        # lines: x1, y1, x2, y2, fill=color
        self.root.create_line(0, 100, 600, 100, fill="blue")
        self.root.create_line(0, 200, 600, 200, fill="blue")


if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("TK")
    # # frame = tk.Frame(gui)
    #
    Panel(gui)
    # # frame.pack()
    gui.mainloop()
    # Panel(0)

