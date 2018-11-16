from qianxiao996 import qianxiao996

if __name__=='__main__':
    print('启动父进程')

    #创建子进程
    p= qianxiao996('test')
    #自动调用p进程对象的run方法
    p.start()
    p.join()

    print('父进程结束')