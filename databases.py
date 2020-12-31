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

c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text, 
    address text, 
    city text, 
    state text, 
    zipcode integer
)
""")

# Commit our changes
conn.commit()

# Close connection
conn.close()

mainloop()
