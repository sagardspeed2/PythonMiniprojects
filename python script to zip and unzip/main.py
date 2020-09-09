import os
import tkinter as tk
from tkinter import  ttk
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox, filedialog
import time

root = tk.Tk()

root.title("Py Zip Extractor")
root.config(background = "steelblue")

def createWidgets():

	selectLabel = Label(root, text="Files to zip : ", bg="steelblue")
	selectLabel.grid(row=0, column=0, padx=5, pady=5)

	root.zipFilesEntry = Text(root, height=4, width=40)
	root.zipFilesEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    
	zipBrowseButton = Button(root, width=15, height=1, text="Browse", command=ZipFileBrowse)
	zipBrowseButton.grid(row=0, column=3, padx=5, pady=5)

	zipNameLabel = Label(root, text="Zipped Location : ", bg="steelblue")
	zipNameLabel.grid(row=1, column=0, padx=5, pady=5)

	root.zipFolderEntry = Entry(root, width=30, textvariable = zipFileName)
	root.zipFolderEntry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

	zipSaveButton = Button(root, width=15, height=1, text="Browse", command=zipSaveBrowse)
	zipSaveButton.grid(row=1, column=3, padx=5, pady=5)

	zipButton = Button(root, width=20, text="Zip", command=zipFiles)
	zipButton.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

	ttk.Separator(root,orient=HORIZONTAL).grid(row=3, columnspan=4, column=0, sticky="ew")

	unzipLabel = Label(root, text="Files to unzip : ", bg="steelblue")
	unzipLabel.grid(row=4, column=0, padx=5, pady=5)

	root.unzipFilesEntry = Entry(root, width=30)
	root.unzipFilesEntry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
    
	unzipBrowseButton = Button(root, width=15, text="Browse", command=unZipFileBrowse)
	unzipBrowseButton.grid(row=4, column=3, padx=5, pady=5)

	unzipNameLabel = Label(root, text="UnZipped Location : ", bg="steelblue")
	unzipNameLabel.grid(row=5, column=0, padx=5, pady=5)

	root.unzipFolderEntry = Entry(root,  textvariable = unzipFolderName)
	root.unzipFolderEntry.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

	unzipSaveButton = Button(root, width=15, height=1, text="Browse", command=unzipSaveBrowse)
	unzipSaveButton.grid(row=5, column=3, padx=5, pady=5)

	unzipButton = Button(root, width=20, text="unZip", command=unzipFiles)
	unzipButton.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

def ZipFileBrowse():
	root.zipFileSelection = filedialog.askopenfilenames(initialdir = os.getcwd())

	for files in root.zipFileSelection:
		root.files = os.path.basename(files)
		root.zipFilesEntry.insert('2.0', root.files+"\n")
	
	root.zipFilesEntry.config(state=DISABLED)

def zipSaveBrowse():
	zipSaveDestination = filedialog.asksaveasfilename(initialdir = os.getcwd(), filetypes = (("zip files","*.zip"),), defaultextension='.zip')
	zipFileName.set(zipSaveDestination)
	root.zipFolderEntry.config(text=zipSaveDestination)

def zipFiles():
	zipFiles = root.zipFilesEntry.get("1.0","end-1c")
	zipName = zipFileName.get()

	if zipFiles == '':
		messagebox.showerror("ERROR", "Please, Select Files !")
		return

	if zipName == '':
		messagebox.showerror("ERROR", "Please, Select Destination !")
		return

	with ZipFile(zipName, 'w') as zip_file:
		for file in root.zipFileSelection:
			zip_file.write(file, os.path.basename(file))
	
	messagebox.showinfo("SUCCESS", "Files Zipped Successfully !")

def unZipFileBrowse():
	root.unzipFileSelection = filedialog.askopenfilename(initialdir = os.getcwd(), filetypes = (("zip files","*.zip"),))

	root.files = os.path.basename(root.unzipFileSelection)
	root.unzipFilesEntry.insert('0', root.files)
	root.unzipFilesEntry.config(state=DISABLED)

def unzipSaveBrowse():
	unzipSaveDestination = filedialog.askdirectory(initialdir = os.getcwd())
	unzipFolderName.set(unzipSaveDestination)
	root.unzipFolderEntry.config(text=unzipSaveDestination)

def unzipFiles():
	unzipFiles = root.unzipFilesEntry.get()
	unzipLocation = unzipFolderName.get()

	if unzipFiles == '':
		messagebox.showerror("ERROR", "Please, Select Files !")
		return
	
	if unzipLocation == '':
		messagebox.showerror("ERROR", "Please, Select Destination !")
		return

	unZipDir = root.unzipFileSelection + time.strftime("%Y%m%d-%H%M%S")
	os.mkdir(unZipDir)
	with ZipFile(root.unzipFileSelection, 'r') as unzip_file:
		unzip_file.extractall(unZipDir)
	
	messagebox.showinfo("SUCCESS", "Files Unzipped SuccessFully")

zipFileName = StringVar()
unzipFolderName = StringVar()

createWidgets()

root.mainloop()