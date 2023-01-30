import tkinter as tk


class Popup:
    def __init__(self):

        def run():
            box = int(self.textbox.get('1.0', tk.END))
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
        self.textbox.pack(padx=10, pady=50, anchor="center")

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
