from tkinter import *
from tkinter import messagebox

window=Tk()
window.wm_title("ERP")
window.geometry('1350x700')
window.configure()
	
def add_student():
	f.pack_forget()
	from add_student import add_one
	add_one(window)
def search_student():
	f.pack_forget()
	from view_student import view_one
	view_one(window)
def delete_student():
	f.pack_forget()
	from delete_student import delete_one
	delete_one(window)

def fee_submit():
	f.pack_forget()
	from update_fees import add_one
	add_one(window)
def fee_details():
	f.pack_forget()
	from view_fees import view_one
	view_one(window)
	
def add_course():
	f.pack_forget()
	from add_course import add_one
	add_one(window)
def view_course():
	f.pack_forget()
	from view_course import view_one
	view_one(window)
def delete_course():
	f.pack_forget()
	from delete_course import delete_one
	delete_one(window)

def add_workshop():
	f.pack_forget()
	from add_workshop import add_one
	add_one(window)
def view_workshop():	
	f.pack_forget()
	from view_workshop import view_one
	view_one(window)
def delete_workshop():
	f.pack_forget()
	from delete_workshop import delete_one
	delete_one(window)

def exit():
	if messagebox.askyesno("EXIT","Do you want close window?"):
		window.quit()
	
#menu bar code below
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Admission", command=add_student)
filemenu.add_command(label="View Student", command=search_student)
filemenu.add_command(label="Delete Student", command=delete_student)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="Menu", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Fees Details", command=fee_details)
helpmenu.add_command(label="Submit Fees", command=fee_submit)
menubar.add_cascade(label="Fees", menu=helpmenu)

coursemenu = Menu(menubar, tearoff=0)
coursemenu.add_command(label="Add Course", command=add_course)
coursemenu.add_command(label="View Course", command=view_course)
coursemenu.add_command(label="Delete Course", command=delete_course)
menubar.add_cascade(label="Course", menu=coursemenu)

workshopmenu = Menu(menubar, tearoff=0)
workshopmenu.add_command(label="Add Details", command=add_workshop)
workshopmenu.add_command(label="View students", command=view_workshop)
workshopmenu.add_command(label="delete Workshop Details", command=delete_workshop)
menubar.add_cascade(label="Workshop", menu=workshopmenu )


window.config(menu=menubar)

#title bar code below
l1=Label(window,text="ERP SYSTEM",bg="black",fg="White",font=("default",40,'bold'),relief='raised',bd=10)
l1.pack(side=TOP,fill=X,padx=10)

#frame
f=Frame(window,bg="black",height=600,relief='solid',bd=10)
f.pack(fill=BOTH,pady=20,padx=10)

img=PhotoImage(file="E:/3_edge_coaching/ADMIN/LOGOS/logo.png")
l=Label(f,image=img,bg="black",relief='raised',bd=2)
l.pack(fill=BOTH,ipadx=100,ipady=100)

window.mainloop()