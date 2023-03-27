from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

def login():
    uname=user.get()
    pasw=paswd.get()
    
    if uname == "nitesh" and pasw == '1234':
        messagebox.showinfo('Login',"Succesfully Login!!!")
        # messagebox.askyesno("do you again login...")
    else:
        messagebox.showinfo('Error',"Username or Password Incorrect!!!")    


    
  

root=Tk()
root.config(bg='#0096DC')
root.title('Login Page')
root.geometry('300x300')
# root.iconbitmap('favicon.ico')

img=Image.open('imge.png')
img_size=img.resize((70,70))
img=ImageTk.PhotoImage(img_size)

img_labl=Label(root,image=img).pack(pady=10)

ttk.Label(root,text='ABC BANKING APP',foreground='white',background='#0096DC',font=('verdana',18)).pack()

ttk.Label(root,text='User Name : ',foreground='white',background='#0096DC',font=('verdana',12)).pack(pady=(15,5))
user=ttk.Entry(root)
user.pack(pady=5)

ttk.Label(root,text='Password : ',foreground='white',background='#0096DC',font=('verdana',12)).pack()
paswd=ttk.Entry(root)
paswd.pack()

ttk.Button(root,text='Login',command=login).pack(pady=(10,5))




root.mainloop()