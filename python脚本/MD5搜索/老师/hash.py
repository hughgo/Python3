import hashlib

p = open('passwords.txt', 'r')
passlist = []
for line in p.readlines():
    passlist.append(line.strip())
    p.close()

for passwd in passlist:
    if hashlib.md5(passwd).hexdigest() == '5416d7cd6ef195a0f7622a9c56b55e84':
        print passwd