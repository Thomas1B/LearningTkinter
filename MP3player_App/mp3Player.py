# ************** MP3 PLayer App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *
# from PIL import ImageTk, Image

#####################  #####################







##################### Main Program #####################

# Making Main (root) window.
root = Tk()
root.title("MP3 Player")
root.geometry("{}x{}".format(500,400))
root.iconbitmap("images/music_icon.ico")

# Defining Images
play_img = PhotoImage(file="images/play.png")
pause_img = PhotoImage(file="images/pause.png")
forward_img = PhotoImage(file="images/skip_end.png")
back_img = PhotoImage(file="images/skip_start.png")
stop_img = PhotoImage(file="images/stop.png")

# Creating Playlist box
playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

# Creating Media Control Frame
media_frame = Frame(root)
media_frame.pack(pady=20)

# Creating Media Control Buttons
play_btn = Button(media_frame, image=play_img, overrelief=SUNKEN, bd=0)
forward_btn = Button(media_frame, image=forward_img, overrelief=SUNKEN, bd=0)
back_btn = Button(media_frame, image=back_img, overrelief=SUNKEN, bd=0)
pause_btn = Button(media_frame, image=pause_img, overrelief=SUNKEN, bd=0)
stop_btn = Button(media_frame, image=stop_img, overrelief=SUNKEN, bd=0)

back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
forward_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Creating Menu Bar
main_menu = Menu(root)
root.config(menu=main_menu)




root.mainloop()
