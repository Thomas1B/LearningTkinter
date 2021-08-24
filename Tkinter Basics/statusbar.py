import os
os.system("clear")


from tkinter import *


root = Tk()
root.title("Learning TKinter - Intro to Frames")
# root.geometry("{}x{}".format(400,400))
root.iconbitmap("Album1/sun_image.ico")



def fake_command():
    pass



def show():
    my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide():
    my_frame.grid_forget()

def new():
    hide_menu_frames()
    current_status.set("File Status")
    file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

def cut():
    hide_menu_frames()
    current_status.set("Cut Status")
    edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide_menu_frames():
    edit_frame.grid_forget()
    file_frame.grid_forget()



# Defining a Menu.
my_menu = Menu(root)
root.config(menu = my_menu)

# Create Menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

# Creating the second Menu.
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = cut)
edit_menu.add_command(label = "Copy", command = fake_command)
edit_menu.add_command(label = "Paste", command = fake_command)



# ****** File menu frame ******
file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief=SUNKEN)
# file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
file_frame_label = Label(file_frame, text = "File Frame", font = ("Helvetica", 20))
file_frame_label.grid(row=0, column = 0, padx=15, pady=15)

# ****** Edit menu frame ******
edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief=SUNKEN)
# file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
edit_frame_label = Label(edit_frame, text = "Cut Frame", font = ("Helvetica", 20))
edit_frame_label.grid(row=0, column = 0, padx=15, pady=15)


# Creating status bar
current_status = StringVar()
current_status.set("Waiting")

my_status = Label(root, textvariable = current_status, bd=2, relief="sunken", width=56, anchor=E)
my_status.grid(row=2, column=0)





root.mainloop()
