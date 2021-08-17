import os
os.system("clear")

# ************* Radio Buttons *************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Check Boxes")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def Toppings():
    if v.get() == "Pepperoni":
        Label(root, text = "You picked Pepperoni").pack()
    else:
        Label(root, text = "You did not pick Pepperoni").pack()


# Check Boxes
v = StringVar() # sets default option

check = Checkbutton(root, text = "Pepperoni", variable = v, onvalue = "Pepperoni", offvalue = "No Pepperoni")
check.deselect()
check.pack()


btn = Button(root, text = "Select Toppings", command = Toppings)
btn.pack(pady=10)






root.mainloop()
