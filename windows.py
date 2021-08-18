import os
os.system("clear")

# ************* Creating New Windows *************

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning TKinter - Main Window ")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")

'''
****** Puts windows into the taskbar ******
iconify minimizes the window.
deiconify shows the window.


'''



def open():
    window = Toplevel()
    window.title("New Window")
    window.geometry("{}x{}".format(600,800))
    window.iconbitmap("Album1/sun_image.ico")
    Label(window, text = "This is Brisk!", font=("Helvetica, 16")).pack(pady=10)


    img = ImageTk.PhotoImage(Image.open("Album1/Brisk1.png"))
    img_label = Label(window, image=img).pack()



    Button(window, text="Quit", command = window.destroy).pack()

    # Minimize Original Window, puts windows to taskbar
    Button(window, text="Show Main Window", command = root.deiconify).pack() # show window
    Button(window, text="Hide Main Window", command = root.iconify).pack() # hide window

    # Withdraw Original Window, Doesn't show in taskbar
    # Button(window, text="Show Main Window", command = root.deiconify).pack()
    # Button(window, text="Hide Main Window", command = root.withdraw).pack()

    Button(window, text="Quit Main Window", command = root.destroy).pack()

    window.mainloop()





Button(root, text = 'Open new window', command = open).pack(pady=5)
Button(root, text="Quit Main Window", command = root.destroy).pack()




root.mainloop()
