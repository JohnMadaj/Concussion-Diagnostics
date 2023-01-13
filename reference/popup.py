import tkinter as tk


class Popup:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Concussion Diagnostics")

        self.textbox = tk.Text(self.root, height=1)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=50, anchor="center")

        button = tk.Button(self.root, text="Show Message", command=self.run)
        button.pack(padx=10, pady=10, anchor="s")

        self.root.mainloop()

    def shortcut(self, event):
        if event.keysym == "Return":
            self.run()

    def run(self):
        box = str(self.textbox.get('1.0', tk.END))
        if int(box) > 0:
            self.root.destroy()


if __name__ == "__main__":
    Popup()
