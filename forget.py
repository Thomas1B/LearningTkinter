import os
os.system("clear")

# ************* Using Grid Forget *************

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning TKinter - Files")
root.geometry("{}x{}".format(600,400))
root.iconbitmap("Album1/sun_image.ico")


from tkinter import filedialog # need to open files.


# Submit function
def submit():
    global msg
    msg = Label(root, text="Hello " + e.get() + "!")
    msg.grid(row=3, column=0)


# Clear function
def clear():
    global msg
    msg.grid_forget()



label = Label(root, text= "Enter your name").grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0, padx=10)

btn = Button(root, text= "Submit", command = submit).grid(row=2, column=0, pady=5)
btn_clear = Button(root, text= "Clear", command = clear).grid(row=2, column=1, pady=5)








root.mainloop()
