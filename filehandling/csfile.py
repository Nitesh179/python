import csv
import random

with open('csvfile.csv','r',newline='') as f:
 '''  w=csv.writer(f)
  w.writerow(['Eid','Ename','desg','contact'])
  n=int(input("enter no. of employee : "))

  for i in range(n):
    eno=random.randint(0,100)
    print("EId : ",eno)
    ename=input("Enter Name : ")
    edesg=input("Enter Designation : ")
    econ=input("Enter contact No.: ")
    w.writerow([eno,ename,edesg,econ])

print("{} employee data will be stored!!!!".format(n))   '''

 r=csv.reader(f)
 data=list(r)

 for i in data:
  for j in i:
   print(j,'\t',end='')
  print()