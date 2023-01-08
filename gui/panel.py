import tkinter as tk
from PIL import Image, ImageTk


class Panel:

    def __init__(self, frame):
        gui = tk.Tk()

        self.root = tk.Canvas(gui, width=600, height=400)
        self.root.pack()

        self.root.config(bg="blue")

        # self.root.toplabel = tk.Label(text="shit")
        # self.root.toplabel.pack(padx=10, pady=10)
        #
        # self.root.btn = tk.Button(self.root, text="button")
        # self.root.btn.pack()

        # img = Image.open("diagram.png")
        # # img=img.resize((200,200))
        # self.root.create_image(10, 10, image=ImageTk.PhotoImage(img))

        gui.mainloop()


if __name__ == "__main__":
    # gui = tk.Tk()
    # gui.title("TK")
    # # frame = tk.Frame(gui)
    #
    # Panel(gui)
    # # frame.pack()
    # gui.mainloop()
    Panel(0)

