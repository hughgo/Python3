#coding=utf8
import socket
import threading


def scan(host,cport):
    for x in range(660):
       p=x+660*cport
       try:
         if p < 65535:
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             s.connect((host, p))
             s.settimeout(0.1)
             print("local open port : %d"%p)
             s.close()
         else :
             break
       except Exception:
           pass
if __name__=="__main__":

    list = []
    for i in range(100):
            t = threading.Thread(target=scan,args=('10.60.250.52',i,))
            list.append(t)
            t.start()

    for threadinglist in list:
            threadinglist.join()
