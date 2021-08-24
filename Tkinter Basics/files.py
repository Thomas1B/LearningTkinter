import os
os.system("clear")

# ************* Open files with Filedialog *************

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning TKinter - Files")
root.geometry("{}x{}".format(600,400))
root.iconbitmap("Album1/sun_image.ico")


from tkinter import filedialog # need to open files.


# Open filedialog Box


def open_file():
    root.filename = filedialog.askopenfilename(initialdir="/LearningTKinker", title="Open a File", filetypes = (("PNG files","*.png"), ("All files","*.*")))
    Label(root, text= "FilePath: " + root.filename).pack()

    global img
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(root, image=img)
    img_label.pack(pady=10)
    root.geometry("{}x{}".format(800,600))




btn = Button(root, text="Open a File", command=open_file).pack(pady=10)









root.mainloop()
