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



canvas.create_line(0, 100, 300, 100, fill="red")
canvas.create_line(150, 0, 150, 200, fill="red")




root.mainloop()
