import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import random

music_player = tkr.Tk()
music_player.title("Music Player")
music_player.geometry("670x500")
music_player.configure(bg='#1E1E1E')

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='#1E1E1E', fg='#FFFFFF', selectmode=tkr.SINGLE, highlightthickness=0)
for item in song_list:
    play_list.insert(tkr.END, item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def set_volume(val):
    volume = int(val) / 100.0
    pygame.mixer.music.set_volume(volume)

def next_song():
    current_song_index = play_list.curselection()[0]
    next_song_index = (current_song_index + 1) % len(song_list)
    play_list.selection_clear(0, tkr.END)
    play_list.activate(next_song_index)
    play_list.selection_set(next_song_index, last=None)
    pygame.mixer.music.load(play_list.get(next_song_index))
    var.set(play_list.get(next_song_index))
    pygame.mixer.music.play()

def prev_song():
    current_song_index = play_list.curselection()[0]
    prev_song_index = (current_song_index - 1) % len(song_list)
    play_list.selection_clear(0, tkr.END)
    play_list.activate(prev_song_index)
    play_list.selection_set(prev_song_index, last=None)
    pygame.mixer.music.load(play_list.get(prev_song_index))
    var.set(play_list.get(prev_song_index))
    pygame.mixer.music.play()

def shuffle():
    global song_list
    if shuffle_button["text"] == "Shuffle":
        random.shuffle(song_list)
        shuffle_button["text"] = "Sort"
    else:
        song_list.sort()
        shuffle_button["text"] = "Shuffle"
    play_list.delete(0, tkr.END)
    for item in song_list:
        play_list.insert(tkr.END, item)

label = tkr.Label(music_player, text="Music Player", font="Helvetica 24 bold", bg='#1E1E1E', fg='#FFFFFF')
label.pack(pady=10)

var = tkr.StringVar()
song_title = tkr.Label(music_player, textvariable=var, font="Helvetica 14", bg='#1E1E1E', fg='#FFFFFF')
song_title.pack()

frame1 = tkr.Frame(music_player, bg='#1E1E1E')
frame1.pack(pady=20)

play_button = tkr.Button(frame1, text="Play", font="Helvetica 12 bold", command=play, bg='#1E1E1E', fg='#FFFFFF', bd=0)
play_button.pack(side=tkr.LEFT, padx=(10, 0))

stop_button = tkr.Button(frame1, text="Stop", font="Helvetica 12 bold", command=stop, bg='#1E1E1E', fg='#FFFFFF', bd=0)
stop_button.pack(side=tkr.LEFT, padx=(10, 0))

pause_button = tkr.Button(frame1, text="Pause", font="Helvetica 12 bold", command=pause, bg='#1E1E1E', fg='#FFFFFF', bd=0)
pause_button.pack(side=tkr.LEFT, padx=(10, 0))

unpause_button = tkr.Button(frame1, text="Unpause", font="Helvetica 12 bold", command=unpause, bg='#1E1E1E', fg='#FFFFFF', bd=0)
unpause_button.pack(side=tkr.LEFT, padx=(10, 0))

prev_button = tkr.Button(frame1, text="Prev", font="Helvetica 12 bold", command=prev_song, bg='#1E1E1E', fg='#FFFFFF', bd=0)
prev_button.pack(side=tkr.LEFT, padx=(10, 0))

next_button = tkr.Button(frame1, text="Next", font="Helvetica 12 bold", command=next_song, bg='#1E1E1E', fg='#FFFFFF', bd=0)
next_button.pack(side=tkr.LEFT, padx=(10, 0))

shuffle_button = tkr.Button(frame1, text="Shuffle", font="Helvetica 12 bold", command=shuffle, bg='#1E1E1E', fg='#FFFFFF', bd=0)
shuffle_button.pack(side=tkr.LEFT, padx=(10, 0))

scale = tkr.Scale(frame1, from_=0, to=100, orient=tkr.HORIZONTAL, command=set_volume, bg='#1E1E1E', fg='#FFFFFF', highlightthickness=0, bd=0)
scale.set(50)
pygame.mixer.music.set_volume(0.5)
scale.pack(side=tkr.LEFT, padx=(10, 0))

play_list.pack(fill=tkr.BOTH, expand="true")

music_player.mainloop()