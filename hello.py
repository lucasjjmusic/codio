import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message():
    msg = MIMEMultipart('alternative')
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.login("gcsetestemail@gmail.com", "GCSEtest")

    toEmail, fromEmail = "12johnstonl@glynschool.org", "gcsetestemail@gmail.com"
    msg['Subject'] = ("Case Number #" + str(randint(1,100000000)))
    msg['From'] = fromEmail
    body = 'This is the message'

    content = MIMEText(body, 'plain')
    msg.attach(content)
    s.sendmail(fromEmail, toEmail, msg.as_string())
    s.ehlo()
    s.starttls()
    server.close()
    