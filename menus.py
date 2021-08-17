import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Menus")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")


# ****** Intro to Menus ******



def fake_command():
    pass







# Defing a Menu.
my_menu = Menu(root)
root.config(menu = my_menu)

# Create Menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = fake_command)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)










root.mainloop()
