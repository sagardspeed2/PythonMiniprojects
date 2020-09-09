import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import threading
from threading import Timer
import os

# creating object of window
root = tk.Tk()

# setting the title and background and disabling the resizing property
root.title("File Search Engine")
root.config(background="skyblue")
root.resizable(False, False)

# make two frame, 1 for controller and 2 for output
upper = Frame(root, borderwidth=2, relief="solid", bg="skyblue")
upper.pack(side="top", expand=True, fill="both")

down = Frame(root, borderwidth=2, relief="solid", bg="skyblue")

# create frame style
s = ttk.Style()
s.configure('new.TFrame', background='skyblue')

# create canvas and scrollbar for scroll
canvas = tk.Canvas(down, bg="skyblue", highlightthickness=0)
scrollbar = ttk.Scrollbar(down, orient="vertical", command=canvas.yview)
scrollbar_frame = ttk.Frame(canvas, style='new.TFrame')

# bind the scrollbar_frame to canvas
scrollbar_frame.bind(
	"<Configure>",
	lambda e: canvas.configure(
		scrollregion=canvas.bbox("all")
	)
)

# create window of canvas and configure it
canvas.create_window((0, 0), window=scrollbar_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

down.pack(side="bottom", expand=True, fill="both")

# function of creating design of module
def CreateModule():

    # create label for path select
    path_label = Label(upper, text='Select Folder Path : ', bg="skyblue")
    path_label.grid(row=0, column=0, padx=10, pady=5)

    # create entrybox for path_label
    upper.path_label_entry = Entry(upper, width=36, textvariable=pathLabel)
    upper.path_label_entry.grid(row=0, column=1, padx=10, pady=5)

    # create button for path_label
    path_label_button = Button(upper, text="Browse", command=browse_dir)
    path_label_button.grid(row=0, column=2, padx=5, pady=5)

    # create label for file types
    file_type = Label(upper, text='Enter File Type : ', bg='skyblue')
    file_type.grid(row=1, column=0, padx=10, pady=5)

    # create entrybox for file_type
    upper.file_type_entry = Entry(upper, width=36, textvariable=fileType)
    upper.file_type_entry.grid(row=1, column=1, padx=10, pady=5)

    # create button for search file_type in pathLabel
    seach_file = Button(upper, text="Search Files", command=fileSearch)
    seach_file.grid(row=2, column=0, padx=10, pady=5, columnspan=2)


# function of folder selection
def browse_dir():
    # open filedialog box for select folder
    pathLabel.set('')
    path_text = filedialog.askdirectory()

    # pass folder name in entry box
    upper.path_label_entry.insert('0', path_text)

    # remove all widget from output frame for insert new widgets
    for widget in scrollbar_frame.winfo_children():
        widget.destroy()

    # remove the grid after remove all widgets of 2 frame
    down.pack_forget()


# function for search file_type in pathLabel
def fileSearch():

    # make a grid of frame, canvas and scrollbar to insert new widgets
    down.pack(side="bottom", expand=True, fill="both")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # fetch values of pathLabel and fileType from CreateModule function
    pathName = pathLabel.get()
    fileExt = '.'+fileType.get()

    pathDir = os.chdir(pathName)  # change current directory to user defined directory

    fileList = os.listdir(pathDir)  # fetching file lest of given directory

    count = 1  # serialization number
    row = 3

    # iterate all widgets
    for file in fileList:

        if file.lower().endswith(fileExt):

            # file name label using for loop
            file_name = Label(scrollbar_frame, text=f"{count} --- {file}", bg="skyblue")
            file_name.grid(row=row, column=0, padx=10, pady=5, columnspan=2, sticky=W)

            filePath = pathLabel.get()
            file_open_path = os.path.join(filePath, file)

            scrollbar_frame.file_name_button = Button(scrollbar_frame, text="open", command= lambda currentFile=file: fileOpen(currentFile))
            scrollbar_frame.file_name_button.grid(row=row, column=2, padx=10, pady=5, sticky=E)

            count += 1
            row += 1

        else:

            print("no file found")


# function of open file in their program
def fileOpen(file):

    # fetch path of file and file name
    filePath = pathLabel.get()

    file_open_path = os.path.join(filePath, file)

    # open file
    os.startfile(file_open_path)


# calling create module function

pathLabel = tk.StringVar()
fileType = tk.StringVar()
file_name_ext = tk.StringVar()

CreateModule()

# infinite loop to run application
root.mainloop()
