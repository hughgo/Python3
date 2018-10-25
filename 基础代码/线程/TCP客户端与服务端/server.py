import socket
import threading
#创建socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定ip和端口t
server.bind(('10.60.250.230',8080))

#监听
server.listen(5)
print("服务器启动成功")

def run(ck):
    data = clintSocker.recv(1024)
    print("客户端发送的数据：", data.decode("utf-8"))
    sendData = input("请输入给客户端发送的数据")
    clintSocker.send(sendData.encode('utf-8'))

while True:
    # 等待连接
    clintSocker, clintAddress = server.accept()
    print("%s -- %s 连接成功" % (str(clintSocker), clintAddress))
    t =threading.Thread(target=run,args=(clintSocker,))
    t.start()

