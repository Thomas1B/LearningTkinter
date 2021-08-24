import os
os.system("clear")


# ****** Intro to using TKinter ******
from tkinter import *


root = Tk()
root.title("Learning TKinter - hello world")
root.geometry("{}x{}".format(400,400))


label = Label(root, text = "Hello World!")
label.pack()

'''
Label options:

fg      - foreground color
bg      - background color
height  - height length
width   - width length

relief - effects. FLAT, RAISED, SUNKEN, GROOVE, RIDGE. default is FLAT.
.pack(padx=x, pady = y) giving padding to Label.


'''

Label(root, text = "Welcome!", fg = "red", bg = "green", font = ("Helvetica", 32), relief = SUNKEN).pack(pady=50)





root.mainloop()
