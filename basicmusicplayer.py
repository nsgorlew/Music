#Python audio player
#Import Modules
import pygame
import tkinter as tkr
import os

#Create Window
playwindow = tkr.Tk()

#Edit Window
playwindow.title("Audio Player")
playwindow.geometry("450x500")

# Playlist Register
os.chdir("Song.mp3") # Path of playlist needs to go here
print(os.getcwd)
songlist = os.listdir()

# Volume Input
VolumeLevel = tkr.Scale(playwindow, from_=0.0, to_=1.0, orient=tkr.HORIZONTAL, resolution=0.1)

# Playlist Input
playlist = tkr.Listbox(playwindow, highlightcolor="blue", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1

# Pygame Inits
pygame.init()
pygame.mixer.init()

# Action Event
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

# Register Buttons
Button1 = tkr.Button(playwindow, width=5, height=3, text="PLAY", command=Play)
Button2 = tkr.Button(playwindow, width=5, height=3, text="STOP", command=ExitPlayer)
Button3 = tkr.Button(playwindow, width=5, height=3, text="PAUSE", command=Pause)
Button4 = tkr.Button(playwindow, width=5, height=3, text="UNPAUSE", command=UnPause)

# Song Name
var = tkr.StringVar()
songtitle = tkr.Label(playwindow,textvariable=var)

# Place Widgets
Button1.pack(fill="x") # will stretch button to fill whole window
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
songtitle.pack()
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")

# Activate
playwindow.mainloop()