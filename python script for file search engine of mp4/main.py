# python script for file search engine of mp4

import tkinter as tk
from tkinter import *
import os

# creating object of window
root = tk.Tk()

# setting the title and backgroung and disabling the resizing property
root.title("File Search Engine")
root.resizable(False, False)
root.config(background = "skyblue")

reLoop = 'Y'

while reLoop != 'N':

    fileType = input("Enter Which Type of File you Want to Search : ")

    fileExt = "." + fileType

    print(fileExt)

    directory = input(f"Enter Folder Path to listout {fileExt} files : ")

    newDir = os.chdir(directory)

    anyFile = os.listdir(newDir)

    count = 1

    for file in anyFile:

        if file.endswith(fileType):

            for file in anyFile:

                print(f"{count}. ---- {file}")

                count += 1

            print(f"***** {count - 1} {fileExt} Files Found !!")

            break

        else:

            print(f"No {fileExt} Files Found in Given Location")
            break

    reLoop = input("You want to Search Another File ?? y or n ")