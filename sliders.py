from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders!")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL).pack()

mainloop()
