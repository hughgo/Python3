import socket

udpServer =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.connect(("10.60.250.230",9999))

while True:
    data, addr =udpServer.recvfrom(1024)
    print("客户端说：",data.decode('utf-8'))


