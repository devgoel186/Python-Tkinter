from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
# """)

f_name = Entry(root, width=30).grid(row=0, column=0, padx=20)
l_name = Entry(root, width=30).grid(row=1, column=0, padx=20)
address = Entry(root, width=30).grid(row=2, column=0, padx=20)
city = Entry(root, width=30).grid(row=3, column=0, padx=20)
state = Entry(root, width=30).grid(row=4, column=0, padx=20)
zipcode = Entry(root, width=30).grid(row=5, column=0, padx=20)


# Commit our changes
conn.commit()

# Close connection
conn.close()

mainloop()
