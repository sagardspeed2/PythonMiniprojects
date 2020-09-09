import os
import smtplib
import tkinter as tk
from tkinter import *
from email import encoders
from tkinter import messagebox
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.filedialog import askopenfilenames
import re

root = tk.Tk()

root_background = 'aquamarine4'

root.title("DMail")
root.config(background=root_background)
root.resizable(False, False)
root.geometry('820x700')

email_reg_ex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# _sendMailBtn_State = DISABLED

def CreateWidgets():
	titleLabel = Label(root, text="Welcome To DMail System", bg=root_background, font=('', 15, 'bold'))
	titleLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

	labelfromEmail = Label(root, text="Email Id : ", bg=root_background, font=('', 15, 'bold'))
	labelfromEmail.grid(row=1, column=0, pady=5, padx=5)

	root.entryfromEmail = Entry(root, width=50, textvariable=fromEmail)
	root.entryfromEmail.grid(row=1, column=1, pady=5, padx=5)
	root.entryfromEmail.focus_set()

	labelPasswordEmail = Label(root, text="Password : ", bg=root_background, font=('', 15, 'bold'))
	labelPasswordEmail.grid(row=2, column=0, pady=5, padx=5)

	root.entryPasswordEmail = Entry(root, width=50, textvariable=passwordEmail, show='*')
	root.entryPasswordEmail.grid(row=2, column=1, pady=5, padx=5)

	root.showPwdBtn = Button(root, text="Show Password", width=15)
	root.showPwdBtn.grid(row=2, column=2, pady=5, padx=5)
	root.showPwdBtn.bind("<Button-1>", showPwdBtn)
	root.showPwdBtn.bind("<ButtonRelease-1>", hidePwdBtn)

	labelToEmail = Label(root, text="To Email Id : ", bg=root_background, font=('', 15, 'bold'))
	labelToEmail.grid(row=3, column=0, pady=5, padx=5)

	root.entryToEmail = Entry(root, width=50, textvariable=toEmail)
	root.entryToEmail.grid(row=3, column=1, pady=5, padx=5)

	labelSubjectEmail = Label(root, text="Subject : ", bg=root_background, font=('', 15, 'bold'))
	labelSubjectEmail.grid(row=4, column=0, pady=5, padx=5)

	root.entrySubjectEmail = Entry(root, width=50, textvariable=subjectEmail)
	root.entrySubjectEmail.grid(row=4, column=1, pady=5, padx=5)

	labelAttachmentEmail = Label(root, text="Attachment : ", bg=root_background, font=('', 15, 'bold'))
	labelAttachmentEmail.grid(row=5, column=0, pady=5, padx=5)

	root.entryAttachmentEmail = Text(root, width=38, height=5)
	root.entryAttachmentEmail.grid(row=5, column=1, pady=5, padx=5)

	attachmentBtn = Button(root, text="Browse", command=fileBrowse, width=15)
	attachmentBtn.grid(row=5, column=2, pady=5, padx=5)

	labelBodyEmail = Label(root, text="Message : ", bg=root_background, font=('', 15, 'bold'))
	labelBodyEmail.grid(row=6, column=0)

	root.bodyEmail = Text(root, width=100, height=20)
	root.bodyEmail.grid(row=7, column=0, pady=5, padx=5, columnspan=3)

	sendEmailBtn = Button(root, text="Send Mail", command=sendMail, width=15, highlightbackground='limegreen')
	sendEmailBtn.grid(row=8, column=2, padx=5, pady=5)
	sendEmailBtn.configure(background="#4CAF50")

	resetEmailBtn = Button(root, text="Reset", command=resetMail, width=15, highlightbackground='limegreen')
	resetEmailBtn.grid(row=8, column=1, padx=5, pady=5)
	resetEmailBtn.configure(background="#FF0")

	exitBtn = Button(root, text="Exit", command=emailExit, width=15, highlightbackground='red')
	exitBtn.grid(row=8, column=0, padx=5, pady=5)
	exitBtn.configure(background="red")

def showPwdBtn(event):
	root.entryPasswordEmail.config(show='')

def hidePwdBtn(event):
	root.entryPasswordEmail.config(show='*')

def fileBrowse():
	root.filename = askopenfilenames(initialdir='YOUR DIRECTORY PATH')

	for files in root.filename:
		filename = os.path.basename(files)
		root.entryAttachmentEmail.insert('1.0', filename+'\n')

def sendMail():
	_fromEmail = fromEmail.get()
	_passwordEmail = passwordEmail.get()
	_toEmail = toEmail.get()
	_subjectEmail = subjectEmail.get()
	_bodyEmail = root.bodyEmail.get('1.0', END)
	_is_attachedFile = root.entryAttachmentEmail.get('1.0', END)

	if _fromEmail == '' :
		messagebox.showerror('ERROR', 'Please Enter Your Email Id !')
		root.entryfromEmail.focus_set()
	elif _passwordEmail == '' :
		messagebox.showerror('ERROR', 'Please Enter Password !')
		root.entryPasswordEmail.focus_set()
	elif _toEmail == '' :
		messagebox.showerror('ERROR', 'Please Enter Receiver Email Id !')
		root.entryToEmail.focus_set()
	else:

		if not filterEmail(_fromEmail):
			messagebox.showerror('ERROR', 'Please Enter valid Your Email Id !')
			root.entryfromEmail.focus_set()
		elif not filterEmail(_toEmail):
			messagebox.showerror('ERROR', 'Please Enter valid Receiver Email Id !')
			root.entryToEmail.focus_set()
		else:
			message = MIMEMultipart()
			
			message['From'] = _fromEmail
			message['To'] = _toEmail
			message['Subject'] = _subjectEmail
			
			message.attach(MIMEText(_bodyEmail))

			if(not (_is_attachedFile and not _is_attachedFile.isspace())):
				pass
			else:
				for files in root.filename:
					_attachment = open(files, 'rb').read()
					_emailAttach = MIMEBase('application', 'octet-stream')
					_emailAttach.set_payload(_attachment)
					encoders.encode_base64(_emailAttach)
					_emailAttach.add_header('Content-Disposition', 'attachment; filename= %s' % os.path.basename(files))
					message.attach(_emailAttach)

			try:
				smtp = smtplib.SMTP('smtp.gmail.com', 587)
				smtp.starttls()
				smtp.login(_fromEmail, _passwordEmail)
				smtp.sendmail(_fromEmail, _toEmail, message.as_string())
				messagebox.showinfo('SUCCESS', 'Email sent to ' + str(_toEmail))
				smtp.quit()
				resetMail()
			except smtplib.SMTPAuthenticationError:
				messagebox.showerror('ERROR', 'Invalid Username and Password')
			except smtplib.SMTPConnectError:
				messagebox.showerror('ERROR', 'Please try again later !')

def filterEmail(email):
	if(re.search(email_reg_ex, email)):
		return True

def emailExit():
	MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit ?')
	if MsgBox == 'yes':
		root.destroy()

def resetMail():
	fromEmail.set('')
	passwordEmail.set('')
	toEmail.set('')
	subjectEmail.set('')
	root.bodyEmail.delete('1.0', END)
	_is_attachedFile = root.entryAttachmentEmail.get('1.0', END)
	if(not (_is_attachedFile and not _is_attachedFile.isspace())):
		pass
	else:
		root.entryAttachmentEmail.delete('1.0', END)
		root.filename = ''

fromEmail = StringVar()
passwordEmail = StringVar()
toEmail = StringVar()
subjectEmail = StringVar()

CreateWidgets()

root.mainloop()