# ************** Paint App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser as color
from tkinter import filedialog as fd

##################### Global Variables ######################

global brush_color
brush_color = "black"


##################### Functions #####################

def paint(event): # Function to draw on canvas

    # Changing Brush Parameters.
    # for brush_type screen Radiobuttons.
    brush_width = int(round(brush_slider.get()))

    # Starting position
    x1 = event.x - 1
    y1 = event.y - 1

    # Ending Position
    x2 = event.x + 1
    y2 = event.y + 1

    # Drawing on canvas
    canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type.get(), smooth=True)

def change_brush_size(event): # Function to change brush size
    # Getting the
    size = int(round(brush_slider.get()))
    slider_label.config(text=size)

def change_brush_color(): # Function to change the Bursh color
    global brush_color
    brush_color = "black"
    brush_color = color.askcolor(color=brush_color)[1]

def change_canvas_color(): # Function to change the Canvas background color.
    global canvas_color
    canvas_color = "white"
    canvas_color = color.askcolor(color=canvas_color)[1]
    canvas.config(bg=canvas_color)

def clear_ink(): # Function to clear to clear the canvas.
    canvas.delete("all")

def reset_canvas_color(): # Function to rest canvas color.
    canvas.config(bg="white")

def clear_all(): # Function to reset canvas color and clear ink.
    canvas.delete("all")
    canvas.config(bg="white")

def save_image(): # Function to save the current paint job
    pass

def open_image(): # Function to open saved images
    pass


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

# Creating Brush Slider label.
slider_label = Label(brush_size_frame, text=brush_slider.get())
slider_label.pack()

# Creating Brush type Frame.
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height = 400)
brush_type_frame.grid(row=0, column=1, padx = 50)

brush_type = StringVar()
brush_type.set("round")

# Radio Buttons for brush types.
brush_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_radio1.pack(anchor=W) #anchor=W, aligns the buttons.
brush_radio2.pack(anchor=W)
brush_radio3.pack(anchor=W)

# Creating Brush color Frame
change_color_frame =  LabelFrame(brush_options_frame, text="Change Colors")
change_color_frame.grid(row=0, column=2)

# Change Brush color Button.
brush_color_btn = Button(change_color_frame, text="Brush Color", command=change_brush_color)
brush_color_btn.pack(padx=10, pady=10)

# Change canvas background
canvas_color_btn = Button(change_color_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_btn.pack(padx=10, pady=10)

# Creating Menu Bar.
main_menu = Menu(root)
root.config(menu=main_menu)

# Creating Save Menu
save_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = "Save Options", menu=save_menu)
save_menu.add_command(label="Save Image", command=save_image)
save_menu.add_command(label="Open Saved Images", command=open_image)

# Creating Clear Menu.
clear_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = "Clear Options", menu=clear_menu)
clear_menu.add_command(label="Clear Ink", command = clear_ink)
clear_menu.add_command(label="Reset Canvas Color", command = reset_canvas_color)
clear_menu.add_command(label="Clear Everything", command = clear_all)


root.mainloop()
