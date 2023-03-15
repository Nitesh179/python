# we have to raise exception using 'raise' keyword :

class OldAgeError(Exception):
    def __init__(self,args):
        self.msg=args

class YoungAgeError(Exception):
    def __init__(self,args):
        self.msg=args        

age=int(input("Enter Age : "))
if age>60:
    raise OldAgeError("You are not eligible to drive.")
elif age<18:
    raise YoungAgeError("You are under 18 not eligible.")
else:
    print("you are eligible")