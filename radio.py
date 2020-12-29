from tkinter import *

root = Tk()
root.title("Radio Buttons")

r = IntVar()

Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

root.mainloop()
