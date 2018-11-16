# coding=utf8
#注意：本程序在python3下编写，请用python3调试运行
#自定义加密与解密  by qianxiao996
#博客地址：https://blog.csdn.net/qq_36374896
#首先你要在程序的目录下有一个密码表的txt文件，用-----分割字母与密码
#运行程序即可实现密码表里的加密于解密规则
#本程序支持中文加密。
#感觉这程序和古代的电报差不多= =

import base64
def print_heads():
    print("***************************************************")
    print("*         qianxiao996自定义加密解密工具           *")
    print("*                                                 *")
    print("*      （1）加密                （2）解密         *")
    print("*                    退出(Q)                      *")
    print("***************************************************")

#读取txt内容到passwd_list列表
def read_passwd_list():
    passwd_list = []
    with open("密码表.txt", 'r',encoding="utf-8") as f:  #打开文件
        for each in f:  #遍历文件
            each = each.replace('\n', '')  #替换换行符为空格
            passwd_list.append(each)   #添加到列表
        f.close()   #关闭文件
    return passwd_list   #返回值

#加密
def encrypt():
    k=0   #存放字符串字符统计个数
    unencryptstr =""   #存放加密后的字符串
    str = input("请输入要加密的字符串:")
    list = read_passwd_list() #读取值到list列表
    for j in str:   #遍历整个字符串
        for i in list:  #遍历列表输出加密后的字符串
            if j == i[0]:  #判断字符是否等于列表中的元素的首部
                unencryptstr += i[6:]+"---"    #加密并添加---
                k=k+1
    encryptstr=base64.b64encode((unencryptstr[:-3]).encode('utf-8'))  #  base64加密
    if k == len(str):
        print('加密后的字符串为:',encryptstr.decode('utf-8'))   #打印加密后的值
    else:
        print("字典中没有对应的加密值！")
    exit(0)

#解密
def decrypt():
    decryptstr=""    #存放解密后的字符串
    base64decrypt= input("请输入要解密的字符串:")
    str=base64.b64decode(base64decrypt).decode('utf-8')  #base64解密
    str=str.replace('\n', '').split('---')  #分割字符串放到str列表
    list = read_passwd_list()   #读取值到密码表list列表

    #取出list的后六位
    listend6=[]
    for k in list:
        listend6.append(k[6:])  #放入listend6列表
    for j in str:  # 遍历字符串
        for i in list:  #遍历列表
            if j in listend6:   #如果字符串存在于列表
                if  j == i[6:]:   #相等
                    decryptstr+=i[0]  # 输出解密的字符串，不换行输出
            else:
                print("解密失败!")
                exit(0)

    print('解密后的字符串为:',decryptstr)
    exit(0)

#主函数
def main():
    print_heads()
    choose=input("请输入您的选择:")
    while True:
        if(choose!=""):
            if(choose == "1"):
                encrypt()#加密
            elif(choose == "2"):
                decrypt()#解密
            elif(choose=='q'or str(choose)=='Q'):
                exit(0)  #exit(1)表示发生错误后退出程序，   exit(0)表示正常退出。
            else:
                choose = input("输入错误，请重新输入：")
                continue  #跳出本次循环
        choose = input("请不要输入空字符，请重新输入：")

if __name__=="__main__":
    main()