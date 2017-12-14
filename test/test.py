import os
import time
import requests
from bs4 import BeautifulSoup
url='http://www.zhihu.com/login/email'
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
'Connection':'keep-alive',
'Host':'www.zhihu.com',
'Referer':'https://www.zhihu.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

loginurl = 'http://www.zhihu.com/login/email'
session = requests.Session()
html = session.get(url=loginurl, headers=headers).content
soup = BeautifulSoup(html, "html.parser")
xsrf=soup.find('input',{'name':'_xsrf'})['value']

def getchap():
    tm=str(int(time.time()*1000))
    checkcodeurl = 'http://www.zhihu.com/captcha.gif'
    print (checkcodeurl)
    checkcode = session.get(url=checkcodeurl, headers=headers).content
    with open('./checkcode.png', 'wb') as f:
        f.write(checkcode)
    print('已经打开验证码，请输入')
    os.startfile(r'checkcode.png')
    charp = input('请输入验证码：')
    os.remove(r'checkcode.png')
    return  charp
phone_num='18516608583'
password='112631spring'
charp=getchap()
print (charp)
postdata={'phone_num':phone_num,
     'password':password,
    '_xsrf':xsrf,
    'captcha_type':'en',
    'captcha': charp,
}
response=session.post(loginurl,headers=headers,data=postdata)
login_code=response.text
print('服务器端返回响应码：', response.status_code)
#print(response.json())
tempurl = 'https://www.zhihu.com/question/57964452/answer/155231804'
tempresponse = session.get(tempurl, headers=headers)
soup = BeautifulSoup(tempresponse.text, 'html.parser')
print(soup.title)