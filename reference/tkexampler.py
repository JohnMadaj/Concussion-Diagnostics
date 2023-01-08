import tkinter as tk

font1 = ('Arial', 18)

root = tk.Tk()

root.geometry("800x500")
root.title("Jacks software")

label = tk.Label(root, text="Im making software! -jack", font=('Arial', 33))
label.pack(padx=50)

textbox = tk.Text(root, font=('Impact', 12), height=3)
textbox.pack(padx=20)

myentry = tk.Entry(root)
myentry.pack()

button = tk.Button(root, text="Button that doesnt do anything yet", font=('Arial', 10))
button.pack(padx=10, pady=40)

# menu = tk.Menu(root, title="Menu")

buttonframe = tk.Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="uno", font=font1)
btn1.grid(row=0, column=0, sticky="we") #we = west, east (acronym)

btn2 = tk.Button(buttonframe, text="dos", font=font1)
btn2.grid(row=0, column=1, sticky="we") #we = west, east (acronym)

btn3 = tk.Button(buttonframe, text="tres", font=font1)
btn3.grid(row=0, column=2, sticky="we") #we = west, east (acronym)

btn4 = tk.Button(buttonframe, text="get", font=font1)
btn4.grid(row=1, column=0, sticky="we") #we = west, east (acronym)

btn5 = tk.Button(buttonframe, text="more", font=font1)
btn5.grid(row=1, column=1, sticky="we") #we = west, east (acronym)

btn6 = tk.Button(buttonframe, text="buttons", font=font1)
btn6.grid(row=1 , column=2, sticky="we") #we = west, east (acronym)

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="placed")
anotherbtn.place(x=139, y=42, height=100, width=100)


root.mainloop()




