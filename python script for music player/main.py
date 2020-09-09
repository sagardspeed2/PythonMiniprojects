import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import threading
from threading import Timer
import getpass

background_color = "STEELBLUE"
foreground_color = "#fff"
playButton_state = DISABLED
pauseButton_state = DISABLED
stopButton_state = DISABLED
volUpButton_state = DISABLED
volDownButton_state = DISABLED

playTime = 0

def CreateWidgets():

	trackLabel = Label(root, text="SELECT AUDIO TRACK : ", bg=background_color, fg=foreground_color)
	trackLabel.grid(row=0, column=0, padx=5, pady=5)

	trackEntry = Entry(root, width=35, textvariable=audioTrack)
	trackEntry.grid(row=0, column=1, padx=5, pady=5)

	browseButton = Button(root, text="BROWSE", width=20, command=Browse)
	browseButton.configure(background="#FFA500")
	browseButton.grid(row=0, column=2, padx=5, pady=5)

	root.playButton = Button(root, text="PLAY", width=20, state=playButton_state, command=Play)
	root.playButton.configure(background="#c4ffc4")
	root.playButton.grid(row=1, column=0, pady=5, padx=5)

	root.pauseButton = Button(root, width=20, text="PAUSE", state=pauseButton_state, command=Pause)
	root.pauseButton.configure(background="#fffacd")
	root.pauseButton.grid(row=1, column=1, padx=5, pady=5)

	root.resumeButton = Button(root, width=20, text="RESUME", command=Resume)
	root.resumeButton.configure(background="#ff0")
	root.resumeButton.grid(row=1, column=2, padx=5, pady=5)
	root.resumeButton.grid_remove()

	root.stopButton = Button(root, text="STOP", width=20, state=stopButton_state, command=Stop)
	root.stopButton.configure(background="#FF4D4D")
	root.stopButton.grid(row=2, column=0, pady=5, padx=5)

	root.volUpButton = Button(root, text="Volume UP", width=20, state=volUpButton_state, command=VolumeUp)
	root.volUpButton.configure(background="#c4ffc4")
	root.volUpButton.grid(row=1, column=2, pady=5, padx=5)

	root.volDownButton = Button(root, text="Volume Down", width=20, state=volDownButton_state, command=VolumeDown)
	root.volDownButton.configure(background="#FF4D4F")
	root.volDownButton.grid(row=2, column=2, pady=5, padx=5)

def Browse():
	global playButton_state
	audioFile = filedialog.askopenfilename(
		initialdir = "C:/Users/"+getpass.getuser()+"/Music",
		title="Select audio file",
		filetypes=(("MP3", "*.mp3"),("WAV","*.wav"))
		)
	audioTrack.set(audioFile)
	if audioFile:
		playButton_state = NORMAL
		CreateWidgets()
		t = Timer(0.05, ButtonchangeColor_disable_to_enable_initial)
		t.start()

def ButtonchangeColor_disable_to_enable_initial():
	root.playButton.configure(background="#0F0")

def Play():
	global playButton_state, pauseButton_state, stopButton_state, volUpButton_state, volDownButton_state
	audioFile = audioTrack.get()
	if audioFile:
		pygame.mixer.music.load(audioFile)
		pygame.mixer.music.play()
		playButton_state = DISABLED
		pauseButton_state = NORMAL
		stopButton_state = NORMAL
		volUpButton_state = NORMAL
		volDownButton_state = NORMAL
		# audioStatus = Label(root, width=20, text="Song is playing", bg=background_color)
		# audioStatus.grid(row=2, column=1, padx=5, pady=5)
		CreateWidgets()
		t = Timer(0.05, ButtonchangeColor_disable_to_enable_play)
		t1 = Timer(0.05, ShowTrackTime)
		t.start()
		t1.start()

def ButtonchangeColor_disable_to_enable_play():
	root.pauseButton.configure(background="#ff0")
	root.stopButton.configure(background="#f00")
	root.volUpButton.configure(background="#0f0")
	root.volDownButton.configure(background="#f00")

def ShowTrackTime():
	thread1 = threading.Timer(1.0, ShowTrackTime)
	thread1.setDaemon(True)
	thread1.start()
	seconds=int((pygame.mixer.music.get_pos()/1000)%60)
	minutes=int((pygame.mixer.music.get_pos()/(1000*60))%60)
	minutes = '0'+str(minutes) if len(str(minutes)) == 1 else str(minutes)
	seconds = '0'+str(seconds) if len(str(seconds)) == 1 else str(seconds)
	trackTime = str(minutes)+':'+str(seconds)
	audioStatus = Label(root, width=20, text=trackTime, bg=background_color)
	audioStatus.grid(row=2, column=1, padx=5, pady=5)

def Pause():
	# global playTime
	if pygame.mixer.music.get_busy():
		# pygame.mixer.music.fadeout(500)
		# playTime = pygame.mixer.music.get_pos()
		# t = Timer(0.05, pygame.mixer.music.pause)
		# t.start()
		pygame.mixer.music.pause()
		root.pauseButton.grid_remove()
		root.resumeButton.grid(row=1, column=1, padx=5, pady=5)
		audioStatus = Label(root, width=20, text="Song Paused", bg=background_color)
		audioStatus.grid(row=2, column=1, padx=5, pady=5)

def Resume():
	# global playTime
	if pygame.mixer.music.get_busy():
		# pygame.mixer.music.set_pos(playTime)
		# pygame.mixer.music.play(0, playTime)
		pygame.mixer.music.unpause()
		root.resumeButton.grid_remove()
		root.pauseButton.grid()
		audioStatus = Label(root, width=20, text="Song is playing", bg=background_color)
		audioStatus.grid(row=2, column=1, padx=5, pady=5)

def Stop():
	global pauseButton_state, playButton_state, stopButton_state
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
		pauseButton_state = DISABLED
		playButton_state = NORMAL
		stopButton_state = DISABLED
		CreateWidgets()
		audioStatus = Label(root, width=20, text="Song Stoped", bg=background_color)
		audioStatus.grid(row=2, column=1, padx=5, pady=5)
		t = Timer(0.05, ButtonchangeColor_disable_to_enable_stop)
		t.start()

def ButtonchangeColor_disable_to_enable_stop():
	root.playButton.configure(background="#0f0")
	root.pauseButton.configure(background="#fffacd")
	root.stopButton.configure(background="#FF4D4F")
	root.volUpButton.configure(background="#0f0")
	root.volDownButton.configure(background="#f00")


def VolumeUp():
	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

def VolumeDown():
	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)

root = tk.Tk()

root.title("Python Music Player")
root.geometry("730x110")
root.resizable(False, False)
root.config(background=background_color)

pygame.mixer.init()

audioTrack = StringVar()

CreateWidgets()

root.mainloop()