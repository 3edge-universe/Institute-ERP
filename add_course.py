from tkinter import *
from tkinter import messagebox
from course import *

course=Course()


def add_one(window):
	def add_course():
		if (name_var.get()=="" or price_var.get()==0 or duration_var.get()==0):
			messagebox.showinfo("Error","All Field Should Filled !!")
		elif (price_var.get().isdigit()==False):
			messagebox.showinfo("Error","Price is Not Proper!! Try again")
			price.delete(0,END)
			price.config(highlightbackground="red", highlightcolor="red")
			price.focus_set()
		elif (duration_var.get().isdigit()==False):
			messagebox.showinfo("Error","Duration is Not Proper!! Try again")
			duration.delete(0,END)
			duration.config(highlightbackground="red", highlightcolor="red")
			duration.focus_set()
		else:
			if messagebox.askyesno("Alert","Want to add course?"):
				status=course.register(name_var.get(),price_var.get(),duration_var.get())
				if status=="0":
					messagebox.showinfo("Error","Course is Already Exit !!Try Another Course")
					name.delete(0,END)
					name.config(highlightbackground="red", highlightcolor="red")
					name.focus_set()
				else:
					messagebox.showinfo("Success","course Added successfully with id="+str(status))
					window.destroy()
					import main
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="Add Course",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,pady=10,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	sn=Label(subframe,text="Course Name",bg="black",fg="White",font=("default",16,'bold'))
	sn.grid(row=0,column=0,pady=10,padx=10)
	name_var=StringVar()
	name=Entry(subframe,textvariable=name_var,font=("default",16))
	name.grid(row=0,column=1,columnspan=2,pady=10,padx=10)
	
	p=Label(subframe,text="Price",bg="black",fg="White",font=("default",16,'bold'))
	p.grid(row=1,column=0,pady=10,padx=10)
	price_var=StringVar()
	price=Entry(subframe,textvariable=price_var,font=("default",16))
	price.grid(row=1,column=1,columnspan=2,pady=10,padx=10)
	
	
	d=Label(subframe,text="Duration in Hour",bg="black",fg="White",font=("default",16,'bold'))
	d.grid(row=2,column=0,pady=10,padx=10)
	duration_var=StringVar()
	duration=Entry(subframe,textvariable=duration_var,font=("default",16))
	duration.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
	
	b1=Button(subframe,text="Add",width=12,bg="blue",fg="Green",command=add_course,font=("default",18,'bold'))
	b1.grid(row=3,column=0,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=3,column=2,rowspan=2,pady=10,padx=10)