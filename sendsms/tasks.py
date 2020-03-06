from __future__ import absolute_import

from sendsms.celerys import app

from sendsms.config import Config

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

@app.task
def add(x, y):
    print(x+y)
    return x + y

@app.task(bind=True)
def send_email(receiver='',mail_title='',mail_content=''):

    sender_qq = Config.sender_qq
    pwd = Config.sender_pwd

    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = str(receiver)
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

    return receiver