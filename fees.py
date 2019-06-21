from tkinter import *
from tkinter import messagebox
import sqlite3
import re

class Fees():
	def __init__(self):
		self.conn=sqlite3.connect("3_edge_universe.db")
		self.curr=self.conn.cursor()
		self.curr.execute('''create table if not exists receipt_detail(Receipt_NO Integer,
	Date DATE NOT NULL,Student_id Integer NOT NULL,
	Submitted_Amount Integer NOT NULL,Total_Amount Integer NOT NULL,Submitted_BY varchar NOT NULL)''')
		self.conn.commit()
		
	def register(self,date,stud_id,submit_amount,total_amount,by):
		'''	This is fee submission form'''
		s="SELECT Receipt_NO FROM receipt_detail"
		self.curr.execute(s)
		data=self.curr.fetchall()
		ids=[i[0] for i in data]
		data=[i[1] for i in data]
		if len(ids)==0:
			rid=0
		else:
			rid=int(list(ids)[-1])+1
		query='''INSERT INTO `receipt_detail` VALUES 
		('%d','%s','%d','%d','%d','%s')
		'''%(rid,date,int(stud_id),int(submit_amount),int(total_amount),by)
		self.curr.execute(query)
		self.update(stud_id,submit_amount)
		return rid
		
	def login(self,stud_id,r_no):
		'''this is student details form '''
		s="SELECT Mobile_No FROM student_record"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if r_no not in data:
			return "0"
		sql="SELECT Total_Fees, Submitted_Fee FROM student_record WHERE Stu_Id='%d' and `Mobile_No`='%s'"%(int(stud_id),r_no)
		self.curr.execute(sql)
		data=self.curr.fetchall()
		return data[0]
		
	def view(self,stud_id):
		self.curr.execute("SELECT * FROM receipt_detail WHERE Student_id='%d'"%(int(stud_id)))
		rows=self.curr.fetchall()
		return rows
		
	def update(self,stud_id,amount):
		'''	This is Update Info form'''
		s="SELECT `Submitted_Fee` FROM `student_record` WHERE `Stu_Id`="+stud_id
		self.curr.execute(s)
		data=self.curr.fetchall()
		amount=str(int(data[0][0])+int(amount))
		query="UPDATE `student_record` SET `Submitted_Fee`='"+amount+"' WHERE `Stu_Id`="+stud_id
		self.curr.execute(query)
		self.conn.commit()
		return "1"