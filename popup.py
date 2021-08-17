import os
os.system("clear")

# ************* Pop Up Boxes *************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Pop Up Message Boxes")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")


'''
Types of Popup boxes:
showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
'''
from tkinter import messagebox # Need to explicit import this!!!


def popup():
    messagebox.showinfo("Showinfo Popup", "This is a \"showinfo\" pop up box.")



popup_btn = Button(root, text = "Click to see Pop Up!", command=popup)
popup_btn.pack(pady=20)













root.mainloop()
