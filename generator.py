'''t=(x for x in range(10000000000)if x%2==0) #--> generator can't store it execute only
l=[x for x in range(1000)if x%2==0] # -->list store in memory


for i in l:
     print(i)'''


'''def mygen():
    yield 'A'

g=mygen()
print(next(g))
'''

'''def count_down(num):
    print("your time starts now !!!")
    while num>0:
        yield num
        num-=1

val=count_down(30)       
for x in val:
    print(x) '''

# fibonacci
'''def fibo(length):
    a,b,c=0,1,0
    while length>0:
        yield a
        c=a+b
        a=b
        b=c
        length-=1

l=fibo(10)
# print(next(l))
for i in l:
    print(i)       
    '''

# ----------------------------------------------------------------------------------------------------------

import time
import random

names=['sunny','bunny','jay','suresh','vinny','chinny','chiku']
courses=['java','python','blockchain']

def stud_list(people):
    result=[]
    for i in range(people):
        person={
            'id':i,
            'name':random.choice(names),
            'course':random.choice(courses)
        }

        result.append(person)

    return result

def stud_gen(people):
   
    for i in range(people):
        person={
            'id':i,
            'name':random.choice(names),
            'course':random.choice(courses)
        }
        yield person


t1=time.perf_counter()
# people=stud_list(10000000)
people=stud_gen(10000000)
# for i in people:
#   print(i)
t2=time.process_time()

print("Total Time : {}".format(t1-t2))