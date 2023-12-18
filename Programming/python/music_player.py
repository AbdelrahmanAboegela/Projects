import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import random

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("400x600")
music_player.configure(bg='black')

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='black', fg='white', selectmode=tkr.SINGLE, highlightthickness=0)
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
    next_song_index = (current_song_index + 1) % play_list.size()
    play_list.selection_clear(0, tkr.END)
    play_list.activate(next_song_index)
    play_list.selection_set(next_song_index, last=None)
    play()

def prev_song():
    current_song_index = play_list.curselection()[0]
    prev_song_index = (current_song_index - 1) % play_list.size()
    play_list.selection_clear(0, tkr.END)
    play_list.activate(prev_song_index)
    play_list.selection_set(prev_song_index, last=None)
    play()

shuffle_mode = False

def toggle_shuffle():
    global shuffle_mode
    if shuffle_mode:
        shuffle_mode = False
        play_list.delete(0, tkr.END)
        song_list.sort()
        for item in song_list:
            play_list.insert(tkr.END, item)
    else:
        shuffle_mode = True
        play_list.delete(0, tkr.END)
        shuffled_list = song_list.copy()
        random.shuffle(shuffled_list)
        for item in shuffled_list:
            play_list.insert(tkr.END, item)

Button1 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="PLAY", command=play, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)
Button2 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="STOP", command=stop, bg="#D32F2F", fg="white", borderwidth=0, highlightthickness=0)
Button3 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)
Button4 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)
Button5 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="NEXT", command=next_song, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)
Button6 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="PREV", command=prev_song, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)
Button7 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="SHUFFLE", command=toggle_shuffle, bg="#1DB954", fg="white", borderwidth=0, highlightthickness=0)

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 16 bold", textvariable=var, bg='black', fg='white')

volume_slider = tkr.Scale(music_player, from_=0, to=100, orient=tkr.HORIZONTAL, command=set_volume, bg='black', fg='white', highlightthickness=0)

song_title.pack(pady=20)
play_list.pack(fill="both", expand="yes", padx=20, pady=10)
Button1.pack(side=tkr.LEFT, padx=20, pady=10)
Button2.pack(side=tkr.RIGHT, padx=20, pady=10)
Button3.pack(side=tkr.LEFT, padx=20, pady=10)
Button4.pack(side=tkr.RIGHT, padx=20, pady=10)
Button5.pack(side=tkr.LEFT, padx=20, pady=10)
Button6.pack(side=tkr.RIGHT, padx=20, pady=10)
Button7.pack(side=tkr.BOTTOM, padx=20, pady=10)
volume_slider.pack(pady=20)

music_player.mainloop() 