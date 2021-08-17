import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Images")
# root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



# ****** Intro to Images ******

from PIL import ImageTk, Image

img = ImageTk.PhotoImage(Image.open("Album1/Brisk1.png"))
img_label = Label(image = img).pack(pady=10)








root.mainloop()
