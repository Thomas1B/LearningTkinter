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

def add():
    pass


def subtract():
    pass

def multiply():
    pass

def divide():
    pass









# # menu items
math_menu = Menu(main_menu)
main_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Addition", command=add)
math_menu.add_command(label="Subtraction", command=subtract)
math_menu.add_command(label="Mutliplication", command=multiply)
math_menu.add_command(label="Division", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit Program", command=root.quit)






root.mainloop()
