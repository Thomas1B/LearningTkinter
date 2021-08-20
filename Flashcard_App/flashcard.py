import os
os.system("clear")

# ************* Making a flashcard app *************

from tkinter import *
# from PIL import ImageTk, Image
import random as r

#################################################################
# ************************** Functions **************************

def start_screen(): # Function for the Screen screen
    # ************ Start Screen ************
    hide_frames()
    start_frame.pack(fill="both", expand=1)
    text="Welcome to Math Flashcards!"
    start_label = Label(start_frame, text=text, font=("Helvetica", 20, "bold"), relief=SUNKEN, fg='black', bg='gold', bd=10, padx=10, pady=15)
    start_label.pack(pady=30)

    # Buttons
    add_btn = Button(start_frame, text="Addition Flashcards", overrelief=SUNKEN, command=add).pack(ipadx=14,ipady=5)
    subtract_btn = Button(start_frame, text="Subtraction Flashcards", overrelief=SUNKEN, command=subtract).pack(ipadx=6, ipady=5)
    multiply_btn = Button(start_frame, text="Mutliplication Flashcards", overrelief=SUNKEN, command=multiply).pack(ipady=5)
    divide_btn = Button(start_frame, text="Division Flashcards", overrelief=SUNKEN, command=divide).pack(ipadx=16, ipady=5)
    quit_btn = Button(start_frame, text = "Quit Flashcard", overrelief=SUNKEN, command=root.quit).pack(pady=10, ipadx=28, ipady=5)


# ************* Functions to check if the answers given are correct. *************

