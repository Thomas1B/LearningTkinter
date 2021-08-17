import os
os.system("clear")


# ****** Intro to using TKinter ******
from tkinter import *


root = Tk()
root.title("Learning TKinter - hello world")
root.geometry("{}x{}".format(400,400))

'''
Grid Options:

row     - which row
column  - which column

columnspan - how many columns to span
rowspan   - how many rows to span

sticky     - location of window, E,S,W,N

'''


label = Label(root, text = "Hello World!", fg='white', bg="black")
label.grid(row=0, column = 0, columnspan=3)


Label(root, text = "Welcome!").grid(row = 1, column = 1, sticky=E)
Label(root, text ="How are you?").grid(row=2, column = 2)




root.mainloop()
