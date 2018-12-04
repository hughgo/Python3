from socket import *
import threading      #导入线程相关模块

lock = threading.Lock()
openNum = 0
threads = []              #定义线程列表

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()        #因为openNum是个全局变量，每个线程不能对openNum 同时操作，只有获得所的线程才可以操作 openNum
        openNum+=1
        print('[+] %d open' % port)
        lock.release()        #线程对全局变量openNum操作完成后，需要释放锁，其他线程才可以继续修改全局变量openNum
        s.close()
    except:                     #如果端口没开，那么就直接pass，不执行其他输出操作。
        pass

def main():
    host = input('请输入IP地址:')
    setdefaulttimeout(1)
    #ports = [20, 21, 22, 23, 80, 111, 3306, 843]     #定义要扫描的端口，也可以在for中使用range进行定义，看个人需求，例如 for p in range(1,1024):
    for p in range(1,65535):
    #for p in ports:
        t = threading.Thread(target=portScanner,args=(host,p))
        threads.append(t)
        t.start()

    for t in threads:        #等待线程列表中的所以线程的执行完毕
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port' % (openNum))

if __name__ == '__main__':
    main()