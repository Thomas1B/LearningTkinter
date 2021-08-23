# ************** MP3 PLayer App using TKinter module **************

import os
os.system("clear") # clears terminal

from tkinter import *
from tkinter import filedialog as fd
import pygame as pg # for mp3 files
pg.mixer.init() # Initalizing pygame
import time


##################### Global Variables #####################

# Global variable to hold filepath where mp3 files are stored.
# Using String format() Method.
global music_filepath
music_filepath = "C:/Users/thoma/OneDrive/University/PythonStuff/LearningTKinter/MP3player_App/music/{}.mp3"

# Global variable to hold parts that need to be stripped, see add_song() and add_songs.
global replace_part1
replace_part1 = "C:/Users/thoma/OneDrive/University/PythonStuff/LearningTKinter/MP3player_App/music/"

# Creating Pause variable, see pause().
global paused
paused = False

##################### Functions #####################

def add_song(): # adds a song to the playlist
    new_song = fd.askopenfilename(initialdir="music/", title="MP3 Player - Adding One Song", filetypes=(("Mp3 Files","*.mp3"), ))

    # Changing name of new_song to a simplier one. Since askopenfilename return entire FilePath.
    new_song = new_song.replace(replace_part1, "")
    new_song = new_song.replace(".mp3", "")
    playlist_box.insert(END, new_song)

def add_songs(): # adds many songs to the playlist
    new_songs = fd.askopenfilenames(initialdir="music/", title="MP3 Player - Adding Many Songs", filetypes=(("Mp3 Files","*.mp3"), ))

    # Changing name of new_song to a simplier one. Since askopenfilename return entire FilePath.
    for song in new_songs:
        song = song.replace(replace_part1, "")
        song = song.replace(".mp3", "")
        playlist_box.insert(END, song)

def delete_song(): # Function to delete one song from playlist
    playlist_box.delete(ANCHOR)

def delete_all(): # Function to delete all songs from playlist
    playlist_box.delete(0, END)

def play(is_paused): # Plays the Song
    global paused
    paused = is_paused

    if (paused):
        pg.mixer.music.unpause()
        paused = False
    else:
        song = playlist_box.get(ACTIVE)
        song = music_filepath.format(song)
        pg.mixer.music.load(song)
        pg.mixer.music.play()

    play_time()

def stop(): # Stops the Song
    pg.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

def pause(is_paused): # Pauses the Song
    global paused
    paused = is_paused

    if paused:
        pg.mixer.music.unpause()# Unpause
        paused = False
    else:
        pg.mixer.music.pause()# Pause
        paused = True

def next_song(): # Goes to the next song
    # getting the current song, returns a tuble of location (pos,)
    cur_song = playlist_box.curselection()[0]
    next_song = cur_song+1 # getting the next song's pos

    # if the current song is the last in the playlist, goes back to the first.
    if (next_song >= playlist_box.size()):
        next_song = 0

    # reconstructing song filepath
    song = playlist_box.get(next_song)
    song = music_filepath.format(song)

    # Loading song then play it.
    pg.mixer.music.load(song)
    pg.mixer.music.play()

    # Updating bar in playlist
    playlist_box.selection_clear(0, END)
    playlist_box.activate(next_song)
    playlist_box.selection_set(next_song)

def prev_song(): # Goes to the previous song

    # getting the current song, returns a tuble of location (pos,)
    cur_song = playlist_box.curselection()[0]
    next_song = cur_song-1 # getting the next song's pos

    # if the current song is the first in the playlist, goes back to the last.
    if (next_song < 0):
        next_song = playlist_box.size()-1

    # reconstructing song filepath
    song = playlist_box.get(next_song)
    song = music_filepath.format(song)

    # Loading song then play it.
    pg.mixer.music.load(song)
    pg.mixer.music.play()

    # Updating bar in playlist
    playlist_box.selection_clear(0, END)
    playlist_box.activate(next_song)
    playlist_box.selection_set(next_song)

def play_time(): # Function to deal with time.
    # Getting the time played of the song.
    current_time = int(pg.mixer.music.get_pos()/1000) # pg.mixer.music.get_pos() returns time in milliseconds

    # Converting current_time into time format.
    current_time = time.strftime("%M:%S", time.gmtime(current_time))

    status_bar.config(text=current_time)
    status_bar.after(1000, play_time) # runs play_time() every 1 second.



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
play_btn = Button(media_frame, image=play_img, overrelief=SUNKEN, bd=0, command=lambda: play(paused))
forward_btn = Button(media_frame, image=forward_img, overrelief=SUNKEN, bd=0, command = next_song)
back_btn = Button(media_frame, image=back_img, overrelief=SUNKEN, bd=0, command = prev_song)
pause_btn = Button(media_frame, image=pause_img, overrelief=SUNKEN, bd=0, command= lambda: pause(paused))
stop_btn = Button(media_frame, image=stop_img, overrelief=SUNKEN, bd=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
forward_btn.grid(row=0, column=3, padx=10)
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
delete_menu.add_command(label="Delete All Songs from the Playlist", command=delete_all)

# Creating Status Bar
status_bar = Label(root, text="Nothing", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Temporary Label
my_label = Label(root, text="")
my_label.pack(pady=5)





root.mainloop()
