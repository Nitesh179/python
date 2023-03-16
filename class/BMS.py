import os,rich,sys,random,datetime
from rich.console import Console
from rich.table import Table
import csv
import pandas as pd


class ABC_Bank:
    bank_name="ABC BANK LTD"
    IFSC_code="ABCB0000189"
    # CustomerList=[]
    # for dummy data :
    name=['nitesh','vinay','sunny','bunny','jay','suresh','vinny','chinny','chiku','neeraj']
    date=['18-04-2001','11-02-2001','05-02-2015','15-02-2020','02-02-2012','11-02-2012','13-02-2001','12-03-2011','12-02-2010','12-02-2002']
    address=['indore','indore','bhopal','ujjain','devas']
    bal=[12000,13000,50000,15000,20000,17000]


    CustomerList=[]



    # ========== Create account function ========= 
    def createAccount(self):
        # while True:
        #     deposite=int(input("Enter Deposite Amount : "))
        #     if deposite>10000:
        #         break
        #     elif deposite ==0 : sys.exit(0)
        #     elif deposite<10000 and deposite>0 : print("Insufficient Balance!!!\n\n Try again other wise press 0 to exit : \n")
        
        #   taking customer information :
        #  random.randint(100,500)
        with open('csvfile.csv','a',newline='') as f:
            w=csv.writer(f)
            w.writerow(['acc_no','openingDate','name','contact','dob','address','balance']) 


            for i in range(1,30):
                
                acc_no=random.randint(100,500),
                openingDate=random.choice(self.date),
                name=random.choice(self.name),
                contact=random.randint(1111111111,9999999999),
                dob=random.choice(self.date),
                address=random.choice(self.address),
                balance=random.choice(self.bal)
                w.writerow([str(acc_no), str(openingDate), str(name), str(contact), str(dob), str(address), str(balance)])
            
            # self.CustomerList.append(obj) 
          
         


        # acc_no=321
        # openingDate = datetime.date.today()
        # name=input("Enter Customer Name : ")
        # contact=int(input("Enter phone No. : "))
        # date=input("enter date in this format dd-mm-yyyy : ").split('-')
        # dob=datetime.date(int(date[2]),int(date[1]),int(date[0]))
        # address=input("Enter Customer Address : ")
        # obj = {"acc_no":acc_no,
        #        "openingDate":openingDate,
        #        "name":name,
        #        "contact":contact,
        #        "dob":dob,
        #        "address":address,
        #        "balance":deposite}   
        return self.CustomerList   


    
    # =================== Check account detail ===================
    def check_detail(self,acc):
        for Ac_detail in self.CustomerList:
            if Ac_detail["acc_no"]==acc:
                return Ac_detail
        print("Account not found !!! \n\nPlease try another number")
        
    #  ==================== Customer lists ==================== 
    def customer_list(self):
        # table = Table(title="ABC Bank Customers Details")
        # table.add_column("Acc.No", justify="right", style="cyan", no_wrap=True)
        # table.add_column("Open date", style="grey0")
        # table.add_column("Customer Name", style="grey0")
        # table.add_column("Contact No", style="grey0")
        # table.add_column("Balance", justify="right", style="green")
        
        # for customer in self.CustomerList:
        #     # acc=str(customer['acc_no'])

        #     table.add_row(str(customer['acc_no']),str(customer['openingDate']),str(customer['name']),str(customer['contact']),str(customer['balance']))
        # console = Console()
        # console.print(table)


        data = pd.read_csv("csvfile.csv")
        print(data)



    #  ==================== modify account ==================== 
    def update_detail(self,acc):
        inc,flag=0,False
        for Ac_detail in self.CustomerList:
            if Ac_detail["acc_no"]==acc:
                print("Which information you want to update ? \n\n1. Name \n2. Contact \n3. Address \n4. Date of Birth\n5. exit ")
            while True:   
                choice = int(input("Enter here : "))
                if choice == 1:
                   Ac_detail["name"]==input("Enter name here : ")
                elif choice == 2:
                   Ac_detail["contact"]==input("Enter contact here : ")
                elif choice == 3:
                   Ac_detail["address"]==input("Enter address here : ")
                elif choice == 4:
                   Ac_detail["dob"]==input("Enter dob here : ")
                elif choice == 5:
                   flage = True
                   break
            inc+=1
            if flag:
                self.CustomerList.pop(inc)
                break
        return self.CustomerList
                    

                


        # print("Account not found !!! \n\nPlease try another number")


a1=ABC_Bank()

print(a1.createAccount())

a1.customer_list()

# res = a1.update_detail(int(input("Enter account number : ")))
# print(res)


# a1.check_detail(321)
