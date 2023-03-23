from conn import connection
from db import createdb

# database=createdb()

def table(db):
    con=connection()
    emp=con.cursor()

    emp.execute(f'use {db}')
    tablename=input("Table Name : ")
    col=int(input("No. of Columns : "))
   
    data=""
    for i in range(col):
        cn=input("Column Name : ")
        ct=input("Type : ")
        data+=(f"{str(cn)} {str(ct)},")
    print(data[:-1])        
    emp.execute(f"create table {tablename} ({data[:-1]})")
    
    print("Data Inserted ....")


table("pythondb")




