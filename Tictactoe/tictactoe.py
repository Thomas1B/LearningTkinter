# ************** Tic Tac Toe using TKinter module **************

import os
os.system("clear") # clears terminal


################### Importing Modules ###################
from tkinter import *
from tkinter import ttk


################### Gloabal Variables ###################
global program_title
program_title = "Tic Tac Toe"


################### Functions ###################

def clicked(btn):
    pass




################### Main Program ###################5

# Making Main (root) window.
root = Tk()
root.title(program_title)
root_x = 432 # Do Not Change
root_y = 503 # Do Not Change
root.geometry("{}x{}".format(root_x, root_y))
root.resizable(width=False, height=False) # Stops user from resizes window.


# Creating Message Frame
msg_frame = Frame(root, bg='light blue', width=100, height=120)
msg_frame.pack(fill="both", expand=1)

# separator = Frame(root, bg='black', height=1) # Creating a dividing line.
# separator.pack(fill='x', pady=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

# Creating Main Frame
board_frame = Frame(root, bg='black', width = 425, height=380)
board_frame.pack(fill='both', expand=1)


# Options for Buttons.
font = ("Helvetica", 20)
relief = FLAT # relief style for Buttons.
overr = SUNKEN # overrelief style for Buttons.
width = 8 # Do Not Change
height = 3 # Do Not Change

# Creating Buttons for board
btn1 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn1)) # Rotw 1
btn2 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn2))
btn3 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn3))

btn4 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn4)) # Row 2
btn5 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn5))
btn6 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn6))

btn7 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn7)) # Row 3
btn8 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn8))
btn9 = Button(board_frame, text="", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn9))

# Griding Buttons to screen.
btn1.grid(row=0, column=0, padx=(5,2), pady=(5,2)) # Row 1
btn2.grid(row=0, column=1, padx=(2,2), pady=(5,2))
btn3.grid(row=0, column=2, padx=(2,2), pady=(5,2))

btn4.grid(row=1, column=0, padx=(5,2), pady=(2,2)) # Row 2
btn5.grid(row=1, column=1, padx=(2,2), pady=(2,2))
btn6.grid(row=1, column=2, padx=(2,2), pady=(2,2))

btn7.grid(row=2, column=0, padx=(5,2), pady=(2,5)) # Row 3
btn8.grid(row=2, column=1, padx=(2,2), pady=(2,5))
btn9.grid(row=2, column=2, padx=(2,2), pady=(2,5))





root.mainloop()
