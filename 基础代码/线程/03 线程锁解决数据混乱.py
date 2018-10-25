import threading

#锁对象
lock =threading.Lock()
num=10

def run(n):
    global num

    for i in range(1000):
        # 锁
        #确保了这段代码只能由一个线程从头到尾的执行
        #阻止了多线程的并发运行，包含锁的某段代码实际上只能以单线程执行，所以效率大大的降低了
        #由于可以存在多个锁，不同线程存在不同的锁，并试图获取其他的锁，可能造成死锁。导致多个线程挂起。只能靠操作系统强制终止。
        '''
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
        #修改完一定要释放锁
            lock.release()
            '''
        #与上面代码功能相同，with lock可以自动上锁与解锁
        with lock:
            num = num + n
            num = num - n


if __name__ == '__main__':
    t1=threading.Thread(target=run,args=(6,))
    t2=threading.Thread(target=run,args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('num= ',num)