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
    # messagebox.showinfo("This is my popup!", "Hello World")
    # messagebox.showwarning("This is my popup!", "Hello World")
    # messagebox.showerror("This is my popup!", "Hello World")
    # messagebox.askquestion("This is my popup!", "Hello World")
    # messagebox.askokcancel("This is my popup!", "Hello World")

    # askyesno - returns (0,1) ; askokcancel - returns (0,1) ; askquestion - returns ("yes","no")
    response = messagebox.askyesno("This is my popup!", "Hello World")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text="Show Popup!", command=popup).pack()

mainloop()
