from tkinter import *

root = Tk()
root.title("Frames in Tkinter")

frame = LabelFrame(root, text="This is a frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b1 = Button(frame, text="Don't click here!")
b2 = Button(frame, text="....or here")

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
