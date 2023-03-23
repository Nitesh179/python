
import smtplib
from email.message import EmailMessage

def sendMail1(email):
 try :
   user=input("enter your name : ")
   # message=(f"subject:Wellcome To ABC Bank Ltd🎉\n\n Hello, {user} \nCongratulations Your account has been successfully created with Account No. 5554.\nThank you for choosing \nWe are glad that you joined us. For this reason, we are giving you a special offers.\n\n- 10X Cashpoints on Amazon, Flipkart, Swiggy & more\n- 5X Cashpoints on EMI spends\n- upto 1500 off on HRX products\n- Rs 2,500 Amazon Voucher \n\n\nNOTE : We have a special offer for few customers only Hurry up!!!") 
   s=smtplib.SMTP("smtp.gmail.com",587) 
   s.starttls()
   s.login('bnitesh179@gmail.com','ozdgaqrqszagxndz')
   # s.sendmail("bnitesh179@gmail.com",email,message)
   msg = EmailMessage()
   msg.set_content('This is my HKFC BANK')

   msg['Subject'] = 'Wellcome To ABC Bank Ltd🎉'
   msg['From'] = "bnitesh179@gmail.com"
   msg['To'] = email

   s.send_message(msg)
   s.quit()
   print("Send mail succesfully...")
 except Exception: print("Mail not sent....")

sendMail1("niteshb780@gmail.com")    



# import smtplib
# try:
#  smObj=smtplib.SMTP("smtp.gmail.com",587)
#  smObj.starttls()
#  user=input("enter your name : ")
#  message=(f"Hello, {user} Wellcome to Python Blockchain Program.")
#  smObj.login('bnitesh179@gmail.com','qrzhtyciaxioppor')    
#  smObj.sendmail('bnitesh179@gmail.com','niteshb780@gmail.com',message)
#  print("email send successfully...")

# except Exception:
#  print("error : mail not send...") 
   