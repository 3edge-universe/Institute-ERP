from tkinter import *
from tkinter import messagebox
import sqlite3
import re

class Workshop():
	def __init__(self):
		self.conn=sqlite3.connect("3_edge_universe.db")
		self.curr=self.conn.cursor()
		self.curr.execute('''create table if not exists workshop_detail
		(Name varchar NOT NULL,Mobile_No varchar NOT NULL,Email_id varchar NOT NULL,
		Class varchar NOT NULL,Address varchar NOT NULL,Pin_Code varchar NOT NULL,
		Collage varchar NOT NULL,workshop_id Integer NOT NULL)''')
		self.curr.execute('''create table if not exists workshop
		(workshop_id Integer PRIMARY KEY ,date DATE NOT NULL,Topic varchar NOT NULL,
		time varchar NOT NULL)''')
		
		self.conn.commit()
		
	def workshop_register(self,date,topic,time):
		s="SELECT workshop_id FROM workshop"
		self.curr.execute(s)
		data=self.curr.fetchall()
		ids=[i[0] for i in data]
		if len(ids)==0:
			wid=0
		else:
			wid=int(list(ids)[-1])+1
		query="INSERT INTO workshop VALUES ('%d','%s','%s','%s')"%(wid,date,topic,time)
		self.curr.execute(query)
		self.conn.commit()
		return wid
	
	def student_register(self,name,mobile_no,email,cls,add,pin,coll,wid):
		query='''INSERT INTO `workshop_detail` VALUES 
		('%s','%s','%s','%s','%s','%s','%s','%d')'''%(name,mobile_no,email,cls,add,pin,coll,int(wid))
		self.curr.execute(query)
		self.conn.commit()
		return "1"
	
	def login(self,w_id):
		'''this is student details form '''
		self.curr.execute("SELECT * FROM workshop_detail WHERE `workshop_id`="+w_id)
		rows=self.curr.fetchall()
		return rows	
		
	def delete(self,w_id):
		query="DELETE FROM `workshop_detail` WHERE `workshop_id`="+w_id
		self.curr.execute(query)
		self.conn.commit()
		return "1"