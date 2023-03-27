from tkinter import *
from tkinter import ttk
def add():
    # ttk.Label(root,text=int(first.get()) + int(second.get())).pack(pady=(10,5))
    ans=int(first.get()) + int(second.get())
    result.config(text=ans)

def sub():
    ans=int(first.get()) - int(second.get())
    result.config(text=ans)    

def mod():
    ans=int(first.get()) % int(second.get())
    result.config(text=ans)    


def div():
    ans=int(first.get()) / int(second.get())
    result.config(text=ans)    

def mul():
    ans=int(first.get()) * int(second.get())
    result.config(text=ans)    


root=Tk()
root.title("Operators")
root.config(background='#385170')

root.geometry('400x400')

ttk.Label(root,text="Enter 1st No : ").pack(pady=(10,5))
first=Entry(root)
first.pack(pady=(10,5))

ttk.Label(root,text="Enter 2nd No : ").pack(pady=(10,5))
second=Entry(root)
second.pack(pady=(10,5))


ttk.Button(root,text='+',command=add).pack(pady=(10,5))
ttk.Button(root,text='-',command=sub).pack(pady=(10,5))
ttk.Button(root,text='/',command=div).pack(pady=(10,5))
ttk.Button(root,text='%',command=mod).pack(pady=(10,5))
ttk.Button(root,text='*',command=mul).pack(pady=(10,5))


result=StringVar()
# result.set(ans)
result=ttk.Label(root)
result.pack(padx=20,pady=30)

root.mainloop()