import os
os.system("clear")

# ************* Radio Buttons *************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to radiobuttons")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def radio():
    Label(root, text = "You picked " + str(v.get()) + "!").pack()


# Radio Buttons
v = IntVar()
v.set(1) # sets default option

rbtn1 = Radiobutton(root, text='One', variable=v, value=1).pack()
rbtn2 = Radiobutton(root, text='Two', variable=v, value=2).pack()

btn = Button(root, text="Click me!", command = radio).pack(pady=10)






root.mainloop()
