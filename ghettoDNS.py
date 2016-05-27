# ghettoDNS
# justin parus

import requests
import smtplib

fromaddr = ''
toaddrs  = ['recipient_1', 'recipient_2']
subject  = 'ghettoDNS public IP'

# login credentials
username = ''
password = ''

# Retrieve public ip and print
# or can use 'http://ident.me'
ip = requests.get('https://api.ipify.org').text
print('Public IP ' + ip)

# Set up message
recipients = ''
for x in toaddrs:
  recipients += x + ','

msg = msg = "\r\n".join([
  "From: " + fromaddr,
  "To: " + recipients,
  "Subject: " + subject,
  "",
  ip
  ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo() 
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.close()
print('Successfully sent mail')
