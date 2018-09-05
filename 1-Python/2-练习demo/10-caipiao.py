#encoding=utf8
from urllib import request
import gzip  # 解压缩返回的页面代码
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import re

def getHtml(url): # 获取页面源代码
    page = request.urlopen(url)
    html = page.read()
    html = gzip.decompress(html)
    html = html.decode('utf-8')
    return html


def getball(html): #正则匹配开奖号码
    regall = r'<p id="zj_area">(.+)</p>'
    reg  = r'<span class="red_ball">([0-9])</span>'
    balllist = re.findall(regall,html)
    openball = re.findall(reg,balllist[0])
    return openball

def insertTxt(file,data):# 将开奖号码保存到文件中
    in_put = open(file, 'w')
    in_put.write(str(data))
    in_put.close()

def getTxt(file): # 将文件中读取之前的开奖号码
    out_put = open(file,'r')
    result = out_put.read()
    out_put.close()
    return result

def deal(url): # 主逻辑
    html = getHtml(url)
    openball = str(getball(html)) # 将开奖的list转换成str
    print(openball)
    oldball = getTxt('data.txt')  # 从文件中读取历史开奖号码
    if openball == oldball:
        print('还没开奖')
    else:
        insertTxt('data.txt', openball)  # 更新开奖号码保存文件

        #发送邮箱
        mail_form = "pingan8787@163.com"
        mail_to = "pingan8787@qq.com"
        #发送邮件主题
        mail_object = '七星彩开奖结果'
        #发送邮箱服务器
        mail_smtpserver = 'smtp.163.com'
        #发送邮箱用户/密码
        mail_username = 'pingan8787@qq.com'
        mail_password = 'pingan60617'
        msg = MIMEText('本期七星彩开奖结果：'+openball, 'text', 'utf-8')

        msg['From'] = Header("python系统", 'utf-8')
        msg['To'] =  Header("", 'utf-8')
        msg['Subject'] = Header(mail_object, 'utf-8')

        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_smtpserver)
        smtpObj.login(mail_username,mail_password)
        smtpObj.sendmail(mail_form,mail_to, msg.as_string())
        print('和上次号码不同，已开奖')
        smtpObj.quit()

deal('http://caipiao.163.com/award/qxc/')