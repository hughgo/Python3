# 特点：把参数进行打包，单独传输
#
# 优点：数量大，安全
#
# 缺点：速度慢

import urllib.request
import urllib.parse

url = "http://www.baidu.com"
data=  {
    "username" :"sunck",
    "passwd" :"666"
}
#对要发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url, postData)
#发起请求
req.add_header( "User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
