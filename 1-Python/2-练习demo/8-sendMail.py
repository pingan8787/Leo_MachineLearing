#encoding=utf8
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def sendMail(mail): # 主逻辑
        #发送邮箱
        mail_from = ""
        #发送邮件主题
        mail_object = '测试python发送邮件'
        #发送邮箱服务器
        mail_smtpserver = 'smtp.163.com'
        #发送邮箱用户/密码
        mail_username = ''
        mail_password = ''

        # 编写HTML类型的邮件正文
        msg = MIMEText('<html><h1>大佬好！</h1></html>', 'html', 'utf-8')
        msg['from'] = mail_from
        msg['to'] = mail
        msg['Subject'] = Header(mail_object, 'utf-8')
        print('发送者：'+mail_from+',接收者：'+mail)
        smtpObj = smtplib.SMTP(mail_smtpserver,25)
        # smtpObj.connect(mail_smtpserver,25)
        smtpObj.login(mail_username,mail_password)
        smtpObj.sendmail(mail_from, mail, msg.as_string())
        print('发送成功')
        smtpObj.quit()

sendMail('')