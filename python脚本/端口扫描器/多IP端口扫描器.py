from socket import *
import threading      #导入线程相关模块
import re

lock = threading.Lock()
threads = []              #定义线程列表

def portScanner(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        result = s.connect_ex((host, port))
        if result == 0:
            lock.acquire()
            print(' [+] The port is: %5s ' % (port))
            lock.release()
        s.close()
    except:                     #如果端口没开，那么就直接pass，不执行其他输出操作。
        pass

def openfile():
    IP=[]
    f= open('../json提取IP域名/花椒直播域名IP地址.txt','r')
    data=f.read()
    f.close()
    iplist = re.findall(r'\d+\.\d+\.\d+\.\d+', data)
    for i in iplist:
        if i not in IP:  # 列表去重
            IP.append(i)
    return IP

def main():
    setdefaulttimeout(1)
    filedata = openfile()
    #ports = [20, 21, 22, 23, 80, 111, 3306, 843, ]     #定义要扫描的端口，也可以在for中使用range进行定义，看个人需求，例如 for p in range(1,1024):

    for host in filedata:
        print ('[*] Scan ip is %s ' % (host))
        print( '[*] begin  scan  ...')
        for p in range(1, 65535):
        #for p in ports:
            t = threading.Thread(target=portScanner,args=(host,p))
            threads.append(t)
            t.start()
        for t in threads:        #等待线程列表中的所以线程的执行完毕
            t.join()
        print('[*] begin  end  ...\n')
    print('[*] The scan is complete!')

if __name__ == '__main__':
    main()


