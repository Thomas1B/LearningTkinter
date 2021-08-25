# ************** Paint App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *


##################### Functions #####################

def paint(event): # Function to draw
    canvas.config(bg="black")



##################### Main Program #####################

# Making Main (root) window.
root = Tk()
root.title("Paint Program")
root.geometry("{}x{}".format(800,800))
# root.iconbitmap()

# Creating Canvas Widgit.
w = 600 # Width for canvas
h = 400 # Height for canvas
canvas = Canvas(root, width=w, height=h, bg="white")
canvas.pack(pady=20)



canvas.create_line(0, 100, 300, 100, fill="red")
canvas.create_line(150, 0, 150, 200, fill="red")

canvas.bind("<B1-Motion>", paint) # left-click on mouse



root.mainloop()
