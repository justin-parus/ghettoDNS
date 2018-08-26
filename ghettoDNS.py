# ghettoDNS
# justin parus

import requests
import smtplib
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import usrMngr


class GhettoDNS:
    '''Simple DNS Server work-around.'''

    def __init__(self):
        self.email_usr = usrMngr.UsrMngr(True, '')
        self.last_ip = ''
        self.email_url = 'gmail.com'
        self.mail_server = 'smtp.gmail.com:587'
        # other options 'http://ident.me', 'http://icanhazip.com'
        self.ip_server = 'https://api.ipify.org'

    def mail_ip(self):
        print("Attempting to check ip and mail at ", datetime.datetime.now())
        try:
            ip = requests.get(self.ip_server).text
            print("  ip is     ", ip)
            print("  old ip is ", self.last_ip)

            if self.last_ip != ip:
                self.last_ip = ip

                email_addr = (
                    self.email_usr.get_username() + '@' + self.email_url
                )
                subject = 'ghettodns public ip'
                msg = msg = '\r\n'.join([
                    'From: ' + email_addr,
                    'To: ' + email_addr,
                    'Subject: ' + subject,
                    '',
                    ip
                ])

                with smtplib.SMTP(self.mail_server) as server:
                    server.ehlo()
                    server.starttls()
                    server.login(self.email_usr.get_username(),
                                 self.email_usr.get_password())
                    server.sendmail(email_addr, email_addr, msg)

                print("  successfully mailed new ip")
            else:
                print("  no ip change, not mailing")

        except requests.exceptions.RequestException as err:
            print("Failed to get ip: ", err)
        except smtplib.SMTPException as err:
            print("Failed to send mail: ", err)


if __name__ == '__main__':
    dns = GhettoDNS()

    scheduler = BlockingScheduler()
    scheduler.add_job(dns.mail_ip, 'cron', minute=30)
    print("Press Ctrl+{0} to exit".format('Break' if os.name == 'nt' else 'C'))

    try:
        print("Starting ghettoDNS scheduler")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("\nghettoDNS terminated")
