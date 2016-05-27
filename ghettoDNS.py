# ghettoDNS
# justin parus

# pulls public ip and emails it using gmail
# will need to change google security settings allowing 'less secure apps' to sign in
#   even when using the SSL port

import requests
import smtplib
fromaddr = 'justin.parus@gmail.com'
toaddrs  = 'justin.parus@gmail.com'
subject  = 'ghettoDNS public IP'
username = 'justin.parus'
password = ''

# Retrieve public ip and print
# or can use 'http://ident.me'
ip = requests.get('https://api.ipify.org').text
print('Public IP ' + ip)

# Set up message
msg = msg = "\r\n".join([
  "From: " + fromaddr,
  "To: " + toaddrs,
  "Subject: " + subject,
  "",
  ip
  ])

server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.ehlo() # Optional?.. no this isn't swift
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.close()
print('Successfully sent mail')
