from conn import connection
from db import createdb
import sys

def dataEntry(database,table):
    con=connection()
    emp=con.cursor()

    emp.execute(f'use {database}')
    emp.execute(f'desc {table}')

    colname,collist="",[]     # table columns Name
    for i in emp:
       collist.append(str(i[0]))
       colname+=i[0]+', '


    emp.execute(f"select data_type from information_schema.columns where table_schema = '{database}' and table_name = '{table}'")
    emplst=list(emp)
   
    colname=colname[:-2]
    while True:
        datastr=''
        print(colname)
        for i,j in enumerate(emplst):
            if j[0]=='varchar' or j=='VARCHAR':
                datastr+=(f"'{input(f'Enter {collist[i]} : ')}', ")  
               
            else:   
                datastr+=(f'{input(f"Enter {collist[i]} : ")}, ')
                
        datastr=datastr[:-2]
        
        emp.execute(f"insert into {table} ({colname}) values ({datastr})")
        con.commit()
        
        if int(input("Insert More Data press 1 : "))!=1:
            break
       

# dataEntry('pythondb','empdata')