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

def add_correct(a, b): # Checking if Addition is correct.
    correct = a + b

    # Updating Output Message depending if the given answer is correct.
    global add_answer
    if int(add_answer.get()) == correct:
        text = "{}+{} = {} is Correct!".format(a,b,add_answer.get())
        add_correct_label.config(text=text, font = ("bold", 32))
    else:
        text = "{}+{} = {} is Incorrect!{} Try Again!".format(a,b,add_answer.get(), "\n\n")
        add_correct_label.config(text=text, font = ("bold", 32))


    # Creating a new question if the given answer was correct.
    if int(add_answer.get()) == correct:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}+{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    add_answer.delete(0, "end")


def subtract_correct(a, b): # Checking if Subtraction is correct.
    correct = a - b

    # Updating Output Message depending if the given answer is correct.
    global subtract_answer
    if int(subtract_answer.get()) == correct:
        text = "{}-{} = {} is Correct!".format(a,b,subtract_answer.get())
        subtract_correct_label.config(text=text, font = ("bold", 32))
    else:
        text = "{}-{} = {} is Incorrect!{} Try Again!".format(a,b,subtract_answer.get(), "\n\n")
        subtract_correct_label.config(text=text, font = ("bold", 32))


    # Creating a new question if the given answer was correct.
    if int(subtract_answer.get()) == correct:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}-{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    subtract_answer.delete(0, "end")


def multiply_correct(a, b): # Checking if Mutliplication is correct.
    correct = a * b

    # Updating Output Message depending if the given answer is correct.
    global multiply_answer
    if int(multiply_answer.get()) == correct:
        text = "{}+{} = {} is Correct!".format(a, b, multiply_answer.get())
        multiply_correct_label.config(text=text, font = ("bold", 32))
    else:
        text = "{}+{} = {} is Incorrect!{} Try Again!".format(a, b, multiply_answer.get(), "\n\n")
        multiply_correct_label.config(text=text, font = ("bold", 32))


    # Creating a new question if the given answer was correct.
    if int(multiply_answer.get()) == correct:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}x{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    multiply_answer.delete(0, "end")


def divide_correct(a, b): # Checking if Division is correct.
    correct = round(a / b, 3)

    # Updating Output Message depending if the given answer is correct.
    global divide_answer
    if float(divide_answer.get()) == correct:
        text = "{}/{} = {} is Correct!".format(a,b,divide_answer.get())
        divide_correct_label.config(text=text, font = ("bold", 32))
    else:
        text = "{}/{} = {} is Incorrect!{} Try Again!".format(a, b, divide_answer.get(), "\n\n")
        divide_correct_label.config(text=text, font = ("bold", 32))


    # Creating a new question if the given answer was correct.
    if float(divide_answer.get()) == correct:
        num1.set(r.randint(0,10))
        num2.set(r.randint(1,10))
        text = "{}/{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    divide_answer.delete(0, "end")




# Functioning for menu items

def add(): # Addition Function
    hide_frames()
    add_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
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
    btn = Button(add_frame, text = "Answer!", command = lambda: add_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global add_correct_label
    text = "Enter the Answer!" # default text
    add_correct_label = Label(add_frame, text=text, font = ("bold", 16))
    add_correct_label.pack(pady=5)






def subtract(): # Subtraction Function
    hide_frames()
    subtract_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}-{} = ?".format(num1.get(),num2.get())
    question_label = Label(subtract_frame, text=text, font = ('Helvetica', 32))
    question_label.pack()

    # Creating Entry box
    global subtract_answer
    subtract_answer = Entry(subtract_frame)
    subtract_answer.pack(pady=5)

    # Button to submit answer
    btn = Button(subtract_frame, text = "Answer!", command = lambda: subtract_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see subtract_correct().
    global subtract_correct_label
    text = "Enter the Answer!" # default text
    subtract_correct_label = Label(subtract_frame, text=text, font = ("bold", 16))
    subtract_correct_label.pack(pady=5)



def multiply(): # Mutliplication Function
    hide_frames()
    multiply_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}x{} = ?".format(num1.get(),num2.get())
    question_label = Label(multiply_frame, text=text, font = ('Helvetica', 32))
    question_label.pack()

    # Creating Entry box
    global multiply_answer
    multiply_answer = Entry(multiply_frame)
    multiply_answer.pack(pady=5)

    # Button to submit answer
    btn = Button(multiply_frame, text = "Answer!", command = lambda: multiply_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global multiply_correct_label
    text = "Enter the Answer!" # default text
    multiply_correct_label = Label(multiply_frame, text=text, font = ("bold", 16))
    multiply_correct_label.pack(pady=5)



def divide(): # Division Function
    hide_frames()
    divide_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(1,10))

    # Creating Question label
    global question_label
    text = "{}/{} = ?".format(num1.get(),num2.get())
    question_label = Label(divide_frame, text=text, font = ('Helvetica', 32))
    question_label.pack()

    # Creating Entry box
    global divide_answer
    divide_answer = Entry(divide_frame)
    divide_answer.pack(pady=5)

    # Using unicode
    Label(divide_frame, text = "Round to 3 decimal places if needed").pack()

    # Button to submit answer
    btn = Button(divide_frame, text = "Answer!", command = lambda: divide_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global divide_correct_label
    text = "Enter the Answer!" # default text
    divide_correct_label = Label(divide_frame, text=text, font = ("bold", 16))
    divide_correct_label.pack(pady=5)



def hide_frames(): # Hide Function

    for widget in add_frame.winfo_children(): # clearing add_frame of widgets
        widget.destroy()

    for widget in subtract_frame.winfo_children(): # clearing subtract_frame of widgets
        widget.destroy()

    for widget in multiply_frame.winfo_children(): # clearing multiply_frame of widgets
        widget.destroy()

    for widget in divide_frame.winfo_children(): # clearing divide_frame of widgets
        widget.destroy()

    # Clearing the frames.
    '''
    If a new flashcard is selected (from the menu), this allows the question label to shown
    where the original label was. "Overwrites the label"
    '''
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
