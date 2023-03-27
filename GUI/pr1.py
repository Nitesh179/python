from tkinter import Tk
from tkinter import ttk


root=Tk()
root.title('login page')
root.minsize(300,300)
root.maxsize(500,600)

def demo():
    root.destroy()


ttk.Label(root,text="Hello python").grid(row=1,column=2)
ttk.Label(root,text="Hello python22").grid(row=3,column=4)

ttk.Button(root,text="Quit", command=demo).grid(row=5,column=4)
root.config(background='black')

root.mainloop()