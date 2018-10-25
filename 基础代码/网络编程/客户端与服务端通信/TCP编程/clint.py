import socket

#创建socket
clint = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clint.connect(("10.60.250.230",8080))


while True:
    data = input("请输入给服务器发送的数据：")
    clint.send(data.encode('utf-8'))
    info = clint.recv(1024)
    print("服务器接收到的数据为：",info.decode('utf-8'))



