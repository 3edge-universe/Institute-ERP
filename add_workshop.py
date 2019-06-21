from tkinter import *
from tkinter import messagebox
from workshop import *

workshop=Workshop()


def add_one(window):
	def add_workshop():
		if (name_var.get()=="" or date_var.get()=="" or time_var.get()==""):
			messagebox.showinfo("Error","All Field Should Filled !!")
		elif len(re.findall(r'\w\w\w\w-\w\w\-\w\w',date_var.get()))==0:
			messagebox.showinfo("Error","date is Not Proper!! Try again")
			date.delete(0,END)
			date.config(highlightbackground="red", highlightcolor="red")
			date.focus_set()
		elif len(re.findall(r'\w\w:\w\w',time_var.get()))==0:
			messagebox.showinfo("Error","Time is Not Proper!! Try again")
			time.delete(0,END)
			time.config(highlightbackground="red", highlightcolor="red")
			time.focus_set()
		else:
			if messagebox.askyesno("Alert","Want to add workshop?"):
				status=workshop.workshop_register(date_var.get(),name_var.get(),time_var.get())
				messagebox.showinfo("Success","course Added successfully with id="+str(status))
				f1.pack_forget()
				from add_workshop_detail import add_one
				add_one(window,status)
	
	def back():
		window.destroy()
		import main
	
	f1=Frame(window,bg="black",height=600,relief='solid',bd=10)
	f1.pack(fill=BOTH,pady=20,padx=10)
	l1=Label(f1,text="Add Workshop",bg="white",fg="green",font=("default",30,'bold'))
	l1.pack(fill=BOTH,pady=10,padx=100)
	subframe=Frame(f1,bg="white",height=500,relief='solid',bd=10)
	subframe.pack(fill=BOTH,pady=10,padx=100)
	
	sn=Label(subframe,text="Topic",bg="black",fg="White",font=("default",16,'bold'))
	sn.grid(row=0,column=0,pady=10,padx=10)
	name_var=StringVar()
	name=Entry(subframe,textvariable=name_var,font=("default",16))
	name.grid(row=0,column=1,columnspan=2,pady=10,padx=10)
	
	d=Label(subframe,text="Date",bg="black",fg="White",font=("default",16,'bold'))
	d.grid(row=2,column=0,pady=10,padx=10)
	date_var=StringVar()
	date=Entry(subframe,textvariable=date_var,font=("default",16))
	date.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
	
	t=Label(subframe,text="Time",bg="black",fg="White",font=("default",16,'bold'))
	t.grid(row=1,column=0,pady=10,padx=10)
	time_var=StringVar()
	time=Entry(subframe,textvariable=time_var,font=("default",16))
	time.grid(row=1,column=1,columnspan=2,pady=10,padx=10)
	
	b1=Button(subframe,text="Add",width=12,bg="blue",fg="Green",command=add_workshop,font=("default",18,'bold'))
	b1.grid(row=3,column=0,rowspan=2,pady=10,padx=10)
	
	b2=Button(subframe,text="Cancle",width=12,bg="blue",fg="Green",command=back,font=("default",18,'bold'))
	b2.grid(row=3,column=2,rowspan=2,pady=10,padx=10)