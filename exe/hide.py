import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Pack Forget and Destroy")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Icon.ico")


# ****** Intro to Pack forget and destroy ******

'''
label.pack_forget() clears the label from the screen, which can be packed again.
label.destroy deletes the label entirely.
'''




def click():
    global label1
    label1 = Label(root, text = "Hello " + e.get() + "!")
    label1.pack()


def hide():
    global label1
    label1.pack_forget()


def show():
    global label1
    label1.pack()



Label(root, text = "Enter your name").pack()

e = Entry(root, font = ("Helvetica", 18))
e.pack(pady=10)

btn1 = Button(root, text = "Click me!", command = click).pack(pady=20)
btn2 = Button(root, text = "Hide", command = hide).pack()
btn3 = Button(root, text = "Show", command = show).pack()








root.mainloop()
