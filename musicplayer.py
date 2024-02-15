import tkinter as tk
from tkinter import filedialog
import pygame


# Initialize pygame.mixer
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("MP3 Music Player")

# Playlist container
playlist = []


# Function to load and play music
def play_music():
	if playlist:
		filename = playlist[0]  # Get the first song from the playlist
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()


# Function to add songs to the playlist
def add_to_playlist():
	filename = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
	playlist.append(filename)


# Create buttons
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

add_button = tk.Button(root, text="Add to Playlist", command=add_to_playlist)
add_button.pack()

# Run the main event loop
root.mainloop()
