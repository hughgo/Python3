import threading
def run():
    print('sss')

#延时执行线程
t=threading.Timer(5,run)
t.start()
t.join()
print('父线程结束')
