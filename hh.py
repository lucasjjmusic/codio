from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from random import randint
import smtplib

subject = ("Case Number #" + str(randint(1,100000000)))
with open("text.txt", "w") as text_file:
    print("Purchase Amount: {}".format(TotalAmount), file=text_file)

fromaddr = 'gcsetestemail@gmail.com'  
toaddrs  = '12johnstonl@glynschool.org'  
username = 'gcsetestemail@gmail.com'  
password = 'GCSEtest'  

msg = MIMEMultipart()
msg.attach(MIMEText(file("text.txt").read())

server = smtplib.SMTP("smtp.gmail.com:587")  
server.starttls()
server.connect()
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg.as_string()) 
server.close()  