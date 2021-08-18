import os
os.system("clear")

# ************* Color Chooser*************

from tkinter import *
from PIL import ImageTk, Image

from tkinter import colorchooser # Needs to be explicitly imported.
'''
colorchooser.askcolor() returns a tuple ((r, g, b), hex-color-code).

returned_tupled[0] = (r,g,b)
returned_tupled[1] = string of hex-colorcode

'''


root = Tk()
root.title("Learning TKinter - Colors")
root.geometry("{}x{}".format(600,400))
root.iconbitmap("Album1/sun_image.ico")



def color():
    color = colorchooser.askcolor() # returns a tuple: ((r,g,b), hex-color-code)
    Label(root, text=color).pack()






btn = Button(root, text = "Pick a Color", command = color).pack()



root.mainloop()
