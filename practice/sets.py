# a={}
# # print(type(a)) --> its not empty sets its type is dict 
# s=set()
# print(type(s))

# sets --> mutable changable
'''s={1,2,3,3}
s.add(5)
s.add(2)
s.add(5)
# s.remove(3)
print(s)
print(type(s))'''


# forzenset  --> imutable not changable
s={1,2,2,2,34,4,5,65,2}
fs=frozenset(s)
fs.remove(2)
print(s," => ",fs)