from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = "blue", fg = "white", borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")
# e.get() // To get the value of the value in the entry field e

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click Me!", state=DISABLED, padx = 50, pady = 50)
# myButton = Button(root, text = "Click Me!", command = myClick, fg = "yellow", bg = "#000000")
myButton = Button(root, text = "Enter", command = myClick, fg = "yellow", bg = "#000000")
myButton.pack() # Packs the button in the window 

# Creating a Label Widget
# myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
# myLabel2 = Label(root, text = "My name is Dev Goel").grid(row = 1, column = 0)

# Shoving it onto the screen using pack()
# myLabel.pack()

# Using grid system
# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 0)

root.mainloop()