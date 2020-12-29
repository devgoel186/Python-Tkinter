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


def forward(image_no):
    global my_label, button_next, button_prev, image_list
    my_label.grid_forget()
    my_label = Label(image=image_list[image_no-1])
    button_prev = Button(root, text="<<", command=lambda: backward(image_no-1))

    if image_no == len(image_list):
        button_next = Button(root, text=">>", state=DISABLED)
    else:
        button_next = Button(
            root, text=">>", command=lambda: forward(image_no+1))

    button_prev.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


def backward(image_no):
    global my_label, button_next, button_prev, image_list
    my_label.grid_forget()
    my_label = Label(image=image_list[image_no-1])
    button_next = Button(root, text=">>", command=lambda: forward(image_no+1))

    if image_no == 1:
        button_prev = Button(root, text="<<", state=DISABLED)
    else:
        button_prev = Button(
            root, text="<<", command=lambda: backward(image_no-1))

    button_prev.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


button_prev = Button(root, text="<<", state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_next = Button(root, text=">>", command=lambda: forward(2))
button_prev.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
