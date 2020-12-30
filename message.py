from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Messages")

# Message popups can be of different types as listed below:
# showinfo,
# showwarning,
# showerror,
# askquestion,
# askokcancel,
# askyesno


def popup():
    messagebox.showinfo("This is my popup!", "Hello World")


Button(root, text="Show Popup!", command=popup).pack()

mainloop()
