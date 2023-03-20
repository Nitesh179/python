'''def decor(func):
    def inner(name): 
        if name=='imran' : print("hello congrats for first day...")
        else:func(name)
    return inner  


def wish(name):
    print(f"Hello, {name} good Morning !!!")

# without decorator wish call
wish("nitesh") 
wish("imran")

# with decorator wish call
decorfunction=decor(wish)
decorfunction("imran")'''

'''def smart_div(func):
     def inner(a,b):
          if b==0:
            print("Any No. divided by Zero : infinity")
          else : func(a,b)
  
     return inner  


@smart_div
def division(a,b):
    print("Result is : ",a/b)

division(20,0)
division(10,5)'''

'''
def decor(func):
    def inner(num):
        if num%2!=0:print("Not even no")
        else :func(num)
    return inner
@decor
def even(num):
    print("=> ",num) 

even(int(input("=> ")))
  
'''



# decorator chaining :

def decor(func):
    def inner(name): 
        func(name) #--> this call original wish function
    return inner  

def decor1(func):  #wish("nitesh")
    def inner(name):
       func(name) # --> this call docor inner function
    return inner   


@decor1 
@decor
def wish(name):
    print(f"Hello, {name} good Morning !!!")

# wish("nitesh")
wish("nitesh") # this call decor1 inner function