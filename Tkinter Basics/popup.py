import os
os.system("clear")

# ************* Pop Up Boxes *************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Pop Up Message Boxes")
root.geometry("{}x{}".format(400,400))
# root.iconbitmap("Album1/sun_image.ico")


'''
Types of Popup boxes:
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

askokcancel returns True for Ok, False for Cancel.
askquestion returns yes or no.
askyesno returns 1 for Yes, 0 for No.
'''
from tkinter import messagebox # Need to explicit import this!!!


def showinfo():
    messagebox.showinfo("Showinfo Popup", "This is a \"showinfo\" pop up box.")


def askyesno():
    response = messagebox.askyesno("askyesno Popup", "This is a \"askyesno\" pop up box.")

    if (response == 1):
        Label(root, text = "askyesno - You answered yes!").pack()
    else:
        Label(root, text = "askyesno - You answered no!").pack()


def askquestion():
    response = messagebox.askquestion("askyesno Popup", "This is a \"askquestion\" pop up box.")

    if (response == "yes"):
        Label(root, text = "askquestion - You answered yes!").pack()
    else:
        Label(root, text = "askquestion - You answered no!").pack()


def askokcancel():
    response = messagebox.askokcancel("askokcancel Popup", "This is a \"askokcancel\" pop up box.")

    if (response == True):
        Label(root, text = "askokcancel - You clicked Ok!").pack()
    else:
        Label(root, text = "askokcancel - You clicked Cancel!").pack()




Button(root, text = "Click to see showinfo popup!", command=showinfo).pack(pady=5)
Button(root, text = "Click to see askyesno popup!", command=askyesno).pack(pady=5)
Button(root, text = "Click to see askquestion popup!", command=askquestion).pack(pady=5)
Button(root, text = "Click to see askokcancel popup!", command=askokcancel).pack(pady=5)











root.mainloop()
