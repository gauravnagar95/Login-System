from tkinter import *
import os
from tkinter import messagebox

file = "tempfile.temp"



def Signup():


	global pwordEntry
	global nameEntry
	global roots
    

	roots = Tk()
	roots.title('Signup')
	roots.resizable(0,0)
	instruction = Label(roots, text='==:>>New Credidentials\n',font=("Arial Bold",10), fg='#1DC0A8')
	instruction.grid(row=0,column=0,sticky=W,padx=5, pady=5)
	

	name_label = Label(roots, text='New Username: ')
	pword_label = Label(roots, text='New Password: ')
	name_label.grid(row=1,column=0,sticky=W,padx=5, pady=5)
	pword_label.grid(row=2,column=0,sticky=W,padx=5, pady=5)


	nameEntry = Entry(roots)
	pwordEntry = Entry(roots,show='*')
	nameEntry.grid(row=1,column=1)
	pwordEntry.grid(row=2,column=1)

	signupButton = Button(roots,text="Signup",bg='#153060',fg='white',command=CreateUser)
	signupButton.grid(columnspan=2, sticky=E, padx=5, pady=5)
	roots.mainloop()
    

def CreateUser():
	with open(file, 'w') as f:
		f.write(nameEntry.get())
		f.write('\n')
		f.write(pwordEntry.get())
		f.close()
	roots.destroy()
	Login()	


def Login():
	global nameEntryLogin
	global pwordEntryLogin
	global rootA
	
	rootA = Tk()
	rootA.title('Login')
	rootA.resizable(0,0)

	intruction = Label(rootA, text='==:>>Please Login\n',font=("Arial Bold",10), fg='#1DC0A8')
	intruction.grid(sticky=E)

	nameLabel = Label(rootA, text='Username: ')
	pwordLabel = Label(rootA, text='Password: ')
	nameLabel.grid(row=1, sticky=W,padx=5, pady=5)
	pwordLabel.grid(row=2, sticky=W,padx=5, pady=5)

	nameEntryLogin = Entry(rootA)
	pwordEntryLogin = Entry(rootA, show='*')
	nameEntryLogin.grid(row=1, column=1, padx=5, pady=5)
	pwordEntryLogin.grid(row=2, column=1, padx=5, pady=5)

	loginButton = Button(rootA, text='Login',bg='#153060',fg='white', command=CheckLogin)
	loginButton.grid(row=3,column=1,sticky=E,padx=5, pady=5)

	rmuser= Button(rootA, text='Delete User', fg='red',command=DelUser)
	rmuser.grid(row=3,sticky=W,padx=5, pady=5)
	rootA.mainloop()

def CheckLogin():
	with open(file) as f:
		data = f.readlines()
		print(data)
		uname = data[0].rstrip()
		pword = data[1].rstrip()

	if nameEntryLogin.get() == uname and pwordEntryLogin.get() == pword:
		rootA.destroy()
		home()
		
	else:
		messagebox.showerror('Login_info..', 'Invalid Login\nCheck Username and Password')#shows error message

def DelUser():
	os.remove(file)
	rootA.destroy()
	Signup()

def home():
	global home

	home = Tk()
	home.title('Home...')
	#home.resizable(0,0)
	menu = Menu(home)

	new_item = Menu(menu,tearoff=0)
	edit_item=Menu(menu,tearoff=0)
	selection_item=Menu(menu,tearoff=0)
	edit_item=Menu(menu,tearoff=0)
	view_item=Menu(menu,tearoff=0)

	new_item.add_command(label='New File')
	new_item.add_command(label='Save')
	new_item.add_command(label='Open File')
	new_item.add_separator()
	new_item.add_command(label='Open Folder...')
	new_item.add_separator()
	new_item.add_command(label='Logout',command=Logouthome)

	edit_item.add_command(label='Undo Insert Characters')
	edit_item.add_command(label='Repeat Insert Characters')
	edit_item.add_command(label='Undo Selection')
	edit_item.add_separator()
	edit_item.add_command(label='Cut')
	edit_item.add_command(label='Copy')
	edit_item.add_command(label='Paste')

	selection_item.add_command(label='Split into Lines')
	selection_item.add_command(label='Add Previous Lines')
	selection_item.add_command(label='Add Next Line')
	selection_item.add_command(label='Single Selection')
	selection_item.add_separator()
	selection_item.add_command(label='Select ALL')

	view_item.add_command(label='student_display',command=student_display)
	view_item.add_command(label='Hide Minimap')
	view_item.add_command(label='Hide Tabs')
	view_item.add_command(label='Hide StatusBar')
	view_item.add_separator()
	view_item.add_command(label='Enter FullScreen')
	view_item.add_command(label='Layout')
	view_item.add_command(label='Groups')
	view_item.add_command(label='Focus Groups')

	 
	menu.add_cascade(label='File', menu=new_item)
	menu.add_cascade(label='Edit',menu=edit_item)
	menu.add_cascade(label='Selection',menu=selection_item)
	menu.add_cascade(label='View',menu=view_item)
	home.config(menu=menu)
	
	home.mainloop()

def student_display():
    # python dictionary
    students_detail = {
                'Gaurav':{'roll_no':101,'physics_marks':97,'chemistry_marks':92,'maths_marks':100},
                'Rahul':{'roll_no':102,'physics_marks':92,'chemistry_marks':98,'maths_marks':95},
                'Sonu':{'roll_no':103,'physics_marks':98,'chemistry_marks':95,'maths_marks':97},
                'Rakesh':{'roll_no':102,'physics_marks':100,'chemistry_marks':93,'maths_marks':100}
                }
#---------------------------------------------------------------    
    heading_label = Label(home, text='Student list:>>>:')
    heading_label.grid(row=0,column=0,padx=5,pady=5)
#------------------------------------------------------------------
    
    col_name = Label(home, text='Student Name')
    col_name.grid(row=1,column=0,padx=1,pady=5)
    
    col_roll_no = Label(home, text='Roll Number')
    col_roll_no.grid(row=1,column=1,padx=1,pady=5)

    col_p_m = Label(home, text='Physics Marks')
    col_p_m.grid(row=1,column=2,padx=1,pady=5)

    col_c_m = Label(home, text='Chemistry Marks')
    col_c_m.grid(row=1,column=3,padx=1,pady=5)

    col_m_m = Label(home, text='Maths Marks')
    col_m_m.grid(row=1,column=4,padx=1,pady=5)
#---------------------------------------------------------------

    row = 2
    column = 0
    for student in students_detail:
        name = Label(home, text=f'{student}')
        name.grid(row=row,column=column,padx=1,pady=5)
        column = column+1

            
        roll_no = Label(home, text=f'{str(students_detail[student]["roll_no"])}')
        roll_no.grid(row=row,column=column,padx=1,pady=5)
        column = column+1

        p_m = Label(home, text=f'{students_detail[student]["physics_marks"]}')
        p_m.grid(row=row,column=column,padx=1,pady=5)
        column = column+1

        c_m = Label(home, text=f'{students_detail[student]["chemistry_marks"]}')
        c_m.grid(row=row,column=column,padx=1,pady=5)
        column = column+1

        m_m = Label(home, text=f'{students_detail[student]["maths_marks"]}')
        m_m.grid(row=row,column=column,padx=1,pady=5)

        row=row+1
        column=0        
#---------------------------------------------------------------------        

            
#GauravNagar            
            

        
        
            
            
        

    
        
        
        
        
    
    
	

    
def Logouthome():
	home.destroy()
	Login()

    
if os.path.isfile(file):
	Login()
else:
	Signup()
        
 


    


    
    
