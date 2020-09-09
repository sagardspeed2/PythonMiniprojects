import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()

root.title("PYQR Generator")
root.geometry("510x510")
root.resizable(False, False)
root.config(background = "darkolivegreen4")

def createWidgets():

	download_path_label = Label(text="Save To : ", bg="darkolivegreen4")
	download_path_label.grid(row=0, column=0, padx=5, pady=5)

	root.download_path = Entry(width=30, textvariable=dwl_path)
	root.download_path.grid(row=0, column=1, pady=5)

	path_label_button = Button(width=10, text="Browse", command=Browse)
	path_label_button.grid(row=0, column=2, padx=5, pady=5)

	label = Label(text = "Enter Text : ", bg="darkolivegreen4")
	label.grid(row=1, column=0, padx=5, pady=5)

	root.entry = Entry(width=30, textvariable=qrText)
	root.entry.grid(row=1, column=1, padx=5, pady=5)

	button = Button(width=10, text = "Generate", command = QRCodeGenerate)
	button.grid(row=1, column=2, padx=5, pady=5)

	label = Label(text = "QR Code : ", bg="darkolivegreen4")
	label.grid(row=2, column=0, padx=5, pady=5)

	root.imageLabel = Label(root, background="darkolivegreen4")
	root.imageLabel.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    

def Browse():
    path_text = filedialog.askdirectory()
    root.download_path.insert('0', path_text)

def QRCodeGenerate():
	qrString = qrText.get()
	savePath = dwl_path.get() + '\\'

	if qrString != '':
		
		qrGenerate = pyqrcode.create(qrString)
		qrCodeName = savePath + qrString + ".png"
		qrGenerate.png(qrCodeName, scale = 10)

		image = Image.open(qrCodeName)
		image = image.resize((400, 400), Image.ANTIALIAS)

		image = ImageTk.PhotoImage(image)

		root.imageLabel.config(image = image)
		root.imageLabel.photo = image

	else:
		messagebox.showerror("ERROR", "Please, Enter Text !")

dwl_path = StringVar()
qrText = StringVar()

createWidgets()

root.mainloop()