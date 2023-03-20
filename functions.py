# function without return :
'''def odd_even(num):
        if num==0: print("this is netural number")
        elif num%2!=0:print("this is odd number")
        else :print("this is even number")

odd_even(int(input("=> ")))'''


# function with return :
'''def factorial(num):
    res=1
    while num>0:
        res*=num
        num-=1
    return res

print(factorial(4))    
'''

# function with multiple return stmt:
'''def calc(num1,num2):
   add=num1+num2
   sub=num1-num2
   mul=num1*num2
   div=num1/num2
   return add,sub,mul,div


print(calc(int(input("num 1 => ")),int(input("num 2 => "))))'''

# 4 types of arguments in function :

# positional argument :
'''def pow_fun(num,p):
    res=num
    while p>1:
     res=num*res
     p-=1
    return res

print(pow_fun(int(input("number => ")),int(input("power => "))))'''

# keyword argument :
'''def wish(name,greet):
    print(f"Hello, {name} {greet}")

wish(name="jay",greet="Good Morning...")  '''  

# default argument :
'''def default_args(name,wish="good morning",sal=10000):
    return f"hello,{name} your salary is {sal}"

print(default_args(input("enter your name => ")))'''

# variable length argument (same as => var args method in java)
#    *n = it uses tupple --> variables argument
#   **n = it uses dictionary --> keyword argument

'''def sum(*n):
    tot=0
    for i in n:
        tot=tot+i
    return tot 

print(sum())   
print(sum(20,10,10))  
print(sum(20,10))  '''

# Recursive function :

'''def factorial(num):
    total=1
    if num==0: total=1
    else : total=num*factorial(num-1)

    return total 
print(factorial(int(input("=> "))))'''

# Anonymous function or lambda function :

# sum=lambda a,b : a+b
# print(sum(10,20)) 

'''biggest=lambda a,b,c : a if a>b and a>c else b if b>c else c
print(biggest(120,20,10))'''

# lambda function with filter() method : return filtered value only
    # without lamdba function : 

'''def is_even(num):
    if num%2==0: return True
    else : return False

l=[10,20,1,5,9,12,200]
lst=list(filter(is_even,l))
print(lst)    
'''
 
    # with lamdba function : 
'''l=[10,20,1,5,9,12,200]
lst=list(filter(lambda x : x%2==0,l))
print(lst)
'''

# lambda function with sorted() method :
#  reverse=True --> desc order bydefault asc order :

'''l=[10,20,1,5,9,12,200]
lst=list(sorted(filter(lambda x : x%2==0,l),reverse=True))
print(lst)'''

 # lambda function with map() method :
  
'''l=[1,2,3,4,5]
lst=list(map(lambda x : x*x*x,l))

print(lst)'''

# Function Aliasing :

'''wish=lambda name : print(f"Hello, {name} Good Morning...")
greet=wish
del wish
greet("nitesh")'''

# Nested Function :
# def university(uname):
#     def Acollage():print("Arhint collage registration Open...")
#     def Bcollage():print("This is Brillent collage...")
#     Acollage()  

# university("DAVV")   


