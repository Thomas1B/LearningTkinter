import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Buttons")
root.geometry("{}x{}".format(400,400))


# ****** Intro to Buttons ******


def click():
    label1 = Label(root, text = "Hello " + e.get())
    label1.pack()




Label(root, text = "Enter your name").pack()

e = Entry(root, font = ("Helvetica", 18))
e.pack(pady=10)

btn1 = Button(root, text = "Click me!", command = click).pack(pady=20)









root.mainloop()
