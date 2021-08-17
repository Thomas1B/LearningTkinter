import os
os.system("clear")

# ************* Combo boxes*************

from tkinter import *


root = Tk()
root.title("Learning TKinter - Combo Boxes")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def Select():
    response = my_combo.get()

    if response == "Monday":
        Label(root, text="You selected Monday!").pack()
    elif response == "Tuesday":
        Label(root, text="You selected Tuesday!").pack()
    elif response == "Wednesday":
        Label(root, text="You selected Wednesday!").pack()
    else:
        Label(root, text = "Invalid Entry!").pack()


'''
Combo Boxes:

'''
from tkinter import ttk # must be explicitly imported!!!




options = ["Monday", "Tuesday", "Wednesday"]

my_combo = ttk.Combobox(root, value = options)
# my_combo.current(0) # sets default option.
my_combo.pack(pady=10)


Button(root, text = "Select", command=Select).pack()


root.mainloop()
