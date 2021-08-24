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
    global row
    global msg_list
    msg = Label(root, text="Hello " + e.get() + "!")
    msg.grid(row=row, column=0)
    msg_list.append(msg)
    e.delete(0, END) # clears Entry of text
    row+=1


# Clear function
msg_list = []
def clear():
    global msg_list
    e.delete(0, END) # clears Entry of text
    for msg in msg_list:
        msg.grid_forget()



label = Label(root, text= "Enter your name", font= ("Bold", "16"))
label.grid(row=0, column=0, columnspan=2, padx=10)

e = Entry(root)
e.grid(row=1, column=0, padx=10, columnspan=2)

row = 3 # default row to print message, see submit().
btn = Button(root, text= "Submit", command = submit).grid(row=2, column=0, pady=5)
btn_clear = Button(root, text= "Clear Screen", command = clear).grid(row=2, column=1, pady=5)








root.mainloop()
