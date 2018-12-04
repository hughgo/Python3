#
#
# 特点：把数据拼接到请求路径的后面传递给服务器
#
# 优点：速度快
#
# 缺点：承载的数据量小，不安全

import urllib.request

url = "http://stu.1000phone.net"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)