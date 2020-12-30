from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")

# var = IntVar()

# c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
# c.pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!",
                variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


def check_status():
    my_label = Label(root, text=var.get()).pack()


Button(root, text="Check status!", command=check_status).pack(padx=10, pady=10)

mainloop()
