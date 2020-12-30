from tkinter import *

root = Tk()
root.title("Radio Buttons")

r = IntVar()
r.set("0")

list_frame = LabelFrame(
    root, text="Types of Pizzas Available", padx=50, pady=50)
list_frame.pack(padx=10, pady=10)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(list_frame, text=text, variable=pizza,
                value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text="Your selected type = " + value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r,
#             value=1, command=lambda: clicked(1)).pack()
# Radiobutton(root, text="Option 2", variable=r,
#             value=2, command=lambda: clicked(2)).pack()

Button(root, text="Click Me!", command=lambda: clicked(pizza.get())).pack(pady=10)

# myLabel = Label(root, text=r.get())
# myLabel.pack()

root.mainloop()