def add_correct(a, b): # Checking if Addition is correct.
    correct = a + b
    check = False # check for creating a new question

    # Updating Output Message depending if the given answer is correct.
    global add_answer
    if int(add_answer.get()) == correct:
        text = "{}+{} = {} is Correct!".format(a,b,add_answer.get())
        add_correct_label.config(text=text, font = ("bold", 18))
        check = True
    else:
        text = "{}+{} = {} is Incorrect!{} Try Again!".format(a,b,add_answer.get(), "\n\n")
        add_correct_label.config(text=text, font = ("bold", 18))

    # Creating a new question if the given answer was correct.
    if check:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}+{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    add_answer.delete(0, "end")

def subtract_correct(a, b): # Checking if Subtraction is correct.
    correct = a - b
    check = False # check for creating a new question

    # Updating Output Message depending if the given answer is correct.
    global subtract_answer
    if int(subtract_answer.get()) == correct:
        text = "{}-{} = {} is Correct!".format(a,b,subtract_answer.get())
        subtract_correct_label.config(text=text, font = ("bold", 18))
        check = True
    else:
        text = "{}-{} = {} is Incorrect!{} Try Again!".format(a,b,subtract_answer.get(), "\n\n")
        subtract_correct_label.config(text=text, font = ("bold", 18))

    # Creating a new question if the given answer was correct.
    if check:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}-{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    subtract_answer.delete(0, "end")

def multiply_correct(a, b): # Checking if Mutliplication is correct.
    correct = a * b
    check = False # check for creating a new question

    # Updating Output Message depending if the given answer is correct.
    global multiply_answer
    if int(multiply_answer.get()) == correct:
        text = "{}x{} = {} is Correct!".format(a, b, multiply_answer.get())
        multiply_correct_label.config(text=text, font = ("bold", 18))
        check = True
    else:
        text = "{}x{} = {} is Incorrect!{} Try Again!".format(a, b, multiply_answer.get(), "\n\n")
        multiply_correct_label.config(text=text, font = ("bold", 18))

    # Creating a new question if the given answer was correct.
    if check:
        num1.set(r.randint(0,10))
        num2.set(r.randint(0,10))
        text = "{}x{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    multiply_answer.delete(0, "end")

def divide_correct(a, b): # Checking if Division is correct.
    correct = round(a / b, 3)
    check = False # check for creating a new question

    # Updating Output Message depending if the given answer is correct.
    global divide_answer
    if float(divide_answer.get()) == correct:
        text = "{}/{} = {} is Correct!".format(a,b,divide_answer.get())
        divide_correct_label.config(text=text, font = ("bold", 18))
        check = True
    else:
        text = "{}/{} = {} is Incorrect!{} Try Again!".format(a, b, divide_answer.get(), "\n\n")
        divide_correct_label.config(text=text, font = ("bold", 18))

    # Creating a new question if the given answer was correct.
    if check:
        num1.set(r.randint(0,10))
        num2.set(r.randint(1,10))
        text = "{}/{} = ?".format(num1.get(),num2.get())
        question_label.config(text=text)

    # Clearing answer box.
    divide_answer.delete(0, "end")


# ************* Functioning for menu items *************

def add(): # Addition Function
    hide_frames()
    add_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1, num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}+{} = ?".format(num1.get(),num2.get())
    question_label = Label(add_frame, text=text, font = ('Helvetica', 32), bg='light blue')
    question_label.pack(pady=10)

    # Creating Entry box
    global add_answer
    add_answer = Entry(add_frame)
    add_answer.pack(pady=5, ipady=5)

    # Button to submit answer
    btn = Button(add_frame, text = "Answer!", font=("bold", 12), overrelief=SUNKEN, padx=10, pady=10, command = lambda: add_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global add_correct_label
    text = "Enter the Answer!" # default text
    add_correct_label = Label(add_frame, text=text, font = ("bold", 16), bg='light blue')
    add_correct_label.pack(pady=5)

    # Button to go back to the home screen.
    home_btn = Button(add_frame, text="Go to Home Screen", overrelief=SUNKEN, command = start_screen).pack(pady=60, ipadx=5, ipady=5)

def subtract(): # Subtraction Function
    hide_frames()
    subtract_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1, num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}-{} = ?".format(num1.get(),num2.get())
    question_label = Label(subtract_frame, text=text, font = ('Helvetica', 32), bg='light blue')
    question_label.pack(pady=10)

    # Creating Entry box
    global subtract_answer
    subtract_answer = Entry(subtract_frame)
    subtract_answer.pack(pady=5, ipady=5)

    # Button to submit answer
    btn = Button(subtract_frame, text = "Answer!", font=("bold", 12), overrelief=SUNKEN, command = lambda: subtract_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see subtract_correct().
    global subtract_correct_label
    text = "Enter the Answer!" # default text
    subtract_correct_label = Label(subtract_frame, text=text, font = ("bold", 16), bg='light blue')
    subtract_correct_label.pack(pady=5)

    # Button to go back to the home screen.
    home_btn = Button(subtract_frame, text="Go to Home Screen", overrelief=SUNKEN, command = start_screen).pack(pady=60, ipadx=5, ipady=5)

def multiply(): # Mutliplication Function
    hide_frames()
    multiply_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1, num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(0,10))

    # Creating Question label
    global question_label
    text = "{}x{} = ?".format(num1.get(),num2.get())
    question_label = Label(multiply_frame, text=text, font = ('Helvetica', 32), bg='light blue')
    question_label.pack(pady=10)

    # Creating Entry box
    global multiply_answer
    multiply_answer = Entry(multiply_frame)
    multiply_answer.pack(pady=5, ipady=5)

    # Button to submit answer
    btn = Button(multiply_frame, text = "Answer!", font=("bold", 12), overrelief=SUNKEN, command = lambda: multiply_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global multiply_correct_label
    text = "Enter the Answer!" # default text
    multiply_correct_label = Label(multiply_frame, text=text, font = ("bold", 16), bg='light blue')
    multiply_correct_label.pack(pady=5)

    # Button to go back to the home screen.
    home_btn = Button(multiply_frame, text="Go to Home Screen", overrelief=SUNKEN, command = start_screen).pack(pady=60, ipadx=5, ipady=5)

def divide(): # Division Function
    hide_frames()
    divide_frame.pack(fill="both", expand=1)

    # Creating random numbers.
    global num1, num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(r.randint(0,10))
    num2.set(r.randint(1,10))

    # Creating Question label
    global question_label
    text = "{}/{} = ?".format(num1.get(),num2.get())
    question_label = Label(divide_frame, text=text, font = ('Helvetica', 32), bg='light blue')
    question_label.pack(pady=10)

    Label(divide_frame, text = "(Round to 3 decimal places if needed)", bg='light blue').pack(pady=5)

    # Creating Entry box
    global divide_answer
    divide_answer = Entry(divide_frame)
    divide_answer.pack(pady=5, ipady=5)

    # Button to submit answer
    btn = Button(divide_frame, text = "Answer!", font=("bold", 12), overrelief=SUNKEN, command = lambda: divide_correct(num1.get(), num2.get()))
    btn.pack(pady=10)

    # Creating Output Message label, see add_correct().
    global divide_correct_label
    text = "Enter the Answer!" # default text
    divide_correct_label = Label(divide_frame, text=text, font = ("bold", 16), bg='light blue')
    divide_correct_label.pack(pady=5)

    # Button to go back to the home screen.
    home_btn = Button(divide_frame, text="Go to Home Screen", overrelief=SUNKEN, command = start_screen).pack(pady=60, ipadx=5, ipady=5)

def hide_frames(): # Hide Function

    # Clearing Frames of widgets
    for widget in start_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()
    for widget in subtract_frame.winfo_children():
        widget.destroy()
    for widget in multiply_frame.winfo_children():
        widget.destroy()
    for widget in divide_frame.winfo_children():
        widget.destroy()

    # Clearing the frames.
    '''
    If a new flashcard is selected (from the menu), this allows the question label to shown
    where the original label was. "Overwrites the label"
    '''
    start_frame.pack_forget()
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()


#################################################################
# Creating the root Screen.

root = Tk()
root.title("Learning TKinter - Flashcard")
root.geometry("{}x{}".format(600,500))
root.iconbitmap("globe.ico")

# Creating Main Menu
main_menu = Menu(root)
root.config(menu = main_menu)


# ************* Creating Main Menu items *************
math_menu = Menu(main_menu)
main_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Addition", command=add)
math_menu.add_command(label="Subtraction", command=subtract)
math_menu.add_command(label="Mutliplication", command=multiply)
math_menu.add_command(label="Division", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Exit Program", command=root.quit)


# ************* Creating Frames *************
start_frame = Frame(root, width=400, height=400, bg="light blue") # Welcome Screen Frame
add_frame = Frame(root, width=400, height=400, bg="light blue")
subtract_frame = Frame(root, width=400, height=400, bg="light blue")
multiply_frame = Frame(root, width=400, height=400, bg="light blue")
divide_frame = Frame(root, width=400, height=400, bg="light blue")

start_screen() # Starting the Welcome Screen.

root.mainloop()
