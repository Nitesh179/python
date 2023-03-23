import mysql.connector
import pandas

empdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Tout@52',
    database='pythondb'
)

emp=empdb.cursor()

# create table : ----------------------------------------

# emp.execute(''' 
#   create table empdata(
#   eid int(3) primary key,
#   ename varchar(20) NOT NULL,
#   edesg varchar(20),
#   esalary int(5)
#   )
# ''')
# empdb.commit()   

# insert single data in empdata table :---------------------------------

# id=int(input("Employee ID : "))
# name=input("Employee Name : ")
# desg=input("Employee Designation : ")
# sal=int(input("Employee Salary : "))

# emp.execute(f"insert into empdata values({id},'{name}','{desg}',{sal})")
# empdb.commit()

# insert multiple data in empdata table :-----------------------------------

# query="insert into empdata(eid, ename, edesg, esalary) values(%s, %s, %s, %s)"
# list=[]
# n=int(input("how many record you insert : "))
# for i in range(n):
#     id=int(input("Employee ID : "))
#     name=input("Employee Name : ")
#     desg=input("Employee Designation : ")
#     sal=int(input("Employee Salary : "))

#     data=(id,name,desg,sal)
#     list.append(data)
#     print('\n')

# emp.executemany(query, list)
# empdb.commit()

# print(emp.rowcount, "insert rows")

# show data from empdata :

# emp.execute("select * from empdata")

# for i in emp.fetchall():
#     print(i)

# print(pandas.Series(emp.fetchall()))
# print(pandas.DataFrame(emp.fetchall(),index=["n1","n2",'n3']))

