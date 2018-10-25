from multiprocessing import Process
from time import  sleep
import os

def run(str):
    while True:
        #os.getpid()获取当前进程号
        #os.getppid()获取当前的父进程号
        print('sunck is %s man-%s--%s'%(str,os.getpid(),os.getppid()))
        sleep(1.2)
if __name__=="__main__":
    print('主进程启动-%s'% os.getpid())
    #创建子进程
    #target说明进程执行的任务
    p = Process(target=run,args=('nice',))
    p.start()

    while True:
        print("sun is a man")
        sleep(1)


