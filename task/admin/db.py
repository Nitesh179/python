from conn import connection
import sys,os

def createdb(con):
    
    emp=con.cursor()
    
    while True:
        os.system("clear")
        ch = int(input("\n1. Create DB\n2. Show DB\n3. Remove Database\n4. Use DB\n5. Exit\n\nSelect Option : "))
    
        if ch==1:
            emp.execute(f'create database {input("Enter DataBase Name : ")}')
            print("Database Created !!!")

        elif ch==2:
            emp.execute('show databases')
            database=list(emp)

            for i,db in enumerate(database):
                print(f"{i+1}. {db}\n")
            choice = int(input("Choose Any One : "))
            return database[choice-1]
        elif ch==3:
               emp.execute(f'drop database {input("DB Name : ")}')
               print("Database Deleted !!!")

        elif ch==4:
            emp.execute(f'use {input("DB Name : ")}')
            print("Database Changed....")
            return emp
        
        elif ch==5:
            sys.exit(0)

# createdb()

con = connection()
createdb(con)