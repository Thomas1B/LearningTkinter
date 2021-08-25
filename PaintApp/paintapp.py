# ************** Paint App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *
import tkinter.ttk as ttk


##################### Functions #####################

def paint(event): # Function to draw on canvas

    # Changing Brush Parameters.
    brush_width = int(round(brush_slider.get()))
    brush_color = "green"
    # Brush types: BUTT, ROUND, PROJECTING
    brush_type = ROUND

    # Starting position
    x1 = event.x - 1
    y1 = event.y - 1

    # Ending Position
    x2 = event.x + 1
    y2 = event.y + 1

    # Drawing on canvas
    canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)

def change_brush_size(event): # Function to change brush size
    # Getting the
    size = int(round(brush_slider.get()))
    slider_label.config(text=size)




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

canvas.bind("<B1-Motion>", paint) # Binding canvas to left-click on mouse

# Creating Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Creating Brush Size frame
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)

# Creating Brush Slider
brush_slider = ttk.Scale(brush_size_frame, from_=100, to=1, command=change_brush_size, orient=VERTICAL, value=10)
brush_slider.pack(padx=10, pady=10)

# Creating Brush Slider label
slider_label = Label(brush_size_frame, text=brush_slider.get())
slider_label.pack()


root.mainloop()
