from tkinter import *
from tkinter import messagebox
from course import *

course=Course()


def view_one(window):
	def view_course():
		if (id_var.get()=="" or name_var.get()==""):
			messagebox.showinfo("Error","Fill course id and registered mobile!!")
		else:
			if messagebox.askyesno("Alert","Login?"):
				status=course.login(name_var.get())
				if status[0]=="0":
					messagebox.showinfo("Error","course id or Name does not exist! Try again")
					c_id.delete(0,END)
					c_id.config(highlightbackground="red", highlightcolor="red")
					c_id.focus_set()
					name.delete(0,END)
				else:
					name_var.set(status[1])
					price_var.set(status[2])
					duration_var.set(status[3])
	def update_student():
		if (name_var.get()=="" or price_var.get()==0 or duration_var.get()==0):
			messagebox.showinfo("Error","All Field Should Filled !!")
		else:
			if messagebox.askyesno("Alert","Want to update course?"):
				status=course.update(name_var.get(),price_var.get(),duration_var.get())
				messagebox.showinfo("Success","course updated successfully")
				window.destroy()
				import main
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="View course",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	#login details below
	si=Label(subframe,text="Course Id",bg="black",fg="White",font=("default",16,'bold'))
	si.grid(row=0,column=0,pady=10,padx=10)
	id_var=StringVar()
	c_id=Entry(subframe,textvariable=id_var,font=("default",16))
	c_id.grid(row=0,column=1,pady=10)
	
	m=Label(subframe,text="Course Name",bg="black",fg="White",font=("default",16,'bold'))
	m.grid(row=0,column=2,pady=10,padx=10)
	name_var=StringVar()
	name=Entry(subframe,textvariable=name_var,font=("default",16))
	name.grid(row=0,column=3,columnspan=2,pady=10)
	
	b=Button(subframe,text="Login",width=12,bg="blue",fg="Green",command=view_course,font=("default",18,'bold'))
	b.grid(row=0,column=5)
	
	#View details start from here
	p=Label(subframe,text="Price",bg="black",fg="White",font=("default",16,'bold'))
	p.grid(row=1,column=0,pady=10,padx=10)
	price_var=IntVar()
	price=Entry(subframe,textvariable=price_var,font=("default",16))
	price.grid(row=1,column=1,columnspan=2,pady=10,padx=10)
	
	d=Label(subframe,text="Duration",bg="black",fg="White",font=("default",16,'bold'))
	d.grid(row=1,column=3,pady=10,padx=10)
	duration_var=StringVar()
	duration=Entry(subframe,textvariable=duration_var,font=("default",16))
	duration.grid(row=1,column=4,columnspan=2,pady=10,padx=10)
	
	b1=Button(subframe,text="Update",width=12,bg="blue",fg="Green",command=update_student,font=("default",18,'bold'))
	b1.grid(row=2,column=1,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=2,column=3,rowspan=2,pady=10,padx=10)