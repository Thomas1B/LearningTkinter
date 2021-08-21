import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Images")
# root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



# ****** Intro to Images ******

from PIL import ImageTk, Image

# img1 = ImageTk.PhotoImage(Image.open("Album1/Brisk1.png"))
img2 = PhotoImage(file="Album1/Brisk2.png")
# img_label1 = Label(image = img1).pack(pady=10)
img_label = Label(image = img2).pack(pady=10)








root.mainloop()
