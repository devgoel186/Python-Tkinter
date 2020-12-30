from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Open any file!")

root.filename = filedialog.askopenfilename(initialdir="./src", title="Select a file!", filetypes=(
    ("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All Files", "*.*")))
Label(root, text=root.filename).pack()

mainloop()
