import tkinter as tk
from tkinter import messagebox

font1 = ("Arial", 18)
font2 = ("Times New Roman", 12)


class GUI:

    def __init__(self):
        self.num = 1
        self.root = tk.Tk()


        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openfun)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="This button doesnt do anything")

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.root.title("Class GUI")
        self.label = tk.Label(self.root, text="Class Software (Q to close)", font=font1)
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=2, font=font2)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_var = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=font1, variable=self.check_var)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=font1, command=self.show_message)
        # passing show_message as function hence no parenthesis
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def show_message(self):
        if self.check_var.get():
            messagebox.showinfo(title="Message", message="hitler had some good points")
            print(self.num)
            self.num +=1
        else:
            print(self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        print(event)
        if event.keysym == "Control_L":
            print("You hit CTRL L")
            self.show_message()
        if event.keysym == "q":
            self.on_closing()

    def on_closing(self):
        if messagebox.askyesno(title="Are u sure?", message="???? are you?"):
            print("Goodbye, come again!")
            self.root.destroy()

    def openfun(self):
        messagebox.showinfo(title="Open", message="You fucking idiot theres nothing to open this isnt a real program")


if __name__ == "__main__":
    gui = GUI()
