#使用方法
#目录下必须有一个名为字典的TXT文件
#输入32位小写的MD5 即可寻找出文件中的原始值
import os
import hashlib

def curlmd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()

def exit():
    if str == 'q':
        os._exit(0)
path = os.path.abspath('字典.txt')
str = input("请输入32位的MD5值：")
str=str.lower()
def query():
    for line in file.readlines():
        line = line.decode("utf-8").strip("\r\n")
        src = curlmd5(line)
        if src == str:
            print('您的查询结果为：%s' % line)
            os._exit(0)
while True:
    while str!='':
        file = open(path, "rb")
        query()
        file.close()
        str = input("查询结果为空，请重新输入(q退出)：")
        exit()
    str = input("请不要输入空字符，请重新输入(q退出)：")
    exit()

