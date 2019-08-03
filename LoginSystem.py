from tkinter import *
import os
from tkinter import messagebox

file = 'tempfile.temp'

def Signup():

	global nameEntry
	global pwordEntry
	global roots

	roots = Tk()
	roots.title('Signup')
	roots.resizable(0,0)

	instruction = Label(roots, text='==:>>New Credidentials\n',font=('Arial Bold',10),fg='#1DC0A8')
	instruction.grid(row=0,column=0,sticky=W,padx=5,pady=5)

	name_label = Label(roots, text='New Username: ')
	pword_label= Label(roots, text='New Password: ')
	name_label.grid(row=1,column=0,sticky=W,padx=5,pady=5)
	pword_label.grid(row=2,column=0,sticky=W,padx=5,pady=5)

	nameEntry = Entry(roots)
	pwordEntry = Entry(roots,show='*')
	nameEntry.grid(row=1,column=1)
	pwordEntry.grid(row=2,column=1)

	signupButton = Button(roots,text='Signup',bg='#153060',fg='white',command=CreateUser) #CreateUser is function name
	signupButton.grid(columnspan=2,sticky=E,padx=5,pady=5)

	roots.mainloop()

def CreateUser():
	f = open(file, 'w')
	f.write(nameEntry.get())
	f.write('\n')
	f.write(pwordEntry.get())
	f.close()
	roots.destroy()
	Login() # Calling the Login method


def Login():

	global nameEntryLogin
	global pwordEntryLogin
	global rootL

	rootL = Tk()
	rootL.title('Login')
	rootL.resizable(0,0)

	instruction = Label(rootL, text='==:>>Please Login\n',font=("Arial Bold",10),fg='#1DC0A8')
	instruction.grid(sticky=E)

	nameLabel = Label(rootL, text='Username: ')
	pwordLabel = Label(rootL,text='Password: ')
	nameLabel.grid(row=1, sticky=W, padx=5, pady=5)
	pwordLabel.grid(row=2,sticky=W, padx=5, pady=5)


	nameEntryLogin = Entry(rootL)
	pwordEntryLogin = Entry(rootL, show='*')
	nameEntryLogin.grid(row=1,column=1,padx=5,pady=5)
	pwordEntryLogin.grid(row=2,column=1,padx=5,pady=5)

	loginButton = Button(rootL, text='Login',bg='#153060',fg='white',command=CheckLogin) #CheckLogin method
	loginButton.grid(row=3,column=1,sticky=E,padx=5,pady=5)

	removeUser = Button(rootL,text='Delete User', fg='red',command=DelUser)
	removeUser.grid(row=3,sticky=W,padx=5,pady=5)

	rootL.mainloop()


def CheckLogin():
	f=open(file)
	data = f.readlines()
	print(data)

	uname = data[0].rstrip()
	pword = data[1].rstrip()

	if nameEntryLogin.get() == uname and pwordEntryLogin.get() == pword:
		rootL.destroy()
		home()
	else:
		messagebox.showerror('Logininfo..','Invalid Login\nCheck Username and Password') # show error message



def DelUser():
	os.remove(file)
	rootL.destroy()
	Signup()





def home():

	global home

	home = Tk()
	home.title('Home..')
	home.resizable(0,0)
	home.geometry('700x400')
	menu = Menu(home)

	new_item = Menu(menu, tearoff=0)
	edit_item = Menu(menu,tearoff=0)
	

	new_item.add_command(label='New File')
	new_item.add_command(label='Save')
	new_item.add_command(label='Open Folder..')

	new_item.add_separator()

	new_item.add_command(label='Logout',command=Logouthome)

	edit_item.add_command(label='Show Label',command=other)
	edit_item.add_command(label='Repeat Insert Characters')
	edit_item.add_command(label='Undo Selection')


	new_item.add_separator()

	edit_item.add_command(label='Cut')
	edit_item.add_command(label='Copy')
	edit_item.add_command(label='Paste')




	menu.add_cascade(label='File', menu=new_item)
	menu.add_cascade(label='Edit', menu=edit_item)

	home.config(menu=menu)

	home.mainloop()

def Logouthome():
	home.destroy()
	Login()

def other():
	homelabel=Label(home, text='CoderDesk...',font=('Algerian',30),fg='#F1761B')
	homelabel.place(x=50,y=50)



if os.path.isfile(file):
	Login()
else:
	Signup()