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
  FROMADDR = ''
  TOADDRS = ['', '']
  USERNAME = ''
  PASSWORD = ''
  MAILSERVERADDR = 'smtp.gmail.com:587'
  # other options 'http://ident.me', 'http://icanhazip.com'
  IPSERVERADDR = 'https://api.ipify.org'

  # functions
  def mailIP(self):
    # Retrieve public ip and print
    ip = requests.get(GhettoDNS.IPSERVERADDR).text

    if self.lastIP != ip:
      self.lastIP = ip

      # Set up message
      subject = 'ghettodns public ip'
      recipients = ''
      for x in GhettoDNS.TOADDRS:
        recipients += x + ','

      msg = msg = "\r\n".join([
        "From: " + GhettoDNS.FROMADDR,
        "To: " + recipients,
        "Subject: " + subject,
        "",
        ip
        ])

      server = smtplib.SMTP(GhettoDNS.MAILSERVERADDR)
      server.ehlo() 
      server.starttls()
      server.login(GhettoDNS.USERNAME, GhettoDNS.PASSWORD)
      server.sendmail(GhettoDNS.FROMADDR, GhettoDNS.TOADDRS, msg)
      server.close()


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
    pass
