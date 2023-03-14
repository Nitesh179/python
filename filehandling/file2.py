import os,sys
'''
fname=input("enter file name : ")
if os.path.isfile(fname):
    print("this file available...")
else: print("file not found")    '''


fname=input("enter file name : ")
if os.path.isfile(fname):
    print("this file available...")
    f=open('text.txt','r')
else: 
    print("file not found") 
    sys.exit(0)   

lcount=wcount=ccount=0
for i in f:
    lcount=lcount+1
    word=i.split()
    wcount=wcount+len(word)
    ccount=ccount+len(i)

print("No. of lines => ",lcount)    
print("No. of words => ",wcount)
print("No. of char => ",ccount)
