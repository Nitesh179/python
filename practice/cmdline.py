from sys import argv

# print(type(argv[1])) --> type string and argv is list argv[0](cmdline.py) after any thing is commad line argument

# if int(argv[1])>10:
#     print("greater done...")

if(int(argv[1])>int(argv[2]) and int(argv[1])>int(argv[3])) : print(argv[1] ,"is largest value")

elif int(argv[2])>int(argv[3]) : print(argv[2] ,"is largest value")

else : print(argv[3] ,"is largest value")

print(argv[1],argv[2],argv[3],sep=":")



# #### print statements

    # by default output values are seperated by space.If we want we can specify seperator by using "sep" attribute

    # a,b,c=10,20,30
    # print(a,b,c,sep=":")

    # if u want to output in same line with space --> hello nitesh how are you ?
    # print("hello ",end='')
    # print('nitesh ',end='')
    # print("how are you ?")

# a,b,c=10,"chess",5.11
# print("vijay age is %d" %a)
# print("vijay hobby is %s" %b)
# print("vijay height is %f" %c)

# print("detail info %d  %s  %f"%(a,b,c))

# print("hello"*10)

# name="sunny"
# salary=20000
# desg="Accountant"

# print("good morning {0} are you selected for {1} position amount of salary decided {2}".format(name,desg,salary))