import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Buttons")
root.geometry("{}x{}".format(400,400))


# ****** Intro to Buttons ******


def click():
    Label(root, text = "You clicked me!").pack()




btn1 = Button(root, text = "Click me!", command = click).pack(pady=20)








root.mainloop()
