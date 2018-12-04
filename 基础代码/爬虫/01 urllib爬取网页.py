import urllib.request
#向指定的URL发送请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")
#读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
data  = response.read()
print(data)

#读取一行
#data = response.readline()

#读取文件的全部内容，会把读取到的数据赋值给一个列表变量
# data = response.readlines()
# print(data)

#将爬取到的网页写入文件
# with open(r"C:\fle\file1.html","wb") as f:
#     f.write(data)


#response 属性
#返回当前环境的有关信息
#print(response.info)
#返回状态码
#print(response.getcode())
# if response.getcode() == 200 or response.getcode == 304:
#     #处理网页信息
#     pass
#返回当前正在爬取的URL地址
# print(response.geturl())

# url = "https://www.baidu.com/"
# #编码
# newUrl2 = urllib.request.quote(url)
# print(newUrl2)
# #解码
# newUrl = urllib.request.unquote(newUrl2)
# print(newUrl)
