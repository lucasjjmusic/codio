import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from random import randint

send_from = ("gcsetestemail@gmail.com")
send_to = ("12johnstonl@glynschool.org")
sub = ("Case Number #" + str(randint(1,100000000)))
subject = (sub)
text = ("")

def send_mail(send_from, send_to, subject, text, files=["text.txt"]):
    
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)
    
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login("gcsetestemail@gmail.com", "GCSEtest")
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")
        
send_mail(send_from, send_to, subject, text)
