from tkinter import *
from tkinter import messagebox
from workshop import *

workshop=Workshop()


def delete_one(window):
	def delete_course():
		if (id_var.get()==""):
			messagebox.showinfo("Error","Fill workshop id!!")
		elif messagebox.askyesno("Alert","Are you sure want to delete Workshop Details?"):
			status=workshop.delete(id_var.get())
			if status=="0":
				messagebox.showinfo("Error","Unable to delete data")
			else:
				messagebox.showinfo("Success","Workshop student data deleted Successfully.")
				window.destroy()
				import main
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="Delete Workshop Details",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	#login details below
	si=Label(subframe,text="Workshop Id",bg="black",fg="White",font=("default",16,'bold'))
	si.grid(row=0,column=0,pady=10,padx=10)
	id_var=StringVar()
	student_id=Entry(subframe,textvariable=id_var,font=("default",16))
	student_id.grid(row=0,column=1,pady=10)
	
	b1=Button(subframe,text="Delete",width=12,bg="blue",fg="Green",command=delete_course,font=("default",18,'bold'))
	b1.grid(row=1,column=1,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=1,column=3,rowspan=2,pady=10,padx=10)