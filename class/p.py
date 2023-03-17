'''class Student:
    def __init__(this,name,age,city):
        this.name=name
        this.age=age
        this.city=city

    def talk(this):
        return (f"student name : {this.name}\nStudent age : {this.age}\nStudent city : {this.city}\n")


s1=Student("Nitesh",21,"indore")
print(s1.talk())

this=10
print(this)'''

'''import os
print("************************************************************")
print("=================== WELCOME TO ABC Bank ====================")
print("************************************************************")
print("             (1). Open New Client Account ")
print("             (2). The Client Withdraw a Money ")
print("             (3). The Client Deposit a Money ")
print("             (4). Check Clients & Balance ")
print("             (5). Quit ")
print("************************************************************")

EnterLetter = int(input("Select option : "))

os.system('clear')'''




# import click


# @click.group()
# def app():
#     """Awesome app doing awesome things."""


# @app.command()
# @click.option("--count", default=1, help="How much love you want")
# @click.argument("name")
# def spread(name, count):
#     """Spread the love."""
#     for i in range(count):
#         print(f"{name} loves you ❤️")


# @app.command(name="print")
# @click.argument("filepath", metavar="FILE", type=click.Path(exists=True))
# @click.option("--show-meta", default=False, is_flag=True)
# def print_(filepath, show_meta):
#     """Print the file."""
#     if show_meta:
#         print(f"File path: {filepath}")
#         print("-" * 80)
#     with open(filepath, "r") as f:
#         print(f.read())
#  == "__main__":
#     app()

# input("Enter any key")
# import datetime
# time_str = input("enter date in this format yyyy-mm-dd")
# time=datetime.datetime.strptime(time_str, "%Y-%m-%d")

# print(time)

# import datetime
# d=input("Enter date").split('-')
# date2=date1.split("-")
# time=datetime.date(int(date2[0]),int(date2[1]),int(date2[2]))
# # today = datetime.date.today1()
# print(time)

# def show(*inp):
#     for i in inp:
#         if i=="1":
#             print("one")
#         elif i=="2":
#             print("two")

# inp = [input("Enter multiple value").split(" ")]

# print(inp)

# show(inp)

# import datetime
# import pymongo

# cluster = pymongo.MongoClient('mongodb+srv://vinsharex:G0emexG4oEc92DW9@pythonprojects.gn9deee.mongodb.net/customer_detail?retryWrites=true&w=majority')
# db = cluster["customer_detail"]
# client = db["Client_detail"]

# date=datetime.date.today()
# client.insert_one({"_id":0, "user 1":"Soumi","dob": datetime.datetime.utcnow()})

 
# from datetime import datetime
# d1=datetime.today()
# # d = datetime(d1)
# print(d1.strftime('%Y-%m-%d'))    
 

# for updating data customer_data :

# for data in client.find():
#  client.update_one({"_id":data['_id']}, {"$set": {"adhar":str(random.randint(111111111111,999999999999))}}, upsert=True)


#  delay execution in python :
# import time

# for i in range(1,6):
#     print(i)
#     time.sleep(2)

# import time
# import csv,pymongo,datetime,time

# from rich.live import Live
# from rich.table import Table

# cluster = pymongo.MongoClient('mongodb+srv://vinsharex:G0emexG4oEc92DW9@pythonprojects.gn9deee.mongodb.net/customer_detail?retryWrites=true&w=majority')
# db = cluster["customer_detail"]
# client = db["customer_data"]


# table = Table()
# table.add_column("Row ID")
# table.add_column("Description")
# table.add_column("Level")

# with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
#     data = client.find().sort("acc_no",1)
    
#     for customer in data:
#         time.sleep(0.4)  # arbitrary delay
#         d2 = str(customer['openingDate']).split(" ")[0].split("-")
#         d1 = datetime.datetime(int(d2[0]),int(d2[1]),int(d2[2]))
#         d=datetime.datetime.strftime(d1,'%Y-%m-%d')
#         # print(customer['acc_no'],customer['openingDate'],customer['name'],customer['contact'],customer['dob'],customer['address'],customer['balance'])
#         table.add_row(str(customer['acc_no']),str(d),str(customer['adhar']),str(customer['name']),str(customer['contact']),str(customer['dob']),str(customer['address']),str(customer['balance']))
        
#         # update the renderable internally
#         # table.add_row(f"{row}", f"description {row}", "[red]ERROR")

