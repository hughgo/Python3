import urllib.request
import random
url = "http://www.baidu.com"

# 模拟请求头
headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
     # "Content-Type": "text/html;charset=utf-8"
}
#设置一个请求体
req = urllib.request.Request(url,headers = headers)
#发起请求
respone = urllib.request.urlopen(req)
data  = respone.read()
print(data)

# agnetsList  = [
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
# ]
# agentStr = random.choice(agnetsList)
# req = urllib.request.Request(url)
# #向请求体里添加了User-Agent
# req.add_header("User-Agent",agentStr)
# response = urllib.request.urlopen(req)
# #print(response.read().decode("utf-8"))
#
# data  = response.read()
# print(data)

#将爬取到的网页写入文件
with open(r"C:\fle\file3.html","wb") as f:
    f.write(data)