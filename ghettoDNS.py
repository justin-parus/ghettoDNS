# ghettoDNS
# justin parus

import requests
import smtplib
import os
from apscheduler.schedulers.blocking import BlockingScheduler

class GhettoDNS:
  """Simple DNS Server work-around"""
  def __init__(self):
    self.lastIP = ''

  # static
  from_addr = ''
  to_addrs = ['', '']
  username = ''
  password = ''
  mail_server = 'smtp.gmail.com:587'
  # other options 'http://ident.me', 'http://icanhazip.com'
  ip_server = 'https://api.ipify.org'

  def mailIP(self):
    try:
      ip = requests.get(GhettoDNS.ip_server).text

      if self.lastIP != ip:
        self.lastIP = ip

        subject = 'ghettodns public ip'
        recipients = ''
        for x in GhettoDNS.to_addrs:
          recipients += x + ','

        msg = msg = "\r\n".join([
          "From: " + GhettoDNS.from_addr,
          "To: " + recipients,
          "Subject: " + subject,
          "",
          ip
          ])
        
        server = smtplib.SMTP(GhettoDNS.mail_server)
        server.ehlo() 
        server.starttls()
        server.login(GhettoDNS.username, GhettoDNS.password)
        server.sendmail(GhettoDNS.from_addr, GhettoDNS.to_addrs, msg)
        server.close()
        
        print('Successfully mailed new IP:', ip)

    except requests.exceptions.RequestException as err:
      print('Failed to get ip:', err)
    except smtplib.SMTPException as err:
      print('Failed to send mail:', err)


if __name__ == '__main__':
  dns = GhettoDNS()

  scheduler = BlockingScheduler()
  scheduler.add_job(dns.mailIP, 'cron', hour='19', minute='0', second='0')
  print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

  try:
    print('Starting scheduler')
    scheduler.start()
  except (KeyboardInterrupt, SystemExit):
    print('Process ended')
