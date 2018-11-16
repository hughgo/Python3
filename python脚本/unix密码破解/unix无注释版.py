#!/usr/bin/env python
#-*- coding:utf-8 -*-
import crypt

user_passfile = "/etc/shadow"
zidian = "/root/桌面/password.txt"


def get_pass(user_passfile):
    used = {}
    f=open(user_passfile,"r")
    userline = f.readlines()
    f.close()
    for i in userline:
        if len(i.split(":")[1]) > 3:
            used[i.split(":")[0]]=i.split(":")[1]
    return used

def look_d(zidian):
    f = open(zidian,'r')
    mwlist = f.readlines()
    f.close()
    return mwlist


def main(user_passfile,zidian):
    used = get_pass(user_passfile)
    mingwen = look_d(zidian)
    for user in used:
        passwd = used[user]
        salt = "$6$"+passwd.split("$")[2]
        for passwdmw in mingwen:
              if passwd == crypt.crypt(passwdmw.rstrip(),salt):
                    print("userName:%s passWord:%s" %(user,passwdmw.rstrip()))


if __name__ == "__main__":
    main(user_passfile,zidian)
