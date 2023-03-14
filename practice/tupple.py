# tupple datatype :

# it is an immutable dt in python 
# t=()

# t=(1) --> it is not a tuple type is int

# t=(1,) --> this is tuple single 
t=(1,2,3,4)

print(t[2])

# print(t)

# tuple methods

# t=(1,4,5,6,1,6,1,1)
# print(t.count(6))

# print(t.index(6))


# tupple and list quest :

#1 store fruit by user in list

# i=1
# lst=[]
# while i<8 :
#     lst.append(input("=> "))
#     i+=1

# print(lst)

#2 store marks of 7 sub and show ascending order

# i=1
# list=[]
# while i<6:
#     list.append(int(input("=> ")))
#     i+=1
# list.sort()
# print(list)    

#3 sum of all elem in the list

# list=[1,4,5,3]

# print(sum(list))
                      # OR
# i=0
# sum=0
# while i< len(list) :
#     sum+=list[i]
#     i+=1
# print(sum)    

#4 how many 0 elem in tuple

# tu=(1,0,4,0,5,0,4,0)
# print(tu.count(0))