# find odd even no ?

"""if int(input("..=> "))==0 : print("this is netural number")
elif int(input("=> "))%2==0 : print("this is even number")
else :  print("this is odd number")"""

even=lambda enum:enum if enum%2==0 else "not even"
print(even)

# check given number is between 0-100 ?

"""if int(input("=> "))<101 : print("valid number...")
else : print("invalid number...")"""

#  user enter number and print spelling of word : "shortest logic" ?

"""di={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five"}

val=int(input("=> "))

for i in di :
     if i == val:
      print(di[i])"""

# odd even series ?

"""for i in range(2,20,2):
      print(i,"< even")"""

# prime number series ?
'''c=0
for i in range(2,20):
    for j in range(2,i):
         if i%j==0 and i!=j:
             c+=1
             break
    if c==0:
        print(i) 
    c=0'''

# LOOPS Questions :

# right angled traingle ?
'''
*
**
***
****
*****
'''
'''
for i in range(5):
    for j in range(5):
        if i>=j:
            print("*",end='')
    print()     '''




# reverse given string ?
'''str="NITESH"
for i in reversed(str):
    print(i,end="")
print()
   
# OR

s=input("=> ")
print(s[::-1])'''

# reverse order of words from the sentence ?

'''n=input("=> ")
n=n.split()

for i in reversed(n):
   print(i,end="")'''

# reverse each letter inside string ?

'''n=input("=> ")
n=n.split()

for i in n:
    for j in reversed(i):
      print(j,end="")
    print(" ")    '''

