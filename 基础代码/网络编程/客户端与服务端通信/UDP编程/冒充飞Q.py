import socket
import time
udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(("10.60.250.230",8080))
while True:
    udp.send("sunck is good man".encode('utf-8'))
    time.sleep(1)