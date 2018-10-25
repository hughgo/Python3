import socket

clint =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#clint.connect(("10.60.250.230",9988))

while True:
    data = input("请输入数据：")
    clint.sendto(data.encode("utf-8"),('10.60.250.230',9988))

