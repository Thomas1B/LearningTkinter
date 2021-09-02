# ************** Tic Tac Toe using TKinter module **************

import os
os.system("clear") # clears terminal


################### Importing Modules ###################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


################### Gloabal Variables ###################
# global program_title
program_title = "Tic Tac Toe"

default_sym = "X" # X,O - sets symbol for first player
player = default_sym

count = 0 # counts how many turns.
winner = False


################### Functions ###################

def clicked(btn): # Function handle when a button is clicked.
    global player, count

    if btn['text'] == " " and player == "X":
        btn['text'] = "X"
        player = "O" # switch player
        count+=1

    elif btn['text'] == " " and player == "O":
        btn['text'] = "O"
        player = "X" # switch player
        count+=1

    if count >= 3:
        check()

def check(): # Function to check for winner.
    winner_symbol = "" # for winner popup.
    t = 'text' # var to make things easier.

    global winner
    if btn1[t] == btn2[t] == btn3[t] != " ": # Across row 1
        winner = True
        winner_symbol = btn1[t]
        btn1.config(bg='red')
        btn2.config(bg='red')
        btn3.config(bg='red')
    elif btn4[t] == btn5[t] == btn6[t] != " ": # Across row 2
        winner = True
        winner_symbol = btn4[t]
        btn4.config(bg='red')
        btn5.config(bg='red')
        btn6.config(bg='red')
    elif btn7[t] == btn8[t] == btn9[t] != " ": # Across row 3
        winner = True
        winner_symbol = btn7[t]
        btn7.config(bg='red')
        btn8.config(bg='red')
        btn9.config(bg='red')
    elif btn1[t] == btn4[t] == btn7[t] != " ": # Down column 1
        winner = True
        winner_symbol = btn1[t]
        btn1.config(bg='red')
        btn4.config(bg='red')
        btn7.config(bg='red')
    elif btn2[t] == btn5[t] == btn8[t] != " ": # Down column 2
        winner = True
        winner_symbol = btn2[t]
        btn2.config(bg='red')
        btn5.config(bg='red')
        btn8.config(bg='red')
    elif btn3[t] == btn6[t] == btn9[t] != " ": # Down column 3
        winner = True
        winner_symbol = btn3[t]
        btn3.config(bg='red')
        btn6.config(bg='red')
        btn9.config(bg='red')
    elif btn1[t] == btn5[t] == btn9[t] != " ": # Diagonal 1-5-9
        winner = True
        winner_symbol = btn1[t]
        btn1.config(bg='red')
        btn5.config(bg='red')
        btn9.config(bg='red')
    elif btn3[t] == btn5[t] == btn7[t] != " ": # Diagonal 3-5-7
        winner = True
        winner_symbol = btn3[t]
        btn3.config(bg='red')
        btn5.config(bg='red')
        btn7.config(bg='red')
    if winner: # if there is a winner, display popup.
        text = "Congratulations!\n\n  Player '{}' Wins!".format(winner_symbol)
        messagebox.showinfo("Winner!", text)
        for btn in btn_list:
            btn['state'] = DISABLED

def refresh(): # Function to clear the board.
    global player, count, winner

    count = 0
    player = default_sym
    winner = False

    for btn in btn_list: #
        btn['text'] = " "
        btn['bg'] = 'white'
        btn['state'] = ACTIVE



################### Main Program ###################5

# Making Main (root) window.
root = Tk()
root.title(program_title)
root_x = 432 # Do Not Change
root_y = 380 # Do Not Change
root.geometry("{}x{}".format(root_x, root_y))
root.resizable(width=False, height=False) # Stops user from resizes window.

# Creating Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_bar.add_command(label="New Game!", command=refresh)


# Creating Main Frame
board_frame = Frame(root, bg='black', width = 425, height=380)
board_frame.pack(fill='both', expand=1)


# Options for Buttons.
font = ("Helvetica", 20)
relief = FLAT # relief style for Buttons.
overr = SUNKEN # overrelief style for Buttons.
width = 8 # Do Not Change
height = 3 # Do Not Change


########### Board set up ###########
'''
1,2,3
4,5,6
7,8,9
'''

# Creating Buttons for board
btn1 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn1)) # Row 1
btn2 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn2))
btn3 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn3))

btn4 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn4)) # Row 2
btn5 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn5))
btn6 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn6))

btn7 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn7)) # Row 3
btn8 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn8))
btn9 = Button(board_frame, text=" ", font=font, width=width, height=height, relief=relief, overrelief=overr, command = lambda: clicked(btn9))

btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8,btn9]

# Griding Buttons to screen.
btn1.grid(row=0, column=0, padx=(5,2), pady=(5,2)) # Row 1
btn2.grid(row=0, column=1, padx=(2,2), pady=(5,2))
btn3.grid(row=0, column=2, padx=(2,2), pady=(5,2))

btn4.grid(row=1, column=0, padx=(5,2), pady=(2,2)) # Row 2
btn5.grid(row=1, column=1, padx=(2,2), pady=(2,2))
btn6.grid(row=1, column=2, padx=(2,2), pady=(2,2))

btn7.grid(row=2, column=0, padx=(5,2), pady=(2,5)) # Row 3
btn8.grid(row=2, column=1, padx=(2,2), pady=(2,5))
btn9.grid(row=2, column=2, padx=(2,2), pady=(2,5))


check()


root.mainloop()
