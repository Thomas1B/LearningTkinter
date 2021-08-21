# ************** MP3 PLayer App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *
from tkinter import filedialog as fd


##################### Functions #####################

def add_song(): # adds a song to the playlist
    new_song = fd.askopenfilename(initialdir="music/", title="MP3 Player - Adding One Song", filetypes=(("Mp3 Files","*.mp3"), ))

    # Changing name of new_song to a simplier one. Since askopenfilename return entire FilePath.
    new_song = new_song.replace("C:/Users/thoma/OneDrive/University/PythonStuff/LearningTKinter/MP3player_App/music/", "")
    new_song = new_song.replace(".mp3", "")
    playlist_box.insert(END, new_song)

def add_songs(): # adds many songs to the playlist
    new_songs = fd.askopenfilenames(initialdir="music/", title="MP3 Player - Adding One Song", filetypes=(("Mp3 Files","*.mp3"), ))

    # Changing name of new_song to a simplier one. Since askopenfilename return entire FilePath.
    for song in new_songs:
        song = song.replace("C:/Users/thoma/OneDrive/University/PythonStuff/LearningTKinter/MP3player_App/music/", "")
        song = song.replace(".mp3", "")
        playlist_box.insert(END, song)

def delete_song(): # Function to delete one song from playlist
    pass

def delete_songs(): # Function to delete many songs from playlist
    pass

def delete_all(): # Function to delete all songs from playlist
    pass


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
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
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


# ******** Creating Main Menu and Dropdown Menus on the Main Menubar ********

# Creating Menu Bar
main_menu = Menu(root)
root.config(menu=main_menu)

# Creating Add Song Menu Dropdown
add_song_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one Song to the Playlist", command=add_song) # adds one song to the playlist.
add_song_menu.add_command(label="Add Many Songs to the Playlist", command=add_songs) # adds many songs to the playlist.

# Creating Delete Song Menu Dropdown
delete_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Delete Songs", menu=delete_menu)
delete_menu.add_command(label="Delete One Song from the Playlist", command=delete_song)
delete_menu.add_command(label="Delete Many Songs from the Playlist", command=delete_songs)
delete_menu.add_command(label="Delete All Songs from the Playlist", command=delete_all)

# Temporary Label
my_label = Label(root, text="")
my_label.pack(pady=20)



root.mainloop()
