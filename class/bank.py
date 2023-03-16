import sys

class Bank:
  balance=0
  def __init__(self,bal):
    if bal>10000:
     self.balance=bal
    else : print("10,000 deposite required!!!!!") 

  def withdraw(self,amt):
    if self.balance>amt:
     bal=self.balance
     bal=bal-amt
     self.balance=bal
     return self.balance
    else : print("Insufficient balance ")

  def deposite(self,amt):
    bal=self.balance
    bal=bal+amt
    self.balance=bal 
    return self.balance

  def sbalance(self):
    return self.balance   


print("\n\n\t\t#========== WELOCOME To ABC Bank ==========#\n\n")

while True:
 dep=int(input("enter deposite amount : "))
 if dep>10000:break
 elif input("if you want to exit : press 0 \n otherwise enter Amount : ")=='0':
  sys.exit(0)

person1=Bank(dep)
while(True):

 print("How may i help you choose anyone ?\n  1. withdraw amount\n  2. deposite amount\n  3. check balance\n\n")

 try :
  ch=int(input("enter choice => "))

 except Exception:print("please enter number only")

 else :
  if ch==1:
   res=person1.withdraw(int(input("enter amount : ")))
   print(res)
  elif ch==2:
   res=person1.deposite(int(input("enter amount : ")))
   print(res)
  elif ch==3:
   res=person1.sbalance()
   print(res)
  else :
   print("Please Select correct option...")      
 
 print("want to any operation (y/n)")
 try:
   while True:
    want=input("=> ")
    if want=='y' or want=='yes':
     break
    elif want=='n' or want=='no':
     sys.exit(0)
    else : print("select correct option")
 except Exception:
  print("enter yes or no")
  





