#$Env:email_user="ActualEmail"
#$Env:email_pass="AppPassword"


import os
import smtplib
import imghdr
from email.message import EmailMessage

email_address = os.environ.get('email_user')
email_password = os.environ.get('email_pass')

contacts = ['selected.email@yum.com', 'selected.email2@yum.com']

msg = EmailMessage()
msg['Subject'] = 'Grabbing beers this weekend?'
msg['From'] = email_address
msg['To'] = contacts
msg.set_content('blah blah blah')

files = ['beer.jpg', 'coffee_1.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
    