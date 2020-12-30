from tkinter import *

root = Tk()
root.title("Radio Buttons")

r = IntVar()
r.set("0")


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r,
            value=1, command=lambda: clicked(1)).pack()
Radiobutton(root, text="Option 2", variable=r,
            value=2, command=lambda: clicked(2)).pack()

# myLabel = Label(root, text=r.get())
# myLabel.pack()

root.mainloop()
