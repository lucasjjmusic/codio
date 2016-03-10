import smtplib
from random import randint

###TEST
mana = "1"
model = "5"
name = "1"
response = "1"
extrainfo = "6"
email = "1"
###TEST

user = "gcsetestemail@gmail.com"
pwd = "GCSEtest"
recipient = "12johnstonl@glynschool.org"
subject = ("Case Number #" + str(randint(1,100000000)))
body = ("Manafacturer: '" + mana + "' Model: '" + model + "' Name: '" + name + "' Problem Summary: '" + response +  "' Extra Information: '" + extrainfo + "' Email: '" + email + "'")

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = "gcsetestemail@gmail.com"
    gmail_pwd =  "GCSEtest"
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
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