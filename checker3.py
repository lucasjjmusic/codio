import smtplib
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

###TEST
mana = "1"
model = "5"
name = "1"
response = "1"
extrainfo = "6"
email = "1"
###TEST

user = ("gcsetestemail@gmail.com")
pwd = ("GCSEtest")
recipient = ("12johnstonl@glynschool.org")
subject = ("Case Number #" + str(randint(1,100000000)))
body = ("Hello")
msg = MIMEMultipart('alternative')        

part = MIMEBase('application', "octet-stream")
part.set_payload(open("text.txt", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="text.txt"')

msg.attach(part)

def send_email(user, pwd, recipient, subject, body):
    gmail_user = ("gcsetestemail@gmail.com")
    gmail_pwd =  ("GCSEtest")
    FROM = user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")
        
send_email(user, pwd, recipient, subject, body)