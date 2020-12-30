from tkinter import *

root = Tk()
root.title("Dropdowns")


def show():
    my_label = Label(root, text=clicked.get()).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

Button(root, text="Show Current Selection",
       command=show).pack(padx=10, pady=10)

mainloop()
