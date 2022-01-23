# Database connection from Python

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="pravin", password="JaiGanesh1", database="pravindb")

#get cursor to work with database, connection to databse
mycursor = mydb.cursor() 

# show all databases
'''
print("====== List Databases =======")
mycursor.execute("show databases")

for d in mycursor:
	print(d)

#Get data from table
print("====== Data from Table =======")
mycursor.execute("select * from student")

mycursor.execute("select * from student")
for d in mycursor:
	print(d)

#Insert data into table
print("====== Data from Table =======")
mycursor.execute("insert into student values ('Student_01' , 'NYU')")

for d in mycursor:
	print(d)
'''

#Get data from table
print("====== Data from Table =======")
mycursor.execute("select * from student")

#result = mycursor.fetchall()  # fetch all result
#result = mycursor.fetchone()  # fetch one row

#row = mycursor.fetchone()  # fetch one row
#print(row[0], row[1])

while True:
	row = mycursor.fetchone()   # fetch a single record from cursor
	if row != None:
		print(f"{row[0]}  SecondCol: {row[1]}")
