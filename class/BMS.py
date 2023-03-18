import os,rich,sys,random,datetime,time
from rich.console import Console
from rich.table import Table
import csv,pymongo,getpass
from rich import box
from rich.live import Live
from rich.table import Table
from rich.prompt import Confirm
from rich.panel import Panel
from rich import print

# mongo connection :

cluster = pymongo.MongoClient('mongodb+srv://vinsharex:G0emexG4oEc92DW9@pythonprojects.gn9deee.mongodb.net/customer_detail?retryWrites=true&w=majority')
db = cluster["customer_detail"]
client = db["customer_data"]
dclient = db["delete_customers"]
admindb = db['admin_db']


class ABC_Bank:
    bank_name="ABC BANK LTD"
    IFSC_code="ABCB0000189"
    
   
    
    # =================== Create account function =================== 
    def createAccount(self):

        #  deposite amount check :

        while True:
            deposite=int(input("Enter Deposite Amount : "))
            if deposite>10000:
                break
            elif deposite == 0 : sys.exit(0)
            elif deposite<10000 and deposite>0 : print("Insufficient Balance!!!\n\n Try again other wise press 0 to exit : \n")
        
        adhaar = int(input("enter adhar no : "))
        for data in client.find():
            if data["adhar"]==adhaar:
                return "Account Already exist!!"
                    
                 
        # taking neccessary information of the user :
        data = {"acc_no": random.randint(100,500),
            "openingDate":datetime.datetime.utcnow(),
            "name":input("Enter Customer Name : "),
            "contact":int(input("Enter phone No. : ")),
            "dob":input("enter date in this format yyyy-mm-dd"),
            "address":input("Enter Customer Address : "),
            "adhar":adhaar,
            "balance":deposite}  
        client.insert_one(data)

        return "Your Record successfully created!!!\nYour Account No is :  "+data["acc_no"]

    # =================== Check account detail =================== 
    def check_detail(self,acc):
        n=1
        data = client.find_one({"acc_no":acc})
        if data!=None:
            table = Table(title=f"Mr. {data['name']} Details",box=box.SQUARE_DOUBLE_HEAD)
            table.add_column("SNo.", style="grey30", no_wrap=True)
            table.add_column("Account Details", style="dark_cyan", no_wrap=True)
            table.add_column("Description", style="medium_spring_green", no_wrap=True)

            for item1 in data:
                if "_id"!=str(item1):
                    table.add_row(str(n),str(item1),str(data[item1])) 
                    n=int(n)+1
                # print(item1,data[item1])
            
            console = Console()
            console.print(table)
            
        else : return "Account Number not found !!!"    
        
    # =================== Customer lists =================== 
    def customer_list(self):
        data = client.find().sort("acc_no",1)


        table = Table(title="ABC Bank Customers Details",box=box.SQUARE_DOUBLE_HEAD)
        table.add_column("Acc.No", justify="right", style="deep_pink4", no_wrap=True)
        table.add_column("Open date", style="grey0")
        table.add_column("Adhar No.", style="dark_cyan")
        table.add_column("Customer Name", style="dark_cyan")
        table.add_column("Contact No", style="dark_cyan")
        table.add_column("DoB", style="dark_cyan")
        table.add_column("City",justify="right", style="dark_cyan")
        table.add_column("Balance", justify="right", style="sky_blue2")
        
        # date
        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            for customer in data:
                time.sleep(0.2) 
                d2 = str(customer['openingDate']).split(" ")[0].split("-")
                d1 = datetime.datetime(int(d2[0]),int(d2[1]),int(d2[2]))
                d=datetime.datetime.strftime(d1,'%Y-%m-%d')
                # print(customer['acc_no'],customer['openingDate'],customer['name'],customer['contact'],customer['dob'],customer['address'],customer['balance'])
                table.add_row(str(customer['acc_no']),str(d),str(customer['adhar']),str(customer['name']),str(customer['contact']),str(customer['dob']),str(customer['address']),str(customer['balance']))
                

            # console = Console()
            # console.print(table)

        input("Press enter to exit.")

    # =================== update customer account =================== 
    def update_detail(self,acc):
        
            data = client.find_one({"acc_no":acc})
            # print("Which information you want to update ? \n")
            # self.check_detail(acc)
            n=1
            data = client.find_one({"acc_no":acc})
            if data==None:
                return "Record not found"
            table = Table(title=f"Mr. {data['name']} Details",box=box.SQUARE_DOUBLE_HEAD)
            table.add_column("SNo.", style="grey30", no_wrap=True)
            table.add_column("Account Details", style="dark_cyan", no_wrap=True)
            table.add_column("Description", style="medium_spring_green", no_wrap=True)

            for item1 in data:
                if "_id"!=str(item1) and "acc_no"!=str(item1) and "openingDate"!=str(item1) and "balance"!=str(item1):
                    table.add_row(str(n),str(item1),str(data[item1])) 
                    n=int(n)+1
            table.add_row("6","exit")  
                # print(item1,data[item1])
            
            console = Console()
            console.print(table)
            # ----------------------------------------------------------------------
            
            print(f"Which information you want to update ? [any time you want to exit press 6] \nselect here : ")
            while True:   
                   
                    choice = int(input("Enter here : "))
                    if choice == 1:
                        client.update_one({"_id":data["_id"]}, {"$set": {"name":input("Enter correct name here : ")}}, upsert=False)
                    #    Ac_detail["name"]==input("Enter name here : ")
                    elif choice == 2:
                          client.update_one({"_id":data["_id"]}, {"$set": {"contact":int(input("Enter correct contact here : "))}}, upsert=False)
                  
                        # Ac_detail["contact"]==input("Enter contact here : ")
                    elif choice == 3:
                          client.update_one({"_id":data["_id"]}, {"$set": {"address":input("Enter correct address here : ")}}, upsert=False)
                  
                        # Ac_detail["address"]==input("Enter address here : ")
                    elif choice == 4:
                          client.update_one({"_id":data["_id"]}, {"$set": {"dob":int(input("Enter correct dob here : "))}}, upsert=False)
                  
                        # Ac_detail["dob"]==input("Enter dob here : ")
                    elif choice == 5:
                        client.update_one({"_id":data["_id"]}, {"$set": {"adhar":int(input("Enter correct adhar No here : "))}}, upsert=False)
                    elif choice == 6:
                         return "All detail updated succesfully!!!"

    # =================== customer transactions  =================== 
    def transaction(self,acc):
         data = client.find_one({"acc_no":acc})

         
         while(True):
            time.sleep(3)
            os.system('clear')
            print("\nWhat do you want to do ? \n  1. Deposite Amount \n  2. Withdraw Amount \n  3. Check Account Balance \n  4. Exit")
            # print("How may i help you choose anyone ?\n  1. withdraw amount\n  2. deposite amount\n  3. check balance\n\n")

            try :
                choice=int(input("enter choice => "))

            except Exception:print("please enter number only")

            else :
                if choice==1:
                   amt=int(input("Amount : "))
                   client.update_one({'acc_no':acc},{"$set":{"balance":data['balance']+amt}})
                   print(f"Rs. {amt} Deposited Succesfully!!!!")
                    
                elif choice==2:
                    amt=int(input("Amount : "))
                    self.withdraw(acc,amt,data['balance'])
                    print(f"Rs. {amt} Withdraw Succesfully!!!!")

                elif choice==3:
                        data = client.find_one({"acc_no":acc})
                        bal=data["balance"]
                        print(f" Your Total Balance is : {bal} \n Your Current Balance Is {bal-10000}")
                     
                elif choice==4:
                   break

                else :print("Please Select correct option...")      
            
    # =================== withdraw amount  =================== 
  
    def withdraw(self,acc,amt,bal):
        # data = client.find_one({"acc_no":acc})

        if amt>bal:
            print("Insufficient balance ")
        elif amt<bal and amt>(bal-10000) and bal>0:
            print("Amount will deduct from minimum balance.(2%) Charges  will be deducted from your account")        
            # x=(amt*2)/100
            # finalAmt=bal-(amt+(amt*2)/100)
            client.update_one({"acc_no":acc},{"$set":{"balance":bal-(amt+(amt*2)/100)}})
        elif amt<bal and amt<=(bal-10000):
            client.update_one({"acc_no":acc},{"$set":{"balance":bal-amt}})
            # print("Transaction success ")
        else : print("Wrong input")

    # =================== Delete Account =================== 
   
    def remove_account(self,acc):
          data = client.find_one({"acc_no":acc})
          if data['acc_no']==acc:
              dclient.insert_one(data)
              client.delete_one({'_id':data['_id']})
              return "succesfully Remove from ABC Bank !!!"

    # =================== Deleted Account List =================== 

    def remove_account_list(self):
        data=dclient.find()

        table = Table(title="ABC Bank Deleted Accounts",box=box.SQUARE_DOUBLE_HEAD)
        table.add_column("Acc.No", justify="right", style="deep_pink4", no_wrap=True)
        table.add_column("Open date", style="grey0")
        table.add_column("Adhar No.", style="dark_cyan")
        table.add_column("Customer Name", style="dark_cyan")
        table.add_column("Contact No", style="dark_cyan")
        table.add_column("DoB", style="dark_cyan")
        table.add_column("City",justify="right", style="dark_cyan")
        table.add_column("Balance", justify="right", style="sky_blue2")
        
        with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
            for customer in data:
                time.sleep(0.4) 
                d2 = str(customer['openingDate']).split(" ")[0].split("-")
                d1 = datetime.datetime(int(d2[0]),int(d2[1]),int(d2[2]))
                d=datetime.datetime.strftime(d1,'%Y-%m-%d')
                # print(customer['acc_no'],customer['openingDate'],customer['name'],customer['contact'],customer['dob'],customer['address'],customer['balance'])
                table.add_row(str(customer['acc_no']),str(d),str(customer['adhar']),str(customer['name']),str(customer['contact']),str(customer['dob']),str(customer['address']),str(customer['balance']))
           
        input("Press enter to exit.")

    # =================== Add New Admin =================== 
    
    def admin(self):
        user=input("User name : ")
        pwd=int(getpass.getpass("Password : "))
        data=admindb.find_one({"uname":user})
        if data == None:
            admindb.insert_one({'uname':user, "pass":pwd})
            return "New Admin Added Succesfully !!!"


