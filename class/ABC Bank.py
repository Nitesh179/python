customerList=[{"name":"a",
               "id":0,
               "Balance":"50000"
               },
               {"name":"a",
               "id":1,
               "Balance":"40000"
               },
               {"name":"a",
               "id":2,
               "Balance":"3000"
               }
               ]

print(customerList[int(input("Enter customer id"))]["Balance"])

# login
# name=""
# while login=="Nitesh":
#     login = input("Enter name")



class ABC_Bank:
    bank_name="ABC BANK LTD"
    IFSC_code="ABCB0000189"

    def __init__(self,accNo,deposite):
        #   loop check all acc if exist then customer() call otherwise openAcc()
        self.openAcc(accNo,deposite)

    def openAcc(self):
        name=input("Enter Customer Name : ")
        if self.deposit>10000:
            balance=self.deposit-10000    


#===================== useful parts ========================:

# detail = filter(lambda x:x["id"]==2, customerList)
# for i in detail:
    # print(i)
# customerList[int(input("Enter customer id"))]["Balance"]