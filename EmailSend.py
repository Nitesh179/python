'''
import smtplib

def sendMail(email):
 try :
    user=input("enter your name : ")

    message=(f"Hello, {user} Wellcome to Python Blockchain Program.")
    s=smtplib.SMTP("bnitesh179@gmail.com",587) 
    print("tuunhdfjhnj")
    # print("smtp lib")
    s.starttls()
    s.login('bnitesh179@gmail.com','ozdg aqrq szag xndz')
    s.sendmail("bnitesh179@gmail.com",email,message)
    print("Send mail succesfully...")

 except Exception: print("Mail not sent....")

sendMail("neerajoon121@gmail.com")    


'''

from GoogleNews import GoogleNews

news=GoogleNews(period='1d')
news.search("India")
result=news.result()

import pandas as pd
data=pd.DataFrame.from_dict(result)
data=data.drop(columns=["imgage"])
data.head()
