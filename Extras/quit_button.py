from tkinter import *

root = Tk()
root.title("Quit Button")

Button(root, width="20", fg="green",
       text="Click to close app", command=root.quit).pack()

root.mainloop()
