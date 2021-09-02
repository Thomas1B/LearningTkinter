# ************** Tic Tac Toe using TKinter module **************

import os
os.system("clear") # clears terminal


################### Importing Modules ###################
from tkinter import *


################### Gloabal Variables ###################
global program_title
program_title = "Tic Tac Toe"

################### Functions ###################






################### Main Program ###################

# Making Main (root) window.
root = Tk()
root.title(program_title)
root_x = 700 # window sizes
root_y = 500
root.geometry("{}x{}".format(root_x, root_y))







root.mainloop()
