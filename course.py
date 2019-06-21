from tkinter import *
from tkinter import messagebox
import sqlite3
import re

class Course():
	def __init__(self):
		self.conn=sqlite3.connect("3_edge_universe.db")
		self.curr=self.conn.cursor()
		self.curr.execute("create table if not exists course(c_id Integer PRIMARY KEY,Name varchar NOT NULL,Price NOT NULL,duration integer NOT NULL)")
		self.conn.commit()
		
	def register(self,name,price,duration):
		'''	This is admission form'''
		s="SELECT c_id,Name FROM course"
		self.curr.execute(s)
		data=self.curr.fetchall()
		ids=[i[0] for i in data]
		data=[i[1] for i in data]
		if len(ids)==0:
			cid=0
		else:
			cid=int(list(ids)[-1])+1
		if name.lower() in data:
			return "0"
		query="INSERT INTO `course` VALUES ('%d','%s','%s','%s')"%(cid,name.lower(),price,duration)
		self.curr.execute(query)
		s="SELECT `c_id` FROM `course` where `Name`='"+name.lower()+"'"
		self.curr.execute(s)
		cid=self.curr.fetchone()[0]
		self.conn.commit()
		return cid
		
	def login(self,name):
		'''this is student details form '''
		s="SELECT `Name` FROM `course`"
		self.curr.execute(s)
		data=self.curr.fetchall()
		data=[i[0] for i in data]
		if name.lower() not in data:
			return "0"
		sql="SELECT * FROM `course` where `Name`='"+name.lower()+"'"
		self.curr.execute(sql)
		data=self.curr.fetchall()
		return data[0]
	
	def update(self,name,price,duration):
		'''	This is Update Info form'''
		query='''UPDATE `course` SET `Price`='%s',`duration`='%s' WHERE `Name`='%s' '''%(price,duration,name.lower())
		self.curr.execute(query)
		self.conn.commit()
		return "1"
	
	def delete(self,name):
		query="DELETE FROM `course` WHERE `Name`='"+name.lower()+"'"
		self.curr.execute(query)
		self.conn.commit()
		return "1"