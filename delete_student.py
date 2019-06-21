from tkinter import *
from tkinter import messagebox
from student import *

student=Student()


def delete_one(window):
	def view_student():
		if (id_var.get()=="" or mobile_var.get()==""):
			messagebox.showinfo("Error","Fill student id and registered mobile!!")
		elif (mobile_var.get().isdigit()==False) or len(mobile_var.get())!=10:
			messagebox.showinfo("Error","Phone No is Not Proper!! Try again")
			mobile.delete(0,END)
			mobile.config(highlightbackground="red", highlightcolor="red")
			mobile.focus_set()
		else:
			if messagebox.askyesno("Alert","Login?"):
				status=student.login(id_var.get(),mobile_var.get())
				if status[0]=="0":
					messagebox.showinfo("Error","Student id or Mobile no does not exist! Try again")
					student_id.delete(0,END)
					student_id.config(highlightbackground="red", highlightcolor="red")
					student_id.focus_set()
					mobile.delete(0,END)
				else:
					name_var.set(status[1])
					lastname_var.set(status[2])
					batch_var.set(status[10])
					year_var.set(status[11])
	
	def delete_student():
		if messagebox.askyesno("Alert","Are you sure want to delete data?"):
			status=student.delete(id_var.get(),mobile_var.get())
			if status=="0":
				messagebox.showinfo("Error","Unable to delete data")
			else:
				messagebox.showinfo("Success","student data deleted Successfully.")
				window.destroy()
				import main
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="View Student",bg="white",fg="green",font=("default",30,'bold'))
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
	sn=Label(subframe,text="First Name",bg="black",fg="White",font=("default",16,'bold'))
	sn.grid(row=1,column=0,pady=10,padx=10)
	name_var=StringVar()
	name=Entry(subframe,textvariable=name_var,font=("default",16))
	name.grid(row=1,column=1,columnspan=2,pady=10,padx=10)
	
	ln=Label(subframe,text="Last Name",bg="black",fg="White",font=("default",16,'bold'))
	ln.grid(row=1,column=3,pady=10,padx=10)
	lastname_var=StringVar()
	lastname=Entry(subframe,textvariable=lastname_var,font=("default",16))
	lastname.grid(row=1,column=4,columnspan=2,pady=10,padx=10)
	
	batch=Label(subframe,text="batch No",bg="black",fg="White",font=("default",16,'bold'))
	batch.grid(row=7,column=0,pady=10,padx=10)
	batch_var=StringVar()
	batchno=Entry(subframe,textvariable=batch_var,font=("default",16))
	batchno.grid(row=7,column=1,columnspan=2,pady=10,padx=10)

	y=Label(subframe,text="year",bg="black",fg="White",font=("default",16,'bold'))
	y.grid(row=7,column=3,pady=10,padx=10)
	year_var=StringVar()
	year=Entry(subframe,textvariable=year_var,font=("default",16))
	year.grid(row=7,column=4,columnspan=2,pady=10,padx=10)
	
	b1=Button(subframe,text="Delete",width=12,bg="blue",fg="Green",command=delete_student,font=("default",18,'bold'))
	b1.grid(row=9,column=1,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=9,column=3,rowspan=2,pady=10,padx=10)