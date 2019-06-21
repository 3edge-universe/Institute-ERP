from tkinter import *
from tkinter import messagebox
import sqlite3
import re

class Student():
	def __init__(self):
		self.conn=sqlite3.connect("3_edge_universe.db")
		self.curr=self.conn.cursor()
		self.curr.execute('''create table if not exists student_record
		(Stu_Id INTEGER PRIMARY KEY,First_Name VARCHAR NOT NULL,Last_Name varchar NOT NULL,
		DOB DATE NOT NULL,Fathers_Name varchar NOT NULL,Address varchar NOT NULL,
		Pin_Code varchar NOT NULL,Mobile_No varchar NOT NULL,Mobile_No2 varchar,
		Email_id varchar NOT NULL,Batch_no varchar NOT NULL,Year varchar NOT NULL,Total_Fees INTEGER,
		Submitted_Fee INTEGER)''')
		self.conn.commit()
		
	def register(self,name,lname,dob,fname,add,pin,mob1,mob2,email,bno,year):
		'''	This is admission form'''
		s="SELECT Stu_Id,Mobile_No FROM student_record"
		self.curr.execute(s)
		data=self.curr.fetchall()
		ids=[i[0] for i in data]
		data=[i[1] for i in data]
		if len(ids)==0:
			sid=0
		else:
			sid=int(list(ids)[-1])+1
		if mob1 in data:
			return "0"
		query='''INSERT INTO student_record VALUES 
		('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',0,0)
		'''%(sid,name,lname,dob,fname,add,pin,mob1,mob2,email,bno,year)
		self.curr.execute(query)
		self.conn.commit()
		return sid
		
	def login(self,stud_id,r_no):
		'''this is student details form '''
		stud_id=int(stud_id)
		s="SELECT Mobile_No FROM student_record"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if r_no not in data:
			return "0"
		sql="SELECT * FROM `student_record` where `Stu_Id`='%d' and `Mobile_No`='%s'"%(stud_id,r_no)
		self.curr.execute(sql)
		data=self.curr.fetchall()
		return data[0]
	
	def update(self,stud_id,name,lname,dob,fname,add,pin,mob1,mob2,email,bno,year,tfees):
		'''	This is Update Info form'''
		query='''UPDATE `student_record` SET `First_Name`='%s',`Last_Name`='%s',`DOB`='%s',`Fathers_Name`='%s',`Address`='%s',`Pin_Code`='%s',
		`Mobile_No`='%s',`Mobile_No2`='%s',`Email_id`='%s',`Batch_no`='%s',`Year`='%s',`Total_Fees`='%d' WHERE `Stu_Id`='%d'
		'''%(name,lname,dob,fname,add,pin,mob1,mob2,email,bno,year,int(tfees),int(stud_id))
		self.curr.execute(query)
		self.conn.commit()
		return "1"
	
	def delete(self,stud_id,r_no):
		query="DELETE FROM `student_record` WHERE `Stu_Id`="+stud_id+" and `Mobile_No`="+r_no
		self.curr.execute(query)
		query="DELETE FROM `receipt_detail` WHERE `Student_id`="+stud_id
		self.curr.execute(query)
		self.conn.commit()
		return "1"