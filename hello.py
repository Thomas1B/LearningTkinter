import os
os.system("clear")


# ****** Intro to using TKinter ******
from tkinter import *


root = Tk()
root.title("Learning TKinter - hello world")
root.geometry("{}x{}".format(400,400))


label = Label(root, text = "Hello World!").pack()





root.mainloop()
