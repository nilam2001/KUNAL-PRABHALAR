import mysql.connector as mysql
conn=mysql.connect(user="root",password="bhavya123",host='127.0.0.1')
c=conn.cursor()
#c.execute("create database bhavya")
#c.execute("show databases")
c.execute("use bhavya")
#c.execute("create table studentss(sid int(5),sname varchar(20),slocation varchar(20))")
#print(c.fetchall())
#c.execute("show tables from bhavya")

'''c.execute("insert into studentss values(1,'daniel','malad')")
c.execute("insert into students values(2,'hardik','borivali')")
c.execute("insert into students values(3,'shiva','nalasopara')")
c.execute("insert into students values(4,'daniel','gorai')")
c.execute("insert into students values(5,'daniel','maladwest')")'''
'''c.execute("select  *from students")
rows=c.fetchall()
sid=rows[1][0]
sid1=rows[2][0]
print(sid)
c.execute("update students set sname='stu' where sid="+str(sid))
c.execute("update students set sname='abc' where sid="+str(sid1))
conn.commit()'''
#c.execute("select * from students")
c.execute("drop table students")
#c.execute("show table from bhavya")
#c.execute("drop database bhavya")    
#print(c.fetchall())
conn.close()
