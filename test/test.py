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
soup = BeautifulSoup(html,'lxml')
xsrf=soup.find('input',{'name':'_xsrf'})['value']

phone_num='18516608583'
password='123123123123'

postdate={'phone_num':phone_num,
     'password':password,
    '_xsrf':xsrf,
    'captcha_type':'en'
}
login_page=session.post(loginurl,headers=headers,data=postdate)
login_code=login_page.text
print(login_page.msg) 