while True :
    os.system('clear')
    print("************************************************************")
    print("*                   WELCOME TO ABC Bank                    *")
    print("************************************************************")
    print("*                     Admin Login                          *")
    print("*                                                          *")
    print("*           User name                                      *", end="\r",flush=True)
    uname = input("*           User name :")
    print("*                                                          *")
    print("*           Password                                       *", end="\r",flush=True)
    pwd = int(getpass.getpass("*           password :"))
    print("*                                                          *")
    print("************************************************************")
 
    data = admindb.find_one({"uname":uname})
    
    if data['pass'] == pwd and uname == data['uname']:
        time.sleep(2)
        while True:
            os.system('clear')
            print(Panel.fit('''[steel_blue]------------------------------------------------------------
|                 WELCOME TO ABC Bank                      |
------------------------------------------------------------\n
|            (1). Open New Account                         |\n
|            (2). Account Detail                           |\n
|            (3). Customers List                           |\n
|            (4). Transactions                             |\n
|            (5). Update Details                           |\n
|            (6). Remove Account                           |\n
|            (7). Deleted Account List                     |\n
|            (8). Create Admin                             |\n
|            (9). Quit                                     |\n
------------------------------------------------------------'''))

            choice= int(input("Select option : "))
            customer=ABC_Bank()

            if choice==1:
                print(customer.createAccount())
                time.sleep(5)
            elif choice==2:
                print(customer.check_detail(int(input("Account No : "))))
                input("Press enter to exit.")
                time.sleep(1)
            elif choice==3:
                print(customer.customer_list())
                time.sleep(1)
            elif choice==4:
                print(customer.transaction(int(input("Account No : "))))
                time.sleep(5)
            elif choice==5:
                print(customer.update_detail(int(input("Account No : "))))  
                time.sleep(5)
            elif choice==6:
                print(customer.remove_account(int(input("Account No : "))))
                time.sleep(1)
            elif choice==7:
                print(customer.remove_account_list())
                time.sleep(1)
            elif choice==8:    
               print(customer.admin())    
               time.sleep(2)
            elif choice==9:    
                sys.exit(0)      
    else : 
        choice = Confirm.ask("Incorrect User name or Password !!! \nDo you want to try again ?")
        # print("Incorrect User name or Password !!! \nPress enter to try again.\nPress 0 to exit")
        if choice:
         time.sleep(1.8)
        else:    
         sys.exit(0) 
        # print(choice, type(choice))

