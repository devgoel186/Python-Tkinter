from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images and Icons")
root.iconbitmap("./src/favicon.ico") # Will set an icon for the window

my_img = ImageTk.PhotoImage(Image.open("./src/lambo.png"))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()