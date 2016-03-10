import smtplib, os
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

TotalAmount = ("hfhnti")
with open("text.txt", "w") as text_file:
    print("Purchase Amount: {}".format(TotalAmount), file=text_file)
    
sub = ("Case Number #" + str(randint(1,100000000)))
    
files=['text.txt']
server="smtp.gmail.com"
port=587
username="gcsetestemail@gmail.com"
password="GCSEtest"
isTls=True

msg = MIMEMultipart()
msg["gcsetestemail@gmail.com"] = send_from
msg["12johnstonl@glynschool.org"] = COMMASPACE.join(send_to)
msg['Date'] = formatdate(localtime = True)
msg[sub] = subject

msg.attach( MIMEText(text) )

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
    msg.attach(part)

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
if isTls: smtp.starttls()
smtp.login(username,password)
smtp.sendmail(send_from, send_to, msg.as_string())
smtp.close()
