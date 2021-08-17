import os
os.system("clear")

# ************* Creating New Windows *************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Windows")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def open():
    window = Toplevel()
    window.title("New Window")
    window.geometry("{}x{}".format(300,200))
    window.iconbitmap("Album1/sun_image.ico")
    Label(window, text = "This is a new window!").pack(pady=10)
    window.mainloop()


Button(root, text = 'Open new window', command = open).pack(pady=5)




root.mainloop()
