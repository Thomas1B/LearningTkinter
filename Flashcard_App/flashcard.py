import os
os.system("clear")

# ************* Making a flashcard app *************

from tkinter import *
# from PIL import ImageTk, Image
import random as r

root = Tk()
root.title("Learning TKinter - Flashcard")
root.geometry("{}x{}".format(600,400))
root.iconbitmap("globe.ico")




# Creating Main Menu
main_menu = Menu(root)
root.config(menu = main_menu)

# Functions to check if the answers given are correct.

def add_correct(a, b):
    correct = a + b

    # Output Message to display
    global add_answer
    if int(add_answer.get()) == correct:
        text = "{} is Correct!".format(add_answer.get())
        add_correct_label.config(text=text, font = ("bold", 32))
    else:
        text = "{} is Incorrect!{} Try Again!".format(add_answer.get(), "\n\n")
        add_correct_label.config(text=text, font = ("bold", 32))




# Functioning for menu items

def add(): # Addition Function
    hide_frames()
    add_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10)) # random numbers
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}+{} = ?".format(num1.get(),num2.get())
    question_label = Label(add_frame, text=text, font = ('Helvetica', 32))
    question_label.pack()

    # Creating Entry box
    global add_answer
    add_answer = Entry(add_frame)
    add_answer.pack(pady=5)

    # Button to submit answer
    global add_btn
    add_btn = Button(add_frame, text = "Answer!", command = lambda: add_correct(num1.get(), num2.get()))
    add_btn.pack(pady=10)

    # Correct or Incorrect message
    global add_correct_label
    add_correct_label = Label(add_frame, text = "Enter the Answer!", font = ("bold", 16))
    add_correct_label.pack(pady=5)






def subtract(): # Subtraction Function
    hide_frames()
    subtract_frame.pack(fill="both", expand=1)

def multiply(): # Mutliplication Function
    hide_frames()
    multiply_frame.pack(fill="both", expand=1)



def divide(): # Division Function
    hide_frames()
    divide_frame.pack(fill="both", expand=1)


def hide_frames(): # Hide Function
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()






# # menu items
math_menu = Menu(main_menu)
main_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Addition", command=add)
math_menu.add_command(label="Subtraction", command=subtract)
math_menu.add_command(label="Mutliplication", command=multiply)
math_menu.add_command(label="Division", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit Program", command=root.quit)


# Creating math Frames
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400)
multiply_frame = Frame(root, width=400, height=400)
divide_frame = Frame(root, width=400, height=400)




root.mainloop()
