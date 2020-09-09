from tkinter import *
from bs4 import BeautifulSoup
import re, json, requests, tkinter as tk

root = tk.Tk()

root.geometry("428x350")
root.title("Istagram Followers Counter")
root.config(background = 'deepskyblue4')

def CreateWidgets():
	idLabel = Label(root, text="Instagram Id : ", background="deepskyblue4")
	idLabel.grid(row=0, column=0, padx=5, pady=5)

	root.idEntry = Entry(root, width=30, textvariable=instaId)
	root.idEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

	findBtn = Button(root, width=45, text="Count Followers", command=exactCount)
	findBtn.grid(row=1, column=0, columnspan=2, pady=5, padx=5)
	
	followersLabel = Label(root, text="Followers Count : ", background="deepskyblue4")
	followersLabel.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
	followersLabel.config(font=("Courier", 35))

	root.countLabel = Label(root, background="darkslategrey", fg="yellowgreen")
	root.countLabel.config(font=("Courier", 50))

def exactCount():
	insta_id = instaId.get()
	insta_page = requests.get('https://www.instagram.com/'+insta_id)
	soup = BeautifulSoup(insta_page.text, "html.parser")

	script = soup.find('script', text=re.compile('window._sharedData'))
	page_json = script.text.split(' = ', 1)[1].rstrip(';')
	data = json.loads(page_json)

	followers = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
	root.countLabel.grid(row=3, column=0, padx=5, pady=50, columnspan=2)
	root.countLabel.config(text=str(followers))

instaId = StringVar()

CreateWidgets()

root.mainloop()