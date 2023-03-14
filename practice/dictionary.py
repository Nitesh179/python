# dictionary like a object key value pair

di={'name':'Nitesh',
    'class':12,
    'sub':['eng','hindi','maths'],
    'city':'indore'
}
# print(di.items()) # --> key, values in a tuples form
# print(di['class'])
# print(di['sub'][0]) 

# methods 

# print(di.keys()) --> keys as a arary format
# print(di.values())  --> values in aarray formate
# newdi={
#     'lovish':'firend',
#     'kavish':'childhood frd',
#     'komal':'best sister'
# }
# di.update(newdi)

# print(di.popitem())

for x in di :
    print(di[x])

# print(di)
