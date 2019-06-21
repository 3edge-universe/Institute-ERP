from tkinter import *
from tkinter import messagebox
from student import *

student=Student()


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
					dob_var.set(status[3])
					father_var.set(status[4])
					add_var.set(status[5])
					pin_var.set(status[6])
					mobile1_var.set(status[7])
					mobile2_var.set(status[8])
					email_var.set(status[9])
					batch_var.set(status[10])
					year_var.set(status[11])
					tf_var.set(status[12])
	def update_student():
		if (name_var.get()=="" or email_var.get()=="" or mobile1_var.get()=="" or father_var.get()=="" or add_var.get()=="" or pin_var.get()=="" or dob_var.get()=="" or batch_var.get()=="" or year_var.get()=="" or tf_var.get==""):
			messagebox.showinfo("Error","All Field Should Filled !!")
		elif len(re.findall(r'\w+@\w+\.\w+',email_var.get()))==0:
			messagebox.showinfo("Error","Email structure is Wrong !! Try Again")
			email.delete(0,END)
			email.config(highlightbackground="red", highlightcolor="red")
			email.focus_set()
		elif (mobile1_var.get().isdigit()==False) or len(mobile1_var.get())!=10:
			messagebox.showinfo("Error","Phone No is Not Proper!! Try again")
			mobile1.delete(0,END)
			mobile1.config(highlightbackground="red", highlightcolor="red")
			mobile1.focus_set()
		elif (pin_var.get().isdigit()==False) or len(pin_var.get())!=6:
			messagebox.showinfo("Error","Pin No is Not Proper!! Try again")
			pincode.delete(0,END)
			pincode.config(highlightbackground="red", highlightcolor="red")
			pincode.focus_set()
		elif (year_var.get().isdigit()==False) or len(year_var.get())!=4:
			messagebox.showinfo("Error","year is Not Proper!! Try again")
			year.delete(0,END)
			year.config(highlightbackground="red", highlightcolor="red")
			year.focus_set()
		elif (tf_var.get().isdigit()==False):
			messagebox.showinfo("Error","Total fees is Not Proper!! Try again")
			tfees.delete(0,END)
			tfees.config(highlightbackground="red", highlightcolor="red")
			tfees.focus_set()
		elif len(re.findall(r'\w\w\w\w-\w\w\-\w\w',dob_var.get()))==0:
			messagebox.showinfo("Error","date of birth is Not Proper!! Try again")
			dateob.delete(0,END)
			dateob.config(highlightbackground="red", highlightcolor="red")
			dateob.focus_set()
		else:
			if messagebox.askyesno("Alert","Are you sure want to update data?"):
				status=student.update(id_var.get(),name_var.get(),lastname_var.get(),dob_var.get(),father_var.get(),add_var.get(),pin_var.get(),mobile1_var.get(),mobile2_var.get(),email_var.get(),batch_var.get(),year_var.get(),tf_var.get())
				if status=="0":
					messagebox.showinfo("Error","Mobile No is Already Exit !!Try Another Mobile")
					mobile1.delete(0,END)
					mobile1.config(highlightbackground="red", highlightcolor="red")
					mobile1.focus_set()
				else:
					messagebox.showinfo("Success","student data was Updated Successfully.")
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
	
	dob=Label(subframe,text="Date of Birth",bg="black",fg="White",font=("default",16,'bold'))
	dob.grid(row=2,column=0,pady=10,padx=10)
	dob_var=StringVar()
	dateob=Entry(subframe,textvariable=dob_var,font=("default",16))
	dateob.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
	
	
	fn=Label(subframe,text="Father's name",bg="black",fg="White",font=("default",16,'bold'))
	fn.grid(row=2,column=3,pady=10,padx=10)
	father_var=StringVar()
	father=Entry(subframe,textvariable=father_var,font=("default",16))
	father.grid(row=2,column=4,columnspan=2,pady=10,padx=10)

	address=Label(subframe,text="Address",bg="black",fg="White",font=("default",16,'bold'))
	address.grid(row=3,column=0,pady=10,padx=10)
	add_var=StringVar()
	view=Entry(subframe,textvariable=add_var,font=("default",16))
	view.grid(row=3,column=1,columnspan=2,pady=10,padx=10)

	pin=Label(subframe,text="Pin Code",bg="black",fg="White",font=("default",16,'bold'))
	pin.grid(row=3,column=3,pady=10,padx=10)
	pin_var=StringVar()
	pincode=Entry(subframe,textvariable=pin_var,font=("default",16))
	pincode.grid(row=3,column=4,columnspan=2,pady=10,padx=10)
	
	m1=Label(subframe,text="Mobile No",bg="black",fg="White",font=("default",16,'bold'))
	m1.grid(row=4,column=0,pady=10,padx=10)
	mobile1_var=StringVar()
	mobile1=Entry(subframe,textvariable=mobile1_var,font=("default",16))
	mobile1.grid(row=4,column=1,columnspan=2,pady=10,padx=10)
	
	m2=Label(subframe,text="Mobile No",bg="black",fg="White",font=("default",16,'bold'))
	m2.grid(row=4,column=3,pady=10,padx=10)
	mobile2_var=StringVar()
	mobile2=Entry(subframe,textvariable=mobile2_var,font=("default",16))
	mobile2.grid(row=4,column=4,columnspan=2,pady=10,padx=10)
	
	e=Label(subframe,text="Email",bg="black",fg="White",font=("default",16,'bold'))
	e.grid(row=5,column=0,pady=10,padx=10)
	email_var=StringVar()
	email=Entry(subframe,textvariable=email_var,font=("default",16))
	email.grid(row=5,column=1,columnspan=2,pady=10,padx=10)
	
	batch=Label(subframe,text="batch No",bg="black",fg="White",font=("default",16,'bold'))
	batch.grid(row=6,column=0,pady=10,padx=10)
	batch_var=StringVar()
	batchno=Entry(subframe,textvariable=batch_var,font=("default",16))
	batchno.grid(row=6,column=1,columnspan=2,pady=10,padx=10)

	y=Label(subframe,text="year",bg="black",fg="White",font=("default",16,'bold'))
	y.grid(row=6,column=3,pady=10,padx=10)
	year_var=StringVar()
	year=Entry(subframe,textvariable=year_var,font=("default",16))
	year.grid(row=6,column=4,columnspan=2,pady=10,padx=10)
	
	z=Label(subframe,text="Total Fees",bg="black",fg="White",font=("default",16,'bold'))
	z.grid(row=7,column=0,pady=10,padx=10)
	tf_var=StringVar()
	tfees=Entry(subframe,textvariable=tf_var,font=("default",16))
	tfees.grid(row=7,column=1,columnspan=2,pady=10,padx=10)
	
	b1=Button(subframe,text="Update",width=12,bg="blue",fg="Green",command=update_student,font=("default",18,'bold'))
	b1.grid(row=8,column=1,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=8,column=3,rowspan=2,pady=10,padx=10)