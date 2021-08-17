import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - icons")
root.geometry("{}x{}".format(400,400))


# ****** Intro to icons ******

filepath = "Album1/sun_image.ico"
root.iconbitmap(filepath)





###########################################

def click():
    label1 = Label(root, text = "Hello " + e.get())
    label1.pack()


Label(root, text = "Enter your name").pack()

e = Entry(root, font = ("Helvetica", 18))
e.pack(pady=10)

btn1 = Button(root, text = "Click me!", command = click).pack(pady=20)






root.mainloop()
