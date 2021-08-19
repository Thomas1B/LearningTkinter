import os
os.system("clear")

# ************* Making a flashcard app *************

from tkinter import *
from PIL import ImageTk, Image
from tkinter import colorchooser


root = Tk()
root.title("Learning TKinter - Flashcard")
root.geometry("{}x{}".format(600,400))
root.iconbitmap("globe.ico")




# Creating Main Menu
main_menu = Menu(root)
root.config(menu = main_menu)




# Functioning for menu items

def add(): # Addition Function
    hide_frames()
    add_frame.pack(fill="both", expand=1)


def subtract(): # Subtraction Function
    hide_frames()
    subtract_frame.pack(fill="both", expand=1)

def multiply(): # Mutliplication Function
    hide_frames()
    multiply_frame.pack(fill="both", expand=1)



def divide(): # Division Function
    hide_frames()
    divide_frame.pack(fill="both", expand=1)


def hide_frames(): # Hide Function
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()






# # menu items
math_menu = Menu(main_menu)
main_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Addition", command=add)
math_menu.add_command(label="Subtraction", command=subtract)
math_menu.add_command(label="Mutliplication", command=multiply)
math_menu.add_command(label="Division", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit Program", command=root.quit)


# Creating math Frames
add_frame = Frame(root, width=400, height=400, bg="blue")
subtract_frame = Frame(root, width=400, height=400, bg="red")
multiply_frame = Frame(root, width=400, height=400, bg="yellow")
divide_frame = Frame(root, width=400, height=400, bg="green")




root.mainloop()
