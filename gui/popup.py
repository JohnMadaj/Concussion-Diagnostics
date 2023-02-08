from constants import *


class Popup:
    def __init__(self):

        def run():
            box = int(self.textbox.get('1.0', tk.END))
            # com_box = int(self.com_box.get('1.0', tk.END))
            # if com_box > 0:
            #     COMPORT = com_box
            if int(box) > 0:
                self.root.destroy()
                self.output = box

        def run_default():
            self.root.destroy()
            self.output = 10

        def shortcut(event):
            if event.keysym == "Return":
                run()

        self.root = tk.Tk()
        self.root.geometry("400x270")
        self.root.title("Concussion Diagnostics")

        label = tk.Label(self.root, text="Number of Participants")
        label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=1)
        self.textbox.bind("<KeyPress>", shortcut)
        self.textbox.pack(padx=10, pady=0, anchor="center")


        label2 = tk.Label(self.root, text="COM Port (change from default):")
        label2.pack(padx=10, pady=10)
        #
        # self.com_box = tk.Text(self.root, height=1)
        # self.com_box.bind("<KeyPress>", shortcut)
        # self.com_box.pack(padx=10, pady=0, anchor="center")

        button = tk.Button(self.root, text="Run", command=run)
        button.pack(padx=10, pady=10, anchor="s")

        default_button = tk.Button(self.root, text="Run Default (10)", command=run_default)
        default_button.pack(anchor="s")

        self.textbox.bind("<KeyPress>", shortcut)
        self.output = 0
        self.root.mainloop()


if __name__ == "__main__":
    p = Popup()
    print(p.output)
