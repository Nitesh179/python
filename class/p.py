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


# if __name__ == "__main__":
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

def show(*inp):
    for i in inp:
        if i=="1":
            print("one")
        elif i=="2":
            print("two")

inp = [input("Enter multiple value").split(" ")]

print(inp)

show(inp)
