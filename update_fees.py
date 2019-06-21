from tkinter import *
from tkinter import messagebox
from fees import *

fees=Fees()


def add_one(window):
	def add_student():
		if (dob_var.get()=="" or si_var.get()=="" or sf_var.get()=="" or tf_var.get()=="" or by_var.get()==""):
			messagebox.showinfo("Error","All Field Should Filled !!")
		elif (si_var.get().isdigit()==False):
			messagebox.showinfo("Error","Student Id is Not Proper!! Try again")
			sid.delete(0,END)
			sid.config(highlightbackground="red", highlightcolor="red")
			sid.focus_set()
		elif (sf_var.get().isdigit()==False):
			messagebox.showinfo("Error","year is Not Proper!! Try again")
			sfees.delete(0,END)
			sfees.config(highlightbackground="red", highlightcolor="red")
			sfees.focus_set()
		elif (tf_var.get().isdigit()==False):
			messagebox.showinfo("Error","year is Not Proper!! Try again")
			tfees.delete(0,END)
			tfees.config(highlightbackground="red", highlightcolor="red")
			tfees.focus_set()
		elif len(re.findall(r'\w\w\w\w-\w\w\-\w\w',dob_var.get()))==0:
			messagebox.showinfo("Error","date of birth is Not Proper!! Try again")
			dateob.delete(0,END)
			dateob.config(highlightbackground="red", highlightcolor="red")
			dateob.focus_set()
		else:
			if messagebox.askyesno("Alert","Are You Sure?"):
				status=fees.register(dob_var.get(),si_var.get(),sf_var.get(),tf_var.get(),by_var.get())
				messagebox.showinfo("Success","fees submitted successfully with id="+str(status))
				window.destroy()
				import main
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="submit Fees",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,pady=10,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	dob=Label(subframe,text="Date",bg="black",fg="White",font=("default",16,'bold'))
	dob.grid(row=0,column=0,pady=10,padx=10)
	dob_var=StringVar()
	dateob=Entry(subframe,textvariable=dob_var,font=("default",16))
	dateob.grid(row=0,column=1,columnspan=2,pady=10,padx=10)
	
	si=Label(subframe,text="Student id",bg="black",fg="White",font=("default",16,'bold'))
	si.grid(row=1,column=0,pady=10,padx=10)
	si_var=StringVar()
	sid=Entry(subframe,textvariable=si_var,font=("default",16))
	sid.grid(row=1,column=1,columnspan=2,pady=10,padx=10)

	sa=Label(subframe,text="Submitted Amount",bg="black",fg="White",font=("default",16,'bold'))
	sa.grid(row=2,column=0,pady=10,padx=10)
	sf_var=StringVar()
	sfees=Entry(subframe,textvariable=sf_var,font=("default",16))
	sfees.grid(row=2,column=1,columnspan=2,pady=10,padx=10)

	ta=Label(subframe,text="Total Amount",bg="black",fg="White",font=("default",16,'bold'))
	ta.grid(row=2,column=3,pady=10,padx=10)
	tf_var=StringVar()
	tfees=Entry(subframe,textvariable=tf_var,font=("default",16))
	tfees.grid(row=2,column=4,columnspan=2,pady=10,padx=10)
	
	name=Label(subframe,text="Submitted By",bg="black",fg="White",font=("default",16,'bold'))
	name.grid(row=3,column=0,pady=10,padx=10)
	by_var=StringVar()
	sby=Entry(subframe,textvariable=by_var,font=("default",16))
	sby.grid(row=3,column=1,columnspan=2,pady=10,padx=10)

	b1=Button(subframe,text="Add",width=12,bg="blue",fg="Green",command=add_student,font=("default",18,'bold'))
	b1.grid(row=4,column=1,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=4,column=3,rowspan=2,pady=10,padx=10)