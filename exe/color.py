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
root.iconbitmap("C:/Users/thoma/OneDrive/University/PythonStuff/LearningTKinter/exe/sun_image.ico")



def color():
    color = colorchooser.askcolor() # returns a tuple: ((r,g,b), hex-color-code)
    Label(root, text=color).pack()
    Label(root, text="You picked a color!", font = ("Bold", 12), bg = color[1]).pack()






btn = Button(root, text = "Pick a Color", command = color).pack()



root.mainloop()
