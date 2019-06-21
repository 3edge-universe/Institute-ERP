from tkinter import *
from tkinter import messagebox
from workshop import *

workshop=Workshop()


def view_one(window):
	def view_student():
		if (id_var.get()==""):
			messagebox.showinfo("Error","Fill Workshop id")
		else:
			row=workshop.login(id_var.get())
			if row=="0":
				messagebox.showinfo("Error","Workshop id does not exist! Try again")
				student_id.delete(0,END)
				student_id.config(highlightbackground="red", highlightcolor="red")
				student_id.focus_set()
			else:
				for i in range(len(row)):
					cols = []
					for j in range(7):
						e = Entry(subf,relief="ridge")
						e.grid(row=i+1,column=j, sticky=NSEW)
						e.insert(END,row[i][j])
						cols.append(e)
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="View Workshop Details",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	#login details below
	si=Label(subframe,text="Workshop Id",bg="black",fg="White",font=("default",16,'bold'))
	si.grid(row=0,column=0,pady=10,padx=10)
	id_var=StringVar()
	student_id=Entry(subframe,textvariable=id_var,font=("default",16))
	student_id.grid(row=0,column=1,pady=10)

	b=Button(subframe,text="Login",width=12,bg="blue",fg="Green",command=view_student,font=("default",18,'bold'))
	b.grid(row=0,column=5)
	
	#fee receipt details below
	subf=Frame(subframe,bg="black",height=300,relief='solid',bd=10)
	subf.grid(row=1,column=0,columnspan=4,rowspan=5,pady=10,padx=10)
	e1 = Label(subf,text='Name',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e1.grid(row=0,column=0)
	e2 = Label(subf,text='Mobile_no',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e2.grid(row=0,column=1)
	e3 = Label(subf,text='Email',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e3.grid(row=0,column=2)
	e4 = Label(subf,text='class',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e4.grid(row=0,column=3)
	e5 = Label(subf,text='Address',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e5.grid(row=0,column=4)
	e6 = Label(subf,text='Pin',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e6.grid(row=0,column=5)
	e7 = Label(subf,text='Collage',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e7.grid(row=0,column=5)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=9,column=3,rowspan=2,pady=10,padx=10)