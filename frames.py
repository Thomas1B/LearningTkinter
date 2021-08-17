import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Frames")
root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def fake_command():
    pass



def show():
    my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)




def hide():
    my_frame.grid_forget()




# Defining a Menu.
my_menu = Menu(root)
root.config(menu = my_menu)

# Create Menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = fake_command)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

# Creating the second Menu.
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = fake_command)
edit_menu.add_command(label = "Copy", command = fake_command)
edit_menu.add_command(label = "Paste", command = fake_command)

# Creating a third menu
view_menu = Menu(my_menu)
my_menu.add_cascade(label = "View", menu = view_menu)

# Creating a sub menu
options_menu = Menu(my_menu)
file_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Preferences", command = fake_command)
options_menu.add_command(label = "Settings", command = fake_command)


view_menu.add_command(label = "Increase Font Size", command = fake_command)
view_menu.add_command(label = "Decrease Font Size", command = fake_command)


show_button = Button(root, text = "Show", command=show).grid(row=0, column=0)
show_button = Button(root, text = "Hide", command=hide).grid(row=0, column=1)


# ************ Intro to Frames ************

my_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief=SUNKEN)
my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

frame_label = Label(my_frame, text = "Hello World!", font = ("Helvetica", 20))
frame_label.grid(row=0, column = 0, padx=15, pady=15)





root.mainloop()
