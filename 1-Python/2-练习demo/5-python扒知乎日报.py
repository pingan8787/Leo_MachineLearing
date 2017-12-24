# 安装requests
# pip install requests
# 1.获取源码
# import requests
# url = 'http://daily.zhihu.com/'
# res = requests.get(url).text
# print(res)
'''
直接访问可能会500错误 如下
<html><body><h1>500 Server Error</h1>
An internal server error occured.
</body></html>
'''
## 由于知乎禁止爬虫，所以需要添加一些伪装
# 2.设置浏览器伪装效果
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# url = 'http://daily.zhihu.com/'
# res = requests.get(url,headers=headers).text
# print(res)
'''
获取到页面所有html标签元素，这里不粘贴出来
'''

# 3.代理设置，防止网站服务器屏蔽
## xicidaili.com/nn/ 西刺代理提供了很多可用的国内IP，可以直接拿来使用。
# import requests
# proxies = {
#   "http": "http://110.73.15.232:8123",
#   "https": "http://112.114.96.162:8118",
# }
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# url = 'http://daily.zhihu.com/'
# res = requests.get(url,headers=headers,proxies=proxies).text
# print(len(res))
# ## 为了便于测试，只打印出返回数据的长度
# ## 若返回说主机没有反应，则是因为代理的问题，换个新的就可以
# 10728

############################
#另外完整代码
作者：小小造数君
链接：https://www.zhihu.com/question/29372574/answer/172891401
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
from bs4 import BeautifulSoup
import os, time
import re
# import http.cookiejar as cookielib

# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

######### 构造用于网络请求的session
session = requests.Session()
# session.cookies = cookielib.LWPCookieJar(filename='zhihucookie')
# try:
#     session.cookies.load(ignore_discard=True)
# except:
#     print('cookie 文件未能加载')

############ 获取xsrf_token
homeurl = 'https://www.zhihu.com'
homeresponse = session.get(url=homeurl, headers=headers)
homesoup = BeautifulSoup(homeresponse.text, 'html.parser')
xsrfinput = homesoup.find('input', {'name': '_xsrf'})
xsrf_token = xsrfinput['value']
print("获取到的xsrf_token为： ", xsrf_token)

########## 获取验证码文件
randomtime = str(int(time.time() * 1000))
captchaurl = 'https://www.zhihu.com/captcha.gif?r='+\
             randomtime+"&type=login"
captcharesponse = session.get(url=captchaurl, headers=headers)
with open('checkcode.gif', 'wb') as f:
    f.write(captcharesponse.content)
    f.close()
# os.startfile('checkcode.gif')
captcha = input('请输入验证码：')
print(captcha)

########### 开始登陆
headers['X-Xsrftoken'] = xsrf_token
headers['X-Requested-With'] = 'XMLHttpRequest'
loginurl = 'https://www.zhihu.com/login/email'
postdata = {
    '_xsrf': xsrf_token,
    'email': '邮箱@qq.com',
    'password': '密码'
}
loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
print('服务器端返回响应码：', loginresponse.status_code)
print(loginresponse.json())
# 验证码问题输入导致失败: 猜测这个问题是由于session中对于验证码的请求过期导致
if loginresponse.json()['r']==1:
    # 重新输入验证码，再次运行代码则正常。也就是说可以再第一次不输入验证码，或者输入一个错误的验证码，只有第二次才是有效的
    randomtime = str(int(time.time() * 1000))
    captchaurl = 'https://www.zhihu.com/captcha.gif?r=' + \
                 randomtime + "&type=login"
    captcharesponse = session.get(url=captchaurl, headers=headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(captcharesponse.content)
        f.close()
    os.startfile('checkcode.gif')
    captcha = input('请输入验证码：')
    print(captcha)

    postdata['captcha'] = captcha
    loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
    print('服务器端返回响应码：', loginresponse.status_code)
    print(loginresponse.json())




##########################保存登陆后的cookie信息
# session.cookies.save()
############################判断是否登录成功
profileurl = 'https://www.zhihu.com/settings/profile'
profileresponse = session.get(url=profileurl, headers=headers)
print('profile页面响应码：', profileresponse.status_code)
profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
div = profilesoup.find('div', {'id': 'rename-section'})
print(div)