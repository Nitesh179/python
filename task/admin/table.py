from conn import connection
from db import createdb
import os,sys

database=createdb()

def table(db):
    con=connection()
    emp=con.cursor()

    emp.execute(f'use {db}')
    while True:
        os.system("clear")
        ch = int(input("\n1. Create Table\n2. Show Table\n3. Remove Table\n4. Exit\n\nSelect Option : "))

        if ch==1:
            tablename=input("Table Name : ")
            col=int(input("No. of Columns : "))
            data=""
            for i in range(col):
                cn=input("Column Name : ")
                ct=input("Type : ")
                data+=(f"{str(cn)} {str(ct)},")
            print(data[:-1])        
            emp.execute(f"create table {tablename} ({data[:-1]})")
            con.commit()
            print(f"{col} Table Created Succesfully !!!")
            return emp 
        
        elif ch==2:
            emp.execute('show tables')
            database=list(emp)

            for i,table in enumerate(database):
                print(f"{i+1}. {table}\n")

            return emp    
        
        elif ch==3:
            emp.execute(f"drop table {input('Table Name : ')}")
            print("Table Deleted !!!")

        elif ch==4:
            sys.exit(0)    

# table("pythondb")

# table(database)



