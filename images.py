from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images and Icons")
root.iconbitmap("./src/favicon.ico")  # Will set an icon for the window

my_img1 = ImageTk.PhotoImage(Image.open("./src/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./src/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./src/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("./src/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("./src/img5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)

button_next = Button(root, text="<<", command="")
button_prev = Button(root, text=">>", command="")
button_next.grid(row=1, column=0)
button_prev.grid(row=1, column=2)

root.mainloop()
