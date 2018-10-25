from multiprocessing import Process
from time import  sleep


def run(str):
        print('子进程启动')
        sleep(3)
        print('子进程结束')
if __name__=="__main__":
    print('父进程启动')
    p = Process(target=run,args=('nice',))
    p.start()

    #父进程的结束不能影响子进程，让父进程等待子进程结束再执行父进程
    p.join()
    print('父进程结束')


