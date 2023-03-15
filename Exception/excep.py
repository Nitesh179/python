
'''print('stmt 1')

try:
    print(10/0)
    print("stmt 2") # this stmt is not executed
except ZeroDivisionError :
    print(10/1)
    print("stmt 3")
print("stmt 4")        
'''

'''try:
    print("stmt1")
    print(100/0)

except Exception :
     print("stmt2")
     print(100/1)
finally : print("Stmt3")'''

# multiple except block with try :
'''
try:
    a=int(input("1st No : "))
    b=int(input("2nd No : "))
    print(a/b)

except ValueError:
    print("Please Enter Number only")
except ZeroDivisionError:
    print("can't divide with zero")

finally:print("Finally...")'''

'''try:
    print(5/0)
except ZeroDivisionError:print("Zero not found")    
except ArithmeticError:print("Arithmetic error")'''

# try except with else block :

# try:
#     print(10/0)

# except ZeroDivisionError:print("Can't divide with zero")
# else : print("Else block execute")    


