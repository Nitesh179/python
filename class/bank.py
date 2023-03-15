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

  def deposite(self,amt):
    bal=self.balance
    bal=bal+amt
    self.balance=bal 
    return self.balance

  def sbalance(self):
    return self.balance   

person1=Bank(int(input("enter deposite amount : ")))

while(True):

 print("How may i help you choose anyone ?\n  withdraw amount(press 1)\n  deposite amount(press 2)\n  check balance(press 3)\n\n")

 try :
  ch=int(input("enter choice => "))

 except Exception:print("please enter number only")

 else :
  if ch==1:
   res=person1.withdraw(int("enter amount : "))
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
   want=input("=> ")
   if want=='y' or want=='yes':
    pass
   elif want=='n' or want=='no':
    break
   else : print("select correct option")
 except Exception:
  print("enter yes or no")





