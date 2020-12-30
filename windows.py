from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Hello there!")


# Toplevel() will create a second window alongwith the main root window
def open():
    top = Toplevel()
    top.title("My Second Window!")
    Button(top, text="Close Window!", command=top.destroy).pack(padx=20, pady=20)


btn = Button(root, text="Open Second Window",
             command=open).pack(padx=50, pady=50)

mainloop()
