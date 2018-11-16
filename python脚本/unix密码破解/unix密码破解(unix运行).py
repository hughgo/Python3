#!/usr/bin/env python         #指定这是一个python文件，使用这个解释器执行
#-*- coding:utf-8 -*-         #设定编码格式，防止报错
#unix系统下使用，必须把注释删掉，不然有可能报错

import crypt                  #调用crypt这个库

user_passfile = "/etc/shadow"   #获取系统密码路径
zidian = "/root/桌面/password.txt" #获取字典路径

#提取系统中的用户名和密文
def get_pass(user_passfile):
    used = {}                  #定义一个空字典
    f=open(user_passfile,"r")  #读取系统密码文件
    userline = f.readlines()   #将该文件转换为列表格式
    f.close()                  #关闭文件
    for i in userline:         #遍历列表里的内容
        if len(i.split(":")[1]) > 3:  #以":"分割，取第二个元素的长度，也就是完整密文值的长度，如果大于3，我们认定它有密码，把它取出来
            used[i.split(":")[0]]=i.split(":")[1]  #我们将取出的密文给了相应的用户，这里的used[i.split(":")[0]]是字典的key,也就是系统中的用户名，后面的i.split(":")[1]是用户名后的加密密文
    return used      #返回这个字典

#提取我们密码字典里的内容
def look_d(zidian):
    f = open(zidian,'r')   #读取字典文件内容
    mwlist = f.readlines() #将读取的内容转换为列表
    f.close()              #关闭文件
    return mwlist          #返回这个列表

#根据密文是否相同判断出对应的用户和密码
def main(user_passfile,zidian):
    used = get_pass(user_passfile)        #调用自定义函数get_pass
    mingwen = look_d(zidian)              #调用自定义函数look_d
    for user in used:
        passwd = used[user]               #一次遍历每个用户的密文
        salt = "$6$"+passwd.split("$")[2]  #获取盐值
        for passwdmw in mingwen:       #遍历系统中的每个完整密文
              if passwd == crypt.crypt(passwdmw.rstrip(),salt):    #如果我们猜想的密文与系统中的密文相同，输入它的用户名和密码
                    print("userName:%s passWord:%s" %(user,passwdmw.rstrip()))


if __name__ == "__main__":
    main(user_passfile,zidian)
