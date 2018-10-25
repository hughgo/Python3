#coding = utf-8
import urllib.request
from urllib import error
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
url = input("输入你要扫描到的网址：")
txt = input("输入字典的完整路径(默认php.txt)：")

#从字典中读取每一行与url组合，然后添加到url_list
url_list = []
if txt == "":
    txt = "php.txt"
try:
    with open(txt,'r') as f:
        for each in f:
            each = each.replace('\n','')
            url_list.append(each)
        f.close()
except:
    print("打开字典失败！")

for li in url_list:
    #设置一个请求体
    conn = "http://" + url +"/"+ li

    req = urllib.request.Request(conn,headers = headers)
    #发起请求
    try:
         response = urllib.request.urlopen(req)
         # 返回状态码
         print("%s------------->%s" % (conn, response.getcode()))
    except error.HTTPError as e: #http错误
        print('%s------------->%s' %(conn, e.code))
    except error.URLError :  # URL错误
         print("域名访问失败！")
         exit(1)