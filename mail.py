#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.qq.com'  #设置服务器
mail_user='xxx@qq.com'    #用户名
mail_pass='xxx'   #口令 

sender = 'xxx@qq.com'
receivers = ['xxx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 

def send_mail(title, content, plain = 'plain'):
  # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
  message = MIMEText(content, plain, 'utf-8')
  message['From'] = Header('King', 'utf-8')   # 发送者
  message['To'] =  Header('King', 'utf-8')    # 接收者
  message['Subject'] = Header(title, 'utf-8')
  try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
  except smtplib.SMTPException:
    print('Error: 无法发送邮件')
