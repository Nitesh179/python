'''f=open('text.txt','r')
data=f.read()
print(data)
f.close()
'''

'''f=open('text.txt','r')
data=f.read(12)
print(data)'''

'''f=open('text.txt','r')
for i in range(3):
 data=f.readline()
 print(data)'''

'''f=open('text.txt','r')
file=f.readline()

for i in file:
 data=f.readline()
 print(data)'''

#   using with statement :

'''with open('text.txt','w') as f:
    f.write('This is a birthday its your birthday....')
'''
with open('text.txt','r') as f:
#     # print(dir('encoding'))

#     l1=f.readline()
#     print(l1,end='')
#     l2=f.readline()
#     print(l2,end='')
#     l3=f.readline()
#     print(l3,end='')
#     l4=f.readline()
#     print(l4,end='')


# tell(), seek() :

 ''' print(f.read(5))
 print(f.tell())
 print(f.read(6))
 print(f.tell())
 print(f.read(3))'''

 

