# ************** Paint App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *



##################### Main Program #####################

# Making Main (root) window.
root = Tk()
root.title("Paint Program")
root.geometry("{}x{}".format(800,800))
# root.iconbitmap()

w = 600 # Width for canvas
h = 400 # Height for canvas
canvas = Canvas(root, width=w, height=h, bg="white")
canvas.pack(pady=20)


x1 = 0
y1 = 100

x2 = 300
y2 = 100
canvas.create_line(x1, y1, x2, y2, fill="red")




root.mainloop()
