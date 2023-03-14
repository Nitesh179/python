def addition(*n):
    s=0
    for i in n:
       s=s+i
    print(s)

    
def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:return n1/n2
    else : return print("infinity")

def mod(n1,n2):
    return n1%n2 
       