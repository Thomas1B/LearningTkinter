# ************** MP3 PLayer App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *

#####################  #####################







##################### Main Program #####################

# Making Main (root) window.
root = Tk()
root.title("MP3 Player")
root.geometry("{}x{}".format(500,400))
root.iconbitmap("images/music_icon.ico")

# Creating Playlist box
playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

# Creating Media Control Frame
media_frame = Frame(root)
media_frame.pack(pady=20)

# Creating Media Control Buttons
play_btn = Button(media_frame, text="Play")
forward_btn = Button(media_frame, text="Forward")
back_btn = Button(media_frame, text="Back")
pause_btn = Button(media_frame, text="Pause")
stop_btn = Button(media_frame, text="Stop")

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)


root.mainloop()
