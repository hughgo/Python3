import socket
#1.创建一个socket
#参数1：指定协议 AF_INET   AF_INET6
#参数2：SOCK_STREAM执行使用面向流的TCP协议
sk =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2.建立连接
#参数：是一个元组，第一个参数为要连接的服务器的地址，第二个为要连接的端口号
sk.connect(("www.baidu.com",80))

#3.发送数据
sk.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

#等待接收数据
data = []
while True :
    #每次接收1k的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr =( b''.join(data)).decode('utf-8')

#断开连接
sk.close()
#print(dataStr)

#分开头和数据
headers, HTML = dataStr.split('\r\n\r\n',1)
#print(headers)
print(HTML)