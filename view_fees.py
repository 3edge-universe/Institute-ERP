from tkinter import *
from tkinter import messagebox
from fees import *

fees=Fees()


def view_one(window):
	def view_student():
		if (id_var.get()=="" or mobile_var.get()==""):
			messagebox.showinfo("Error","Fill student id and registered mobile!!")
		elif (mobile_var.get().isdigit()==False) or len(mobile_var.get())!=10:
			messagebox.showinfo("Error","Phone No is Not Proper!! Try again")
			mobile.delete(0,END)
			mobile.config(highlightbackground="red", highlightcolor="red")
			mobile.focus_set()
		else:
			status=fees.login(id_var.get(),mobile_var.get())
			if status[0]=="0":
				messagebox.showinfo("Error","Student id or Mobile no does not exist! Try again")
				student_id.delete(0,END)
				student_id.config(highlightbackground="red", highlightcolor="red")
				student_id.focus_set()
				mobile.delete(0,END)
			else:
				tf_var.set(status[0])
				sf_var.set(status[1])
				rf_var.set(str(int(status[0])-int(status[1])))
				row=fees.view(id_var.get())
				for i in range(len(row)):
					cols = []
					for j in range(6):
						e = Entry(subf,relief="ridge")
						e.grid(row=i+1,column=j, sticky=NSEW)
						e.insert(END,row[i][j])
						cols.append(e)
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="View Fees Details",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	#login details below
	si=Label(subframe,text="Student Id",bg="black",fg="White",font=("default",16,'bold'))
	si.grid(row=0,column=0,pady=10,padx=10)
	id_var=StringVar()
	student_id=Entry(subframe,textvariable=id_var,font=("default",16))
	student_id.grid(row=0,column=1,pady=10)
	
	m=Label(subframe,text="Register No",bg="black",fg="White",font=("default",16,'bold'))
	m.grid(row=0,column=2,pady=10,padx=10)
	mobile_var=StringVar()
	mobile=Entry(subframe,textvariable=mobile_var,font=("default",16))
	mobile.grid(row=0,column=3,columnspan=2,pady=10)
	
	b=Button(subframe,text="Login",width=12,bg="blue",fg="Green",command=view_student,font=("default",18,'bold'))
	b.grid(row=0,column=5)
	
	#View details start from here
	sn=Label(subframe,text="Total Fees",bg="black",fg="White",font=("default",16,'bold'))
	sn.grid(row=1,column=0,pady=10,padx=10)
	tf_var=StringVar()
	tfees=Entry(subframe,textvariable=tf_var,font=("default",16))
	tfees.grid(row=1,column=1,columnspan=2,pady=10,padx=10)
	
	ln=Label(subframe,text="Submitted fees",bg="black",fg="White",font=("default",16,'bold'))
	ln.grid(row=1,column=3,pady=10,padx=10)
	sf_var=StringVar()
	sfees=Entry(subframe,textvariable=sf_var,font=("default",16))
	sfees.grid(row=1,column=4,columnspan=2,pady=10,padx=10)
	
	mn=Label(subframe,text="Remaining Fees",bg="black",fg="White",font=("default",16,'bold'))
	mn.grid(row=2,column=0,pady=10,padx=10)
	rf_var=StringVar()
	rfees=Entry(subframe,textvariable=rf_var,font=("default",16))
	rfees.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
	
	#fee receipt details below
	subf=Frame(subframe,bg="black",height=300,relief='solid',bd=10)
	subf.grid(row=3,column=0,columnspan=4,rowspan=5,pady=10,padx=10)
	e1 = Label(subf,text='Receipt_No',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e1.grid(row=0,column=0)
	e2 = Label(subf,text='Date',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e2.grid(row=0,column=1)
	e3 = Label(subf,text='Student_Id',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e3.grid(row=0,column=2)
	e4 = Label(subf,text='Submitted',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e4.grid(row=0,column=3)
	e5 = Label(subf,text='Total',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e5.grid(row=0,column=4)
	e6 = Label(subf,text='Submitted By',relief="ridge",bg="black",fg="White",font=("default",16,'bold'))
	e6.grid(row=0,column=5)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=9,column=3,rowspan=2,pady=10,padx=10)