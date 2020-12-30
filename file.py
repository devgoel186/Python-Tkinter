from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Open any file!")


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="./src", title="Select a file!", filetypes=(
        ("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All Files", "*.*")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    label = Label(image=my_img).pack()


my_btn = Button(root, text="Open File", command=open).pack()


mainloop()
