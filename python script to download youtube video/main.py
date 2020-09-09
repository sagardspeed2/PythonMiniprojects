import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


def CreateWidget():

    linkLabel = Label(root, text="ENTER THE VIDEO LINK : ", bg='skyblue')
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=60)
    root.linkText.grid(row=1, column=1, pady=5, columnspan=2)

    destinationLabel = Label(root, text="SAVE DESTINATION : ", bg='skyblue')
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38)
    root.destinationText.grid(row=2, column=1, pady=5)

    browseButton = Button(root, text="BROWSE", command=BROWSE, width=15)
    browseButton.grid(row=2, column=2, pady=5)

    dwldButton = Button(root, text="DOWNLOAD", command=Download, width=50)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)


def BROWSE():

    root.destinationDir = filedialog.askdirectory(initialdir=r"C:\Users\admin\Downloads")
    root.destinationText.insert('1', root.destinationDir)


def Download():

    getVideo = YouTube(root.linkText.get())

    videoStream = getVideo.streams.first()

    videoStream.download(root.destinationDir)

    messagebox.showinfo("SUCCESS", "VIDEO DOWNLOADED AND SAVED IN \n" + root.destinationDir)


root = tk.Tk()
root.geometry("650x110")
root.title("Py Youtube Video Download")
root.resizable(False, False)
root.config(background='skyblue')

CreateWidget()

root,mainloop()