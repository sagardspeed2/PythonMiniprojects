import tkinter as tk
from tkinter import *
import youtube_dl as yd
from tkinter import messagebox, filedialog


def CreateWidget():

    linkLabel = Label(root, text="ENTER THE VIDEO LINK : ", bg='slategrey')
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=60)
    root.linkText.grid(row=1, column=1, pady=5, columnspan=2)

    destinationLabel = Label(root, text="SAVE AUDIO IN : ", bg='slategrey')
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38)
    root.destinationText.grid(row=2, column=1, pady=5)

    browseButton = Button(root, text="BROWSE", command=BROWSE, width=15)
    browseButton.grid(row=2, column=2, pady=5)

    dwldButton = Button(root, text="DOWNLOAD AUDIO", command=Download, width=30)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)


def BROWSE():

    root.destinationDir = filedialog.askdirectory(initialdir=r"C:\Users\admin\Downloads")
    root.destinationText.insert('1', root.destinationDir)


def Download():

    videoLink = root.linkText.get()

    savePath = root.destinationText.get()

    audDWLDopt = {

        'format' : 'bestaudio/best',
        'outtmpl' : savePath+"/%(title)s.%(ext)s",
        'postprocessors' : [{

            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '320'

        }],

    }

    with yd.YoutubeDL(audDWLDopt) as aud_dwld:
        aud_dwld.download([videoLink])

    messagebox.showinfo("SUCCESS", "VIDEO CONVERTED AND DOWNLOAD AS AUDIO")


root = tk.Tk()
root.geometry("650x110")
root.title("Py Youtube Video Download")
root.resizable(False, False)
root.config(background='slategrey')

CreateWidget()

root,mainloop()